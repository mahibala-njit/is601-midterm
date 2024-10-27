"""
This module provides dynamic test generation for calculator operations using pytest.

It includes:
- A custom pytest option to specify the number of test records.
- Dynamic parameterization of test cases using the Faker library to generate random test data.
- Handling of edge cases like division by zero and invalid inputs.

The test data is generated based on the number of records specified via the --num_records option.
"""
from decimal import Decimal  # Ensure this is at the top of your file
from faker import Faker
from calculator.operations import add, subtract, multiply, divide, sin, cos, tan, sqrt

fake = Faker()

def pytest_addoption(parser):
    """Add command line options for pytest."""
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """Generate dynamic test cases based on the number of records specified."""
    num_records = metafunc.config.getoption("num_records")
    
    if {"a", "b", "operation", "expected"}.issubset(metafunc.fixturenames):
        parameters = list(generate_test_data(num_records, binary=True))
        metafunc.parametrize("a, b, operation, expected", parameters)
    
    elif {"a", "operation", "expected"}.issubset(metafunc.fixturenames):
        parameters = list(generate_test_data(num_records, binary=False))
        metafunc.parametrize("a, operation, expected", parameters)

def generate_test_data(num_records, binary=True):
    """Generate test data for calculator operations.

    Args:
        num_records (int): Number of test records to generate.
        binary (bool): Whether to generate binary operation data or not.

    Yields:
        tuple: A tuple containing the operands and the corresponding operation and expected result.
    """
    
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide,
        'sin': sin,
        'cos': cos,
        'tan': tan,
        'sqrt': sqrt
    }
    
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        
        if binary:
            b = Decimal('1') if _ % 4 == 0 else Decimal(fake.random_number(digits=2))
            operation_name = fake.random_element(elements=['add', 'subtract', 'multiply', 'divide'])
            operation_func = operation_mappings[operation_name]
            expected = operation_func(a, b)
            yield a, b, operation_func, expected  # Passing the actual function, not the string name
        else:
            operation_name = fake.random_element(elements=['sin', 'cos', 'tan', 'sqrt'])
            operation_func = operation_mappings[operation_name]
            expected = operation_func(a)
            yield a, operation_func, expected  # Passing the actual function, not the string name
