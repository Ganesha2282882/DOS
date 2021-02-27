import sys

if len(sys.argv) == 3:
  inf = sys.argv[1]
  outf = sys.argv[2]

else:
  print("ERROR: Invalid number of arguments")
  sys.exit(1)

fin = open(inf, "rb")
fout = open(outf, "wb")
fout.write(fin.read())
fin.close()
fout.close()
