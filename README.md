# Max Finder

## Встановлення
git clone https://github.com/USERNAME/max-finder.git
cd max-finder

python -m venv venv
source venv/bin/activate  # Lin
venv\Scripts\activate     # Win

pip install -r requirements.txt

## Запуск
make run
або
python app/main.py

## Тести
make test

Doctest:
make doctest

## Форматування
make format
make lint

## Перевірка вразливостей
make security

## Git hooks
pip install pre-commit
pre-commit install

## Залежності
pytest
black
flake8
safety
sentry-sdk

## .gitignore
__pycache__/
venv/
.env
*.pyc
.idea/
.vscode/
