run:
	python app/main.py

test:
	PYTHONPATH=. pytest

doctest:
	python -m doctest -v app/main.py

lint:
	flake8 .

format:
	black .

format-check:
	black --check .

security:
	pip install safety
	safety check

all: lint format-check test doctest security
