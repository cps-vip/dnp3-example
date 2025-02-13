from time import sleep

from devices.master import Master

if __name__ == '__main__':
    master_dnp3_address = 1
    master_name = "Master"
    outstation_dnp3_address = 1024
    outstation_ip = "127.0.0.1:20000"

    master = Master(master_name, master_dnp3_address)
    master.add_outstation(outstation_dnp3_address, outstation_ip)
    master.activate()

    sleep(10)

    master.deactivate()
    master.destroy()
