# CHANGELOG


## v0.1.0 (2025-04-13)

### Bug Fixes

- Correct path in version_variables for semantic release configuration
  ([`4380f8e`](https://github.com/shawnoster/uvws/commit/4380f8e45b938dba2d9de22e9d05927a9f0a18ff))

- Update tag format for plugin-one and add semantic release configuration for sqa-cli
  ([`e823ed4`](https://github.com/shawnoster/uvws/commit/e823ed4a1d01470cac19a08bc96087ca009777c7))

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

### Chores

- **core-release**: Release `core@0.0.0` [skip ci]
  ([`48c6a55`](https://github.com/shawnoster/uvws/commit/48c6a55f429ac50f101ea34264024e656ddf3867))

- **core-release**: Release `core@0.1.0` [skip ci]
  ([`de3215d`](https://github.com/shawnoster/uvws/commit/de3215d78f3ff31f308234c5b5b1f036dd62f27b))

- **core-release**: Release `core@0.2.0` [skip ci]
  ([`5fc3aeb`](https://github.com/shawnoster/uvws/commit/5fc3aeb663651c396ba5e4c1edcf39eeb53f54a7))

- **core-release**: Release `core@0.2.1` [skip ci]
  ([`2e217dd`](https://github.com/shawnoster/uvws/commit/2e217dd8b3e54b18cbefd0846a960f3740f0c323))

- **core-release**: Release `core@0.2.2` [skip ci]
  ([`08a29ba`](https://github.com/shawnoster/uvws/commit/08a29bae6732b8e11ef6730ce7047d87aba866f5))

- **core-release**: Release `core@0.2.3` [skip ci]
  ([`ae22bb8`](https://github.com/shawnoster/uvws/commit/ae22bb873b81d36f0b15de58ac149943ecdba1f1))

- **core-release**: Release `core@0.3.0` [skip ci]
  ([`4d8e382`](https://github.com/shawnoster/uvws/commit/4d8e382132e003c28546e0f341a042dade60d04f))

- **core-release**: Release `core@0.3.1` [skip ci]
  ([`2dac0c8`](https://github.com/shawnoster/uvws/commit/2dac0c80796a2a46b92c736219dd28354b1db759))

- **sqa-api-release**: Release sqa-api@0.1.0 [skip ci]
  ([`71e4645`](https://github.com/shawnoster/uvws/commit/71e4645036d85acf176a0333572636efd79355bc))

- **sqa-api-release**: Release sqa-api@0.1.1 [skip ci]
  ([`f1f2576`](https://github.com/shawnoster/uvws/commit/f1f2576d4a81221cf064053f2422d86b88370fc9))

- **sqa-api-release**: Release sqa-api@0.1.2 [skip ci]
  ([`ea6b165`](https://github.com/shawnoster/uvws/commit/ea6b165a4fa0aa01e16cafc8d3529dd7e45012b3))

- **sqa-cli-release**: Release sqa-cli@0.1.0 [skip ci]
  ([`c553cb5`](https://github.com/shawnoster/uvws/commit/c553cb560ec04aa86142799fd201841266ca445b))

- **svc1-release**: Release `svc1@0.1.0` [skip ci]
  ([`5a6ea02`](https://github.com/shawnoster/uvws/commit/5a6ea028b9698e22d39178d13bfadf1065f49501))

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
