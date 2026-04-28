import unittest
from unittest.mock import patch, mock_open, call
import parse_and_summarize
import os

class TestParseAndSummarize(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='# Mocked Content')
    def test_create_deep_notes(self, mock_file):
        parse_and_summarize.create_deep_notes()

        # Verify calls to open
        template_path = os.path.join('resources', 'session2_notes.md')

        # Filter for only 'open' calls (ignoring __enter__, __exit__, etc.)
        open_calls = [c for c in mock_file.mock_calls if c[0] == '']

        expected_open_calls = [
            call(template_path, 'r', encoding='utf-8'),
            call('part2_sales.md', 'w', encoding='utf-8')
        ]
        self.assertEqual(open_calls, expected_open_calls)

        # Verify that content read from template was written to output
        handle = mock_file()
        handle.write.assert_called_with('# Mocked Content')

if __name__ == '__main__':
    unittest.main()
