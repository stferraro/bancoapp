from models.user import User
from models.account import Account
from models.operation import Operation
from datetime import date
import ast

def cargar_datos():
    try:
        with open("../recursos/usuarios.txt", "r") as file:
            usuarios = ast.literal_eval(file.read())
    except FileNotFoundError:
        print("Archivo de usuarios no encontrado.")
    return usuarios
    
        
def busca_usuario(cedula) -> User:
    usuarios = cargar_datos()
    if cedula in usuarios:
        contraseña = input("Ingrese su contraseña: ")
        intentos = 0
        while usuarios[cedula] != contraseña:
            print("Contraseña incorrecta.")
            contraseña = input("Ingrese su contraseña: ")
            intentos += 1
            if intentos >= 3:
                print("Ha excedido el número de intentos.")
                return None
        user = User(cedula, contraseña)
        return user
    else:
        print("Usuario no encontrado.")
    return None

cuentas = [
    Account('1234567890', 500.0, 'Ahorros'),
    Account('0987654321', 800.0, 'Corriente'),
    Account('1122334455', 1200.0, 'Ahorros')
]

def print_txt(numero_cuenta, operaciones):
    try:
        with open(f"../recursos/{numero_cuenta}.txt", "w") as file:
            file.write(operaciones)
    except Exception as e:
        print(f"Error al guardar las operaciones: {e}")

def realiza_operacion(usuario):
    if usuario:
        print("Bienvenido vamos a realizar operaciones")
        usuario.add_account(cuentas[0])
        usuario.add_account(cuentas[1])
        usuario.add_account(cuentas[2])
        operacion = int(input("Ingrese el tipo de operación (1.depositar,2.retirar,3.consultar,4.consulta ultima operaciones,0.salir): "))
        while operacion != 0:
            match operacion:
                case 1:
                    numero_cuenta = input("Ingrese el número de cuenta: ")
                    cuenta1 = usuario.search_account(numero_cuenta)
                    if cuenta1:
                        monto = float(input("Ingrese el monto a depositar: "))
                        operation = Operation("OP001", date.today(), "Depósito", monto)
                        cuenta1.add_operation(operation)
                        try:
                            cuenta1.deposit(monto)
                            print(f"Depósito exitoso. datos de la cuenta: {str(cuenta1)}")
                        except ValueError as e:
                            print(e)
                    else:
                        print("Cuenta no encontrada.")
                case 2:
                    numero_cuenta = input("Ingrese el número de cuenta: ")
                    cuenta1 = usuario.search_account(numero_cuenta)
                    if cuenta1:
                        monto = float(input("Ingrese el monto a retirar: "))
                        operation = Operation("OP001", date.today(), "Retiro", monto)
                        cuenta1.add_operation(operation)
                        try:
                            cuenta1.withdraw(monto)
                            print(f"Retiro exitoso. datos de la cuenta: {str(cuenta1)}")
                        except ValueError as e:
                            print(e)
                    else:
                        print("Cuenta no encontrada.")
                case 3:
                    numero_cuenta = input("Ingrese el número de cuenta: ")
                    cuenta1 = usuario.search_account(numero_cuenta)
                    if cuenta1:
                        print(f"Datos de la cuenta: {str(cuenta1)}")
                    else:
                        print("Cuenta no encontrada.")
                case 4:
                    numero_cuenta = input("Ingrese el número de cuenta: ")
                    print(usuario.print_operations(numero_cuenta))
                    print_txt(numero_cuenta, usuario.print_operations(numero_cuenta))
                case _:
                    print("Opción no válida.")
            operacion = int(input("Ingrese el tipo de operación (1.depositar,2.retirar,3.consultar,4.consulta ultima operaciones,0.salir): "))
    else:
        print("No se pudo realizar la operación debido a problemas de autenticación.")
                
cedula_usuario = input("Ingrese su cédula: ")
usuario = busca_usuario(cedula_usuario)
realiza_operacion(usuario)


