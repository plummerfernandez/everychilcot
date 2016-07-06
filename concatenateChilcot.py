# -*- coding: utf-8 -*-
import string, os

def mergeTxts(raws_folder, out_file):
	src_files = os.listdir(raws_folder)
	count = 0
	filenames = []
	for file_name in src_files:
		print file_name
		full_file_name = os.path.join(raws_folder, file_name)
		filenames.append(full_file_name)

	# filenames = ['file1.txt', 'file2.txt', ...]
	with open(out_file, 'w') as outfile:
		for fname in filenames:
			with open(fname) as infile:
				for line in infile:
					outfile.write(line)




def Main():
	### Find local files
	localdir = os.path.dirname(os.path.realpath(__file__))
	raws = "txt_cleaned"
	out = "allTextOrdered.txt"
	raws_folder = os.path.join(localdir, raws)
	out_file = os.path.join(localdir, out)

	mergeTxts(raws_folder, out_file)


if __name__ == '__main__':
	Main()