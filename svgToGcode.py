import svgpathtools

def svg_to_gcode(svg_file, feed_rate, plunge_rate, z_depth):
    # Load the SVG file
    paths, attributes = svgpathtools.svg2paths(svg_file)

    # Create a list to store the G-code commands
    gcode_commands = []

    # Set the initial position to the starting point of the first path
    current_x = paths[0][0].start.real
    current_y = paths[0][0].start.imag

    # Set the initial feed rate and plunge rate
    gcode_commands.append(f"F{feed_rate}")
    gcode_commands.append(f"G1 Z{z_depth} F{plunge_rate}")

    # Generate G-code commands for each path in the SVG
    for path in paths:
        # Move to the starting point of the path
        gcode_commands.append(f"G0 X{path[0].start.real} Y{path[0].start.imag}")

        # Iterate over the segments in the path
        for segment in path:
            if isinstance(segment, svgpathtools.Line):
                # Line segment
                end_x = segment.end.real
                end_y = segment.end.imag
                gcode_commands.append(f"G1 X{end_x} Y{end_y}")
            elif isinstance(segment, svgpathtools.CubicBezier):
                # Cubic Bezier curve segment (approximated as a series of small line segments)
                num_segments = 10  # Number of line segments to approximate the curve
                for t in range(1, num_segments + 1):
                    point = segment.point(t / num_segments)
                    end_x = point.real
                    end_y = point.imag
                    gcode_commands.append(f"G1 X{end_x} Y{end_y}")
            # Add other segment types as needed (e.g., QuadraticBezier, Arc)

        # Move back to the starting point of the path
        gcode_commands.append(f"G1 X{path[0].start.real} Y{path[0].start.imag}")

    # Move to the safe Z position and set the feed rate to 0
    gcode_commands.append(f"G0 Z0 F{feed_rate}")

    # Convert the list of G-code commands to a string
    gcode = "\n".join(gcode_commands)

    return gcode

# Example usage
svg_file = "android-logo.svg"  # Replace with the path to your SVG file
feed_rate = 1000  # Replace with the desired feed rate (units per minute)
plunge_rate = 100  # Replace with the desired plunge rate (units per minute)
z_depth = -5  # Replace with the desired Z depth for cutting or engraving

gcode = svg_to_gcode(svg_file, feed_rate, plunge_rate, z_depth)

# Save the G-code to a file
with open("output.gcode", "w") as file:
    file.write(gcode)
