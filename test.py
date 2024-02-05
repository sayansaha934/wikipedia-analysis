import requests
import unittest

class TestWordFrequencyAnalysis(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:8000"  # Update with your FastAPI server URL

    def test_word_frequency_analysis_success(self):
        topic = "Python"
        n = 5
        response = requests.get(f"{self.BASE_URL}/word-frequency-analysis/", params={"topic": topic, "n": n})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("topic", data)
        self.assertEqual(data["topic"], topic)
        self.assertIn("top_words", data)
        self.assertIsInstance(data["top_words"], list)

    def test_word_frequency_analysis_not_found(self):
        topic = "NonExistentTopic"
        n = 5
        response = requests.get(f"{self.BASE_URL}/word-frequency-analysis/", params={"topic": topic, "n": n})
        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertIn("detail", data)
        self.assertEqual(data["detail"], "Wikipedia article not found for the given topic")

    def test_search_history_endpoint(self):
        response = requests.get(f"{self.BASE_URL}/search-history/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)

if __name__ == '__main__':
    unittest.main()
