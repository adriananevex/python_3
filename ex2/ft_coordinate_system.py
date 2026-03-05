import sys
import math

def distance_3d(p1, p2):
  x1, y1, z1 = p1
  x2, y2, z2 = p2
  return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

def parse_coordinates(coord_str):
  parts = coord_str.split(",")
  if len(parts) != 3:
    raise ValueError("Expected format 'x,y,z' with 3 values")
  x = int(parts[0])
  y = int(parts[1])
  z = int(parts[2])
  return tuple((x, y, z))

def main():
  print("=== Game Coordinate System ===")

  origin = tuple((
