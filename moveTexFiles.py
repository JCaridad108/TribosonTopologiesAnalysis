#!/usr/bin/env python3.7
import os
import pathlib as pth
## Move .tex files to tex_files directory 

try:
	if pth.Path("./tex_files").is_file():
		tex_files = [str(i) for i in list(pth.Path(".").glob("*.tex"))]
		print(f"Moving...\n    {tex_files}")
	else:
		raise
except:
	print("tex_files/ directory does not exist")
else:
	for f in tex_files:
		os.system("mv {} tex_files".format(f))
		#os.system("mv bkg_histo.tex tex_files")
		#os.system("mv bkg_muon_count.tex tex_files")
		#os.system
