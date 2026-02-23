import sys

def main():
  print("=== Command Quest ===")

if len(sys.argv) == 1:
  print(f"Arguments received: {len(sys.argv) - 1}")
  for i, arg in enumerate(sys.argv[1:], 1):
    print(f"Argument {i}: {arg}")
