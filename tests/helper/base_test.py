import unittest
import unittest.mock

from tests.helper.rule_runner import SimpleRuleRunner
from tests.helper.oh_item import send_command


class BaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.send_command_mock_patcher = unittest.mock.patch(
            "HABApp.openhab.items.base_item.send_command",
            new=send_command,
        )
        self.addCleanup(self.send_command_mock_patcher.stop)
        self.send_command_mock = self.send_command_mock_patcher.start()

        self._runner = SimpleRuleRunner()
        self._runner.set_up()

    def tearDown(self) -> None:
        self._runner.tear_down()
