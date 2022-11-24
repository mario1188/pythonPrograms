"""always start with a letter or underscore"""
number = 5
print(number)

_Number = 10
print(_Number)

suma = number + _Number
print(suma)

decimalNumber = 29.38
print(decimalNumber)

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
