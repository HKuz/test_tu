<!-- Copyright (c) 2025, HKuz and contributors
For license information, please see license.txt-->

## Test TU

<div class="byline">
  Heather Kusmierz 2025-02-06
</div>

Dummy ERPNext app to test the functionality in the [Test Utils](https://github.com/agritheory/test_utils) app.

To test the `test_utils` repository:

Set up a new `version-15` bench and site with ERPNext installed.

Collect and install this app into the site:

```
bench get-app test_tu --branch version-15 https://github.com/HKuz/test_tu.git
bench install-app test_tu
```

If you're working on a branch of `test_utils`, make sure to commit and push the branch up to the `agritheory/test_utils` repository. Next, install the `test_utils` dependency into the bench environment, optionally specifying the branch name with your work on it by including `@<branch name>` at the end. If the branch isn't specified, pip will grab the default branch `main`.

If you make any code changes to your `test_utils` work after installing it to the local environment, you'll need to uninstall/reinstall the package to pick up those changes:

```
cd { bench directory }
source env/bin/activate
pip install git+https://github.com/agritheory/test_utils.git@<branch name>

# To uninstall/reinstall:
pip uninstall test_utils
pip install git+https://github.com/agritheory/test_utils.git@<branch name>
```

If you're using or testing the package's fixtures or functions, modify this app's `tests/setup.py` as-needed to import and run them, then execute to create the data in the local site:

```
bench execute 'test_tu.tests.setup.before_test'
```

If you're testing the pre-commit hooks, then you can add hooks as-needed to the `.pre-commit-config.yaml` file's section for the Test Utils repo.

See the [documentation](./test_tu/docs/index.md) for a few code examples.

## License

mit
