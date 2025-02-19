# Ctypes Example
ctypes is a simple way to call C code from Python. This allows us to use the dnp3 functionality from within Python, unlike the default example where everything is done in C.

## Steps
```bash
cd main
mkdir build
cd build

# Build the outstation, TCP server, and master shared libraries
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=1 ..
cmake --build .  # you can also run "make"

cd ../src
python run_outstation.py

# Open another terminal in the same directory
python run_master.py

# Now try typing commands in either terminal; should work the same as the default example
```
