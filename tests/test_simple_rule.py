from HABApp.openhab.items import NumberItem, StringItem, SwitchItem
from pendulum import duration

from rules.simple_rule import SimpleRule
from tests.helper.base_test import BaseTest
from tests.helper.oh_item import add_mock_item, item_state_change_event


class TestSimpleRule(BaseTest):
    def setUp(self) -> None:
        super().setUp()

        self.temp = add_mock_item(NumberItem, "Temperature", 50)
        self.heating = add_mock_item(SwitchItem, "Heating", "ON")
        self.message = add_mock_item(StringItem, "Message", "")

        self.rule = SimpleRule()

    def test_heating(self):
        self.assertEqual(self.message.get_value(), "")

        item_state_change_event(self.temp.name, 4)
        self.assertEqual(self.heating.get_value(), "ON")

        item_state_change_event(self.temp.name, 15)
        self.assertEqual(self.heating.get_value(), "OFF")

        self.assertEqual(self.message.get_value(), "")
        self._runner.advance_time_by(duration(seconds=1))
        self.assertNotEqual(self.message.get_value(), "")
