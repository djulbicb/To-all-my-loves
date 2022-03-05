# Scope
print("------------SCOPE--------------")
enemies = 1
test = []
playerHealth = 0

def increaseEnemies():
  enemies = 2
  test.append("s")
  print(f"Values of enemies in method: {enemies}")

def game():
  def drinkPotion():
    potionStrength = 2
    print(playerHealth)

increaseEnemies()
game()
print(f"Values of enemies out of method: {enemies}")

# Python nema block scope u pythonu
# ne kreira sublocal scope. Tako da promenljiva je ili u metodi ili van
if 3>2:
  a = 10
print(a) # Da nije deklarisan bacilo bi NameError: a not defined

# Modifying Global Scope
# Nije preporucljivo global, bolje return statement
print("------------GLOBAL SCOPE--------------")
enemies = 1
def increase():
  # deklarisanje global promenljiva
  global enemies

  # enemies = 2 # kreira novu promenljivu
  enemies = 3

def returnIncrease():
  return 4

increase()
print(enemies)
enemies = returnIncrease()
print(enemies)

# Global scope za konstante
# uppercase, snake naming convention
PI_CONSTANT = 3.14159
def calc():
  return PI_CONSTANT