from time import sleep

from devices.outstation import Outstation

if __name__ == '__main__':
    master_dnp3_addr = 1
    outstation_name = "TestOutstation"
    outstation_dnp3_addr = 1024
    outstation_socket_addr = "127.0.0.1:20000"

    outstation = Outstation(outstation_name, outstation_dnp3_addr, master_dnp3_addr, outstation_socket_addr)
    outstation.activate()

    sleep(5)

    outstation.deactivate()
    outstation.destroy()
