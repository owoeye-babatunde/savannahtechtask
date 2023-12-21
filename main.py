import random
import multiprocessing

def create_dwarf_giant_pairs(employees):
    """
    create unique dwarf giant pairs from a list of employees while ensuring fairness and 
    randomness
    Args:
        employees: A list of employee objects, each containing three fields.

    Returns:
        A list of tuples, where each tuple represents a Dwarf-Giant pair (name, name)
    
    """
    unique_employees = {tuple(employee.values()): employee for employee in employees}
    employee_names = list(unique_employees.keys())

    random.shuffle(employee_names)
    pairs = [(employee_names[i], employee_names[-i-1]) for i in range(len(employee_names) // 2)]
    return [(unique_employees[pair[0]]["name"], unique_employees[pair[1]]["name"]) for pair in pairs]


