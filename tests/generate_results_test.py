import unittest

generate_results = __import__("../maven_sonarscanner/generate-results.py")


class Generate_Results_Test(unittest.TestCase):
    def test_generate_results(self):
        """
        Test generation of results
        """

if __name__ == '__main__':
    unittest.main()