def test_exceptions(numerator, denominator):
    try:
        division = numerator / denominator
    except ValueError as value_error:
        print(value_error)
    except NameError as name_error:
        print(name_error)
    except ZeroDivisionError as zero_division_error:
        print(zero_division_error)
    except TypeError as type_error:
        print(type_error)
    else:
        return division


numerator = 1
denominator = 'la'
#print(numerator, '/', denominator, '=', test_exceptions(numerator, denominator))

try:
    x = int(input("Please enter a number: "))
except ValueError:
    print('No valid number')

x = str(input("Please enter a number: "))
