class Bank:
    
    def __init__(self, users: list = None):
        self.__users = users if users is not None else []

    @property
    def _users(self):
        return self.__users

    @_users.setter
    def _users(self, value):
        self.__users = value
        
    def add_user(self, user):
        self.__users.append(user)
    
    def remove_user(self, cedula):
        user = self.search_user(cedula)
        if user:
            self.__users.remove(user)
            return True
        return False
    
    def search_user(self, cedula, contraseña):
        for user in self.__users:
            if user._cedula == cedula and user._contraseña == contraseña:
                return user
        return None 
    
    def __str__(self):
        return '\n'.join(
            [
                f"Usuarios: {[str(user) for user in self.__users]}"
            ]
        )
    
