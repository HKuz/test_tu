## Test TU

Dummy ERPNext app to test Test Utils functionality

To test the `test_utils` repository:

Set up a new `version-15` bench and site with ERPNext installed.

Collect and install this app into the site:

```
bench get-app test_tu --branch version-15 https://github.com/HKuz/test_tu.git
bench install-app test_tu
```

Install the `test_utils` dependency into the bench environment, optionally specifying the branch name by including `@<branch name>` at the end, if needed. Note that all local changes should be committed and pushed up to the `agritheory/test_utils` repository before installing it to the local environment. If any changes are made after installing it to the local environment, it will require an uninstall/reinstall to pick up those changes:

```
cd { bench directory }
source env/bin/activate
pip install git+https://github.com/agritheory/test_utils.git@<branch name>

# To uninstall/reinstall:
pip uninstall test_utils
pip install git+https://github.com/agritheory/test_utils.git@<branch name>
```

Modify this app's `tests/setup.py` as-needed to import and run any `test_utils` fixtures or functions, then execute to create the data in the local site.

Run `bench execute 'test_tu.tests.setup.before_test'`.

## License

mit