# Python Extension Module Example
This method gives the most functionality and flexibility, but also the most complexity. Unlike the ctypes example, using a Python extension module allows you to call the C methods like any normal Python module. Additionally, C code is able to call Python, allowing things like using Python's logger for the dnp3 library.

## Steps
```bash
./install_module.sh

source venv/bin/activate

python run.py

# To test everything worked, look at simulation.log
cat simulation.log
```
