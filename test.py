import unittest
from unittest.mock import Mock, patch
import pandas as pd
from main import GoogleAIWrapper, PandasQueryOutputParser, get_db_chain

class TestGoogleAIWrapper(unittest.TestCase):
    def test_call(self):
        mock_model = Mock()
        mock_model.generate_content.return_value = Mock(text="Test response")
        wrapper = GoogleAIWrapper(mock_model)
        result = wrapper._call("Test prompt")
        self.assertEqual(result, "Test response")

class TestPandasQueryOutputParser(unittest.TestCase):
    def test_parse(self):
        parser = PandasQueryOutputParser()
        result = parser.parse("```python\ndf.head()\n```")
        self.assertEqual(result, "df.head()")

class TestGetDbChain(unittest.TestCase):
    @patch('main.pd.read_csv')
    @patch('main.genai.configure')
    @patch('main.genai.GenerativeModel')
    def test_get_db_chain(self, mock_generative_model, mock_configure, mock_read_csv):
        mock_df = pd.DataFrame({'column1': [1, 2, 3], 'column2': ['a', 'b', 'c']})
        mock_read_csv.return_value = mock_df
        
        mock_model = Mock()
        mock_model.generate_content.return_value = Mock(text="df.head()")
        mock_generative_model.return_value = mock_model

        chain = get_db_chain()
        result = chain("Give me all records")

        self.assertIn("query", result)
        self.assertIn("result", result)
        self.assertIn("answer", result)
        self.assertEqual(result["query"], "df.head()")

if __name__ == '__main__':
    unittest.main()