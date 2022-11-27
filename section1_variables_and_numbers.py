"""always start with a letter or underscore"""
number = 5
print(number)

_Number = 10
print(_Number)

suma = number + _Number
print(suma)

decimalNumber = 29.38
print(decimalNumber)

decimal = number + decimalNumber
print(type(decimal), " ", decimal)


"""concatenate strings"""
cad = "hola mundo"
print(cad)

cad1 = "hy"
cad2 = "world"
cad3 = cad1 + " " + cad2
print(cad3)


"""types of variable"""
print(type(number))
print(type(decimalNumber))

"""data type conversions"""
numberTostring = 89
cadNumber = str(numberTostring)
print(type(cadNumber), " ", cadNumber)

stringToInt = int(cadNumber)
print(type(stringToInt), " ", stringToInt)

floatTostring = 101.23
cadFloat = str(floatTostring)
print(type(cadFloat), " ", cadFloat)
strToFloat = float(cadFloat)
print(type(strToFloat), " ", strToFloat)

"""
EJERCICIO 1
-create a variable "number1" with the value 5, display the type of the variable
-create a variable "number2" with the value 6.5, display the type of the variable
-create a variable "number3" with the value 7, display the type of the variable
-create a variable "suma" wich contains the value of the sum of the other three variables
 show the result and display the type of the varaible
"""
print("----ejercicio 1----")
number1 = 5
print(type(number1))
number2 = 6.5
print(type(number2))
number3 = 7
print(type(number3))
suma = number1+number2+number3
print("suma: ", suma)
print(type(suma))
print("--------------------")

"""
EJERCICIO 2
-create a variable "number1" with the value 5
-create a variable "number2" with the value 3
-create a variable "suma" wich contains the value of the sum of the other two variables
-convert the variable "suma" to string and name it "strSuma"
-create a varaible "resultado" that concatenate the text "el resultado es " and the varaible strSuma
"""
print("----ejercicio 2----")
number1 = 5
number2 = 3
suma = number1 + number2
strSuma = str(suma)
resultado = "el resultado es " + strSuma
print(resultado)