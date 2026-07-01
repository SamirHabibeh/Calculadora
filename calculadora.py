num1 = int(input("numero 1: ")); 
num2 = int(input("numero 2: "));

valor = 0

while True:
    print("-----------------");
    print("       MENU");
    print("-----------------");
    print("seleccione opcion");
    print("1) Sumar");
    print("2) Restar");      
    print("3) Multiplicar");       
    print("4) Dividir "); 
    print("5) Salir")

    opc = int(input("Elige una opcion: "));     

    if (opc == 1):
        print(f"La suma es {num1+num2}");
        break;
    elif (opc == 2):
        print(f"La resta es {num1-num2}");
        break;
    elif (opc == 3):
        print(f"La multiplicacion es {num1*num2}");
        break;
    elif (opc == 4):
        print(f"La division es {num1/num2}");
        break;
    elif(opc == 5):
        print("Hasta pronto!.")
        break
    else:
        print("Opcion no valida");
        break;