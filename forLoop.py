## FOR LOOP STRUCTURE

'''
for "repeated value" in "list":

"true statement"

It takes the items as in sequence and processes them in a loop.


i = 5
print(i in range(5))

list1 = list(range(5))
print(list1)

list2 = list("python")
print(list2)

nums = list(range(8))

squares = []

for i in nums:
  squares.append(i**2)
print(squares)



nums = list(range(8))

even_squares = [i**2 for i in nums if i % 2 == 0]

odd_squares = [i**3 for i in nums if i% 2 == 1]

print(even_squares)
print(odd_squares)


mylist = [3, 5, 12, 7, 65, 35]

sum1 = 0

for i in mylist:
    sum1 = sum1 + i  # sum += i
    print(sum1)

print(sum1)

'''

mylist = [3,5,12,7,65,35]
print(mylist[0])

max1 = mylist[0]

for i in mylist:
  if i > max1:
    max1 = i
    print("max1: ", max1)
    print("i: ", i)
print(max1)

list1 = [1,2,3]
list2 = [4,5,6]

print(list(zip(list1,list2)))

