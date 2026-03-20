
class Account:
    
    "Class that represents a bank account, with its account number and balance."
    
    def __init__(self, account_number: str, amount: float = 0.0, type_account: str = None, operations: list = None):
        self.account_number = account_number
        self.balance = amount
        self.type_account = type_account
        self.operations = operations if operations is not None else []

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, value):
        self.account_number = value

    def get_balance(self):
        return self.balance

    def set_balance(self, value):
        self.balance = value

    def get_type_account(self):
        return self.type_account

    def set_type_account(self, value):
        self.type_account = value

    def get_operations(self):
        return self.operations

    def set_operations(self, value):
        self.operations = value

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def add_operation(self, operation):
        self.operations.append(operation)
        
    def search_operation(self, code):
        for operation in self.operations:
            if operation._code == code:
                return operation
        return None
    
    def remove_operation(self, code):
        operation = self.search_operation(code)
        if operation:
            self.operations.remove(operation)
            return True
        return False        
    
    def search_operations_by_date(self, date):
        return [operation for operation in self.operations if operation._date_operation == date]
    
    def search_operations_by_type(self, type_operation):
        return [operation for operation in self.operations if operation._type_operation == type_operation]
    
    def search_operations_by_code(self, code):
        return [operation for operation in self.operations if operation._code == code]
    
    def __str__(self):
        return '\n'.join(
            [
                f"Numero de cuenta: {self.account_number}, Monto disponible: {self.balance}, Tipo de cuenta: {self.type_account}"
            ]
        )   