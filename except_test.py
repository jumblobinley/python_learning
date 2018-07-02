
list = [1,2,3,4]
try:

    print( list [4] )
except IndexError as err:
    print('Oops')
    print(err)