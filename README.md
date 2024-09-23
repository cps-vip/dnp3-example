# DNP3 Example
## Default Example
default_example contains the [example code](https://github.com/stepfunc/dnp3/tree/1.6.0/ffi/bindings/c) straight from the dnp3 repo.

See the following for running it:

```bash
cd default_example
mkdir build
cd build

# Exporting compile commands allows for proper LSP integration
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=1 ..
cmake --build .

# At this point, open another terminal in the same directory

# In the first, run this:
./outstation_example tcp
# In the second, run this:
./master_example tcp

# In the terminal running the outstation, try entering 'co' (which stands for counter)
# In the terminal running the master, you should see output that looks like 'Counter 7: Value=1 Flags=0x01 Time=0'
# Enter 'co' again and the value will increment as expected
```

## Custom Example

*NOTHING HERE WORKS YET*

Everything outside default_example is where our custom integration example lives. 
* main.py will create a Master and Outstations
* Most of the actual communication logic will be in the C files, while the Python files (besides main.py) will expose a class that calls functions from the C files.

Note that the CMakeLists.txt is different between default_example and the one in src/. This is because we create a shared library out of the C files to call from the Python files.

