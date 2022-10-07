import re

#{1} indica que debe haber solo 1 repeticion
#? indica que puede haber 0 o no mas de 1 repeticion
#?! es una forma de negacion que indica que no puede estar presente una cadena en una posicion indicada



clase="((extern|static|register) +)?" #clases de la variable
tipo="(short int|int|long int|bool|float|double|long double)"#tipo de dato
reservadas="(?!((int|short int|long int|bool|float|double|long double|const|if|else|while|switch|case|break|for|do|static|extern|register|auto)(\s|;)+))"#palabras reservadas
variable=reservadas+"([a-z]|[A-Z]|_)+([a-z]|[A-Z]|_|[0-9])*"#nombre de la variable
operadoresA="(\*|\+|/|-|>|==|<|¡=|<=|>=|=)"#operadores aritmeticos
operadoresL="(&&|\|{2})"
exp="((\s)*=(\s)*)?;"#expresion de asignación MEJORAR


#Expresion regular completa para la declaración de variables numericas
declaracion=" *"+clase+tipo+" +("+variable+";|"+variable+exp+")"
#condSimp = una variable sola, una variable o numero, seguido de un operador aritmetico seguido de una variable o 
#           numero una o mas veces 
condSimp="("+variable+"|("+variable+"|[0-9]+(.[0-9]+)?)(\s)*("+operadoresA+"("+variable+"|[0-9]+(.[0-9]+)?)(\s)*)+)"

#condComp = a una condicion simple o condicion simpleentre parentesis, seguida de un operador logico, seguido de una condicion simple entre parentesis, repetida una o mas veces 
condComp="(\("+condSimp+"\)(\s)*"+operadoresL+"\("+condSimp+"\)(\s)*)"
condicion="("+condSimp+"|"+condComp+"+)"

#expresion regular completa para la condicional if 
CondicionalIF="if\("+condicion+"\)"

#expresion regular completa para la condicional while 
bucleWhile="while\("+condicion+"\)"

cadena = input("Ingrese la cadena: ")
result = re.fullmatch(CondicionalIF, cadena)
if result:
    print("Cadena aceptada")
else:
    print("Cadena NO aceptada")



#<clase><tipo><iden>[=<exp>][,<iden>[=<exp>][...]];
