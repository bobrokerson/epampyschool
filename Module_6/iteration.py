#Task #1
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
  
#Task #2
''' Calculate the total amount you will pay if the purchase costs $N
and the following discounts are provided: if the purchase costs less 
than $100 - a 5% discount, if the purchase costs from $100 to $200 -
a 10% discount, and, finally, if the purchase costs $200 and more - a
15% discount '''

purchase_price = int(input("Enter the purchase price: "))
discount = 0

if purchase_price < 100:
    discount = 5
    purchase_price *= 0.95
elif purchase_price > 200:
    discount = 15
    purchase_price *= 0.85
else:
    discount = 10
    purchase_price *= 0.9
print("Your discount is {}%, the amount to be paid is ${:.2f}.".format(
    discount,
    purchase_price,
))

#Task #3
'''A car drove N miles in 0.5 hours. 
Did the driver violate the traffic rules if the speed limit was 45 mph?'''
hours = 0.5
distance = int(input("Enter the number of miles: "))
while not 0 <= distance:    #checking for correct numeric input
    print("Enter the correct value")
    distance = int(input("Enter the number of miles: "))
 
if distance/hours > 45:
    print("The driver violated the traffic rules")
else:
    print("The driver didn't violate the traffic rules")