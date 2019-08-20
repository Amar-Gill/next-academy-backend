while True:
    try:
        number = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was not a valid number.  Try again...")

def roman(x):

    if type(x) != int:
        return 'wtf??'
    else:
        roman_numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        output = ''

        for index, i in enumerate(values):
            if x >= i:
                output = output + roman_numerals[index]*(x//i)
                x = x%i
        return output


print(roman(number))