def combine_files(file_list, output_file):
    try:
        with open(output_file, 'w') as combined_file:
            for file_name in file_list:
                with open(file_name, 'r') as current_file:
                    lines = current_file.readlines()
                    filtered_lines = [line for line in lines if not (line.strip().startswith(';') or line.strip().startswith('M'))]
                    combined_file.writelines(filtered_lines)

        print("Files combined successfully!")
    except Exception as e:
        print("An error occurred:", e)

# Replace these file names with your actual file paths
file_list = ["Pikachu1.gcode", "Pikachu2.gcode", "Pikachu3.gcode"]
output_file = "Pikachu.gcode"

combine_files(file_list, output_file)
