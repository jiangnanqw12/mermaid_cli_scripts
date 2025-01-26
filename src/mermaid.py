import subprocess
import os

def generate_mermaid_svg(input_file, output_file):
    """
    Generate an SVG file from a Mermaid diagram using Mermaid CLI.

    :param input_file: Path to the input Mermaid file (e.g., 'diagram.mmd').
    :param output_file: Path to the output SVG file (e.g., 'diagram.svg').
    """
    try:
        # Command to invoke Mermaid CLI
        # command = [
        #     r"npx C:\001_tools\mermaid-cli\node_modules\.bin\mmdc",                # Mermaid CLI command
        #     "-i", input_file,      # Input file
        #     "-o", output_file      # Output file
        # ]
        # command = [
        #     r"npx C:\001_tools\mermaid-cli\node_modules\.bin\mmdc",                # Mermaid CLI command
        #     "-h",
        # ]
        command = f'npx "C:\\001_tools\\mermaid-cli\\node_modules\\.bin\\mmdc" -i "{input_file}" -o "{output_file}"'
        # Run the command
        result = subprocess.run(command, check=True, capture_output=True, text=True,shell=True)

        # Check if the process was successful
        if result.returncode == 0:
            print(f"SVG generated successfully: {output_file}")
        else:
            print(f"Error occurred: {result.stderr}")

    except FileNotFoundError:
        print("Mermaid CLI (mmdc) not found. Ensure it is installed and in your PATH.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while generating the SVG: {e.stderr}")

# Example usage
if __name__ == "__main__":
    # Input Mermaid file path
    input_mermaid_file = r"C:\Users\shade\OneDrive\000_gits\tools\mermaid\data\test test data\test.mmd"  # Update this with your .mmd file path
    # Output SVG file path
    output_svg_file = "diagram.svg"     # Update this with your desired output path

    if os.path.exists(input_mermaid_file):
        generate_mermaid_svg(input_mermaid_file, output_svg_file)
    else:
        print(f"Input file not found: {input_mermaid_file}")