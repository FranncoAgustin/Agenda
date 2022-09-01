from os import system



class Agenda:
    def __init__(self) -> None:
        self.contactos = ["", ]
    
    def cuadrado_est(self) -> None:
        print(' '* 50,'='*32,' '*40)
    
    def limpiar_pantalla(self) -> None:
        system('cls')

    def menu(self) -> None:
        self.limpiar_pantalla()
        print(' '* 50,'='*32,' '*40)
        print(' '* 50,"|     Bienvenido al menu       |")
        print(' ' * 50,"| Opcion 1: Añadir contacto.   | \n ",' ' * 48, "| Opcion 2: Editar contacto.   | \n",' ' * 49, "| Opcion 3: Lista de contactos.| \n ",' ' * 48,"| Opcion 5: Cerra agenda.      |" )
        #print(' ' * 50,"| Ingresar opcion deseada:     |",' '*40)
        print(' '* 50,'='*32,)
        opcion=int(input("                                                      Ingresar opcion deseada: "))
        if opcion==1:
                self.limpiar_pantalla()
                self.Añadir_contacto()
        if opcion==2:
                self.limpiar_pantalla()
                self.editar_contacto()
        if opcion==3:
                self.limpiar_pantalla()
                self.lista_contactos()
        if opcion==4:
                self.limpiar_pantalla()
                print("Adios")
                exit
        
    def lista_contactos(self) -> None:
        contador=1
        for r in range(1, len(self.contactos), 1):
            self.cuadrado_est()
            print(f" {' '*49} {contador}. {self.contactos[r]}")
            contador += 1
        self.cuadrado_est()

    def editar_contacto(self):
        self.limpiar_pantalla()
        self.lista_contactos()
        orden = int(input("                                                   | Ingrese el numero del contacto que desea editar: "))
        self.cuadrado_est()
        act_contacto = {"nombre": str,
                        "Tel": int,
                        "Email": str}
        act_contacto["nombre"] = input(f' {" "*49} Ingrese nuevo nombre: ')
        act_contacto["Tel"] = int(input(f' {" "*49} Ingrese nuevo numero de telefono: '))
        act_contacto["Email"] = input(f' {" "*49} Ingrese nuevo email: ')
        self.contactos[orden] = act_contacto
        self.cuadrado_est()
        input("                                                   | Contacto actualizado         | \n                                                   | Presione enter para seguir   |")
        return self.menu()

    def Añadir_contacto(self) -> None:    
        end=False
        while end==False:
            contacto = {"nombre": str,
                        "Tel": int,
                        "Email": str}
            self.limpiar_pantalla()
            self.cuadrado_est()
            contacto["nombre"] = input("                                                          Ingrese su nombre: ")
            contacto["Tel"] = int(input("                                                    Ingrese su numero de telefono: "))
            contacto["Email"] = input("                                                           Ingrese su email: ")
            self.cuadrado_est()
            self.limpiar_pantalla()
            self.cuadrado_est()
            print(' '* 50,"Usted a ingresado:  \n",' '* 49, "Nombre:" ,contacto["nombre"], "\n" ,' '* 49,  "Telefono:" ,contacto["Tel"], "\n",' '* 48," Email:" ,contacto["Email"], "\n",' '* 48," Si esto es correcto y desea guardar los datos: ")
            confirm=int(input("                                                   Por favor ingrese: 1 para guardar, 2 para modificar:  "))
            self.cuadrado_est()
            if confirm==1:
                self.contactos.append(contacto)
                print("                                               Los datos se han guardado correctamente")
                self.cuadrado_est()
                fin=int(input("                                                  Si desea seguir agregando contactos, \n                                              presione 1, si desea volver al menu, presione 2:  "))
                if fin==1:
                    pass
                else:
                    end=True
                    return self.menu()
            elif confirm==2:
                self.limpiar_pantalla()
                self.cuadrado_est()
                print(' '* 50,"Usted a decidido modificar. Los datos \n " ,' '* 48,"anteriormente ingresados no se guardaron.")
                self.cuadrado_est()
                input("                                                   Presione enter para seguir")
            elif confirm!=1 or confirm!=2:
                self.cuadrado_est()
                print("Vuelva a intentar, ingreso mal la opcion")
                self.cuadrado_est()
        return self.menu()        
            

    

            

def main():
    Agenda().menu()


main()