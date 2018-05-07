from cffi import FFI
from os import path
import platform


HERE = path.dirname(path.realpath(__file__))
INCLUDE_FOLDER = path.join(HERE, 'include')
LINUX = platform.system() == 'Linux'

# ----------
# BUILD WRAPPER
# ----------
ffibuilder = FFI()

# prepare cdef
cdef = ""
#if LINUX:
#    cdef += open(path.join(HERE, 'cdef', 'stddef.cdef.h')).read()
cdef += open(path.join(HERE, 'cdef', 'pyopengles2.cdef.h')).read()

ffibuilder.cdef(cdef)


# prepare source
source = '''
#include <GLES2/gl2.h>
#include <GLES2/gl2platform.h>
'''

ffibuilder.set_source(
    '_pyopengles2',
    source,
    libraries=['GLESv2'],
    extra_compile_args=["-I"+INCLUDE_FOLDER]
)


if __name__ == '__main__':
    ffibuilder.compile(verbose=True)
