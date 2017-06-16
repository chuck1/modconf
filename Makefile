
pkg=$(shell cat NAME.txt)

test:
	python3 -m unittest $(pkg).tests

upload:
	@mkdir -p dist
	@rm -f dist/*whl
	python3 setup.py bdist_wheel
	twine upload dist/*whl

