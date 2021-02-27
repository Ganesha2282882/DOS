#!/bin/bash
echo "Compiling DOS subsystem"
cd src
mkdir commands
for i in *.py; do
  pyinstaller --onefile $i
  cp dist/* commands
  rm -rf dist
done
cd commands
tar -czf ../commands.tar.gz .
cd ../..
