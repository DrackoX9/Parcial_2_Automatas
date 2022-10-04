import re


clase="((extern|static|register) +)?"
tipo="(short int|int|long int|bool|float|double|long double)"#agregar el espacio entre tipo u nombre de variable
reservadas="(?!((int|short int|long int|bool|float|double|long double|const|if|else|while|switch|case|break|for|do|static|extern|register|auto)(\s|;)+))"
indent=reservadas+"([a-z]|[A-Z]|_)+([a-z]|[A-Z]|_|[0-9])*;"#falta evitar que se ingresen palabras reservadas
exp="(=[0-9]+(.[0-9]+)*)?;"
#{1} indica que debe haber solo 1 repeticion
#? indica que puede haber 0 o no mas de 1 repeticion
#?! es una forma de negacion que indica que no puede estar presente una cadena en una posicion indicada
variables=" *"+clase+tipo+" +"+indent+""

cadena = input("Ingrese la cadena: ")
result = re.fullmatch(indent, cadena)
if result:
    print("Cadena aceptada")
else:
    print("Cadena NO aceptada")



#<clase><tipo><iden>[=<exp>][,<iden>[=<exp>][...]];
