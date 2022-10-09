import re
from os import system

#{1} indica que debe haber solo 1 repeticion
#? indica que puede haber 0 o no mas de 1 repeticion
#?! es una forma de negacion que indica que no puede estar presente una cadena en una posicion indicada



clase="((extern|static|register)(\s)+)?" #clases de la variable
tipo="(short int|int|long int|bool|float|double|long double|char)"#tipo de dato
reservadas="(?!((char|int|short int|long int|bool|float|double|long double|const|if|else|while|switch|case|break|for|do|static|extern|register|auto)(\s|;)+))"#palabras reservadas
variable=reservadas+"([a-z]|[A-Z]|_)+([a-z]|[A-Z]|_|[0-9])*"#nombre de la variable
operadoresA="(\*|\+|/|-|>|==|<|¡=|<=|>=|=)"#operadores aritmeticos
operadoresL="(&&|\|{2})"




#condSimp = una variable sola, una variable o numero, seguido de un operador aritmetico seguido de una variable o 
#           numero una o mas veces 
condSimp="("+variable+"|[0-9]+(.[0-9]+)?|("+variable+"|[0-9]+(.[0-9]+)?)(\s)*("+operadoresA+"("+variable+"|[0-9]+(.[0-9]+)?)(\s)*)+)"

exp="((\s)*=(\s)*([0-9]+(.[0-9]+)?|"+condSimp+"))?;"#expresion de asignación MEJORAR
#Expresion regular completa para la declaración de variables numericas
declaracion="(\s)*"+clase+tipo+"(\s)+("+variable+";|"+variable+exp+")"

#condComp = a una condicion simple o condicion simpleentre parentesis, seguida de un operador logico, seguido de una condicion simple entre parentesis, repetida una o mas veces 
condComp="(\("+condSimp+"\)(\s)*("+operadoresL+"(\s)*\("+condSimp+"\)(\s)*)+)"
condicion="("+condSimp+"|"+condComp+")"

#expresion regular completa para la condicional if 
CondicionalIF="if\("+condicion+"\)"

#expresion regular completa para la condicional while 
bucleWhile="while\("+condicion+"\)"


def main():
    op=''
    cadena=''
    while op!='5':
        system("cls")
        print ("                     **************************************************")
        print ("                     *        UNVERSIDAD TECNOLOGICA DE PANAMA        *")
        print ("                     *  LENGUAJES FORMALES, AUTOMATAS Y COMPILADORES  *")
        print ("                     *               PROF: Abdiel Kapell              *")
        print ("                     *    Estudiantes: Joseph Rios / Danis Gonzales   *")
        print ("                     **************************************************\n")
        print ("        NOTA: Este programa se basa en la validacion de intrucciones del lenguaje C++\n")
        print ("                                       MENU PRINCIPAL")
        print ("                     Ingrese el numero de la opcion que desea validar\n")
        print ("        1. -------------------------------------------------- Declaracion de variable\n")
        print ("        2. ----------------------------------------------------------- Condicional IF\n")
        print ("        3. -------------------------------------------------------------- Bucle WHILE\n")
        print ("        4. ---------------------------------------------------------- VER EXPRESIONES\n")
        print ("        5. -------------------------------------------------------------------- Salir\n")
        op=input('         -> ')
        if op=='1':
            print ("        INGRESE LA INSTRUCCION CORRESPONDIENTE A LA DECLARACION DE UNA VARIABLE")
            print ("                                   LENGUAJE C++ ")
            cadena=input('         -> ')
            validar(cadena,declaracion)
        elif op=='2':
            print ("        INGRESE LA INSTRUCCION CORRESPONDIENTE A LA DECLARACION DE UNA INSTRUCCION \"IF\"")
            print ("                                   LENGUAJE C++ ")
            cadena=input('         -> ')
            validar(cadena,CondicionalIF)
        elif op=='3':
            print ("        INGRESE LA INSTRUCCION CORRESPONDIENTE A LA DECLARACION DE UNA INSTRUCCION \"WHILE\"")
            print ("                                   LENGUAJE C++ ")
            cadena=input('         -> ')
            validar(cadena,bucleWhile)
        elif op=='4':
            system("cls")
            print('                                EXPRESIONES REGULARES UTILIZADAS\n\n')
            print('                                    DECLARACION DE VARIABLES\n\n')
            print (declaracion+"\n\n")
            print('                                       DECLARACION DE IF\n\n')
            print (CondicionalIF+"\n\n")
            print('                                      DECLARACION DE WHILE\n\n')
            print (bucleWhile+"\n\n")
        elif op!='5':
            print('     ¡INGRESE UN VALOR VALIDO!')
            system('pause')
            op='0'
        system("pause")

#FIN DEL MAIN
def validar(cadena,expresion):
    result = re.fullmatch(expresion, cadena)
    if result:
        print("       --------------------------------INSTRUCCION VALIDA--------------------------\n\n")
    else:
       print("        ------------------------------INSTRUCCION NO VALIDA--------------------------\n\n")
                



main()


