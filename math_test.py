import math
import sys



jim = round (1.222222, 2)
print(jim)

print (math.factorial(500) )

print ( math.log(10) )

print ( math.pow(2,8) )

print (math.floor(2.8))
print()


print (sys.modules)

module_list = sys.modules

for mods in module_list:
    print ("mod = %s " % mods)


