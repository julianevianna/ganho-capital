import sys
from typing import Dict, List


class CliHandler:
    @staticmethod
    def cli_json_from_user() -> List[Dict]:
        lines: List[Dict] = []
        while True:
            line = sys.stdin.readline().strip()
            if line == "":
                break
            if line.lower() == "sair":
                exit(0)
            lines.append(line)  # type: ignore
        return lines

    @staticmethod
    def read_input_from_file(file_path) -> List[Dict]:
        lines: List[Dict] = []
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if line.lower() == "sair":
                    return lines
                lines.append(line)  # type: ignore
        return lines
