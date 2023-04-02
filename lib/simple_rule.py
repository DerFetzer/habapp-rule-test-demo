import logging

import HABApp
from HABApp.openhab.events import ItemStateChangedEvent, ItemStateChangedEventFilter
from HABApp.openhab.items import NumberItem, StringItem, SwitchItem

log = logging.getLogger("Rules.SimpleRule")


class SimpleRule(HABApp.Rule):
    @staticmethod
    def create_instances():
        SimpleRule()

    def __init__(self):
        super().__init__()

        self.temp = NumberItem.get_item("Temperature")
        self.heating = SwitchItem.get_item("Heating")
        self.message = StringItem.get_item("Message")

        self.temp.listen_event(self.handle_temperature, ItemStateChangedEventFilter())

    def handle_temperature(self, event: ItemStateChangedEvent):
        if event.value < 10:
            self.heating.oh_send_command("ON")
        else:
            self.heating.oh_send_command("OFF")
            self.run.soon(lambda: self.message.oh_send_command("Heating off!"))
