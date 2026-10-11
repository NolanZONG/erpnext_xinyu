from frappe.utils import ceil, flt

def calculate_packaging_counts(doc, method=None):
	"""Authoritative calculation for Xinyu packaging count fields on Pick List.

	Runs on validate and before_save: ERPNext rebuilds `locations` in its own
	before_save (set_item_locations), so values must be recomputed afterwards.
	The client script mirrors these formulas only for live feedback while editing.
	"""
	total = 0

	for row in doc.locations or []:
		qty = flt(row.qty)
		weight = flt(row.custom_unit_package_weight)
		row.custom_package_count = ceil(qty / weight) if weight > 0 else 0
		total += row.custom_package_count

	doc.custom_total_package_count = total
