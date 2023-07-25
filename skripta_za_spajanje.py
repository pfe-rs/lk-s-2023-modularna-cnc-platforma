def combine_files(file_list, output_file):
    try:
        with open(output_file, 'w') as combined_file:
            for file_name in file_list:
                with open(file_name, 'r') as current_file:
                    content = current_file.read()
                    combined_file.write(content)

        print("Files combined successfully!")
    except Exception as e:
        print("An error occurred:", e)

# Replace these file names with your actual file paths
file_list = ["file1.txt", "file2.txt", "file3.txt"]
output_file = "combined.txt"

combine_files(file_list, output_file)
