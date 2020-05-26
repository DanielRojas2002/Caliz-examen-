class Empleados ():
    def __init__ (self,idEmpleado,nombre,direccion):
        self.__idEmpleado=idEmpleado
        self.__nombre=nombre
        self.__direccion=direccion
        
    def Agregar(self):
        archivoA=open("./archivos/Empleados.txt","a")
        archivoA.write(idEmpleado+"|"+nombre+"|"+direccion +"|"+ "\n")
        archivoA.close()

menu1=1

while menu1==1:
    print("1=Agregar Empleado")
    print("2=Borrar Empleado")
    print("3=Modificar Empleado")
    print("4=Ver todos los Empleados")
    opcion=int(input("Que opcion eliges: "))

    if opcion==1:
        idEmpleado=(input("Ingrese su numero de ID Empleado: "))
        nombre=(input("Ingrese su nombre de Empleado: "))
        direccion=(input("Ingrese la direccion del Empleado: "))
        a=Empleados(idEmpleado,nombre,direccion)
        a.Agregar()
        print("1=SI")
        print("2=NO")
        menu1=int(input("Desea regresar al Menu Principal: "))
        