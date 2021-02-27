import os
import sys

if len(sys.argv) == 3:
  inf = sys.argv[1]
  outf = sys.argv[2]

else:
  print("ERROR: Invalid number of arguments.")
  sys.exit(1)

os.replace(inf, outf)
