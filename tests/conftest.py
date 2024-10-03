"""
This module provides dynamic test generation for calculator operations using pytest.

It includes:
- A custom pytest option to specify the number of test records.
- Dynamic parameterization of test cases using the Faker library to generate random test data.
- Handling of edge cases like division by zero and invalid inputs.

The test data is generated based on the number of records specified via the --num_records option.
"""
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def pytest_addoption(parser):
    """
    Add a custom command-line option for pytest to specify the number of test records.
    """
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """
    Generate test cases dynamically based on the number of records specified via the pytest command-line option.
    """
    # Check if the test is expecting any of the dynamically generated fixtures
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        modified_parameters = [
            (a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected)
            for a, b, op_name, op_func, expected in parameters
        ]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)

def generate_test_data(num_records):
    """
    Generate test data dynamically for calculator operations.
    Edge cases such as division by zero are handled more frequently.
    """
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    # Edge case for b == 0 should happen more frequently in tests
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal('0') if _ % 4 == 0 else Decimal(fake.random_number(digits=2))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        try:     
            if operation_func == divide and b == Decimal('0'):
                expected = ZeroDivisionError("Cannot divide by zero")
            else:
                expected = operation_func(a, b)
        except:
            expected = ZeroDivisionError("Cannot divide by zero")

        yield a, b, operation_name, operation_func, expected
