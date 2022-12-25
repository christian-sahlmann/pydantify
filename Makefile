PROJECT=pydantify
CODE_DIRS=${PROJECT} tests

# Run pytest
.PHONY: pytest
pytest:
	pdm run pytest -vs ${ARGS}

# Check if the python code needs to be reformatted
.PHONY: black
black:
	pdm run black --check ${CODE_DIRS}

# Python type check
.PHONY: mypy
mypy:
	pdm run mypy ${CODE_DIRS}

# Runn pytest, black and mypy
.PHONY: tests
tests: pytest black mypy