import pytest
from unittest.mock import patch, MagicMock
import report_gen_cli

class TestCLI:
    @patch('argparse.ArgumentParser.parse_args')
    @patch('report_gen.Q1ReportGenerator.print_report')
    def test_cli_default_behavior(self, mock_print_report, mock_parse_args):
        mock_parse_args.return_value = MagicMock(files="/some/path", order='asc', driver=None)
        report_gen_cli.main()
        mock_print_report.assert_called_once()

    #To complete the rest