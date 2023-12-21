from unittest.mock import patch
import report_gen_cli as cli

# Mock data for testing
MOCK_FILES_PATH = "/mock/path"
MOCK_DRIVER_NAME = "Sebastian Vettel"

class TestCLI:
    @patch('report_gen_cli.rpg.Q1Processor')
    @patch('report_gen_cli.rpg.Q1ReportGenerator')
    def test_cli_default_behavior(self, mock_report_generator, mock_processor):
        with patch('sys.argv', ['report_gen_cli.py', '--files', MOCK_FILES_PATH]):
            cli.main()
            mock_processor.assert_called_once_with(MOCK_FILES_PATH)
            mock_report_generator.assert_called_once()

    @patch('report_gen_cli.rpg.Q1Processor')
    @patch('report_gen_cli.rpg.Q1ReportGenerator')
    def test_cli_descending_order(self, mock_report_generator, mock_processor):
        with patch('sys.argv', ['report_gen_cli.py', '--files', MOCK_FILES_PATH, '--order', 'desc']):
            cli.main()
            mock_processor.assert_called_once_with(MOCK_FILES_PATH)
            mock_report_generator.return_value.print_report.assert_called_once_with('desc')

    @patch('report_gen_cli.rpg.Q1Processor')
    @patch('report_gen_cli.rpg.Q1ReportGenerator')
    def test_cli_specific_driver(self, mock_report_generator, mock_processor):
        with patch('sys.argv', ['report_gen_cli.py', '--files', MOCK_FILES_PATH, '--driver', MOCK_DRIVER_NAME]):
            cli.main()
            mock_processor.assert_called_once_with(MOCK_FILES_PATH)
            mock_report_generator.return_value.driver_info.assert_called_once_with(MOCK_DRIVER_NAME)