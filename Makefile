type-check:
	mypy text_statistics/ tests/

test:
	python3 -m unittest discover

lint:
	pylint text_statistics/
	pylint --disable=duplicate-code tests/

sec-lint:
	bandit -r text_statistics/

coverage:
	coverage erase
	coverage run -m unittest discover
	coverage html

mutation-test:
	mut.py --target text_statistics --unit-test tests --disable-operator SCI \
		--colored-output

check: lint type-check sec-lint test

# Run all dev targets and produce reports
dev-report: check coverage mutation-test

build: check
	python3 setup.py sdist bdist_wheel

.PHONEY: type-check test lint sec-lint coverage mutation-test check dev-report \
	build
