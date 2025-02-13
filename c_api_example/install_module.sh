#!/usr/bin/env bash

if [ ! -d "venv" ]; then
    # First create and activate the virtual environment
    python -m venv venv
    source venv/bin/activate

    # Install dependencies to build the extension module
    pip install build
    pip install setuptools
else
    source venv/bin/activate
fi

cd dnp3-module
mkdir -p src/dnp3/include
mkdir -p src/dnp3/lib

# Use CMake to download the Rust DNP3 library
# Also want to set the DNP3_RUST_TARGET variable from the CMake as an env variable
mkdir -p build
cd build
export DNP3_RUST_TARGET="$(cmake .. -DCMAKE_EXPORT_COMPILE_COMMANDS=1 2>&1 | grep DNP3_RUST_TARGET | awk '{print $NF}')"

cp _deps/dnp3-src/include/dnp3.h ../src/dnp3/include
cp "_deps/dnp3-src/lib/$DNP3_RUST_TARGET/libdnp3_ffi.so" ../src/dnp3/lib

cd ..
python -m build
pip install .

