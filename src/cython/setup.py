from distutils.core import setup, Extension
from Cython.Distutils import build_ext
from distutils.extension import Extension

###
## to build: CC=g++ python setup.py build_ext --inplace
#

###
## Notes:
#
# "-Wno-narrowing" was needed because of the OID char conversions on my platform
# "../parser.c" is needed to include parser functions
# "-std=c++11" is needed due to c++11 dependency

sources = ['mercury.pyx','../dns.c','../utils.c','../parser.c']

setup(ext_modules=[Extension("mercury",
                             sources=sources,
                             language="c++",
                             extra_compile_args=["-std=c++11","-Wno-narrowing"],
                             extra_link_args=["-std=c++11",],
                             runtime_library_dirs=['../'])
                  ],
      cmdclass={'build_ext':build_ext})




