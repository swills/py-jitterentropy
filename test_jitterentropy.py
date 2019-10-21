#!/usr/bin/env python

import jitterentropy

print(jitterentropy.version())
randbytes = jitterentropy.getrandbytes(512)
print(''.join('{:x}'.format(x) for x in randbytes))
