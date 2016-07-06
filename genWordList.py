# -*- coding: utf-8 -*-
import string, os

### Save to clean once complete. 
def appendWordToTxt(word,txt_file):
	with open(txt_file, "a") as myfile:
		myfile.write("\n")
		myfile.write(word)


def readFile(raw_file, out_file):
	with open(raw_file) as fp:
		for i, line in enumerate(fp):
			l  = line.strip()
			words = l.split(" ")

			for w in words:
				#out = w.translate(string.maketrans("",""), string.punctuation) ### removes punctuation, makes it unreadable in series
				out = w 
				### Messy, but in a rush, sorry 
				for o in out:
					if o.isalnum() == True: ## check if there is at least one number or letter, otherwise assume its a dash or something 
						#print out
						appendWordToTxt(out, out_file)
						break ## found something so we can stop the search

			### TESTING PHASE LINE LIMIT	
			#if i == 10: # TESTING PHASE
			#	break


def Main():
	### Find local files
	localdir = os.path.dirname(os.path.realpath(__file__))
	raw = "allTextOrdered.txt"
	out = "Chilcot-Report_word-by-word.txt"
	raw_file = os.path.join(localdir, raw)
	out_file = os.path.join(localdir, out)

	readFile(raw_file, out_file)


if __name__ == '__main__':
	Main()