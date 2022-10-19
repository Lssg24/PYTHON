class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellido}\nBalance de cuenta: {self.balance}'

    def depositar(self, deposito):
        self.balance += deposito
        print('Deposito acepatado')
        pass

    def retirar(self, retirar):
        if self.balance >= retirar:
            self.balance -= retirar
            print('Retiro Realizado')
        else:
            print('Fondos insuficientes')


def crear_cliente():
    nombre_cli = input('Ingresa tu nombre:')
    apellido_cli = input('Ingresa tu apellido: ')
    numero_cuenta = input('Ingresa número cuenta: ')
    cliente = Cliente(nombre_cli, apellido_cli, numero_cuenta)
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != 'S' or opcion != 's':
        print('Selecciona: Depositar (D), Retirar (R) o Salir (S)')
        opcion = input()
        if opcion == 'D' or opcion == 'd':
            monto_deposito = int(input('Ingresa el monto a depositar: '))
            mi_cliente.depositar(monto_deposito)
        elif opcion == 'R' or opcion == 'r':
            monto_retiro = int(input('Ingresa el monto a retirar: '))
            mi_cliente.retirar(monto_retiro)
        print(mi_cliente)
    print('Gracias por operar en banco python')

inicio()