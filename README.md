# cloud-automation-test

## Python application and tests

Requires Python 3.12; no third-party dependencies, services, or secrets are needed.

Run the task summary application:

```sh
python app.py build test deploy
```

Run all three unit tests locally:

```sh
python -m unittest discover -v
```

## View automated test results

GitHub Actions runs **Python tests** on pushes to branches other than `main`
and on pull requests targeting `main`. Open the repository's **Actions** tab,
select **Python tests**, open a run, and select **unit-tests** to view the
**Run unit tests** logs. Pull requests also show results in the **Checks** tab.
