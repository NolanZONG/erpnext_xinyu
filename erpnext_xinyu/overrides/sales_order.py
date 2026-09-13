import frappe
from frappe.utils import ceil, flt

def calculate_packaging_counts(doc, method=None):
	"""Authoritative calculation for Xinyu packaging count fields on Sales Order.

	Runs on validate so values are correct regardless of entry point
	(desk UI, REST API, data import, programmatic creation). The client
	script mirrors these formulas only for live feedback while editing.
	"""
	total = 0

	for row in doc.items or []:
		qty = flt(row.qty)
		weight = flt(row.custom_unit_package_weight)
		row.custom_package_count = ceil(qty / weight) if weight > 0 else 0
		total += row.custom_package_count

	doc.custom_total_package_count = total

def calculate_custom_amounts(doc, method=None):
	"""Authoritative calculation for Xinyu custom pricing fields on Sales Order.

	Runs on validate so values are correct regardless of entry point
	(desk UI, REST API, data import, programmatic creation). The client
	script mirrors these formulas only for live feedback while editing.
	"""
	conversion_rate = flt(doc.conversion_rate) or 1.0
	total_difference = 0.0

	for row in doc.items or []:
		customs_rate = flt(row.custom_customs_rate)
		commission_rate = flt(row.custom_commission_rate)
		factory_rate = flt(row.custom_factory_rate)
		qty = flt(row.qty)

		rebate_rate = 0.0
		if row.item_code:
			rebate_rate = flt(
				frappe.db.get_value("Item", row.item_code, "custom_tax_rebate_rate")
			)

		excl_commission_rate = flt(
			customs_rate - commission_rate,
			row.precision("custom_customs_excl_commission_rate"),
		)
		excl_commission_amount = flt(
			excl_commission_rate * qty,
			row.precision("custom_customs_excl_commission_amount"),
		)
		customs_amount = flt(
			customs_rate * qty,
			row.precision("custom_customs_amount"),
		)
		commission_amount = flt(
			commission_rate * qty,
			row.precision("custom_commission_amount"),
		)

		vat = flt(factory_rate * 0.9, row.precision("custom_vat"))
		tax = flt(
			vat / 1.13 * (rebate_rate / 100.0),
			row.precision("custom_tax"),
		)
		exw = flt(
			(factory_rate - tax) / conversion_rate if conversion_rate else 0.0,
			row.precision("custom_exw"),
		)
		insurance = flt(exw * 1.1 * 0.001, row.precision("custom_insurance"))
		quote = flt(exw + insurance, row.precision("custom_quote"))
		quote_with_credit_term = flt(
			quote * 1.006,
			row.precision("custom_quote_with_credit_term"),
		)
		approved_amount = flt(
			quote_with_credit_term * qty,
			row.precision("custom_approved_amount"),
		)
		difference = flt(
			excl_commission_amount - approved_amount,
			row.precision("custom_difference"),
		)

		row.custom_customs_excl_commission_rate = excl_commission_rate
		row.custom_customs_excl_commission_amount = excl_commission_amount
		row.custom_customs_amount = customs_amount
		row.custom_commission_amount = commission_amount
		row.custom_vat = vat
		row.custom_tax = tax
		row.custom_exw = exw
		row.custom_insurance = insurance
		row.custom_quote = quote
		row.custom_quote_with_credit_term = quote_with_credit_term
		row.custom_approved_amount = approved_amount
		row.custom_difference = difference

		total_difference += difference

	doc.custom_total_difference = flt(
		total_difference,
		doc.precision("custom_total_difference"),
	)
