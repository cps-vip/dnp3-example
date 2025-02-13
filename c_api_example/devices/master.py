from .device import Device, DeviceState

from dnp3 import master

class Master(Device):
    def __init__(self, name: str, master_dnp3_addr: int):
        super().__init__(name)
        self._master_dnp3_addr = master_dnp3_addr

        self._runtime = master.init_runtime()
        self._config = master.create_master_channel_config(master_dnp3_addr)

        self._channels = {}
        self.state = DeviceState.INITIALIZED

    def add_outstation(self, outstation_dnp3_addr: int, outstation_socket_addr: str):
        # Typically one association per channel:
        # https://docs.stepfunc.io/dnp3/1.6.0/guide/docs/api/master/terminology
        master_channel = master.create_tcp_channel(self._runtime, self._master_dnp3_addr, outstation_socket_addr, self._config)
        association_id = master.add_association(master_channel, outstation_dnp3_addr)

        # Note: in the C API, the association ID is the same as the outstation 
        # address, meaning we wouldn't need the dict to also store the association ID. 
        # However, better practice to assume that this could change.
        self._channels[outstation_dnp3_addr] = (master_channel, association_id)

        master.create_poll(master_channel, association_id)


    # Implement abstract method in Device base class
    def destroy(self) -> None:
        self.state = DeviceState.DESTROYED

    # Implement abstract method in Device base class
    def activate(self) -> None:
        # For now, activate/deactivate/destroy will do for every channel
        if self.state == DeviceState.INITIALIZED or self.state == DeviceState.INACTIVE:
            for channel, _ in self._channels.values():
                master.enable_master_channel(channel)
            self.state = DeviceState.ACTIVE
        else:
            raise Exception("Cannot activate Master from state")

    # Implement abstract method in Device base class
    def deactivate(self) -> None:
        if self.state != DeviceState.ACTIVE:
            raise Exception("Trying to deactivate master from bad state")

        for channel, _ in self._channels.values():
            master.disable_master_channel(channel)
        self.state = DeviceState.INACTIVE

