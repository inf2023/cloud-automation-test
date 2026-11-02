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

## Django and PostgreSQL integration tests

The separate **Django PostgreSQL tests** workflow uses Python 3.12, Django 5.2,
and a disposable PostgreSQL 16 service on GitHub-hosted Ubuntu. It runs on pushes
to branches other than `main` and pull requests targeting `main`. Open **Actions**,
select that workflow, and inspect **integration-tests** for migration and test logs.
The existing Python application, tests, and workflow remain independent.

To reproduce locally with Docker and Python 3.12:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-django.txt
docker run --detach --rm --name cloud-integration-postgres \
  -e POSTGRES_DB=cloud_integration -e POSTGRES_USER=cloud_test \
  -e POSTGRES_PASSWORD=disposable-ci-only \
  -p 127.0.0.1:55432:5432 postgres:16
export DJANGO_SECRET_KEY=disposable-integration-test-key
export POSTGRES_HOST=127.0.0.1 POSTGRES_PORT=55432
export POSTGRES_DB=cloud_integration POSTGRES_USER=cloud_test
export POSTGRES_PASSWORD=disposable-ci-only
# Wait until PostgreSQL reports that it is accepting connections:
docker exec cloud-integration-postgres pg_isready -U cloud_test -d cloud_integration
python backend/manage.py check
python backend/manage.py makemigrations --check --dry-run
python backend/manage.py migrate --noinput
python backend/manage.py test tasks --noinput --verbosity 2
python -m unittest discover -v
docker stop cloud-integration-postgres
```

All credentials above and in the workflow are public, test-only values for a
fresh disposable container; never substitute production or TaZa Daily credentials.
Settings require database variables explicitly and reject non-loopback hosts or
database names other than `cloud_integration`. Django creates the separate
`test_cloud_integration` database, applies migrations there, isolates each test,
and destroys it after the run. The container has no persistent volume; stopping
it removes its disposable data. Use only the dedicated container and its test role,
which must be allowed to create the test database. Do not point these commands at
an existing database service.

## Android debug APK

`android/` contains a minimal Kotlin app displaying **Cloud Automation Test**.
The independent **Android debug APK** workflow runs on feature-branch pushes and
pull requests targeting `main`, using a GitHub-hosted Ubuntu runner. It installs
Android platform 35 and build tools 35.0.0, then runs the checked-in Gradle Wrapper
8.13 with JDK 17, AGP 8.13.2, and Kotlin 2.2.21:

```sh
cd android
./gradlew --no-daemon assembleDebug lintDebug
```

Open **Actions → Android debug APK → a successful run**. Under **Artifacts**,
download **cloud-automation-debug-apk**, containing `app-debug.apk`. Artifacts are
retained for 14 days and require a successful upload; a pushed branch alone does
not confirm an APK exists. The APK is debug-signed for testing only. This workflow
needs no production credentials, external secrets, emulator, or release signing.
Existing Python and PostgreSQL workflows continue to run independently.
