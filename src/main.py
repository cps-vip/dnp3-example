import ctypes
import pathlib
# TODO: import TCP_Server, Master, and Oustation objects

if __name__ == "__main__":
    # Load the shared library into ctypes
    libmaster = pathlib.Path().absolute() / "build/libmaster.so"
    liboutstation = pathlib.Path().absolute() / "build/liboutstation.so"
    libtcpserver = pathlib.Path().absolute() / "build/libtcpserver.so"
    # c_libmaster = ctypes.CDLL(libmaster)
    # c_liboutstation = ctypes.CDLL(liboutstation)

    tcp_server = TCP_Server('127.0.0.1')

    # Start at address 1 since addr 0 is usually used for RTU
    master = Master(tcp_server, 1)

    outstation_0 = Outstation(tcp_server, 1000)
    outstation_1 = Outstation(tcp_server, 1001)


