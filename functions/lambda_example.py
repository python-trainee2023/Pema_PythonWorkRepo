# num=[1,2,3,4,5,6]
# even=list(filter(lambda x : x%2==0, num))
# print(even)

# lambda x : x**2 lambad simple expression eg

#map in lambda
num=[1,2,3,4,5,6]
even=list(filter(lambda x : x%2==0, num))
print(even)

square=list(map(lambda x : x**2, num))
print(square)

