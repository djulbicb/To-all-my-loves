studentScores = {
  "Harry" : 81,
  "Ron" : 78,
  "Hermione" : 99,
  "Draco" : 74,
  "Neville" : 62
}

finalScores = {}
for student in studentScores:
  score = studentScores[student]
  if (score >= 91 and score <= 100):
    finalScores[student] = "Outstanding"
  elif (score >= 81 and score <= 90):
    finalScores[student] = "Exceeds expectations"
  elif (score >= 71 and score <= 80):
    finalScores[student] = "Acceptable"
  else:
    finalScores[student] = "Fail"

print(finalScores)

