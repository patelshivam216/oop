# Open the original file in read mode
with open('file1.txt', 'r') as file:
    content = file.read()

# Make changes to the content
new_content = content.replace('old_text', 'new_text')

# Save the modified content to a new file
with open('file31.txt', 'w') as new_file:


    new_file.write(new_content)

print("Changes saved to file2.txt")
