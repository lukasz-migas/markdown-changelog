.PHONY: check dist release test lint docs

check:
	uv build
	uvx twine check dist/*

dist:
	uv build

release:
	uvx twine upload dist/*

test:
	uv run pytest .

lint:
	uv run ruff check markdown_changelog tests

docs:
	uv run zensical build
