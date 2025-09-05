# Steps

Initial setup (only run once):

```bash
# Install uv
sudo apt install uv

# Create virtual environment with free-threading enabled (version 3.14t)
uv venv --python 3.14t venv

# Active the virtual environment
source venv/bin/activate

# Install build dependencies (only dependencies for building should be here, dependencies that the code uses belongs in pyproject.toml)
uv pip install build setuptools

# Make build directory for CMake
mkdir -p build
cd build

# Use CMake to bring in the Rust dnp3 library
DNP3_RUST_TARGET="$(cmake .. -DCMAKE_EXPORT_COMPILE_COMMANDS=1 2>&1 | grep DNP3_RUST_TARGET | awk '{print $NF}')"

# Copy the files we need
cp _deps/dnp3-src/include/dnp3.h ../src/dnp3
cp "_deps/dnp3-src/lib/$DNP3_RUST_TARGET/libdnp3_ffi.so" ../src/dnp3
cd ..
```

After setup:

```bash
# If not already in the venv
source venv/bin/activate

# Builds the Python extension module based on setup.py and pyproject.toml
CFLAGS="-O0 -g3" python -m build

# Installs the extension module to the venv
# Note the name of the .whl may be slightly different; use the one that is there
uv pip install dist/dnp3-module-0.1.0-cp314-cp314t-linux_x86_64.whl

# Now run, specifying whether or not we want to use the GIL
python -Xgil=0 run.py

# If you want to use gdb:
gdb -args python -Xgil=0 run.py
```

