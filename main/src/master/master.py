import os

from config_classes import MasterChannelConfig, RuntimePtr
from ctypes import CDLL, c_void_p, c_char_p, c_uint16

# Have to supply absolute path if the shared library isn't in /usr/lib
# Don't want to actually install these libraries in /usr/lib since they are just for testing
libpath = os.path.abspath(os.path.join(os.path.dirname(__file__), r'../../build/liboutstation.so'))
lib = CDLL(libpath)

class MasterChannelPtr(c_void_p):
    pass

class Master:
    def __init__(self, master_addr: int, runtime: RuntimePtr):
        self._master_channel = None
        self.runtime = runtime

        create_master_channel_config = lib.create_master_channel_config
        create_master_channel_config.argtypes = [c_uint16]
        create_master_channel_config.restype = MasterChannelConfig
        self.config = create_master_channel_config(master_addr)
        

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self._master_channel is not None:
            destroy_master_channel = lib.destroy_master_channel
            destroy_master_channel.argtypes = [MasterChannelPtr]
            destroy_master_channel.restype = None
            destroy_master_channel(self._master_channel)
    
    def create_and_run_tcp_channel(self, runtime: RuntimePtr, master_addr: int, outstation_addr: int):
        run_tcp_channel = lib.run_tcp_channel
        run_tcp_channel.argtypes = [RuntimePtr, c_uint16, c_uint16, MasterChannelPtr]
        run_tcp_channel.restype = c_uint16
        err = run_tcp_channel(runtime, master_addr, outstation_addr, this._master_channel)

    # Where are methods such as destroy_master_channel that are declared in dnp3.h but have no function body actually defined?
    # Need to make sure that a shared runtime is created.