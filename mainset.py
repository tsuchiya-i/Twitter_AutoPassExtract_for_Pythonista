import ui, sys, csv, console, os
from urllib.parse import parse_qsl
import json,urllib,time,re
import webbrowser as wb
from requests_oauthlib import OAuth1Session
import tweepy,notification,shutil
import zipfile, threading

dispv = "version:4.7"
api_n = 1

pos = __file__.find('Pythonista3/Documents')
libdir = __file__[:pos]+"Pythonista3/Documents/site-packages-3/"

def convert_from_hash(hash_text):
	return original_text
def convert_to_hash(text):
	return hash_text
def triple_to_hash(ck):
	return hhhck
def triple_from_hash(hhhck):
	return ck

def on_setting_complete(sender):
    alpha_switch_value = str(sender.superview['alpha_switch'].value)
    img_switch_value = str(sender.superview['img_switch'].value)
    speed = str(sender.superview['speed'].value)
    #print(pqm_lv)
    if sender.superview['speed'].value > 0.94:
        v['continuous_time'].text_color='#7a7a00'
        v['print'].text_color='yellow'
        sender.superview['print'].text = "⚠️注意⚠️\n取得速度が早すぎる可能性があります。不具合が起きたり、処理が追いつかず逆に遅くなる恐れがございます"
    else:
        v['continuous_time'].text_color='black'
        v['print'].text_color='white'
        sender.superview['print'].text = ""
    sender.superview['continuous_time'].text=str(round((((0.205-sender.superview['speed'].value*0.2)+0.01)*900)*api_n,1))
    
    with open('./.option.csv', 'w', encoding='utf8') as (f):
        writer = csv.writer(f)
        writer.writerow([alpha_switch_value, img_switch_value, speed])
    #v.close()
    #sys.exit(3)
    


def speed_controller(sender):
    on_setting_complete(sender)
def on_img_switch(sender):
    on_setting_complete(sender)
def on_poll_switch(sender):
    on_setting_complete(sender)
def on_alpha_switch(sender):
    on_setting_complete(sender)
def update(sender):
    on_setting_complete(sender)
    import urllib.request
    
    
    url1 = ''
    savename1 = ''
    url16 = ''
    savename16 = ''
    try:
        urllib.request.urlretrieve(url1, savename1)
        urllib.request.urlretrieve(url16, savename16)
        if os.path.isfile('./lib/tweepy.zip') and tweepy.__version__ != '3.10.0':
            with zipfile.ZipFile("./lib/tweepy.zip") as zf:
                zf.extractall(libdir)
        v['print'].text_color='white'
        sender.superview['print'].text = "最新バージョンに\nアップデートしました。\nタスクを切ってPythonistaを開き直してください。"
    except:
        sender.superview['print'].text = "既に最新バージョンです。"

def next_link(oauth_callback, f):
	request_token_url= "https://api.twitter.com/oauth/request_token"
	for row in f:
		urltxt = row.strip()
	f.close()
	urltxt = urltxt.decode()
	#スクレイピした暗号を解読
	urlckcs = re.split("",urltxt)
	consumer_key = triple_from_hash(urlckcs[0])
	consumer_secret = triple_from_hash(urlckcs[1])
	twitter = OAuth1Session(consumer_key, consumer_secret)
	response = twitter.post(request_token_url,params={'oauth_callback': oauth_callback})
	request_token = dict(parse_qsl(response.content.decode("utf-8")))
	#連携画面のURLを生成しブラウザで開く
	authenticate_url = "https://api.twitter.com/oauth/authenticate"
	authenticate_endpoint = '%s?oauth_token=%s' \
	% (authenticate_url, request_token['oauth_token'])
	v.close()
	wb.open_new(authenticate_endpoint)

def link_twitter2(sender):
	from urllib.parse import parse_qsl
	import urllib
	oauth_callback = "l"
	f = urllib.request.urlopen('')
	next_link(oauth_callback,f)
def link_twitter3(sender):
	oauth_callback = ""
	f = urllib.request.urlopen('')
	next_link(oauth_callback,f)
def link_twitter4(sender):
	oauth_callback = ""
	f = urllib.request.urlopen('')
	next_link(oauth_callback,f)
def link_twitter5(sender):
	oauth_callback = ""
	f = urllib.request.urlopen('')
	next_link(oauth_callback,f)
def link_twitter1(sender):
	oauth_callback = ""
	f = urllib.request.urlopen('')
	next_link(oauth_callback,f)
def list_check(api):
	try:
		lists = api.lists_all(api.me().screen_name)
		slug = ""
		for i in range(len(lists)):
			if lists[i].name == "guerrilla_list":
				slug = lists[i].slug
				screen_name = lists[i].user.screen_name
		if slug =="":
			new_list = api.create_list(name = "guerrilla_list", mode ="public")
			slug = new_list.slug
			screen_name = new_list.user.screen_name
		return slug, screen_name
	except Exception as e:
		print(e.args)
		print("check")
def cleanset_list(api):
	global v
	clist = list_check(api)
	try:
		list_members = api.list_members(owner_screen_name = clist[1], slug = clist[0])
		members = ""
		for member in list_members:
			api.remove_list_member(owner_screen_name = clist[1], slug = clist[0], screen_name = member.screen_name)
		v['version'].text += "+"
	except Exception as e:
		print(e.args)

tw_api = []
def add_api(num_i):
    global tw_api, v, api_n
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
            me_info = api.me()
            tw_api.append(api)
            v['link'+str(num_i)].text="🟢@"+me_info.screen_name
            api_n += 1
            if num_i == 5:
                cleanset_list(api)
                
        except Exception as e:
            v['link'+str(num_i)].text="連携切れ"
    except:
        v['link'+str(num_i)].text="未連携"

def main():
    global v
    global api_n
    try:
        v = ui.load_view("./src/new_mainset2.pyui")
    except:
        try:
            v = ui.load_view("./src/new_mainset.pyui")
        except:
            v = ui.load_view("./src/mainset.pyui")
    
    
    try:
        with open('./.option.csv', 'r', encoding='utf8') as (f):
            reader = csv.reader(f)
            for i in reader:
                if i[0] == 'True':
                    v['alpha_switch'].value=True
                if i[1] == 'True':
                    v['img_switch'].value=True
                v['speed'].value = float(i[2])

    except Exception as e:
        v['speed'].value = 0.5
        with open('./.option.csv', 'w', encoding='utf8') as (f):
	        writer = csv.writer(f)
	        writer.writerow(['False', 'False', '0.5'])
    
    v['continuous_time'].text = str( round((((0.205-0.2*v['speed'].value)+0.01)*900)*api_n,1))
    v['version'].text = dispv
    v['print'].text = ""
    v.present('sheet')
    for i in range(1,6):
        t = threading.Thread(target=add_api, args=(i,))
        t.start()
        time.sleep(0.1)
    t.join()

if __name__ == '__main__':
    main()

