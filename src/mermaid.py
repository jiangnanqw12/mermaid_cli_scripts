import subprocess
import os
import sys
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


def main():
    # Default file paths
    input_file_path = r"C:\Users\shade\OneDrive\KG\004_Archives\2025\TEC software\架构\TE software.mm 2024-09-20 14.50.29.md"
    output_file_path = "diagram.svg"


    # If command line arguments are provided, use the first one as input path
    if len(sys.argv) > 1:
        input_file_path = fr"{sys.argv[1]}"  # Input file from CLI
    # Get the current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Extract the base name (without extension) from the input
    base_name = os.path.splitext(os.path.basename(input_file_path))[0]

    # Construct the output path: script_dir/../output/base_name.svg
    output_dir = os.path.join(script_dir, '..', 'output')
    output_file_path = os.path.join(output_dir, base_name + '.svg')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # Now call the generate function
    if os.path.exists(input_file_path):
        generate_mermaid_svg(input_file_path, output_file_path)
    else:
        print(f"Input file not found: {input_file_path}")

if __name__ == "__main__":

    main()
