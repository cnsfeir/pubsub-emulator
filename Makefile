include .env
export

.PHONY: \
  linters \
  login \
  start

linters:
	@poetry run python -m black --check --line-length=120 .
	@poetry run python -m flake8 --config .flake8
	@poetry run python -m pylint --rcfile=.pylintrc --recursive=y --ignore=.venv --disable=fixme .
	@poetry run python -m mypy --config-file mypy.ini .

login:
	@gcloud config configurations activate $(PROJECT_ID)
	@gcloud auth application-default login

start:
	@gcloud beta emulators pubsub start --project=$(PROJECT_ID)
