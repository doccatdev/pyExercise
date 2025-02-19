# def convertToFahrenheit(degreesCelcius):
#     fahrenheit = degreesCelcius * (9/5) + 32
#     return fahrenheit

# result = convertToFahrenheit(32)
# print(result)

def convertToCelcius(degreesFahrenheit):
    return (degreesFahrenheit - 32) * (5/9)

result_2 = convertToCelcius(100)
print(result_2)