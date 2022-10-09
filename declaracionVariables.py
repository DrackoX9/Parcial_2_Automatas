import re
from os import system

#{1} indica que debe haber solo 1 repeticion
#? indica que puede haber 0 o no mas de 1 repeticion
#?! es una forma de negacion que indica que no puede estar presente una cadena en una posicion indicada

#clases de la variable
#esta expresion indica
#no mas de una instancia de las palabras contenidas dentro, seguida de uno o mas espacio en blanco 
clase="((extern|static|register)(\s)+)?" 

tipo="(short int|int|long int|bool|float|double|long double|char)"#tipo de dato

#En esta expresion se indica que no puede estar presente ninguna de las cadenas dentro de la expresion
#estas cadenas corresponden a las palabras reservadadas (no todas) que no pueden usarse para nombres de variables
#niega todas las palabras dentro de () si y solo si estan seguidas de uno o mas espacios o ;
reservadas="(?!((char|int|short int|long int|bool|float|double|long double|const|if|else|while|switch|case|break|for|do|static|extern|register|auto)(\s|;)+))"#palabras reservadas


#Nombre de la variable
#uniendo le negacion de palabras reservadas se comprueba que no sea un nombre resercado, si no lo es entonces se valida
#que el nombre de la variable cumpla con las reglas:
#No puede ser una palabra resercada o iniciar con numeros
#puede iniciar con una o mas letras mayus, minus o guion bajo, seguida o no de cualquier cantidad de numeros enteros o letras y guiones
variable=reservadas+"([a-z]|[A-Z]|_)+([a-z]|[A-Z]|_|[0-9])*"#nombre de la variable


#Operadores
#expresiones que indican que se puede usar uno de los operadores contenidos dentro
operadoresA="(\*|\+|/|-|>|==|<|¡=|<=|>=|=)"#operadores aritmeticos
operadoresL="(&&|\|{2})"




#Condicion simple
#Esta expresion indica
#Puede ser una unica variable, un numero o variable seguido de un operador aritmetico con una variable o numero, indicando que
#se puede repetir la parte del operador seguido de variable o numero, mas de una vez
condSimp="("+variable+"|[0-9]+(.[0-9]+)?|("+variable+"|[0-9]+(.[0-9]+)?)(\s)*("+operadoresA+"("+variable+"|[0-9]+(.[0-9]+)?)(\s)*)+)"


#Expresion
#Corresponde a la operacion de asignacion con el signo =
#la expresion indica
#puede o no iniciar con cualquier cantidad de espacios, seguido del signo = con o sin espacios
# despues del igual puede seguir uno o mas numeros del 0 al 9 seguido o no de: . por lo menos un numero
# o despues del igual puede ser una condicion simple
# toda la expresion es opcional o no se puede repetir mas de una vez y finalizada con ;
exp="((\s)*=(\s)*([0-9]+(.[0-9]+)?|"+condSimp+"))?;"

#Condicion compuesta
#La expresion indica
#puede ser una condicion simple, entre parentesis, seguida o no de espacios, seguido de un operadore logico 
#con una condicion simple,entre parentesis, finalizando con o sin espacios
#la parte del operador seguido de la condicion simple se puede utilizar una o mas veces
condComp="(\("+condSimp+"\)(\s)*("+operadoresL+"(\s)*\("+condSimp+"\)(\s)*)+)"


#Condicion 
#La expresion indica que puede ser una condicion simple o una condicion compuesta , debe estar presente una de las dos
condicion="("+condSimp+"|"+condComp+")"


#expresion regular completa para la condicional if 
#La expresion indica
#la palabra if sguida de una condicion,que puede ser simple o compuesta, entre parentesis
CondicionalIF="if\("+condicion+"\)"

#expresion regular completa para la condicional while 
#la expresion indica
#debe iniciar con la palabra while seguida de una condicion, que puede ser simple o compuesta, entre parentesis
bucleWhile="while\("+condicion+"\)"

#Expresion regular para la declaracion de variables
#la expresion indica
#puede iniciar o no con espacion en blanco, seguido o no de una clase, seguida de una tipo de dato, con un espacio
#luego puede ser una variable seguida de ; o una variable con asignacion, teniendo en cuenta que la expresion de asignacion termina con ;
declaracion="(\s)*"+clase+tipo+"(\s)+("+variable+";|"+variable+exp+")"




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


