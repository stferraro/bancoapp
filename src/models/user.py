class User:
    def __init__(self, cedula: str, contraseña: str, accounts: list = None):
        self.__cedula = cedula
        self.__contraseña = contraseña
        self.__accounts = accounts if accounts is not None else []

    @property
    def _cedula(self):
        return self.__cedula

    @_cedula.setter
    def _cedula(self, value):
        self.__cedula = value

    @property
    def _contraseña(self):
        return self.__contraseña

    @_contraseña.setter
    def _contraseña(self, value):
        self.__contraseña = value

    @property
    def _accounts(self):
        return self.__accounts

    @_accounts.setter
    def _accounts(self, value):
        self.__accounts = value
        
    def add_account(self, account):
        self.__accounts.append(account)
        
    def search_account(self, account_number):
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                return account
        return None
    
    def remove_account(self, account_number):
        account = self.search_account(account_number)
        if account:
            self.__accounts.remove(account)
            return True
        return False
    
    def print_operations(self, account_number):
        account = self.search_account(account_number)
        if account:
            return '\n'.join(
                [
                    f"Operaciones de la cuenta {account_number}: {[str(operation) for operation in account.get_operations()]}"
                ]
            )
        return f"No se encontró la cuenta {account_number} para el usuario {self.__cedula}"
    
    
    def print_operation(self, account_number, code):
        account = self.search_account(account_number)
        if account:
            operation = account.search_operation(code)
            if operation:
                return f"Operación encontrada: {str(operation)}"
            return f"No se encontró la operación con código {code} en la cuenta {account_number}"
        return f"No se encontró la cuenta {account_number} para el usuario {self.__cedula}"
    
    
    def __str__(self):
        return '\n'.join(
            [
                f"Cédula: {self.__cedula}, Contraseña: {self.__contraseña},\
                    Cuentas: {[str(account) for account in self.__accounts]}"
            ]
        )
    
