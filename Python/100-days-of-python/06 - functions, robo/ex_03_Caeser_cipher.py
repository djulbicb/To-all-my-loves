art = '''
                                      _       _
                                     (_)     | |
  ___ __ _  ___  ___  ___ _ __    ___ _ _ __ | |__   ___ _ __
 / __/ _` |/ _ \/ __|/ _ \ '__|  / __| | '_ \| '_ \ / _ \ '__|
| (_| (_| |  __/\__ \  __/ |    | (__| | |_) | | | |  __/ |
 \___\__,_|\___||___/\___|_|     \___|_| .__/|_| |_|\___|_|
                                       | |
                                       |_|
'''
letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ' ]

# FUNCTIONS
# ---------------------------------------------------------------

def showLogo():
  print(art)

def encode (text, shift):
  encoded = ""
  for c in text:
    if c not in letters:
      encoded += c
      continue

    index = letters.index(c)

    encodeIndex = index + shift
    while (encodeIndex > len(letters)):
      encodeIndex = encodeIndex % len(letters)

    encoded += letters[encodeIndex]
    #print(c, index)

  print(f"Encoded word is {encoded}")
  return encoded

def decode (text, shift) :
  decoded = ""
  for c in text:
    if c not in letters:
      decoded += c
      continue

    index = letters.index(c)
    decodedIndex = index - shift

    while (decodedIndex < 0):
      decodedIndex = len(letters) - abs(decodedIndex) # ne mora abs jer python podrzava -index

    decoded += letters[decodedIndex]

  print(f"Decoded word is {decoded}")
  return decoded

# MAIN
# ---------------------------------------------------------------
endOfProgram = False
action = 'encode' # input("Enter action, 'encode' or 'decode': ");
text = 'Hello Bojan :3'.lower() # input('Enter message: ').lower()
shift = 109 # int(input('Type the shift number: '))

# while !endOfProgram --- ovo ne moze
# while endOfProgram != True: --- ovo moze
while not endOfProgram:
  showLogo()
  encoded = encode(text, shift);
  decode(encoded, shift)

  reset = input("Do you want to reset (y or n): ")
  if (reset == 'n'):
    endOfProgram = True


