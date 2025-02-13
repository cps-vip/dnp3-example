from tcpserver.tcpserver import TCPServer
from outstation.outstation import Outstation

if __name__ == "__main__":
    with (TCPServer("127.0.0.1:20000") as server,
          Outstation(1024, 1, "any") as outstation):
        # Binds the outstation to the TCP server
        outstation.bind(server)

        # Start the TCP server
        server.run()

        # Start the main input loop of the outstation
        outstation.run()
