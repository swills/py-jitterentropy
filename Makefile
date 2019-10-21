all: jitterentropy.so
jitterentropy.so: jitterentropy.c
	python setup.py build_ext --inplace --verbose
clean:
	-@rm -r jitterentropy.so build > /dev/null 2>&1
test: jitterentropy.so
	pytest -vvv
