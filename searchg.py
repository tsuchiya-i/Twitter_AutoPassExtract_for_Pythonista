import ui,shortcuts,datetime,keyboard,clipboard
import webbrowser,console,sys,re,time
import datetime, threading
from requests_oauthlib import OAuth1Session
import tweepy
import platform
import io
from objc_util import *
from PIL import Image

hour = ""
minutes = ""

tw_api = []

dirr = re.split('/', __file__)
send_code=0
send_code *= 1

def convert_from_hash(hash_text):
	return original_text

try:
	from urllib.parse import quote
	
	f = open('.tw.txt', 'r')
	for row in f:
		settingtxt = row.strip()
	f.close()
	codes = re.split('#', settingtxt)
	CK = convert_from_hash(codes[0])
	CS = convert_from_hash(codes[1])
	AT = convert_from_hash(codes[2])
	AS = convert_from_hash(codes[3])
	au = convert_from_hash(codes[4])
	if not au==str(send_code*33):
		console.hud_alert("購入者コードが無効です。")
		sys.exit()
except Exception as e:
	console.hud_alert('初期設定を先に行ってください。\n',"error")
	sys.exit()
	
def now_set(sender="NONE"):
	now = datetime.datetime.now()
	strnow = now.strftime('%H:%M:%S')
	v['nowtime'].text = strnow
	
def alltime_switch(sender):
	global hour,minutes
	now_set()
	if sender.superview['switch'].value==True:
		v['datepicker'].hidden=True
	else:
		v['datepicker'].hidden=False
		uitime = v['datepicker'].date
		minutes = uitime.strftime('%M')
		iminutes= int(minutes)
		
		if 0 < iminutes < 30:
			v['datepicker'].date=v['datepicker'].date + datetime.timedelta(minutes=30-iminutes)
		elif 30 < iminutes < 60:
			v['datepicker'].date=v['datepicker'].date + datetime.timedelta(minutes=60-iminutes)
		
		hour = str(int(uitime.strftime('%H')))

def detail_switch(sender):
	alltime_switch(sender)
	if sender.superview['detail'].value==True:
		console.hud_alert("少ないRTも検索結果に表示","success",0.5)

def exlow_switch(sender):
	alltime_switch(sender)
	if sender.superview['exlow'].value==True:
		console.hud_alert("少額ゲリラを検索結果から除く","success",0.5)

def gb_switch(sender):
	alltime_switch(sender)
	if sender.superview['gb'].value==True:
		console.hud_alert("GB鯖ゲリラを検索","success",0.5)

def qtime_make(sender):
	qtime=""
	if sender.superview['switch'].value==False:
		if minutes=="00":
			qtime = '('+hour+'時 OR '+hour+':'+minutes+' OR '+str(int(hour)+24)+'時 OR '+str(int(hour)+24)+':'+minutes+') '
		else:
			qtime = '('+hour+'時半 OR '+hour+'時'+minutes+'分 OR '+hour+':'+minutes+' OR '+str(int(hour)+24)+'時半 OR '+str(int(hour)+24)+'時'+minutes+'分 OR '+str(int(hour)+24)+':'+minutes+') '
	if sender.superview['exlow'].value==True:
		qtime+='-"少額" '
	if sender.superview['gb'].value==False:
		qtime+='-"GB" -"グロ" -"ｸﾞﾛ" -"gb" '
	else:
		qtime+='-"jp" -"JP" '
	if sender.superview['detail'].value==False:
		qtime+="min_retweets:5 "
	return qtime

search_fix = '-"自分用" -"共有" -"ノート" -"バトルパス" -filter:replies -"検索用" -"ゲリラ共有" -"先送り" -"#キル集" '
		
def single(sender):
	alltime_switch(sender)
	qtime=qtime_make(sender)
	q = '(シングルゲリラ OR #シングルゲリラ OR #シングル大会 OR #ゲリラシングル OR #シングルルーム) '+search_fix
	q = quote(qtime+q)
	webbrowser.open_new('twitter://search?query='+q)
	keyboard.set_view(None)
	keyboard.insert_text("\n")
	sys.exit()
def duo(sender):
	alltime_switch(sender)
	qtime=qtime_make(sender)
	q = '(デュオゲリ OR #デュオゲリラ OR #デュオ大会 OR #ゲリラデュオ OR #デュオルーム) '+search_fix
	q = quote(qtime+q)
	webbrowser.open_new('twitter://search?query='+q)
	keyboard.set_view(None)
	keyboard.insert_text("\n")
	sys.exit()
def squad(sender):
	alltime_switch(sender)
	qtime=qtime_make(sender)
	q = '(スクゲリ OR スクワット OR スクワッド OR #スクワットゲリラ OR #スクワット大会 OR #ゲリラスクワット OR #スクワットルーム) '+search_fix
	q = quote(qtime+q)
	webbrowser.open_new('twitter://search?query='+q)
	keyboard.set_view(None)
	keyboard.insert_text("\n")
	sys.exit()
def quinted(sender):
	alltime_switch(sender)
	qtime=qtime_make(sender)
	q = '(クイン OR クインテットゲリラ OR クインテッドゲリラ OR #クインテットゲリラ OR #クインテット大会 OR #ゲリラクインテット OR #クインテットルーム) '+search_fix
	q = quote(qtime+q)
	webbrowser.open_new('twitter://search?query='+q)
	keyboard.set_view(None)
	keyboard.insert_text("\n")
	sys.exit()


def url2id(url):
	userids = re.split('/|\\?', url)
	if len(userids) > 3:
		userid = userids[3]
	else:
		console.hud_alert('読み込めないURLです。')
	return userid
	
def tweets2element(atweets):
	atweet_text = ""
	atweet_name = ""
	for atweet in atweets:
		atweet_text += atweet.text+"エックス"
		atweet_name = atweet.author.name
	try:
		return (atweet_text, atweet_name)
	except:
		return ('エラー', '')

def tweet_get(twpy_api, userid):
	try:
		gtweets = twpy_api.user_timeline(count=3, screen_name=userid)
		return tweets2element(gtweets)
	except Exception as e:
		en = re.sub('[^0-9]','', str(e.args))
		if en == '88':
			console.hud_alert('【取得制限エラー】\n時間をおいてお試しください。\nこのエラーが頻繁に出る場合は取得速度を下げてお試しください。\n','error')

def guess_room(uname,ttext):
	candidate1 = re.split("\\D+",uname)
	ttext = re.sub('500|1000|1500|2000|3000|5000|10000', '', ttext)
	candidate2 = re.split("\\D+",ttext)
	
	guess = ""
	for c in candidate1:
		if len(c)>len(guess) and len(c)<6 and len(c)>2:
			guess=c
	if guess == "":
		for c in candidate2:
			if len(c)>len(guess) and len(c)<6 and len(c)>2:
				guess=c
	return guess

def add_api(num_i,idid):
    global tw_api
    try:
        if num_i == 1:
            f = open('.tw.txt', 'r')
        else:
            f = open('.tw'+str(num_i)+'.txt', 'r')
        for row in f:
            settingtxt = row.strip()
        f.close()
        codes = re.split('#', settingtxt)
        CK = convert_from_hash(codes[0])
        CS = convert_from_hash(codes[1])
        AT = convert_from_hash(codes[2])
        AS = convert_from_hash(codes[3])
        au = convert_from_hash(codes[4])
        auth = tweepy.OAuthHandler(CK, CS)
        auth.set_access_token(AT, AS)
        api = tweepy.API(auth)
        try:
            api.user_timeline(count=1, screen_name=idid)
            tw_api.append(api)
        except Exception as e:
            #print(':::::No.'+str(num_i)+':::::')
            en = re.sub('[^0-9]','', str(e.args))
    except:
        pass

def room_paste(sender):
	url =clipboard.get()
	if url.find('https://')==-1:
		console.hud_alert("TwitterURLをコピーしてから実行してください",'error')
		return None
	userid=url2id(url)
	
	add_api(1,userid)
	for i in range(2,6):
		tt = threading.Thread(target=add_api, args=(i,userid))
		tt.start()
		time.sleep(0.15)
	tt.join()
		
	api = OAuth1Session(CK, CS, AT, AS)
	auth = tweepy.OAuthHandler(CK, CS)
	auth.set_access_token(AT, AS)
	TweetName = tweet_get(tw_api[0], userid)
	try:
		roomid = guess_room(TweetName[1],TweetName[0])
	except:
		roomid=""
	if roomid =="":
		console.hud_alert("ルーム番号がみつかりませんでした。")
	else:
		keyboard.backspace(20)
		keyboard.insert_text(roomid)
		keyboard.insert_text('\n')
		keyboard.set_view(None)
		sys.exit()

def extract_code():
	language_preference = ['fi','en','se']
	load_framework('Vision')
	VNRecognizeTextRequest = ObjCClass('VNRecognizeTextRequest')
	VNImageRequestHandler = ObjCClass('VNImageRequestHandler')
	pil_image = clipboard.get_image()
	text = ""

	if pil_image is not None:
	    buffer = io.BytesIO()
	    pil_image.save(buffer, format='PNG')
	    image_data = buffer.getvalue()
	
	    req = VNRecognizeTextRequest.alloc().init().autorelease()
	    req.setRecognitionLanguages_(language_preference)
	    handler = VNImageRequestHandler.alloc().initWithData_options_(image_data, None).autorelease()
	
	    success = handler.performRequests_error_([req], None)
	    if success:
	        for result in req.results():
	            text += str(result.text()) + "\n"
	    else:
	        print('Problem recognizing anything')
	
	text = re.sub(" ","",text)
	dtext = text.split("\n")
	code=""
	
	for d in dtext:
		try:
			if d[0]=="X" and len(d)==16:
				code=d
		except:
			abco=1
		if d.count("AQ") > 0:
			code=d
		
	if not code=="":
		print(code)
		keyboard.insert_text(code)
	else:
		console.hud_alert("認識できませんでした。","error",0.3)

def run_search():
	v['imageview1'].image=ui.Image('./src/logo.png')
	now = datetime.datetime.now()
	strnow = now.strftime('%H:%M:%S')
	v['nowtime'].text = strnow
	
	uitime = v['datepicker'].date
	minutes = uitime.strftime('%M')
	iminutes= int(minutes)
	if 0 < iminutes < 30:
		v['datepicker'].date=v['datepicker'].date + datetime.timedelta(minutes=30-iminutes)
	elif 30 < iminutes < 60:
		v['datepicker'].date=v['datepicker'].date + datetime.timedelta(minutes=60-iminutes)
	
	if keyboard.is_keyboard()==True:
		keyboard.set_view(v)
	else:
		v.present('sheet')
		

strp = platform.platform()
if strp.count("iPhone") > 0:
	v = ui.load_view('./src/searchg_iphone.pyui')
else:
	v = ui.load_view('./src/searchg.pyui')
