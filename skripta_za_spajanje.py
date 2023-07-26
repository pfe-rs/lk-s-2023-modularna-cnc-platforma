import re

comment_regex = re.compile(r'(;|^M).*')

def combine_files(file_list, output_file):
    try:
        with open(output_file, 'w') as combined_file:
            for file_name in file_list:
                with open(file_name, 'r') as current_file:
                    lines = current_file.readlines()
                    processed_lines = [comment_regex.sub('', line) for line in lines]
                    filtered_lines = [line for line in processed_lines if line.strip() != '']
                    combined_file.writelines(filtered_lines)

        print("Files combined successfully!")
    except Exception as e:
        print("An error occurred:", e)

# Replace these file names with your actual file paths
file_list = ["Pikachu1.gcode", "Pikachu2.gcode", "Pikachu3.gcode"]
output_file = "Pikachu.gcode"

combine_files(file_list, output_file)
