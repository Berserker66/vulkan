from distutils.core import setup
from Cython.Build import cythonize


ext_modules = cythonize("vulkan/*.pyx")

setup(
    ext_modules = ext_modules,
    include_dirs = [r"E:\Visual Studio 2017 Community\VC\Redist\MSVC\14.10.25017\onecore\x64\Microsoft.VC150.CRT"],
    name = 'vulkan',
    version = '1.0.61',
    description = 'Ultimate Python binding for Vulkan API',
    author = 'realitix',
    author_email = 'realitix@gmail.com',
    packages = ['vulkan'],
    include_package_data = True,
    install_requires = [
    'cython>=0.27.1'],
    setup_requires = [
    'cython>=0.27.1'],
    url = 'https://github.com/realitix/vulkan',
    keywords = 'Graphics,3D,Vulkan,cffi,cython',
    classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: Android",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX :: Linux",
    "Natural Language :: English",
    "Topic :: Multimedia :: Graphics",
    "Topic :: Scientific/Engineering",
    "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
