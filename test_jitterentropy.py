#!/usr/bin/env python

import jitterentropy

print(jitterentropy.version())
randbytes = jitterentropy.getrandbytes(2048)
print(''.join('{:02x}'.format(x) for x in randbytes))
