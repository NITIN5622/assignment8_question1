import os
import pandas as pd

# Define the directory where your text files are stored
directory_path1= r"C:\Users\ASUS\Downloads\train_test_mails\train-mails"
directory_path2= r"C:\Users\ASUS\Downloads\train_test_mails\test-mails"
data = []

# Loop through each file in the directory
for filename in os.listdir(directory_path1):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory_path1, filename)
        
        # Read the entire file content as a single string
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Determine if the file is spam based on the filename
        is_spam = 1 if filename.startswith("sp") else 0
        
        # Append the filename, content, and spam indicator as a single row to the list
        data.append({'content': content, 'spam': is_spam})

for filename in os.listdir(directory_path2):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory_path2, filename)
        
        # Read the entire file content as a single string
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Determine if the file is spam based on the filename
        is_spam = 1 if filename.startswith("sp") else 0
        
        # Append the filename, content, and spam indicator as a single row to the list
        data.append({'content': content, 'spam': is_spam})

# Convert list to a DataFrame
df = pd.DataFrame(data)

# Save the combined data to a single CSV file
output_file = 'email.csv'
df.to_csv(output_file, index=False)

print(f"Combined data saved to {output_file}")