import os

from system.infrastructure.handlers.cli_handler import CliHandler

if __name__ == "__main__":
    cli_handler = CliHandler()

    input_file = os.environ.get("INPUT_FILE")
    if input_file and os.path.exists(input_file):
        lines = cli_handler.read_input_from_file(input_file)
    else:
        lines = cli_handler.cli_json_from_user()

    print("Input:", lines)
