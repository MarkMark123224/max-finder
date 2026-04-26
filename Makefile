run:
	python app/main.py

test:
	pytest

doctest:
	python -m doctest app/main.py

format:
	black .

lint:
	flake8 .

security:
	pip install safety
	safety check
