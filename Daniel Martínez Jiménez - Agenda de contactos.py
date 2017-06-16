                            #################################################################
                            ########## PROGRAMA QUE SIMULA UNA AGENDA DE CONTACTOS ##########
                            #################################################################

import sys
import os

class AgendaContactos():
    
    def controlContacto(nombre,telefono):                           # CONTROLA EXISTENCIA DEL CONTACTO EN LA AGENDA
        try:
            fich = open("fichero.txt", "r")
        except:
            fich = open("fichero.txt", "w")
            fich.close()
            fich = open("fichero.txt", "r")
        lines = fich.readlines()
        fich.close()

        if lines == []:
            return 1

        for line in lines:
            if nombre+"---"+telefono+"-" in line:
                input("\nEL CONTACTO YA EXISTE. Pulsa INTRO para continuar. ")
                os.system('cls')
                menugeneral()
        return 1

    def controlLista(nombre,telefono):                              # CONTROLA EXISTENCIA DEL CONTACTO EN LA LISTA TEMPORAL
        for i in range (0,len(lista)):
            if nombre+"---"+telefono+"-" in lista[i]:
                print("\nDATOS DE CONTACTO DETECTADOS EN LA LISTA TEMPORAL. ")
                input("\nINTRODUCE DATOS DISTINTOS O BORRA LA LISTA TEMPORAL. Pulsa INTRO para continuar. ")
                os.system('cls')
                menugeneral()

    def abrirFichero(lista):                                        # CONTROLA EXISTENCIA DEL FICHERO Y LO ABRE
        try:
            fich = open("fichero.txt", "r")
        except:
            fich = open("fichero.txt", "w")
            fich.close()
            fich = open("fichero.txt", "r")
        lines = fich.readlines()
        fich.close()

        if lines == []:
            input("\nOPCIÓN NO DISPONIBLE: FICHERO VACÍO. Pulsa INTRO para continuar. ")
            os.system('cls')
            menugeneral()

    def addContacto(nombre,telefono,email,empresa,telefOficina):    # AÑADE NUEVO CONTACTO A LA LISTA TEMPORAL
        lista.append(nombre + '---' + telefono + '-' + email + '-' + empresa + '-' + telefOficina + "\n")
        print("\nNombre: ",nombre,"Teléfono: ",telefono,"E-mail: ",email,"Empresa: ",empresa,"Tlf. Oficina: ",telefOficina)
        input("\nCONTACTO AÑADIDO A LA LISTA TEMPORAL. Pulsa INTRO para continuar. ")

        os.system('cls')
        menugeneral()

    def listarContactos(lista):                                     # MUESTRA LOS CONTACTOS DE LA LISTA TEMPORAL
        if len(lista)==0:
            input("\nLISTA TEMPORAL VACIA. Pulsa INTRO para continuar. ")
        else:
            print("\n\t\tLista de contactos","\n","*"*45,"\n")
            for i in range (0,len(lista)):
                print("Contacto",i+1,":",lista[i])
            input("\nFIN DE LA LISTA TEMPORAL DE CONTACTOS. Pulsa INTRO para continuar. ")

        os.system('cls')
        menugeneral()

    def eliminarContactos(lista):                                   # BORRA LOS CONTACTOS DE LA LISTA TEMPORAL
        if len(lista)==0:
            input("\nLISTA VACÍA. NADA QUE BORRAR. Pulsa INTRO para continuar. ")
        else:
            lista.clear()
            input("\nLISTA TEMPORAL DE CONTACTOS BORRADA. Pulsa INTRO para continuar. ")

        os.system('cls')
        menugeneral()

    def leerContactos(fichero):                                     # MUESTRA LOS CONTACTOS EXISTENTES EN LA AGENDA
        print('\nContenido del fichero:')
        fich = open('fichero.txt','r')
        texto=fich.read()
        if len(texto)==0:
            input("\nFICHERO VACÍO. NADA QUE MOSTRAR. Pulsa INTRO para continuar. ")
            os.system('cls')
            menugeneral()

        print("\n")
        print(texto)

        fich.close()

        input("\nLECTURA TERMINADA. Pulsa INTRO para continuar. ")

        os.system('cls')
        menugeneral()

    def grabarContactos(lista):                                     # GRABA EN LA AGENDA LOS CONTACTOS DE LA LISTA TEMPORAL
        fich = open('fichero.txt', 'a')

        if len(lista)!=0:
            for i in range (0,len(lista)):
                fich.writelines(lista[i])
            if len(lista)==1:
                print("\n--->",len(lista),"CONTACTO GUARDADO.")
            else:
                print("\n--->",len(lista),"CONTACTOS GUARDADOS.")
            lista.clear()
            input("\nGRABACIÓN TERMINADA. Pulsa INTRO para continuar. ")
        else:
            input("\nNO HAY DATOS NUEVOS. Pulsa INTRO para continuar. ")

        fich.close()

        os.system('cls')
        menugeneral()

    def ordenarAgenda(self):                                        # ORDENA LOS CONTACTOS EXISTENTES EN LA AGENDA
        fich = open("fichero.txt", "r")
        lines = fich.readlines()
        fich.close()

        if len(lines)==0:
            input("\nFICHERO VACÍO. NADA QUE ORDENAR. Pulsa INTRO para continuar. ")
            os.system('cls')
            menugeneral()

        lines.sort()

        fich = open("fichero.txt", "w")

        for line in lines:
            fich.write(line)
        fich.close()

        input("\nORDENACIÓN TERMINADA. Pulsa INTRO para continuar. ")

        os.system('cls')
        menugeneral()

    def modificarContacto(nombre_ant,telefono_ant):                 # PERMITE MODIFICAR UN CONTACTO EXISTENTE EN LA AGENDA
        control=0

        fich = open("fichero.txt", "r")
        lines = fich.readlines()
        fich.close()

        for line in lines:
            if nombre_ant+"---"+telefono_ant+"-" in line:
                control+=1
        if control==0:
            input("\nCONTACTO NO ENCONTRADO. Pulsa INTRO para continuar. ")
            os.system('cls')
            menugeneral()

        print("INTRODUCE DATOS NUEVOS")
        nombre = input("\t\tNombre: ")
        telefono = input("\t\tTeléfono: ")

        if nombre_ant != nombre or telefono_ant != telefono:
            AgendaContactos.controlContacto(nombre,telefono)
            AgendaContactos.controlLista(nombre,telefono)

        email = input("\t\tE-mail: ")
        empresa = input("\t\tEmpresa: ")
        telefOficina = input("\t\tTlf. Oficina: ")
        nuevo_contacto=nombre+'---'+telefono+'-'+email+'-'+empresa+'-'+telefOficina

        fich = open("fichero.txt", "w")

        for line in lines:
            if nombre_ant+"---"+telefono_ant+"-" in line:
                fich.write(nuevo_contacto + "\n")
            else:
                fich.write(line)
        input("\nCONTACTO MODIFICADO. Pulsa INTRO para continuar. ")

        fich.close()

        os.system('cls')
        menugeneral()

    def borrarContacto(nombre,telefono):                            # ELIMINA DE LA AGENDA LOS CONTACTOS DESEADOS
        control=0
        fich = open("fichero.txt", "r")
        lines = fich.readlines()
        fich.close()

        fich = open("fichero.txt", "w")

        for line in lines:
            if nombre == "" and telefono == "":
                control+=1
            elif nombre+"---"+telefono+"-" in line:
                control+=1
            else:
                fich.write(line)

        if control==0:
            input("\nCONTACTO NO ENCONTRADO. Pulsa INTRO para continuar. ")
        elif control==1:
            input("\nCONTACTO BORRADO. Pulsa INTRO para continuar. ")
        else:
            input("\nBORRADOS TODOS LOS CONTACTOS DE LA AGENDA. Pulsa INTRO para continuar. ")

        fich.close()

        os.system('cls')
        menugeneral()



# MENÚ GENERAL
lista = []
def menugeneral():
    print("\n\t\t\tAGENDA DE CONTACTOS", "\n", "*" * 65)
    print("1. Añadir contacto")
    print("2. Listar contactos de la lista temporal")
    print("3. Eliminar contactos de la lista temporal")
    print("4. Leer contactos de la agenda")
    print("5. Grabar contactos nuevos en la agenda")
    print("6. Ordenar agenda")
    print("7. Modificar contacto de la agenda")
    print("8. Borrar contacto de la agenda")

    opcion = input("\n\t\t---> Pulsa opción deseada ('S' para SALIR): ")
    while opcion not in ('1', '2', '3', '4', '5', '6', '7', '8', 'S', 's'):
        opcion = input("\t\t---> No lo flipes. Pulsa opción deseada ('S' para SALIR): ")

    os.system('cls')
    
    if opcion == '1':
        print("\n\t\t\tAGENDA DE CONTACTOS", "\n", "*" * 65)
        print("1. Añadir contacto")
        print("\n\tIntroduce datos del nuevo contacto")

        nombre = input("\t\tNombre: ")
        telefono = input("\t\tTeléfono: ")

        control=AgendaContactos.controlContacto(nombre,telefono)
        AgendaContactos.controlLista(nombre,telefono)
        if control == 1:
            email = input("\t\tE-mail: ")
            empresa = input("\t\tEmpresa: ")
            telefOficina = input("\t\tTlf. Oficina: ")

            AgendaContactos.addContacto(nombre, telefono, email, empresa, telefOficina)

    elif opcion == '2':
        print("\n\t\t\tAGENDA DE CONTACTOS", "\n", "*" * 65)
        print("2. Listar contactos de la lista temporal")
        AgendaContactos.listarContactos(lista)

    elif opcion == '3':
        print("\n\t\t\tAGENDA DE CONTACTOS", "\n", "*" * 65)
        print("3. Eliminar contactos de la lista temporal")
        AgendaContactos.eliminarContactos(lista)

    elif opcion == '4':
        print("\n\t\t\tAGENDA DE CONTACTOS", "\n", "*" * 65)
        print("4. Leer contactos de la agenda")
        AgendaContactos.abrirFichero(lista)
        AgendaContactos.leerContactos(lista)

    elif opcion == '5':
        print("\n\t\t\tAGENDA DE CONTACTOS", "\n", "*" * 65)
        print("5. Grabar contactos nuevos en la agenda")
        AgendaContactos.grabarContactos(lista)

    elif opcion == '6':
        print("\n\t\t\tAGENDA DE CONTACTOS", "\n", "*" * 65)
        print("6. Ordenar agenda")
        AgendaContactos.abrirFichero(lista)
        AgendaContactos.ordenarAgenda(lista)

    elif opcion == '7':
        print("\n\t\t\tAGENDA DE CONTACTOS", "\n", "*" * 65)
        print("7. Modificar contacto de la agenda")
        AgendaContactos.abrirFichero(lista)
        print("\nIntroduce el contacto de la agenda a modificar: ")
        nombre = input("\t\tNombre: ")
        telefono = input("\t\tTeléfono: ")
        AgendaContactos.modificarContacto(nombre,telefono)

    elif opcion == '8':
        print("\n\t\t\tAGENDA DE CONTACTOS", "\n", "*" * 65)
        print("8. Borrar contacto de la agenda")
        AgendaContactos.abrirFichero(lista)
        print("\nIntroduce contacto a borrar de la agenda (DOBLE INTRO para BORRAR TODOS): ")
        nombre = input("\t\tNombre: ")
        telefono = input("\t\tTeléfono: ")
        AgendaContactos.borrarContacto(nombre,telefono)

    elif opcion == 'S' or opcion == 's':
        print("\n\t\t\tAGENDA DE CONTACTOS", "\n", "*" * 65)
        input("¡¡¡ HASTA OTRA !!!")
        sys.exit()

menugeneral()
