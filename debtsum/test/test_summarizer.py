import unittest
import pandas as pd
from src.summarizer import Summarizer


class TestSummarizer(unittest.TestCase):

    sample_input  = "data/sample_input.csv"
    sample_output = pd.read_csv("data/sample_output.csv", header=None)

    def test_summarize(self):
        result = Summarizer(self.sample_input).summarize()
        pd.testing.assert_frame_equal(result, self.sample_output, "Should be equal")

if __name__ == "__main__":
    unittest.main()