from io import StringIO
from typing import Any
import csv
from fastapi import Depends
from fastapp.models.operations import OperationCreate, Operation
from fastapp.services.operations import OperationsService


class ReportsService:
    def __init__(self, operations_service: OperationsService = Depends()):
        self.operations_service = operations_service

    def import_csv(self, user_id: int, file: Any):
        reader = csv.DictReader(
            (line.decode() for line in file)
        )
        next(reader, None)
        operations_data = []
        for row in reader:
            operation_data = OperationCreate.parse_obj(row)
            if operation_data.description == '':
                operation_data.description = None
            operations_data.append(operation_data)
        self.operations_service.create_many(
            user_id,
            operations_data,
        )

    def export_csv(self, user_id: int) -> Any:
        output = StringIO()
        writer = csv.DictWriter(
            output,
            fieldnames=[
                'data',
                'type',
                'amount',
                'description',
            ],
            extrasaction='ignore',
        )
        operations = self.operations_service.get_list(user_id)
        writer.writeheader()
        for operation in operations:
            operation_data = Operation.from_orm(operation)
            writer.writerow(operation_data.dict())

        output.seek(0)
        return output
