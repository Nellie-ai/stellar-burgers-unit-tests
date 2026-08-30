# Stellar Burgers Unit Tests

A compact portfolio project demonstrating unit-test design for a small burger domain model. The suite uses pytest fixtures, parameterization, spec-based mocks, shared test data, and enforced 100% line coverage.

## What is tested

- `Bun`: name and price accessors;
- `Ingredient`: type, name, and price accessors;
- `Burger`: bun selection, ingredient addition, removal and movement, total price, and receipt formatting;
- `Database`: available buns and ingredients.

The suite contains 13 test methods that expand to exactly 22 collected test cases.

## Project structure

```text
stellar_burgers/      clean-room demo implementation
tests/                unit tests, fixtures, and shared data
.github/workflows/    compile, collection, test, and coverage CI
pyproject.toml        pytest and coverage configuration
requirements-dev.txt fully pinned test environment
```

## Local setup

Python 3.12 is supported; the verified baseline is Python 3.12.13.

```bash
python -m venv .venv
python -m pip install --requirement requirements-dev.txt
```

Activate the virtual environment using the command appropriate for your operating system, then run:

```bash
python -m compileall -q stellar_burgers tests
python -m pytest --collect-only -q -p no:cacheprovider
python -m pytest -p no:cacheprovider --cov=stellar_burgers --cov-report=term-missing --cov-report=html
```

Coverage is configured to fail below 100%. The generated `htmlcov/`, `coverage.xml`, cache, and Allure directories are intentionally excluded from version control.

## Design notes

- Fixtures live in `tests/conftest.py`.
- Shared values live in `tests/data.py`.
- Collaborators are mocked with `Mock(spec=...)`.
- Parameterization covers multiple values and collection operations without duplicating test logic.
- Assertions target observable behavior through public methods.

## Provenance

The test scenarios were adapted from an educational course project reviewed at commit `8d53baf4243ead6b06f848c65becc0055c52bee5`. The historical source repository is not required to access or run this standalone clean-room portfolio project.

The original production starter files from `Yandex-Practicum/qa-python-project` are not included because the upstream repository does not contain a license or an explicit reuse grant. The `stellar_burgers` package is an independently written minimal demo implementation with new structure and data. See [PROVENANCE.md](PROVENANCE.md) for details.

This repository is an independent portfolio exercise and is not affiliated with or endorsed by Yandex Practicum.

## License

The independently written code in this repository is available under the [MIT License](LICENSE). See [PROVENANCE.md](PROVENANCE.md) for the boundary between this portfolio implementation and the excluded upstream starter-code.
