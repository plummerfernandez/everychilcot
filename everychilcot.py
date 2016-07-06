# -*- coding: utf-8 -*-

from twython import Twython, TwythonError
import os, ConfigParser



### Code adapted from EveryWord, thank you A.Parrish
def get_current_index(index_file_name):
	if not(os.path.isfile(index_file_name)):
		return 0
	with open(index_file_name) as index_fh:
		return int(index_fh.read().strip())

def increment_index(index_file_name, index):
	with open(index_file_name, "w") as index_fh:
		index_fh.truncate()
		index_fh.write("%d" % (index + 1))
		index_fh.close()

def get_current_line(source_file_name, index):
	with open(source_file_name) as source_fh:
		# read the desired line
		for i, status_str in enumerate(source_fh):
			if i == index:
				break
		return status_str.strip()

### returns next word and updates index file
def getNextWord(ind_file, src_file):
	index = get_current_index(ind_file)
	print index
	status_str = get_current_line(src_file, index)
	increment_index(ind_file, index)
	return status_str

### Only twitter function here, simply tweets
def tweetStatus(twitter, msg):
	print ">>> tweeting now"
	print msg
	twitter.update_status(status=msg)
	print "[+] status updated"


def Main():
	### Find local files
	localdir = os.path.dirname(os.path.realpath(__file__))
	ind = "index"
	src = "Chilcot-Report_word-by-word.txt"
	ind_file = os.path.join(localdir, ind)
	src_file = os.path.join(localdir, src)
	### get next word
	nextWord = getNextWord(ind_file, src_file)
	print nextWord

	### tweet status
	# put your twitter api_key, secret, oauth token and oauth secret into settings.cfg
	config = ConfigParser.ConfigParser()
	try:
		localdir = os.path.dirname(os.path.realpath(__file__))
		print localdir
		print localdir
		config.read(localdir + '/settings.cfg')
		print "[+] Read settings"
	except:
		print "[-] Could not read settings"

	tw_key = config.get('twitter','API_KEY')
	tw_secret = config.get('twitter','API_SECRET')
	tw_token = config.get('twitter','OAUTH_TOKEN')
	tw_tsecret = config.get('twitter','OAUTH_TOKEN_SECRET')

	print '[+] Twitter client requested' 

	twitter = Twython(tw_key, tw_secret, tw_token, tw_tsecret) 
	
	tweetStatus(twitter, nextWord)



if __name__ == '__main__':
	Main()
