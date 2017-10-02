call "E:\Visual Studio 2017 Community\VC\Auxiliary\Build\vcvars64.bat"

set INCLUDE=C:\Program Files (x86)\Windows Kits\10\Include\10.0.15063.0\ucrt;C:\Program Files (x86)\Visual C++ BuildTools\VC\Tools\MSVC\14.11.25503\include;C:\Program Files (x86)\Windows Kits\10\Include\10.0.15063.0\shared
set LIB=C:\Program Files (x86)\Windows Kits\10\Lib\10.0.15063.0\ucrt\x64;E:\Visual Studio 2017 Community\VC\Tools\MSVC\14.11.25503\lib\x64;C:\Program Files (x86)\Windows Kits\10\Lib\10.0.15063.0\um\x64
py -3.6 cython_setup.py build_ext --inplace