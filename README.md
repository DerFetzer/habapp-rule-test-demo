# habapp-rule-test-demo

This demo shows how testing of rules is possible with HABApp 1.0.8.
It uses the [SimpleRuleRunner](https://github.com/spacemanspiff2007/HABApp/blob/b3ace7579950f5d8d20b0eb709044533a36de37f/tests/rule_runner/rule_runner.py) from the HABApp repo.
Inspiration and some code has been taken from nobbi123.

To make testing possible it is necessary that rule declaration and instantiation is done in separate files. That is why the rule is inside the `lib` folder.

## Disclaimer
This is a bit hacky at the moment. The final goal should be to implement most of the testing framework upstream.

## Usage
To run the tests you need [poetry](https://python-poetry.org/) and optionally [poethepoet](https://github.com/nat-n/poethepoet).
Run following commands inside the cloned repository:

```Bash
# prepare environment
poetry install

# run tests
# with poe
poe test

# without poe
poetry run python run_tests.py
```
