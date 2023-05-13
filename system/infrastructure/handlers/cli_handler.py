import sys
from typing import List


class CliHandler:
    @staticmethod
    def cli_json_from_user() -> List[str]:
        lines: List[str] = []
        while True:
            line = sys.stdin.readline().strip()
            if line == "":
                break
            if line.lower() == "sair":
                exit(0)
            lines.append(line)
        return lines

    @staticmethod
    def read_input_from_file(file_path) -> List[str]:
        lines: List[str] = []
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if line.lower() == "sair":
                    return lines
                lines.append(line)
        return lines
