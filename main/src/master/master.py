import os

from config_classes import MasterChannelConfig, RuntimePtr, MasterChannelPtr
from ctypes import CDLL, c_void_p, c_char_p, c_uint16

# Have to supply absolute path if the shared library isn't in /usr/lib
# Don't want to actually install these libraries in /usr/lib since they are just for testing
libpath = os.path.abspath(os.path.join(os.path.dirname(__file__), r'../../build/libmaster.so'))
lib = CDLL(libpath)


class Master:
    def __init__(self, master_addr: int, endpoint_ip_port: str):
        init_runtime = lib.init_runtime
        init_runtime.restype = RuntimePtr
        self._runtime = init_runtime()
        if self._runtime is None:
            raise Exception()

        self._master_channel = None

        create_master_channel_config = lib.create_master_channel_config
        create_master_channel_config.argtypes = [c_uint16]
        create_master_channel_config.restype = MasterChannelConfig
        self.config = create_master_channel_config(master_addr)

        create_tcp_channel = lib.create_tcp_channel
        create_tcp_channel.argtypes = [RuntimePtr, c_uint16, c_char_p, MasterChannelPtr]
        create_tcp_channel.restype = MasterChannelPtr
        self._master_channel = create_tcp_channel(self._runtime, master_addr, self._master_channel, endpoint_ip_port)
        

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self._master_channel is not None:
            destroy_master_channel = lib.destroy_master_channel
            destroy_master_channel.argtypes = [MasterChannelPtr]
            destroy_master_channel.restype = None
            destroy_master_channel(self._master_channel)
        if self._runtime is not None:
            destroy_runtime = lib.destroy_runtime
            destroy_runtime.argtypes = [RuntimePtr]
            destroy_server.restype = None
            destroy_runtime(self._runtime)
    
    def run(self, outstation_addr: int):
        run_channel = lib.run_channel
        run_channel.argtypes = [MasterChannelPtr, c_uint16]
        run_channel.restype = c_uint16
        if run_channel(self._master_channel, outstation_addr) == -1:
            raise Exception()