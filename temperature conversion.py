# TEMPERATURE CONVERSION PROGRAM( CELCIUS , FAHRENHEIT , KELVIN )


#CELCIUS TO FAHRENHEIT

celcius = float(input("enter the temperature in celcius"))
fahrenheit = (celcius*1.8)+32
print("temperature in fahrenheit is",fahrenheit)

#CELCIUS TO KELVIN

celcius =float(input("\n enter the temperature in celcius"))
kelvin = celcius + 273.15
print("temperature in kelvin is",kelvin)

#FAHRENHEIT TO CELCIUS

fahrenheit = float(input("enter the temperature in fahrenheit"))
celcius = (fahrenheit-32)*5/9
print("temperature in celcius is",celcius)

#FAHRENHEIT TO KELVIN

fahrenheit =float(input("\n enter the temperature fahrenheit"))
kelvin = (fahrenheit + 459.67)/1.8
print("temperature in kelvin is",kelvin)

#KELVIN TO CELCIUS

kelvin =float(input("\n enter the temperature in kelvin"))
celcius = kelvin - 273.15
print("temperature in celcius is",celcius)

#KELVIN TO FAHRENHEIT

kelvin =float(input("\n enter the temperature kelvin"))
fahrenheit= (1.8*kelvin)- 459.67
print("temperature in fahrenheit is",fahrenheit)


