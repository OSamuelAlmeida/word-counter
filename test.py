import unittest
from unittest import mock
from word_counter import get_words_frequency_from_file, sort_words_frequency


class TestWordCounter(unittest.TestCase):
    def test_count_word_frequencies_simple_string(self):
        mock_file_path = "test_path"
        mock_file_content = "This this is is a mock test Test"

        expected_word_frequencies = {"this": 2, "is": 2, "a": 1, "mock": 1, "test": 2}
        expected_total_words = 8

        word_frequencies = None

        with mock.patch(
            "builtins.open", mock.mock_open(read_data=mock_file_content)
        ) as mock_file:
            word_frequencies, total_words = get_words_frequency_from_file(
                mock_file_path
            )

        mock_file.assert_called_with(mock_file_path)
        self.assertEqual(word_frequencies.items(), expected_word_frequencies.items())
        self.assertEqual(total_words, expected_total_words)

    def test_count_word_frequencies_with_punctuation(self):
        mock_file_path = "test_path"
        mock_file_content = "This this this. is is is. a a, mock test Test"

        expected_word_frequencies = {
            "this": 2,
            "this.": 1,
            "is": 2,
            "is.": 1,
            "a": 1,
            "a,": 1,
            "mock": 1,
            "test": 2,
        }
        expected_total_words = 11

        word_frequencies = None

        with mock.patch(
            "builtins.open", mock.mock_open(read_data=mock_file_content)
        ) as mock_file:
            word_frequencies, total_words = get_words_frequency_from_file(
                mock_file_path
            )

        mock_file.assert_called_with(mock_file_path)
        self.assertEqual(word_frequencies.items(), expected_word_frequencies.items())
        self.assertEqual(total_words, expected_total_words)

    def test_count_word_frequencies_empty_string(self):
        mock_file_path = "test_path"
        mock_file_content = ""

        expected_word_frequencies = {}
        expected_total_words = 0

        word_frequencies = None

        with mock.patch(
            "builtins.open", mock.mock_open(read_data=mock_file_content)
        ) as mock_file:
            word_frequencies, total_words = get_words_frequency_from_file(
                mock_file_path
            )

        mock_file.assert_called_with(mock_file_path)
        self.assertEqual(word_frequencies.items(), expected_word_frequencies.items())
        self.assertEqual(total_words, expected_total_words)

    def test_sort_words_frequency(self):
        words_tuples = [("word1", 3), ("word2", 2), ("word3", 4)]
        expected_sort = [("word3", 4), ("word1", 3), ("word2", 2)]

        sorted_tuple = sort_words_frequency(words_tuples)

        self.assertEqual(expected_sort, sorted_tuple)

    def test_sort_words_frequency_same_frequency(self):
        words_tuples = [("word1", 1), ("word2", 1), ("word3", 1)]
        expected_sort = [("word3", 1), ("word1", 1), ("word2", 1)]

        sorted_tuple = sort_words_frequency(words_tuples)

        self.assertEqual(set(expected_sort), set(sorted_tuple))


if __name__ == "__main__":
    unittest.main()
