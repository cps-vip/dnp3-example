# Python Extension Module Example
## Instructions
If on the Debian VM, install the following packages:

```bash
sudo apt install -y python3 python-is-python3 pip python3.11-venv cmake
```

Then, run the following commands:
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

