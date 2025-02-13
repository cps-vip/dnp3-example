import os

from ctypes import CDLL, c_char_p, c_uint16, c_int

from config_classes import OutstationConfig, ServerPtr, AddressFilterPtr, OutstationPtr
from tcpserver.tcpserver import TCPServer

# Have to supply absolute path if the shared library isn't in /usr/lib
# Don't want to actually install these libraries in /usr/lib since they are just for testing
libpath = os.path.abspath(os.path.join(os.path.dirname(__file__), r'../../build/liboutstation.so'))
lib = CDLL(libpath)

class Outstation:
    def __init__(self, outstation_addr: int, master_addr: int, address_filter: str):
        """ 
        Address filter currently can only be "any" or a wildcard IPv4 address
        """
        self._outstation = None

        create_address_filter = lib.create_address_filter
        create_address_filter.argtypes = [c_char_p]
        create_address_filter.restype = AddressFilterPtr
        self._address_filter = create_address_filter(address_filter.encode())
        if self._address_filter.value is None:
            raise Exception()

        create_outstation_config = lib.create_outstation_config
        create_outstation_config.argtypes = [c_uint16, c_uint16]
        create_outstation_config.restype = OutstationConfig
        self.config = create_outstation_config(outstation_addr, master_addr)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        destroy_address_filter = lib.destroy_address_filter
        destroy_address_filter.argtypes = [AddressFilterPtr]
        destroy_address_filter.restype = None
        destroy_address_filter(self._address_filter)

        if self._outstation is not None:
            destroy_outstation = lib.destroy_outstation
            destroy_outstation.argtypes = [OutstationPtr]
            destroy_outstation.restype = None
            destroy_outstation(self._outstation)

    def bind(self, tcpserver: TCPServer):
        """
        Associates the outstation to the given TCP server. Also initializes the database.
        """
        add_outstation = lib.add_outstation
        add_outstation.argtypes = [ServerPtr, AddressFilterPtr, OutstationConfig]
        add_outstation.restype = OutstationPtr
        self._outstation = add_outstation(tcpserver.server, self._address_filter, self.config)
        if self._outstation.value is None:
            raise Exception()

        init_database = lib.init_database
        init_database.argtypes = [OutstationPtr]
        init_database.restype = None
        init_database(self._outstation)

    def run(self):
        """
        Starts the main input loop for the outstation
        """
        run_outstation = lib.run_outstation
        run_outstation.argtypes = [OutstationPtr]
        run_outstation.restype = c_int
        print("Running")
        return run_outstation(self._outstation)
