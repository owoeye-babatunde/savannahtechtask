import unittest
from main import create_dwarf_giant_pairs

class TestCreateDwarfGiantPairs(unittest.TestCase):
    """
    Test cases for create_dwarf_giant_pairs function.
    """

    def test_pairs(self):
        employees = [
            {"name": "Alice", "field1": 1, "field2": "A"},
            {"name": "Bob", "field1": 2, "field2": "B"},
            {"name": "Charlie", "field1": 1, "field2": "A"},  # Duplicate
            {"name": "David", "field1": 3, "field2": "C"},
        ]

        pairs = create_dwarf_giant_pairs(employees)

        self.assertEqual(len(pairs), 3)  # Correct number of pairs
        self.assertEqual(len(set(pair for pair in pairs)), 3)  # Unique pairs
        self.assertTrue(all(employee["name"] in [pair[0] for pair in pairs] for employee in employees))  # All employees included
        self.assertTrue(all(employee["name"] in [pair[1] for pair in pairs] for employee in employees))  # All employees included
        self.assertFalse(any((pair[1], pair[0]) in pairs for pair in pairs))  # No reverse pairs

if __name__ == "__main__":
    unittest.main()
