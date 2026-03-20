from datetime import date

class Operation:
    "Class that represents a bank operation, with its code, date, type and amount."

    def __init__(
        self, code: str, date_operation: date, type_operation: str, amount: float = 0.0
    ):
        self.__code = code
        self.__date_operation = date_operation
        self.__type_operation = type_operation
        self.__amount = amount

    @property
    def _code(self):
        return self.__code

    @_code.setter
    def _code(self, value):
        self.__code = value

    @property
    def _date_operation(self):
        return self.__date_operation

    @_date_operation.setter
    def _date_operation(self, value):
        self.__date_operation = value

    @property
    def _type_operation(self):
        return self.__type_operation

    @_type_operation.setter
    def _type_operation(self, value):
        self.__type_operation = value

    @property
    def _amount(self):
        return self.__amount

    @_amount.setter
    def _amount(self, value):
        self.__amount = value

    def __str__(self):
        return "\n".join(
            [
                f"Código: {self.__code}, Fecha: {self.__date_operation.strftime('%d-%m-%Y')}"
                f"Tipo: {self.__type_operation}, Monto: {self.__amount}"
            ]
        )
