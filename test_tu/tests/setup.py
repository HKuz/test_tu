import datetime
import random
import types
import os

import frappe
from frappe.desk.page.setup_wizard.setup_wizard import setup_complete
from erpnext.setup.utils import enable_all_roles_and_domains, set_defaults_for_tests  # noqa: F401
from erpnext.accounts.doctype.account.account import update_account_number

from test_utils.utils.setup_fixtures import create_customers
from test_utils.utils.chart_of_accounts import setup_chart_of_accounts, create_bank_and_bank_account


def before_test():
	frappe.clear_cache()
	today = frappe.utils.getdate()
	setup_complete(
		{
			"currency": "USD",
			"full_name": "Administrator",
			"company_name": "Chelsea Fruit Co",
			"timezone": "America/New_York",
			"company_abbr": "CFC",
			"domains": ["Distribution"],
			"country": "United States",
			"fy_start_date": today.replace(month=1, day=1).isoformat(),
			"fy_end_date": today.replace(month=12, day=31).isoformat(),
			"language": "english",
			"company_tagline": "Chelsea Fruit Co",
			"email": "support@agritheory.dev",
			"password": "admin",
			"chart_of_accounts": "Standard with Numbers",  # should be either Standard or Standard with Numbers
			"bank_account": "Primary Checking",
		}
	)
	# enable_all_roles_and_domains()
	set_defaults_for_tests()
	frappe.db.commit()
	create_test_data()
	for modu in frappe.get_all("Module Onboarding"):
		frappe.db.set_value("Module Onboarding", modu, "is_complete", 1)
	frappe.set_value("Website Settings", "Website Settings", "home_page", "login")
	frappe.db.commit()


def create_test_data():
	today = frappe.utils.getdate()

	chart_of_accounts = "IFRS"
	company = frappe.defaults.get_defaults().get("company")
	setup_chart_of_accounts(company=company, chart_template=chart_of_accounts)
	
	settings = frappe._dict(
		{
			"day": today.replace(month=1, day=1),
			"company": company,
			"company_account": frappe.get_value(
				"Account",
				{
					"account_type": "Bank",
					"company": company,
					"is_group": 0,
				},
			),
			"warehouse": frappe.get_value(
				"Warehouse",
				{
					"warehouse_name": "Finished Goods",
					"company": company,
				},
			),
		}
	)
	
	create_bank_and_bank_account(settings)
	create_customers(settings)
