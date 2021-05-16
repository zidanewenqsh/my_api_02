# file: setup.py
# python setup.py build_ext --inplace
from distutils.core import setup
from Cython.Build import cythonize

setup(name='Loop Test app',
      ext_modules=cythonize("loop.pyx"))