from HABApp.openhab.items import NumberItem, SwitchItem

from tests.helper.oh_item import add_mock_item, item_state_change_event
from tests.helper.base_test import BaseTest

from lib.simple_rule import SimpleRule


class TestSimpleRule(BaseTest):
    def setUp(self) -> None:
        super().setUp()

        self.temp = add_mock_item(NumberItem, "Temperature", 50)
        self.heating = add_mock_item(SwitchItem, "Heating", "ON")

        self.rule = SimpleRule()

    def test_heating(self):
        item_state_change_event(self.temp.name, 4)
        self.assertEqual(self.heating.get_value(), "ON")

        item_state_change_event(self.temp.name, 15)
        self.assertEqual(self.heating.get_value(), "OFF")
