import os
import sys
if len(sys.argv) != 1:
  arg = sys.argv[1]

else:
  arg = "."

print("\n".join(os.listdir(arg)))
