#!/usr/bin/env python

import jitterentropy

print(jitterentropy.version())
#randbytes = jitterentropy.getrandbytes(-10)
randbytes = jitterentropy.getrandbytes(16)
print(''.join('{:02x}'.format(x) for x in randbytes))
newFile = open("bytes", "wb")
#newFileByteArray = bytearray(jitterentropy.getrandbytes(1024))
#newFile.write(newFileByteArray)
newFileByteArray = bytearray(jitterentropy.getrandbytes(4096))
newFile.write(newFileByteArray)
# large values take a while
#newFileByteArray = bytearray(jitterentropy.getrandbytes(8000000))
#newFile.write(newFileByteArray)
