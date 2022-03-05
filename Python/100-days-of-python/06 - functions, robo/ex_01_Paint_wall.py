import math

def calc_cans_for_area(width, height, perMeterCoverage):
  area = width * height
  cans = math.ceil(area / perMeterCoverage)
  return cans

print(calc_cans_for_area(2, 4, 5))