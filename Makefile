.PHONY: check dist release test lint


check:
	python setup.py check

dist:
	python setup.py sdist --formats=gztar bdist_wheel

release:
	twine upload dist/*

test:
	pytest .

lint:
	black .
	flake8 .