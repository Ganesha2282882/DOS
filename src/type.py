import sys
if len(sys.argv) != 1:
  arg = sys.argv[1]

else:
  print("ERROR: No file specified.")
  sys.exit(1)

with open(arg, "rt") as f:
  print(f.read())
