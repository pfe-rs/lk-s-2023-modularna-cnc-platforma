import re

comment_regex = re.compile(r'(;|^M).*')

def add_rotation(file_list):
    try:
        for file_name in file_list:
            with open(file_name, 'a') as current_file:
                current_file.write("G0 A120\n")
            current_file.close()
        print("Files changed successfully!")
    except Exception as e:
        print("An error ocurred:", e)

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

file_list = ["Code1.gcode", "Code2.gcode", "Code3.gcode"]
output_file = "Code.gcode"

add_rotation(file_list)
combine_files(file_list, output_file)
