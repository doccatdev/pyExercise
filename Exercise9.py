def getCheeseSquareColor(columns, rows):
    if columns < 1 or columns > 8 or rows < 1 or rows > 8:
        return ''
    if (columns % 2 == rows % 2):
        result = print("White")
    else:
        result = print("Black")
        return result
        
        
getCheeseSquareColor(7,7)