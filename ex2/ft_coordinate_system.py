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

  origin = tuple((0, 0, 0))

  pos = tuple((10, 20, 5))
  print("Position created:", pos)
  dist = distance_3d(origin, pos)
  print("Distance between", origin, "and". pos + (":",), round(dist, 2))
  
  coord_text = "3,4,0"
  print('Parsing coordinates: "3,4,0"')
  try:
    parsed = parse_coordinates(coord_text)
    print("Parsed position:", parsed)
    dist2 = distance_3d(origin, parsed)
    print("Distance between", origin, "and", parsed + (":",), float(dist2))
  except Exception as e:
    print("Error parsing coordinates:", e)

  bad_text = "abc,def,ghi"
  print('Parsing invalid coordinates: "abc,def,ghi"')
  try:
    bad_pos = parse_coordinates(bad_text)
    print("Parsed position:", bad_pos)
  except Exception as e:
    print("Error parsing coordinates:", e)
    print("Error details - type:", type(e).__name__ + ",", "Args:", e.args)

  print("Unpaking demonstration:")
  x, y, z = parsed
  print("Player at x+" + str(x) + ", y=" + str(y) + ", z=" + str(z))
  print("Coordinates: X=" + str(x) + ", Y=" + str(y) + ", Z=" + str(z))

if __name__ == "main__":
  main()