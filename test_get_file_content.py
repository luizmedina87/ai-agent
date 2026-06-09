from functions.get_file_content import get_file_content

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

print("main.py: " + get_file_content("calculator", "main.py"))
print("pkg/calculator.py: " + get_file_content("calculator", "pkg/calculator.py"))
print("/bin/cat (this should return an error string): " + get_file_content("calculator", "/bin/cat"))
print("pkg/does_not_exist.py (this should return an error string): " + get_file_content("calculator", "pkg/does_not_exist.py"))