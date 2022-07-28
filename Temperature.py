celsius = float(input ("Enter the temperature in Celsius "))
farheneit = (9/5)*celsius+32
print(farheneit)
if (farheneit>=104):
    print("It's Hot")
elif (farheneit<=50):
    print("It's Cold")
else:
    print("The temperature is nice")