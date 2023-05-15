import json
import sys
from typing import Dict, List

from system.adapter_entrypoints.cli.cli_entrypoint import CLIEntryPoint
from system.application.dto.operation_list_input import (
    OperationInput,
    OperationsListInput,
)


class CliHandler:
    @staticmethod
    def cli_json_from_user() -> List[Dict]:  # type: ignore
        for line in sys.stdin:
            if line.strip() == "":
                break
            operation_list_input_cli = json.loads(line)
            operation_list_input = OperationsListInput(
                operation_list=[
                    OperationInput(**operation)
                    for operation in operation_list_input_cli
                ],
            )
            cli_handler_output = CLIEntryPoint().operations_list_input(
                operation_list_input,
            )
            print(cli_handler_output)
