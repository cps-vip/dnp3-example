import logging

from time import sleep
from devices.outstation import Outstation
from devices.master import Master

logging.basicConfig(filename="simulation.log", level=logging.INFO, filemode="w+")
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    outstation1_addr = (1024, "127.0.0.1:20000")
    outstation1 = Outstation("Outstation 1", 
                             outstation1_addr[0],
                             1,
                             outstation1_addr[1])
    outstation1.activate()
    outstation1._tcpserver.log_stuff()
    logger.info("Stuff")

    sleep(2)
    outstation1.deactivate()
    outstation1.destroy()

