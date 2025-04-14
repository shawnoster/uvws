# CHANGELOG


## v0.5.1 (2025-04-14)

### Bug Fixes

- **plugin-one**: Replace ValueError with PluginInvalidInput for missing serviceName
  ([`194147f`](https://github.com/shawnoster/uvws/commit/194147f4027d1ed8fbdc9c7552f8f1d2f2fa3a67))

### Chores

- Add publish configuration for semantic release in plugin-one, sqa-api, and sqa-cli
  ([`7acacd9`](https://github.com/shawnoster/uvws/commit/7acacd9f33f5ba9b390d8f6efae33ed88ed312d8))


## v0.5.0 (2025-04-14)

### Refactoring

- **plugin-one**: Streamline semantic release configuration and remove unused options
  ([`67d7614`](https://github.com/shawnoster/uvws/commit/67d7614878a1c8198eb414a59625ec588a1cf84e))


## v0.4.12 (2025-04-14)

### Bug Fixes

- **plugin-one**: Update serviceName in evaluate method to 'test-four'
  ([`1a3d2a8`](https://github.com/shawnoster/uvws/commit/1a3d2a8b7de6d4d261c5cd1835f6c3574564942a))


## v0.4.11 (2025-04-14)

### Bug Fixes

- **plugin-one**: Remove 'chore' from exclude_commit_patterns for semantic release
  ([`67f4cda`](https://github.com/shawnoster/uvws/commit/67f4cdae2a8a96763a4968d738ee7446ff2f3c45))

- **plugin-one**: Update exclude_commit_patterns to match 'chores*' for semantic release
  ([`92ff0a3`](https://github.com/shawnoster/uvws/commit/92ff0a3fd4185ca36ecb03fd1a9d592241d7b5cc))


## v0.4.10 (2025-04-13)


## v0.4.9 (2025-04-13)

### Bug Fixes

- **plugin-one**: Update evaluate method to return correct serviceName
  ([`c7c20eb`](https://github.com/shawnoster/uvws/commit/c7c20eb45fa19975c3b9ab717dbafc02ead85b73))


## v0.4.8 (2025-04-13)

### Bug Fixes

- **plugin-one**: Correct return value in evaluate method to match expected output
  ([`bb3c734`](https://github.com/shawnoster/uvws/commit/bb3c7342c0e69082ff35061a6181fc27415d4499))

- **plugin-one**: Update evaluate method to return correct serviceName
  ([`0118dd9`](https://github.com/shawnoster/uvws/commit/0118dd9584895f6dda7b93ed3fb0c5080fb4dd94))


## v0.4.6 (2025-04-13)


## v0.4.5 (2025-04-13)


## v0.4.4 (2025-04-13)

### Bug Fixes

- **plugin-one**: Update dist_glob_patterns location and format in pyproject.toml
  ([`871fcb9`](https://github.com/shawnoster/uvws/commit/871fcb9ae8ae7da77dfbe99ecd4ccf283f6a4ce7))


## v0.4.3 (2025-04-13)

### Bug Fixes

- **plugin-one**: Correct error message for missing 'serviceName' key
  ([`35d82bc`](https://github.com/shawnoster/uvws/commit/35d82bcbbf8d9ce959516477b36405be1bd45cb5))

- **plugin-one**: Raise ValueError for missing serviceName key in input data
  ([`045a020`](https://github.com/shawnoster/uvws/commit/045a0206e09871d82c57cf54ae46ebdc612508da))

- **plugin-one**: Update dist_glob_patterns to include full path for package distribution
  ([`62bf8d9`](https://github.com/shawnoster/uvws/commit/62bf8d9db7e3571cd3a778f715149867bc7fcd18))

### Chores

- **plugin-one**: Update build command for consistency and add changelog sections
  ([`01d228e`](https://github.com/shawnoster/uvws/commit/01d228e4d2e5f99c018208f07892c17cdb290c59))

- **sqa-api, sqa-cli**: Add changelog sections for semantic release
  ([`c6d1600`](https://github.com/shawnoster/uvws/commit/c6d160023b9635a134f0955230a18a4898380b8c))


## v0.4.2 (2025-04-13)


## v0.4.1 (2025-04-13)

### Bug Fixes

- **plugin-one**: Correct key check and return value in collect method
  ([`a4eb52c`](https://github.com/shawnoster/uvws/commit/a4eb52ca840d79bd424132837a0b83ea1d8a4be1))

- **plugin-one**: Update build command to output to dist directory
  ([`b5189f2`](https://github.com/shawnoster/uvws/commit/b5189f2327a7dee2c8eee11860930e088ed9f1e7))

### Chores

- **plugin-one**: Refine path filters for semantic release commit parsing
  ([`476ab56`](https://github.com/shawnoster/uvws/commit/476ab56bb3d10088537ed3114a3276ced983d771))

- **release**: Remove uv installation step and update path filters for semantic release
  ([`445cedb`](https://github.com/shawnoster/uvws/commit/445cedb6883a78782ec7c697e8910a0c1e012a2b))


## v0.4.0 (2025-04-13)


## v0.3.0 (2025-04-13)


## v0.2.0 (2025-04-13)

### Chores

- Remove outdated changelogs for plugin-one, sqa-api, and sqa-cli
  ([`cf6fcc1`](https://github.com/shawnoster/uvws/commit/cf6fcc19e6331c9ddba8582cf6d81c70e8086e62))


## v0.1.2 (2025-04-13)

### Bug Fixes

- Update version to 2.1.1 for plugin-one and sqa
  ([`4ca715f`](https://github.com/shawnoster/uvws/commit/4ca715f1f5913c19733f7dce1854c175472fabfe))

### Chores

- Standardize commit message format and add dist glob patterns for plugin-one, sqa-api, and sqa-cli
  ([`9a85a5e`](https://github.com/shawnoster/uvws/commit/9a85a5ef9e27fe4dedac7667c104d6dab0c3687f))


## v0.1.1 (2025-04-13)

### Bug Fixes

- Update tag format for plugin-one and add semantic release configuration for sqa-cli
  ([`e823ed4`](https://github.com/shawnoster/uvws/commit/e823ed4a1d01470cac19a08bc96087ca009777c7))

- Update version numbers for plugin-one and sqa-cli to 2.0.4 and 0.3.1 respectively
  ([`b73b4e1`](https://github.com/shawnoster/uvws/commit/b73b4e1f3551075769e6d1090a6302a726ae8743))

### Chores

- **plugin_one-release**: Release plugin_one@0.1.0 [skip ci]
  ([`c41c87c`](https://github.com/shawnoster/uvws/commit/c41c87c57723f771b663ae832594efb6cae0275c))

- **plugin_one-release**: Release plugin_one@0.1.0 [skip ci]
  ([`c6a3caf`](https://github.com/shawnoster/uvws/commit/c6a3caf0dd5a2299b91d2c74c74d72b597f70c56))

- **plugin_one-release**: Release plugin_one@0.1.1 [skip ci]
  ([`26d295d`](https://github.com/shawnoster/uvws/commit/26d295df50a403e2a802cebd85646c7aff87f54c))

### Refactoring

- Refactor code structure for improved readability and maintainability
  ([`3a4e0c4`](https://github.com/shawnoster/uvws/commit/3a4e0c47631ec27e33fffc90343f51a67300bf9c))
