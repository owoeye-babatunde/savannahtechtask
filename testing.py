from main import create_dwarf_giant_pairs

def test_create_giant_pairs():

    employees = [
        {"name": "Alice", "field": 1, "field2": "A"},
        {"name": "Bob", "field1": 2, "field2": "B"},
         {"name": "Charlie", "field1": 1, "field2": "A"},
          {"name": "David", "field1": 3, "field2": "C"}
    ] 
    
    pairs= test_create_giant_pairs(employees)

    assert len(pairs) == 3  
    assert len(set(pair for pair in pairs)) == 3
    assert all(employee["name"] in [pair[0] for pair in pairs] for employee in employees)
    assert all(employee["name"] in [pair[1] for pair in pairs] for employee in employees)
    assert not any((pair[1], pair[0]) in pairs for pair in pairs)



    