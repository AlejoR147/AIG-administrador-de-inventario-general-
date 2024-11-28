import msvcrt
from datetime import datetime

class Bolsa:
    def __init__(self, id, nombre, cantidad, material, tamaño, color):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.material = material
        self.tamaño = tamaño
        self.color = color

    def comprar(self):
        if self.cantidad > 0:
            self.cantidad -= 1
            return True
        else:
            print(f"Lo sentimos, no hay suficientes {self.nombre} en existencia.")
            return False

    def agregar(self, cantidad):
        self.cantidad += cantidad

    def restablecer(self, cantidad):
        self.cantidad = cantidad

    def obtener_informacion(self):
        return f"{self.id} → ------{self.nombre}------\n➥ Cantidad = {self.cantidad}\n➥ Material = {self.material}\n➥ Tamaño = {self.tamaño}\n➥ Color = {self.color}"

    def __str__(self):
        return self.obtener_informacion()

class AIG:
    def __init__(self):
        self.bolsa = {}
        self.id_bolsa_actual = 1
        self.inicializar_inventario()

    def inicializar_inventario(self):
        # Añadir bolsas iniciales al inventario
        self.agregar_bolsa("Bolsa de lona", 10, "Lona", "Grande", "Azul")
        self.agregar_bolsa("Bolsa de plástico", 50, "Plástico", "Mediano", "Rojo")
        self.agregar_bolsa("Bolsa de papel", 30, "Papel", "Pequeño", "Blanco")

    def agregar_bolsa(self, nombre, cantidad, material, tamaño, color):
        bolsa = Bolsa(self.id_bolsa_actual, nombre, cantidad, material, tamaño, color)
        self.bolsa[self.id_bolsa_actual] = bolsa
        self.id_bolsa_actual += 1
        print("Bolsa agregada con éxito ✔")

    def calcular_total_bolsas(self):
        return sum(bolsa.cantidad for bolsa in self.bolsa.values())
    def listar_bolsa(self):
        if not self.bolsa:
            print("No hay bolsas registradas.")
        else:
            for bolsa in self.bolsa.values():
                print(bolsa)
            print("")
            print("En total tenemos:", self.calcular_total_bolsas(), "Bolsas")

    def buscar_bolsa(self, id):
        return self.bolsa.get(id, None)

    def actualizar_bolsa(self, id, cantidad):
        bolsa = self.buscar_bolsa(id)
        if bolsa:
            bolsa.cantidad = cantidad
            print("Bolsa actualizada con éxito.")
        else:
            print("Bolsa no encontrada.")

    def actualizar_bolsas(self, id, nombre, cantidad, material, tamaño, color):
        bolsa = self.buscar_bolsa(id)
        if bolsa:
            bolsa.nombre = nombre
            bolsa.cantidad = cantidad
            bolsa.material = material
            bolsa.tamaño = tamaño
            bolsa.color = color
            print("Bolsa actualizada con éxito.")
        else:
            print("Bolsa no encontrada.")

    def eliminar_bolsa(self, id):
        bolsa = self.buscar_bolsa(id)
        if bolsa:
            del self.bolsa[id]
            print("Bolsa eliminada con éxito.")
        else:
            print("Bolsa no encontrada.")

    def restablecer_inventario(self):
        for bolsa in self.bolsa.values():
            cantidad = int(input(f"Ingrese la cantidad de {bolsa.nombre} a agregar al inventario: "))
            bolsa.restablecer(cantidad)
        print("Inventario restablecido.")

def input_contrasena(prompt="Contraseña: "):
    print(prompt, end="", flush=True)
    contrasena = ""
    while True:
        char = msvcrt.getch()
        if char in {b'\r', b'\n'}:  # Enter key pressed
            break
        elif char == b'\x08':  # Backspace key pressed
            if contrasena:
                contrasena = contrasena[:-1]
                print("\b \b", end="", flush=True)
        else:
            contrasena += char.decode('utf-8')
            print("*", end="", flush=True)
    print()
    return contrasena

contraseña = "12345"
aig = AIG()

def seleccion():
    print("------------------------------------")
    print("1- Administrador")
    print("2- Usuario")
    print("3- Cerrar Programa")
    print("------------------------------------")

def menu_admin():
    print("------------------------------------")
    print("1: Agregar bolsa ")
    print("2: Ver inventario ")
    print("3: Eliminar bolsa ")
    print("4: Actualizar ")
    print("5: Mostrar compras ")
    print("6: Salir del programa ")
    print("------------------------------------")

def menu_actualizar():
    print("------------------------------------")
    print("1: Restablecer inventario ")
    print("2: Nueva cantidad de una bolsa ")
    print("3: Actualizar bolsa ")
    print("4: Salir de este menu")
    print("------------------------------------")

def menu_salida():
    print("****************************************")
    print("****     Saliendo del programa     *****")
    print("****************************************")

def salida():
    print("------------------------------------")
    print("---------Saliendo del menu----------")

print("****************************************")
print("****         BIENVENIDO A TU        ****")
print("***   ADMINISTRADOR DE INVENTARIOS   ***")
print("****            (BOLSAS)            ****")
print("****************************************")
while True:
    seleccion()
    modo = int(input("¿Como desea ingresar? "))
    if modo == 1:
        print("------------------------------------")
        print("-----------Administrador------------")
        print("------------------------------------")
        opcion = input_contrasena("ingrese la contraseña: ")
        if opcion == contraseña:
            while True:
                menu_admin()
                opc = int(input("Eliga una opcion: "))
                if opc == 1:
                    nombre = input("Ingrese el nombre de la nueva bolsa: ")
                    cantidad = int(input("Ingrese la cantidad de la nueva bolsa: "))
                    material = input("Ingrese el material de la nueva bolsa: ")
                    tamaño = input("Ingrese el tamaño de la nueva bolsa: ")
                    color = input("Ingrese el color de la nueva bolsa: ")
                    aig.agregar_bolsa(nombre, cantidad, material, tamaño, color)
                elif opc == 2:
                    print("\nInventario:")
                    aig.listar_bolsa()
                elif opc == 3:
                    id = int(input("Ingrese el ID de la bolsa que desea eliminar: "))
                    aig.eliminar_bolsa(id)
                elif opc == 4:
                    print("------------------------------------")
                    print("-----------Actualizacion------------")
                    while True:
                        menu_actualizar()
                        opc2 = int(input("Eliga una opcion: "))
                        if opc2 == 1:
                            aig.restablecer_inventario()
                        elif opc2 == 2:
                            id = int(input("Ingrese el ID de la bolsa a actualizar: "))
                            cantidad = int(input(f"Ingrese la nueva cantidad de la bolsa : "))
                            aig.actualizar_bolsa(id, cantidad)
                        elif opc2 == 3:
                            id = int(input("Ingrese el ID de la bolsa a actualizar: "))
                            nombre = input("Ingrese el nuevo nombre de la bolsa: ")
                            cantidad = int(input("Ingrese la nueva cantidad de la bolsa: "))
                            material = input("Ingrese el nuevo material de la bolsa: ")
                            tamaño = input("Ingrese el nuevo tamaño de la bolsa: ")
                            color = input("Ingrese el nuevo color de la bolsa: ")
                            aig.actualizar_bolsas(id, nombre, cantidad, material, tamaño, color)
                        elif opc2 == 4:
                            salida()
                            break
                elif opc == 6:
                    salida()
                    break
        else:
            print("------------------------------------")
            print("contraseña incorrecta")
    elif modo == 2:
        print("modo usuario")
    elif modo == 3:
        menu_salida()
        break
