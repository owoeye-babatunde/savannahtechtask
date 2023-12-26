import unittest
from main1 import create_dwarf_giant_pairs

class TestCreateDwarfGiantPairs(unittest.TestCase):
    """
    Test cases for create_dwarf_giant_pairs function.
    """

    def test_pairs(self):
        employees = [
	{
		"department": "R&D",
		"name": "emp1",
		"age": 46
	},
	{
		"department": "Sales",
		"name": "emp2",
		"age": 28
	},
	{
		"department": "R&D",
		"name": "emp3",
		"age": 33
	},
	{
		"department": "R&D",
		"name": "emp4",
		"age": 29
	}
                    ]

#output: [(emp2, emp4), (emp4, emp1), (emp1, emp3), (emp3, emp2)]

        pairs = create_dwarf_giant_pairs(employees)

        self.assertEqual(len(pairs), 2)  # Correct number of pairs
        self.assertEqual(len(set(pair for pair in pairs)), 2)  # Unique pairs
        self.assertFalse(all(employee["name"] in [pair[0] for pair in pairs] for employee in employees))  # All employees included
        self.assertFalse(all(employee["name"] in [pair[1] for pair in pairs] for employee in employees))  # All employees included
        self.assertFalse(any((pair[1], pair[0]) in pairs for pair in pairs))  # No reverse pairs

if __name__ == "__main__":
    employees = [
	{
		"department": "R&D",
		"name": "emp1",
		"age": 46
	},
	{
		"department": "Sales",
		"name": "emp2",
		"age": 28
	},
	{
		"department": "R&D",
		"name": "emp3",
		"age": 33
	},
	{
		"department": "R&D",
		"name": "emp4",
		"age": 29
	}
                    ]
    print(create_dwarf_giant_pairs(employees))
    unittest.main()
