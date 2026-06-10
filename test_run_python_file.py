# test_run_python_file.py
from functions.run_python_file import run_python_file

print("--- Test 1: Usage Instructions ---")
print(run_python_file("calculator", "main.py"))

print("\n--- Test 2: Calculator with input '3 + 5' ---")
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print("\n--- Test 3: Running calculator tests ---")
print(run_python_file("calculator", "tests.py"))

print("\n--- Test 4: Attempting to access ../main.py ---")
print(run_python_file("calculator", "../main.py"))

print("\n--- Test 5: Running non-existent file ---")
print(run_python_file("calculator", "nonexistent.py"))

print("\n--- Test 6: Running text file ---")
print(run_python_file("calculator", "lorem.txt"))