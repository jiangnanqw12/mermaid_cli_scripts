import subprocess
import os
import sys

def build_mermaid_command(input_path, output_path, config_path):
    """
    Build the Mermaid CLI command for generating SVG.

    :param input_path: Path to the input Mermaid file.
    :param output_path: Path to the output SVG file.
    :param config_path: Path to the Mermaid configuration file.
    :return: Command string for Mermaid CLI.
    """
    return f'npx "C:\\001_tools\\mermaid-cli\\node_modules\\.bin\\mmdc" -i "{input_path}" -o "{output_path}" -c "{config_path}"'

def run_mermaid_cli(command):
    """
    Run the Mermaid CLI command and capture its output.

    :param command: Command string for Mermaid CLI.
    :return: subprocess.CompletedProcess object.
    """
    result = subprocess.run(command, check=True, capture_output=True, text=True, shell=True)
    return result

def prepare_paths(input_file_path=None, config_file_path=None):
    """
    Prepare the input, output, and config file paths for the Mermaid CLI process.

    :param input_file_path: Path to the input Mermaid file. If None, uses a default path.
    :param config_file_path: Path to the config file. If None, uses a default config path.
    :return: Tuple of input file path, output file path, and config file path.
    """
    if not input_file_path:
        input_file_path = r"C:\Users\shade\OneDrive\KG\004_Archives\2025\TEC software\架构\tec modules.mmd"

    if not config_file_path:
        config_file_path = r"C:\Users\shade\OneDrive\000_gits\tools\mermaid_cli_scripts\config\mermaid-config.json"

    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_name = os.path.splitext(os.path.basename(input_file_path))[0]

    output_dir = os.path.join(script_dir, '..', 'output')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file_path = os.path.join(output_dir, base_name + '.svg')
    return input_file_path, output_file_path, config_file_path

def generate_mermaid_svg(input_file, output_file, config_file):
    """
    Generate an SVG file from a Mermaid diagram using Mermaid CLI.

    :param input_file: Path to the input Mermaid file.
    :param output_file: Path to the output SVG file.
    :param config_file: Path to the Mermaid configuration file.
    """
    command = build_mermaid_command(input_file, output_file, config_file)
    try:
        result = run_mermaid_cli(command)
        if result.returncode == 0:
            print(f"SVG generated successfully: {output_file}")
            # Uncomment the line below if you want to see standard output
            # print(result.stdout)
        else:
            print(f"Error occurred: {result.stderr}")
    except FileNotFoundError:
        print("Mermaid CLI (mmdc) not found. Ensure it is installed and in your PATH.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while generating the SVG: {e.stderr}")

def main():
    """
    Main function to handle command line input and execute the Mermaid CLI process.
    """
    # Use the first command line argument as the input file path if provided
    if len(sys.argv) > 1:
        input_file_path_arg = sys.argv[1]
    else:
        input_file_path_arg = None

    # Use the second command line argument as the config file path if provided
    if len(sys.argv) > 2:
        config_file_path_arg = sys.argv[2]
    else:
        config_file_path_arg = None

    input_file_path, output_file_path, config_file_path = prepare_paths(input_file_path_arg, config_file_path_arg)

    if os.path.exists(input_file_path):
        generate_mermaid_svg(input_file_path, output_file_path, config_file_path)
    else:
        print(f"Input file not found: {input_file_path}")

if __name__ == "__main__":
    main()
