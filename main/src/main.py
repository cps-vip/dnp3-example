import time
from tcpserver.tcpserver import TCPServer
from outstation.outstation import Outstation

if __name__ == "__main__":
        # TODO: Figure out if this is the way you are supposed to have multiple outstations
    with (TCPServer("127.0.0.1:20000") as server1,
          TCPServer("127.0.0.1:20001") as server2,
          Outstation(1024, 1, "any") as outstation1,
          Outstation(1025, 1, "any") as outstation2):
        outstation1.bind(server1)
        outstation2.bind(server2)
        server1.run()
        server2.run()

        time.sleep(50)
