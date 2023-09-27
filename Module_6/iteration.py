'''Let's help Mary find out how many candies she can buy if 1 candy costs $2 and
she has some amount of money. We can solve the problem in 2 ways: by gradually
decreasing the available amount, but in this case, we can get a negative amount
at the last iteration. The second way presupposes that we add up a total cost
when adding each new candy and compare it with the available amount. Which of
the loops to use? In this case, both would work. The main thing is to correctly
set the condition for a loop'''

price = 2
amount = int(input("amount = "))
count = 0
sum = 0

while amount-sum >= 2:
    count += 1;
    sum += price;
print("The result = ",count)

for i in range(2, 6):
  for j in range(1,11):
    print(i,"*", j,"=", i * j)
  else:
    print("The end of the multiplication by", i)
  print()
    
#list of items
py_list = ['Apple','Mango','Guava','Pineapple']
i = 1

#Iterating over the list
for item in py_list:
  print ('Item ',i,' is ',item)
  i = i+1
