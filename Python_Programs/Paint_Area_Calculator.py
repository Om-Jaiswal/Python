import math

def paint_calc(height, width, cover):
  area = height * width
  num_of_cans = math.ceil(area/cover)
  print(f"You'll need {num_of_cans} cans of paints.")

wall_height = int(input("Height of a wall: "))
wall_width = int(input("width of a wall: "))
coverage = 5
paint_calc(height=wall_height, width=wall_width, cover=coverage)