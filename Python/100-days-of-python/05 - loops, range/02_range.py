# do 20, ali ne 20
for num in range(1, 20):
  print(num)

# step by 3
for num in range(1, 20, 3):
  print(num)

# ex: Sum all numbers from 0 to 100
print("--------------------")
total = 0
for num in range(0, 101):
  total += num
print(total)

# ex: Sum all numbers from 1 to 100, including those
print("--------------------")
sum = 1
for i in range(2,101,2):
  sum += i
print(sum)

sum2 = 0
for i in range(1, 101):
  if i%2 == 0:
    sum2 += i
print(sum2)
