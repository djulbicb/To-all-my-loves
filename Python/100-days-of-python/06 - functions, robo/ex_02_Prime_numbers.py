# Prime brojevi su svi brojevi koji su deljivi samo sa 1 i samim sobom
# koriste se za cicadas, bitcoin i enkripciju

def is_prime(number):
  isPrime = False;

  if (number == 1):
    print(f"{number} is prime")
    return

  for i in range (1, number):
    if (number % i == 0):
      isPrime = False;
      break;
    else:
      isPrime = True;

  if (isPrime):
    print(f"{number} is prime")
  else:
    print(f"{number} is NOT prime")

is_prime(7)