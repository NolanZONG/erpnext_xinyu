app_name = "erpnext_xinyu"
app_title = "ERPNext Xinyu"
app_publisher = "Nolan ZONG"
app_description = "Custom App for Xinyu Chem"
app_email = "zongnan1989@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "erpnext_xinyu",
# 		"logo": "/assets/erpnext_xinyu/logo.png",
# 		"title": "ERPNext Xinyu",
# 		"route": "/erpnext_xinyu",
# 		"has_permission": "erpnext_xinyu.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_xinyu/css/erpnext_xinyu.css"
# app_include_js = "/assets/erpnext_xinyu/js/erpnext_xinyu.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_xinyu/css/erpnext_xinyu.css"
# web_include_js = "/assets/erpnext_xinyu/js/erpnext_xinyu.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "erpnext_xinyu/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "erpnext_xinyu/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "erpnext_xinyu.utils.jinja_methods",
# 	"filters": "erpnext_xinyu.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "erpnext_xinyu.install.before_install"
after_install = "erpnext_xinyu.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "erpnext_xinyu.uninstall.before_uninstall"
# after_uninstall = "erpnext_xinyu.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "erpnext_xinyu.utils.before_app_install"
# after_app_install = "erpnext_xinyu.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "erpnext_xinyu.utils.before_app_uninstall"
# after_app_uninstall = "erpnext_xinyu.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "erpnext_xinyu.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_xinyu.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

doc_events = {
    "Sales Order": {
        "validate": [
            "erpnext_xinyu.overrides.sales_order.calculate_custom_amounts",
            "erpnext_xinyu.overrides.sales_order.calculate_packaging_counts",
        ],
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnext_xinyu.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_xinyu.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_xinyu.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_xinyu.tasks.weekly"
# 	],
# 	"monthly": [
# 		"erpnext_xinyu.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "erpnext_xinyu.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "erpnext_xinyu.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_xinyu.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "erpnext_xinyu.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["erpnext_xinyu.utils.before_request"]
# after_request = ["erpnext_xinyu.utils.after_request"]

# Job Events
# ----------
# before_job = ["erpnext_xinyu.utils.before_job"]
# after_job = ["erpnext_xinyu.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"erpnext_xinyu.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

# 自动安装 fixtures
# Custom Field: 新增的字段
# Property Setter: 新增的字段属性
# Client Script: 新增的客户端脚本
# Server Script: 新增的服务器脚本或打印格式等
fixtures = [
    {
        "dt": "Custom Field",
        "filters": [["dt", "in", ["Sales Order", "Sales Order Item", "Item"]]],
    },
    {
        "dt": "Property Setter",
        "filters": [["doc_type", "in", ["Sales Order", "Sales Order Item", "Item"]]],
    },
    {
        "dt": "Client Script",
        "filters": [["dt", "in", ["Sales Order", "Sales Order Item"]]],
    }
]
