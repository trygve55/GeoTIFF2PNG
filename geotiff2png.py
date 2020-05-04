import os
import gdal

print("Copy file path or drag file into terminal window, then press enter.")
infile = input("Input file:")
outfile = infile.rsplit('.', 1)[0] + ".png\""
print('Infile: ' + infile)
print('Outfile: ' + outfile)

os.system('gdal_translate -of GTiff -of PNG -ot Byte -scale ' + infile + ' ' + outfile)