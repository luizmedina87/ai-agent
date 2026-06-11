from functions.run_python_file import run_python_file

print("--- Test 1: should print the calculator's usage instructions ---")
print(run_python_file("calculator", "main.py"))

print("\n--- Test 2: should run the calculator... which gives a kinda nasty rendered result ---")
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print("\n--- Test 3: should run the calculator's tests successfully ---")
print(run_python_file("calculator", "tests.py"))

print("\n--- Test 4: Attempting to access ../main.py (this should return an error) ---")
print(run_python_file("calculator", "../main.py"))

print("\n--- Test 5: Running non-existent file (this should return an error) ---")
print(run_python_file("calculator", "nonexistent.py"))

print("\n--- Test 6: Running text file (this should return an error) ---")
print(run_python_file("calculator", "lorem.txt"))