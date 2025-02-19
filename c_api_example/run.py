import logging

from time import sleep
from devices.outstation import Outstation
from devices.master import Master

logging.basicConfig(filename="simulation.log", level=logging.INFO, filemode="w+")
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    master_dnp3_addr = 1

    outstation1_addr = (1024, "127.0.0.1:20000")
    outstation1 = Outstation("Outstation 1", 
                             outstation1_addr[0],
                             master_dnp3_addr,
                             outstation1_addr[1])
    outstation1.activate()
    logger.info("Activated outstation 1")


    outstation2_addr = (1025, "127.0.0.1:20001")
    outstation2 = Outstation("Outstation 2", 
                             outstation2_addr[0],
                             master_dnp3_addr,
                             outstation2_addr[1])
    outstation2.activate()
    logger.info("Activated outstation 2")


    master = Master("Master", master_dnp3_addr)
    master.add_outstations([outstation1, outstation2])
    master.activate()
    logger.info("Activated master station")

    sleep(2)

    logger.info("Deactivating outstation 1")
    outstation1.deactivate()
    outstation1.destroy()

    logger.info("Deactivating outstation 2")
    outstation2.deactivate()
    outstation2.destroy()

    logger.info("Deactivating master station")
    master.deactivate()
    master.destroy()
