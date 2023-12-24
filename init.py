file_path = "llama-cpp-python/llama_cpp/server/app.py"

# Read the file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Modify the line containing "default=16" in the max_tokens_field definition
for i, line in enumerate(lines):
    if "max_tokens_field = Field(" in line and "default=16" in lines[i+1]:
        lines[i+1] = lines[i+1].replace("default=16", "default=4096")
        break

# Write the modified content back to the file
with open(file_path, 'w') as file:
    file.writelines(lines)
