import unittest
from LogMonitoring import parse_info, identify_process, calculate_duration, log_messages
from unittest.mock import patch, mock_open

class TestLogMonitoring(unittest.TestCase):

    def test_parse_info(self):
        line = "11:40:20,scheduled task 100, START,56100"
        timestamp, process, status, pid = parse_info(line)
        # verfy if the log line is correctly split
        self.assertEqual(timestamp, "11:40:20")
        self.assertEqual(process, "scheduled task 100")
        self.assertEqual(status, "START")
        self.assertEqual(pid,"56100")

    def test_identify_process(self):
        # verify if the tasj is correctly identified
        self.assertEqual(identify_process("scheduled task 100"), "task")
        # test fot job
        self.assertEqual(identify_process("background job abc"), "job")
    
    def test_calculate_duration(self):
        start_time = "10:45:00"
        end_time = "11:15:00"
        duration = calculate_duration(start_time, end_time)
        
        # verify if the duration between two times is calculated right
        self.assertEqual(duration, 30.0)

    def test_log_messages_error(self):
        mock_file = mock_open()
        with patch("LogMonitoring.open", mock_file):
            log_messages("task", "56800", 16.10)
        
        mock_file.assert_called_once_with("output.txt", "a")
        mock_file().write.assert_called_once_with("Error: task with id: 56800 and duration: 16.10 minutes has exceeded the time limit of 10 minutes\n")
    
    # same implementation for test_log_messages_warning but witha job that has a duration over 5 minutes

if __name__ == "__main__":
    unittest.main()