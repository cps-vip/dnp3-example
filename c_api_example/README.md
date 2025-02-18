# Python Extension Module Example
This method gives the most functionality and flexibility, but also the most complexity. Unlike the ctypes example, using a Python extension module allows you to call the C methods like any normal Python module. Additionally, C code is able to call Python, allowing things like using Python's logger for the dnp3 library.

## Steps
```bash
./install_module.sh

# Open another terminal in this directory

# In one, run:
source venv/bin/activate
./run_master.py

# In the other, run:
source venv/bin/activate
./run_outstation.py
```

