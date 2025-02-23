def area(length, width):
    area = length * width
    return area

output = area(10,4)
print(output)

def perimeter(length, width):
    perimeter = 2 * length + 2 * width
    return perimeter

output = perimeter(10,4)
print(output)


def volume(length, width, height):
    volume = length * width * height
    return volume


output = volume(10,4,5)
print(output)

def surface_area(length,width,height):
    surface = (length * width * 2) + (length * height * 2) + (width * height *2)
    return surface

output = surface_area(10,4,5)
print(output)
