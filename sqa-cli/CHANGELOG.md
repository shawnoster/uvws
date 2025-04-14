# CHANGELOG


## v0.4.8 (2025-04-14)

### Bug Fixes

- **plugin-one**: Update serviceName in evaluate method to 'test-four'
  ([`1a3d2a8`](https://github.com/shawnoster/uvws/commit/1a3d2a8b7de6d4d261c5cd1835f6c3574564942a))


## v0.4.7 (2025-04-14)

### Bug Fixes

- **plugin-one**: Correct error message for missing 'serviceName' key
  ([`35d82bc`](https://github.com/shawnoster/uvws/commit/35d82bcbbf8d9ce959516477b36405be1bd45cb5))

- **plugin-one**: Correct return value in evaluate method to match expected output
  ([`bb3c734`](https://github.com/shawnoster/uvws/commit/bb3c7342c0e69082ff35061a6181fc27415d4499))

- **plugin-one**: Remove 'chore' from exclude_commit_patterns for semantic release
  ([`67f4cda`](https://github.com/shawnoster/uvws/commit/67f4cdae2a8a96763a4968d738ee7446ff2f3c45))

- **plugin-one**: Update dist_glob_patterns location and format in pyproject.toml
  ([`871fcb9`](https://github.com/shawnoster/uvws/commit/871fcb9ae8ae7da77dfbe99ecd4ccf283f6a4ce7))

- **plugin-one**: Update dist_glob_patterns to include full path for package distribution
  ([`62bf8d9`](https://github.com/shawnoster/uvws/commit/62bf8d9db7e3571cd3a778f715149867bc7fcd18))

- **plugin-one**: Update evaluate method to return correct serviceName
  ([`c7c20eb`](https://github.com/shawnoster/uvws/commit/c7c20eb45fa19975c3b9ab717dbafc02ead85b73))

- **plugin-one**: Update evaluate method to return correct serviceName
  ([`0118dd9`](https://github.com/shawnoster/uvws/commit/0118dd9584895f6dda7b93ed3fb0c5080fb4dd94))

- **plugin-one**: Update exclude_commit_patterns to match 'chores*' for semantic release
  ([`92ff0a3`](https://github.com/shawnoster/uvws/commit/92ff0a3fd4185ca36ecb03fd1a9d592241d7b5cc))

- **pyproject**: Remove cookiecutter-sqa-plugin from workspace exclusions
  ([`747c9fd`](https://github.com/shawnoster/uvws/commit/747c9fd1203197d6200fc36d90390859906a68f1))

- **sqa-api**: Update version to 2.0.1 in pyproject.toml and __init__.py
  ([`8b4be51`](https://github.com/shawnoster/uvws/commit/8b4be5128bc7676b09916ad3697dd0f95218d9d6))


## v0.4.3 (2025-04-13)

### Bug Fixes

- **plugin-one**: Raise ValueError for missing serviceName key in input data
  ([`045a020`](https://github.com/shawnoster/uvws/commit/045a0206e09871d82c57cf54ae46ebdc612508da))


## v0.4.2 (2025-04-13)


## v0.4.1 (2025-04-13)

### Bug Fixes

- **plugin-one**: Correct key check and return value in collect method
  ([`a4eb52c`](https://github.com/shawnoster/uvws/commit/a4eb52ca840d79bd424132837a0b83ea1d8a4be1))

- **plugin-one**: Update build command to output to dist directory
  ([`b5189f2`](https://github.com/shawnoster/uvws/commit/b5189f2327a7dee2c8eee11860930e088ed9f1e7))


## v0.4.0 (2025-04-13)


## v0.3.0 (2025-04-13)

### Features

- **plugin-interface**: Add PluginInvalidInput exception for invalid input data
  ([`cac573a`](https://github.com/shawnoster/uvws/commit/cac573a6d17681b2cbb37ba48dd106c1ee97cd30))

- **sqa-api**: Add custom exception class for plugin errors
  ([`bc0a9a1`](https://github.com/shawnoster/uvws/commit/bc0a9a1b4fcf8d7e59d9d179548755d046cdb0d9))


## v0.2.0 (2025-04-13)

### Features

- Add _validate_credentials method to PluginBase for credential validation
  ([`3cfaf72`](https://github.com/shawnoster/uvws/commit/3cfaf72333d3b1b8ec8feb39b359de88b98818a0))


## v0.1.2 (2025-04-13)

### Bug Fixes

- Update project metadata in pyproject.toml
  ([`d7b7e15`](https://github.com/shawnoster/uvws/commit/d7b7e15e1462c87199a42d1c44577ee906e82c89))

- Update version to 2.1.1 for plugin-one and sqa
  ([`4ca715f`](https://github.com/shawnoster/uvws/commit/4ca715f1f5913c19733f7dce1854c175472fabfe))


## v0.1.1 (2025-04-13)


## v0.1.0 (2025-04-13)

### Bug Fixes

- Correct path in version_variables for semantic release configuration
  ([`4380f8e`](https://github.com/shawnoster/uvws/commit/4380f8e45b938dba2d9de22e9d05927a9f0a18ff))

- Update tag format for plugin-one and add semantic release configuration for sqa-cli
  ([`e823ed4`](https://github.com/shawnoster/uvws/commit/e823ed4a1d01470cac19a08bc96087ca009777c7))

- Update version numbers for plugin-one and sqa-cli to 2.0.4 and 0.3.1 respectively
  ([`b73b4e1`](https://github.com/shawnoster/uvws/commit/b73b4e1f3551075769e6d1090a6302a726ae8743))

- **core**: Add dependencies for the project
  ([`385f259`](https://github.com/shawnoster/uvws/commit/385f259d8d5da747bc112b96d2847ef7e6351d7e))

- **core**: Change parameter type of collect and evaluate methods from dict to str
  ([`94be3e8`](https://github.com/shawnoster/uvws/commit/94be3e8a654521112d61b0f67ab10bc1d4a87943))

- **core**: Change parameter type of collect method from str to dict
  ([`db6d88f`](https://github.com/shawnoster/uvws/commit/db6d88f8cc4be0afc6ff2b98187173dd8c236537))

- **core**: Change parameter type of evaluate method from str to dict
  ([`aa73ad0`](https://github.com/shawnoster/uvws/commit/aa73ad0a8b93a0bfe8a7c8a72bc7e5d3e51ba659))

- **core**: Change return type of collect method from dict to str
  ([`529442f`](https://github.com/shawnoster/uvws/commit/529442f597575bd216316bf1f2c2cbe6239e8570))

- **core**: Update core package version to 0.2.3 and add rich dependency
  ([`6ffd791`](https://github.com/shawnoster/uvws/commit/6ffd7915280a3234f20f42357973a96475f07cc3))

- **svc1**: Add missing key check for input data in collect method
  ([`1c07748`](https://github.com/shawnoster/uvws/commit/1c07748d652271a2caefea088126c95019bb0bce))

- **svc1**: Improve error message for missing key in input data
  ([`a41803c`](https://github.com/shawnoster/uvws/commit/a41803cd01ffeffdf0254dec5d162206faeff345))

- **svc1**: Update semantic release configuration and version to 0.3.1
  ([`4a8f894`](https://github.com/shawnoster/uvws/commit/4a8f894edf3f8566da7abb42cbf05a7a7eeef168))

- **svc1**: Update version to 0.1.0 in __init__.py
  ([`0590a5b`](https://github.com/shawnoster/uvws/commit/0590a5b79d5e6ab7e71375c9844274029b87ea0b))

### Features

- **core**: Add PluginBase abstract class for plugin development
  ([`94d6203`](https://github.com/shawnoster/uvws/commit/94d6203af51f84b6ffaa414692cba7d8ede3b3f6))

- **core**: Implement Svc1Plugin with collect and evaluate methods
  ([`91858f5`](https://github.com/shawnoster/uvws/commit/91858f5d949c750e0371edba8fa6439c3a7639a0))

- **core**: Update PluginBase class to require evaluate method implementation
  ([`a6077a4`](https://github.com/shawnoster/uvws/commit/a6077a47bbfd9587b700a4ca1da2c99d0e79862a))

### Refactoring

- Refactor code structure for improved readability and maintainability
  ([`3a4e0c4`](https://github.com/shawnoster/uvws/commit/3a4e0c47631ec27e33fffc90343f51a67300bf9c))
