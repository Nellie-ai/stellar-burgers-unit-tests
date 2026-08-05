# Provenance and reuse decision

## Audited sources

- Educational fork: `Nellie-ai/Diplom_1`
- Reviewed reference: branch `develop1`, commit `8d53baf4243ead6b06f848c65becc0055c52bee5`
- Upstream starter repository: `Yandex-Practicum/qa-python-project`
- Audit date: 2026-08-05

## Starter-code identification

The upstream repository contains these production files:

- `__init__.py`
- `bun.py`
- `burger.py`
- `database.py`
- `ingredient.py`
- `ingredient_types.py`
- `praktikum.py`

In the reviewed fork, `__init__.py`, `bun.py`, `ingredient.py`, and `ingredient_types.py` were byte-for-byte identical to upstream. The remaining production modules differed only in package-relative imports and import ordering. They are therefore treated as upstream starter-code rather than original portfolio implementation.

## License finding

At the audit date, the upstream repository was public but contained no `LICENSE`, `LICENSE.md`, or `COPYING` file. Its README described the assignment but did not grant permission to reproduce or publish derivative copies independently.

Attribution alone was therefore not treated as sufficient permission to republish the starter files in a new independent repository.

## Clean-room decision

This portfolio copy does not include the upstream production files. The `stellar_burgers` package was written from scratch to provide only the public behavior needed by the test scenarios. Class names and the small domain API are retained so the tests remain meaningful; implementation structure, internal state, typing, data values, documentation, and package name are new.

The tests preserve the reviewed scenario design: fixtures, parameterization, spec-based mocks, shared data, test classes, and assertions through public methods. Imports and demo data were adapted for the new package.

The independently written code in this repository is licensed under the MIT License. That license applies only to this repository's clean-room implementation and adapted test suite; it does not grant rights to the excluded upstream starter-code. Any future public release should still recheck applicable course-publication and trademark rules.
