.PHONY: \
  linters


# Runs linters
linters:
	@if [ ! -d ".venv" ]; then \
		echo "Virtual environment not found. Creating one..."; \
		make setup_venv; \
	fi

	poetry run python -m black --check --line-length=120 .
	poetry run python -m flake8 --config .flake8
	poetry run python -m pylint --rcfile=.pylintrc --recursive=y --ignore=.venv --disable=fixme .
	poetry run python -m mypy --config-file mypy.ini .
