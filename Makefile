black:
	black vntin tests setup.py --check

flake:
	flake8 vntin tests setup.py

test:
	pytest

interrogate:
	interrogate -vv --ignore-nested-functions --ignore-semiprivate --ignore-private --ignore-magic --ignore-module --ignore-init-method --fail-under 100 tests
	interrogate -vv --ignore-nested-functions --ignore-semiprivate --ignore-private --ignore-magic --ignore-module --ignore-init-method --fail-under 100 clumper

check: black flake test interrogate

develop:
	pip install mkdocs==1.1 mkdocs-material==4.6.3 mkdocstrings==0.8.0 jinja2==3.0.0

install:
	pip install rich
	python -m pip install -e .

install-dev: install
	python -m pip install -e ".[dev]"
	pre-commit install

install-test: install
	python -m pip install -e ".[test]"
	python -m pip install -e ".[all]"

pypi:
	python setup.py sdist
	python setup.py bdist_wheel --universal
	twine upload dist/*

deploy:
	mkdocs gh-deploy

serve:
	mkdocs serve

clean:
	rm -rf **/.ipynb_checkpoints **/.pytest_cache **/__pycache__ **/**/__pycache__ .ipynb_checkpoints .pytest_cache