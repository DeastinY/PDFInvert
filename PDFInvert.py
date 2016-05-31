import os
import sys
from pdfrw import PdfReader, PdfWriter

if len(sys.argv) != 2:
    print("Usage: InvertOrder.py FILETOINVERT")
    sys.exit()

filename = sys.argv[1]
output = PdfWriter()

for p in reversed(PdfReader(filename).pages):
    output.addpage(p)

fname, fext = os.path.splitext(filename)
outname = fname + "_inv" + fext

print("Writing output to "+outname)

output.write(outname)
