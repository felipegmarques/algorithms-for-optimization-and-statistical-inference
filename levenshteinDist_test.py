import unittest
from levenshteinDist import (
    levenshteinDist, 
)

class TestLevenshteinDistance(unittest.TestCase):

    def test_dist(self):
        source = 'class'
        destination = 'dash'
        expected_modifications = 3

        result = levenshteinDist(source, destination)
        actual_modifications = result['modifications']
        aligned_source = result['source']
        aligned_destination = result['destination']

        self.assertEqual(actual_modifications, expected_modifications)
        self.assertEqual(len(aligned_source), len(aligned_destination))
        modifications = 0
        for i in range(len(aligned_source)):
            if aligned_source[i] == '_' or aligned_destination[i] == '_':
                modifications += 1
            elif (aligned_destination[i] != aligned_source[i]):
                modifications += 1
