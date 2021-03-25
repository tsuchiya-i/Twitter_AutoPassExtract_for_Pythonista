import re,sys,keyboard,shutil,console

pos = __file__.find('Pythonista3/Documents')
libdir = __file__[:pos]+"Pythonista3/Documents/site-packages-3/"

def convert_from_hash(hash_text):
	return original_text

def run(ar1="",ar2="",ar3="1"):
	if keyboard.has_full_access()==False:
		console.hud_alert("フルアクセスを有効にしてください。","error")
		sys.exit()
	if __file__.count('Documents/XAUTO/master.py')==0:
		console.hud_alert("ファイル名もしくはDL場所が異なります。","error")
		sys.exit()
	
	impc=0
	try:
		import requests_oauthlib
	except:
		shutil.move('./lib/oauthlib',libdir)
		impc += 1
	try:
		import tweepy
	except:
		shutil.move('./lib/tweepy',libdir)
		impc += 1
	try:
		from requests_oauthlib import OAuth1Session
		from urllib.parse import parse_qsl
	except:
		shutil.move('./lib/requests_oauthlib',libdir)
		shutil.move('./lib/socks.py',libdir)
		shutil.move('./lib/sockshandler.py',libdir)
		impc += 1
	if impc > 0:
		print("+++++++++++++++\nタスクを切って\nPythonistaを再起動してください。\n+++++++++++++++")
		import sys
		sys.exit()	
	
	
	if not keyboard.is_keyboard():
		try:
			f = open('.tw.txt', 'r')
			for row in f:
				settingtxt = row.strip()
			f.close()
			codes = re.split('#', settingtxt)
			CK = convert_from_hash(codes[0])
			CS = convert_from_hash(codes[1])
			AT = convert_from_hash(codes[2])
			AS = convert_from_hash(codes[3])
			auth = tweepy.OAuthHandler(CK, CS)
			auth.set_access_token(AT, AS)
			tw_api = tweepy.API(auth)
			abc=tw_api.me()
			if not ar3 == "1":
				import sys
				import firstset
				firstset.link(ar1,ar2,ar3)
				sys.exit()
		except Exception as e:
			#print(e)
			import sys
			import firstset
			if len(ar1)==0:
				firstset.run_ui(e)
				sys.exit()
			else:
				firstset.link(ar1,ar2)
				sys.exit()
	
		import mainset
		mainset.main()
	else:
		import xauto
