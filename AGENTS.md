# Project instructions

- Work only in this repository. Preserve the independent Python, Django/PostgreSQL,
  and Android components and their existing workflows.
- Use a feature branch from current main. Never commit directly to main, force push,
  delete existing branches, or merge a PR without explicit user authorization.
- Use the existing isolated checkout; do not create a worktree unless requested.
- Python targets 3.12. Run `python -m unittest discover -v` from the repository root.
- Django dependencies are in requirements-django.txt. Follow README for disposable
  PostgreSQL testing, migrations, and `python backend/manage.py test tasks`.
- Never use production databases, TaZa Daily credentials, or real secrets in tests.
- Android lives in android/. Use JDK 17, Gradle Wrapper 8.13, AGP 8.13.2,
  Kotlin 2.2.21, Android platform 35, and build tools 35.0.0.
- From android/, run `./gradlew --no-daemon assembleDebug lintDebug`.
  Keep generated build outputs and local SDK configuration untracked.
- Keep the Gradle distribution checksum and verify downloaded tools. Do not disable
  TLS verification or commit credentials, SDKs, caches, or signing keys.
- CI builds a debug APK only; release signing and Play Store publishing are out of scope.
- Report executed test/build results separately from unverified checks. A successful
  push does not establish Actions success. If PR creation returns Forbidden, stop
  without repeating the request; report the exact error.
