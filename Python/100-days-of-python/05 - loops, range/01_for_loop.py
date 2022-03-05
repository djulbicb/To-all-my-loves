fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " pie")

# Ex: Calculate avg height
print("---------------------------")
print(sum([15, 12, 13]), len([1, 3]))

heights = "190, 160, 150, 133, 164, 98".split(", ");
sum = 0;
count = 0;
for h in heights:
  sum += int(h)
  count += 1

avg = sum / count;
print(avg, round(avg))
## round zaokruzuje na veci, int na manji

# Ex: Highest score in class
## postoje max() i min()
print("---------------------------")
scores = [11,78,65,22,33,77,95,61,11]
max = scores[0]
min = scores[0]

for s in scores:
  if s > max:
    max = s
    continue
  if s < min:
    min = s
    continue

print(f"Maximum score is {max}, Minimum is {min}")





