import logging

from time import sleep
from devices.outstation import Outstation
from devices.master import Master

logging.basicConfig(filename="simulation.log", level=logging.INFO, filemode="w+")
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    master_dnp3_addr = 1
    master = Master("Master", master_dnp3_addr)

    master.create_channel(1024, "127.0.0.1:20000")
    master.activate()

    sleep(2)

    master.deactivate()
    master.destroy()
