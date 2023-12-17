import pytest
from unittest.mock import patch, mock_open
import report_gen as rpg

# Sample data inpit for testing
SAMPLE_START_LOG = """
SVF2018-05-24_12:02:58.917
NHR2018-05-24_12:02:49.914
"""

SAMPLE_END_LOG = """
SVF2018-05-24_12:04:03.332
NHR2018-05-24_12:04:02.979
"""

SAMPLE_ABBREVIATIONS_TXT = """
SVF_Sebastian Vettel_FERRARI
NHR_Nico Hulkenberg_RENAULT
"""

class TestQ1Processor:
    @patch("builtins.open", new_callable=mock_open, read_data=SAMPLE_START_LOG)
    def test_read_start_log(self, mock_file):
        processor = rpg.Q1Processor("/some/path")
        start_times = processor.read_log_file(processor.start_log_path)
        assert len(start_times) == 2
        assert start_times["SVF"] is not None

        #to complete the rest of methods


class TestQ1ReportGenerator:
    @patch("report_gen.Q1Processor.process_files")
    def test_rank_drivers(self, mock_process_files):
        processor = Q1Processor("/some/path")
        report_generator = Q1ReportGenerator(processor)
        ranked_drivers = report_generator.rank_drivers()
        assert len(ranked_drivers) > 0

    #to complete the rest of methods