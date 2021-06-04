
# resolve
conan install . -s compiler=gcc -s compiler.version=4.9 -s compiler.libcxx=libstdc++ --build

# build
premake4 gmake
make
# (or mingw32-make if in windows-mingw)

./MyApplication
# Hello World Release!
