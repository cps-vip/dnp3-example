# Default Example

default_example contains the [example code](https://github.com/stepfunc/dnp3/tree/1.6.0/ffi/bindings/c) straight from the dnp3 repo.

## Steps

```bash
mkdir build
cd build

# Exporting compile commands allows for proper LSP integration
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=1 ..
cmake --build .  # you can also run "make"

# At this point, open another terminal in the same directory

# In the first, run this:
./outstation_example tcp
# In the second, run this:
./master_example tcp

# In the terminal running the outstation, try entering 'co' (which stands for counter)
# In the terminal running the master, you should see output that looks like 'Counter 7: Value=1 Flags=0x01 Time=0'
# Enter 'co' again and the value will increment as expected
```
