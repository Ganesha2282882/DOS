import os
import sys

if len(sys.argv) == 2:
  f = sys.argv[1]
  
else:
  print("ERROR: Invalid number of arguments.")
  sys.exit(1)

os.remove(f)
