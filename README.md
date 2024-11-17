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

```bash
cd main
mkdir build
cd build

# Build the outstation, TCP server, and master shared libraries
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=1 ..
make

cd ../src
python run_outstation.py

# Open another terminal in the same directory
python run_master.py

# Now try typing commands in either terminal; should work the same as the default example
```

TODO: rest of documentation
