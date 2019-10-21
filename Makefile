all: jitterentropy.so
jitterentropy.so: jitterentropy.c
	python setup.py build_ext --inplace --verbose
clean:
	-rm -r jitterentropy.so build
test: jitterentropy.so
	pytest -vvv
