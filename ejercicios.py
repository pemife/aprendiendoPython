#---------------------------------------------------------
# EJERCICIOS SIMPLES
#---------------------------------------------------------

def ej2():
    cadena = "おはよう世界"
    print("ejercicio2:  " + cadena)

def ej3():
    print("あなたの名前は?")
    nombre = input()
    print("ejercicio3: こんにちは, " + nombre)

def ej4():
    nombre = input("お名前をください: ")
    while True:
        try:
            numero = int(input("お数をください: "))
            break;
        except ValueError:
            print("Debes poner un numero!")

    #print("あなたの名前は " + nombre + " です, そしてあなたの数は " + numero + " です.")
    if isinstance(numero, int):
        for i in range(numero):
            print("あなたの名前は " + nombre + " です")
    else:
        print("エラー: それは数字ではありません")

    #print(bool)

def ej5():
    nombre2 = input("あなたの名前を書いてください: ")
    print("あなたの名前は " + str(len(nombre2)) + " 文字です")

def ej6():
    operacion = ((3+2)/(2*5))**2
    print(operacion)

def ej7():
    while True:
        try:
            peso = float(input("illo, dime tu peso (kg): "))
            while True:
                try:
                    estatura = float(input("illo, dime cuanto mides (m): "))
                    imc = (peso/estatura**2)
                    break
                except ValueError:
                    print("Debes poner metros, por ejemplo 1.70")
            break
        except ValueError:
            print("Debes poner kilogramos, por ejemplo: 74.6")


    print(
    "\n\n" +
    "\t\t   IMC: " + str(imc) + "\n\n" +
    "-------------------------------------------------\n" +
    "| Peso inferior al normal \t|  <18.5\t\t|\n" +
    "| Peso normal \t\t\t|  18.5 - 24.9\t|\n" +
    "| Peso superior al normal\t|  25.0 - 29.9\t|\n" +
    "| Obesidad\t\t\t|  >30.0\t|\n" +
    "-------------------------------------------------"
    )

def ej8():
    while True:
        try:
            n1 = int(input("dame un entero: "))
            break
        except ValueError:
            print("debes poner un entero")

    while True:
        try:
            n2 = int(input("dame otro entero: "))
            break
        except ValueError:
            print("debes poner un entero")
    c = int(n1/n2)
    r = n1%n2
    print(str(n1) + " entre " + str(n2) + " da un cociente de " + str(c) + " y un resto de " + str(r))

def ej9():
    passw = input("dame una contraseña: ")
    passw2 = input("introduce la contraseña de nuevo: ")
    if passw.lower() == passw2.lower():
        print("Las contraseñas coinciden\n" + passw + " -> " + passw.lower() + "\n" + passw2 + " -> " + passw2.lower())
    else:
        print("Las contraseñas NO coinciden")


#ej2()
#ej3()
#ej4()
#ej5()
#ej6()
#ej7()
#ej8()
#ej9()


#---------------------------------------------------------
# EJERCICIOS DE CONDICIONALES
#---------------------------------------------------------

def ej11():
    while True:
        try:
            edad = int(input("dame tu edad: "))
            break;
        except ValueError:
            print("Debes insertar un entero")

    print(edad)

    if edad < 0:
        print("Has nacido acaso?!")
    elif edad >= 0 and edad < 18:
        print("Eres menor de edad")
    elif edad >= 18 and edad < 120:
        print("Eres mayor de edad")
    elif edad >= 120:
        print("Acaso estas vivo?!")
    else:
        print("WTF edad es esa?")

def ej12():
    contrasenia = input("Dame una contraseña: ")
    reContrasenia = input("Repite la contraseña: ")
    if contrasenia.lower() == reContrasenia.lower():
        print("Las contraseñas coinciden")
    else:
        print("Las contraseñas coinciden")


#ej11()
#ej12()
