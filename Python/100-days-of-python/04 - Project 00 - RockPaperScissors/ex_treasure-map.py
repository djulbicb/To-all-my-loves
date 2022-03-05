# Tiles
tiles = [
  [" 📦", "📦", "📦"],
  ["📦", "📦", "📦"],
  ["📦", "📦", "📦"]
]
print(tiles[0],"\n",tiles[1],"\n",tiles[2])
position = "1,2".split(',') # input('where to put treasure')
posX = int(position[0])
posY = int(position[1])
tiles[posX][posY] = 'X'
print(tiles[0],"\n",tiles[1],"\n",tiles[2])