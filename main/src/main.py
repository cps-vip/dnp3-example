import time
from tcpserver.tcpserver import TCPServer
from outstation.outstation import Outstation
from master.master import Master

if __name__ == "__main__":
        # TODO: Figure out if this is the way you are supposed to have multiple outstations
    with (TCPServer("127.0.0.1:20000") as server1,
          Outstation(1024, 1, "any") as outstation1,
          Master(1, "127.0.0.1:20000") as master1):
        outstation1.bind(server1)
        server1.run()
        master1.run(1024)

        time.sleep(50)
