<!-- Copyright (c) 2025, HKuz and contributors
For license information, please see license.txt-->

# Code Examples to Use and Test the Test Utils App

<div class="byline">
  Heather Kusmierz 2025-09-09
</div>

## Pre-Commit Hooks

To use a pre-commit hook from Test Utils, add a section for the repo in the `.pre-commit-config.yaml` file, then add the `id` of any hook you'd like to run.

```
# Example section in the .pre-commit-config.yaml file

  - repo: https://github.com/agritheory/test_utils
    rev: v1.0.0
    hooks:
      - id: update_pre_commit_config
      - id: validate_copyright
        files: '\.(js|ts|py|md)$'
        args: ['--app', 'test_tu']
      - id: clean_customized_doctypes
        args: ['--app', 'test_tu']
      - id: validate_customizations
      - id: bylines
```

If you're testing a hook in a branch that hasn't been merged into the default branch of Test Utils, then there are a few extra steps you'll need to do to test the new code:

- fork the AgriTheory Test Utils repository and clone it locally
- Set a remote called "upstream" that points to the AgriTheory repository: `git remote add upstream git@github.com:agritheory/test_utils.git`
- fetch the upstream branch with the code you want to test: `git fetch upstream branch_name:branch_name`
- merge the new branch into the local forked repo's `main` branch (make sure `main` is checked out, then run `git merge <branch_name>`)
- create a release in your fork with a tag that matches the `rev` line (if necessary)
- change the repo line in the `pre-commit-config.yaml` to use the fork instead

```
  - repo: https://github.com/<your GitHub username>/test_utils
    rev: v1.0.0
    hooks:
      - id: update_pre_commit_config
      # ...
```

## Using Test Fixtures

Below is an example that uses functions from Test Utils to set up an IFRS Chart of Accounts for the test company, create a bank and bank account, and create customers in the test data.

See the `test_utils/utils/setup_fixtures.py` [file](https://github.com/agritheory/test_utils/blob/main/test_utils/utils/setup_fixtures.py) for more options.

```py
# In the tests/setup.py file
import frappe

from test_utils.utils.setup_fixtures import create_customers
from test_utils.utils.chart_of_accounts import setup_chart_of_accounts, create_bank_and_bank_account

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
```
