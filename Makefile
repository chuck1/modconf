
pkg=$(shell cat NAME.txt)

test:
	python3 -m unittest $(pkg).tests

wheel:
	@mkdir -p dist
	@rm -f dist/*
	python3 setup.py bdist_wheel

upload: wheel
	twine upload dist/*whl

