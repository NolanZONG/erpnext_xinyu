import frappe

# Default Serial & Batch item settings (Stock Settings) that should ship with the app.
# Captured from the desired configuration so fresh installs match it.
SERIAL_BATCH_STOCK_SETTINGS = {
    "enable_serial_and_batch_no_for_item": 1,
    "pick_serial_and_batch_based_on": "FIFO",
    "allow_existing_serial_no": 0,
    "use_serial_batch_fields": 0,
    "disable_serial_no_and_batch_selector": 0,
    "allow_negative_stock_for_batch": 0,
    "do_not_use_batchwise_valuation": 0,
    "use_naming_series": 0,
    "naming_series_prefix": "BATCH-",
    "auto_create_serial_and_batch_bundle_for_outward": 0,
    "do_not_update_serial_batch_on_creation_of_auto_bundle": 1,
    "set_serial_and_batch_bundle_naming_based_on_naming_series": 0,
}


def setup_serial_batch_stock_settings():
    """Apply the desired Serial & Batch defaults to Stock Settings (idempotent)."""
    if not frappe.db.exists("DocType", "Stock Settings"):
        return
    frappe.db.set_single_value("Stock Settings", SERIAL_BATCH_STOCK_SETTINGS)


def after_install():
    setup_serial_batch_stock_settings()
