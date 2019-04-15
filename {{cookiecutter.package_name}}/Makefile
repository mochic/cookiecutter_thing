init:
	python -m pip install pip -U
	python -m pip install pipenv
	python -m pipenv install . --dev

check:
	python -m pipenv run flake8

test: check
	python -m pipenv run python -m pytest