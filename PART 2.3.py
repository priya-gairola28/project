x = int(input('enter the 1st value'))   
y = int(input('enter the 2nd value')) 
# Swap code
x ^= y 
y ^= x 
x ^= y 
 

print("Value of x : ", x, " and y : ", y)
