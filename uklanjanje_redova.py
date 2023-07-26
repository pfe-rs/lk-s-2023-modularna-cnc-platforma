def remove_lines_starting_with_semicolon(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Filter out lines starting with ';'
        filtered_lines = [line for line in lines if not (line.strip().startswith(';') or line.strip().startswith('M'))]

        with open(file_path, 'w') as file:
            file.writelines(filtered_lines)

        print(f"Lines starting with ';' removed from {file_path} successfully!")
    except Exception as e:
        print(f"An error occurred while processing {file_path}:", e)

# Replace "file.txt" with the actual file path
file_path = "file.txt"

remove_lines_starting_with_semicolon(file_path)
