import os

from ctypes import CDLL, c_char_p, c_int
from config_classes import RuntimePtr, ServerPtr

# Have to supply absolute path if the shared library isn't in /usr/lib
# Don't want to actually install these libraries in /usr/lib since they are just for testing
libpath = os.path.abspath(os.path.join(os.path.dirname(__file__), r'../../build/libtcpserver.so'))
lib = CDLL(libpath)

class TCPServer:
    def __init__(self, socket_addr: str):
        init_runtime = lib.init_runtime
        init_runtime.restype = RuntimePtr
        self._runtime = init_runtime()
        if self._runtime is None:
            raise Exception()

        init_server = lib.init_server
        init_server.argtypes = [RuntimePtr, c_char_p]
        init_server.restype = ServerPtr
        self.server = init_server(self._runtime, socket_addr.encode())
        if self.server is None:
            raise Exception()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        destroy_server = lib.destroy_server
        destroy_server.argtypes = [ServerPtr]
        destroy_server.restype = None
        destroy_server(self.server)

        destroy_runtime = lib.destroy_runtime
        destroy_runtime.argtypes = [RuntimePtr]
        destroy_server.restype = None
        destroy_runtime(self._runtime)

    def run(self):
        start_server = lib.start_server
        start_server.argtypes = [ServerPtr]
        start_server.restype = c_int
        if start_server(self.server) == -1:
            raise Exception()

