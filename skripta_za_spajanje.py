import pygcode

def merge_gcode_files(file_paths):
    merged_gcode = []

    for file_path in file_paths:
        with open(file_path, 'r') as file:
            gcode_content = file.read()
            gcode = pygcode.GCode().parse(gcode_content)
            merged_gcode.extend(gcode)

    return merged_gcode

def save_merged_gcode(merged_gcode, output_file_path):
    with open(output_file_path, 'w') as output_file:
        for line in merged_gcode:
            output_file.write(str(line) + '\n')

if __name__ == "__main__":
    # Replace these paths with the actual paths of your G-code files
    file1_path = 'Pikachu1.gcode'
    file2_path = 'Pikachu2.gcode'
    file3_path = 'Pikachu3.gcode'

    output_file_path = 'Pikachu.gcode'

    # List the files in the desired order of merging
    file_paths = [file1_path, file2_path, file3_path]

    # Merge the G-code files
    merged_gcode = merge_gcode_files(file_paths)

    # Save the merged G-code to a new file
    save_merged_gcode(merged_gcode, output_file_path)

    print("Merging complete. Merged G-code saved to:", output_file_path)
