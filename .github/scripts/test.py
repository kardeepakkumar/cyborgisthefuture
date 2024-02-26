# Define the file path
file_path = '/Users/kardeepak.kumar/MySprinklr/code/cyborgisthefuture/README.md'

# Read and print the original contents of the file
with open(file_path, 'r+') as file:
    original_contents = file.read()
    print("Original Contents:")
    print(original_contents)
    file.write("\ntest")

# Read and print the updated contents of the file
with open(file_path, 'r') as file:
    updated_contents = file.read()
    print("Updated Contents:")
    print(updated_contents)
