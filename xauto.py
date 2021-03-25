import ui, keyboard, clipboard, time, re, notification, tweepy, os
from time import sleep
from datetime import date
import datetime, sound, sys
from requests_oauthlib import OAuth1Session
import json, urllib, time
from objc_util import *
import csv, console, threading
import requests

alpha_mode = 'False'
img_mode = 'False'
switch = 0
new = ['', '', '', '']
tw_api = []
error_script=""
token = ""
slug=""
my_screen_name=""
list_switch=False

dirr = re.split('/', __file__)
send_code=0
send_code *= 1


url =clipboard.get()
if url.find('https://')==-1:
	console.hud_alert("TwitterURLをコピーしてから実行してください",'error')
	sys.exit(3)


def convert_from_hash(hash_text):
	return original_text
#原文→暗号
def convert_to_hash(text):
	return hash_text

sub_idt = ['いち', 'にー|に', 'さん', 'よん', 'ごー|ご', 'ろく', 'なな', 'はち', 'きゅう', 'れい', 'ぜろ', 'イチ', '二ー|二', 'サン', 'ヨン', 'ゴ|ゴー', 'ロク', 'ナナ', 'ハチ', 'キュウ', 'ゼロ']

sub_numidt = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

idt = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '壱', '弐', '参', '伍', '陸', '①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⓪', '❶', '❷', '❸', '❹', '❺', '❻', '❼', '❽', '❾', '⑴', '⑵', '⑶', '⑷', '⑸', '⑹', '⑺', '⑻', '⑼', '\uf8b7', '\uf8b8', '\uf8b9', '\uf8ba', '\uf8bb', '\uf8bc', '\uf8bd', '\uf8be', '\uf8bf', '\uf8c0', '1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '0⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '0️⃣', '零', '➀', '➁', '➂', '➃', '➄', '➅', '➆', '➇', '➈', ' ⓵', '⓶', '⓷', '⓸', '⓹', '⓺', '⓻', '⓼', '⓽', '𝟏', '𝟐', '𝟑', '𝟒', '𝟓', '𝟔', '𝟕', '𝟖', '𝟗', '0', '𝟬', '𝟭', '𝟮', '𝟯', '𝟰', '𝟱', '𝟲', '𝟳', '𝟴', '𝟵', '𝟢', '𝟣', '𝟤', '𝟥', '𝟦', '𝟧', '𝟨', '𝟩', '𝟪', '𝟫', '𝟶', '𝟷', '𝟸', '𝟹', '𝟺', '𝟻', '𝟼', '𝟽', '𝟾', '𝟿', '𝟘', '𝟙', '𝟚', '𝟛', '𝟜', '𝟝', '𝟞', '𝟟', '𝟠', '𝟡']

numidt = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '2', '3', '5', '6', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
passch = [
 'pass', 'Pass', 'PASS', 'パス', 'ぱす', 'ﾊﾟｽ', '🔑', '🗝', '🔓', '🔐', '🔒', 'ぱ', 'パ', 'ﾊﾟ', 'ps', 'Ps' , 'PS', 'pw', 'PW', 'Pw', '鍵', '𝗣', '𝐏', '𝑃', '𝖯', '𝗣', '𝘗', '𝙋', '𝙿']
roomidt = [
 '🏠', '🏡', '🏘', '🚪', 'room', '番号', 'ル', 'ム', 'る']
vectoridt = ['→', '▶︎', '▶', '⇨', '➡️', '👉', '▷', '⏩', '⇒', '☞', '🔜', '⌇', '｜', '￤', '┆']

show_url = 'https://api.twitter.com/1.1/statuses/show.json'
labs_url = 'https://api.twitter.com/labs/2/tweets'
lim_url = 'https://api.twitter.com/1.1/application/rate_limit_status.json?resources=statuses'

def converter(num):
    big_ch = [
     '０', '１', '２', '３', '４', '５', '６', '７', '８', '９']
    small_ch = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    numpass = ''
    for i in range(len(num)):
        match_flag = 0
        for j in range(10):
            if num[i] == big_ch[j]:
                match_flag = 1
                numpass = numpass + small_ch[j]

        if match_flag == 0:
            numpass = numpass + num[i]

    return numpass


def url2id(url):
    userids = re.split('/|\\?', url)
    if len(userids) > 3:
        userid = userids[3]
    else:
        print('読み込めないURLです。')
        sys.exit(3)
    return userid

def add_img(iurl, itext):
    image_data = urllib.request.urlopen(iurl).read()
    language_preference = ['en']
    load_framework('Vision')
    VNRecognizeTextRequest = ObjCClass('VNRecognizeTextRequest')
    VNImageRequestHandler = ObjCClass('VNImageRequestHandler')
    req = VNRecognizeTextRequest.alloc().init().autorelease()
    req.setRecognitionLanguages_(language_preference)
    handler = VNImageRequestHandler.alloc().initWithData_options_(image_data, None).autorelease()
    image_data = ''
    handler.performRequests_error_([req], None)
    for result in req.results():
        img_num = re.sub('\\D', '', str(result.text()))
        itext += '\n' + img_num
    return itext

def tweets2element(atweets):
    global error_script
    for atweet in atweets:
        atweet_id = atweet.id
        atweet_text = atweet.text
        atweet_name = atweet.author.name
        try:
            aimg_url = atweet.extended_entities['media'][0]['media_url']
        except:
            aimg_url = ''

    try:
        return (
         atweet_id, atweet_text, atweet_name, aimg_url)
    except Exception as e:
        error_script += str(e)
        return ('', 'err', '', '')

def list_tweets2element(ltweets):
    global error_script
    for ltweet in ltweets:
        ltweet_id = ltweet.id
        ltweet_text = "listtt"+ltweet.text
        ltweet_name = ltweet.author.name
        try:
            limg_url = ltweet.extended_entities['media'][0]['media_url']
        except:
            limg_url = ''

    try:
        return (
         ltweet_id, ltweet_text, ltweet_name, limg_url)
    except Exception as e:
        error_script += str(e)
        return ('', 'err', '', '')

def tweet_get(twpy_api, userid, first=False):
    global switch
    try:
        gtweets = twpy_api.user_timeline(count=1, screen_name=userid)
        return tweets2element(gtweets)
    except Exception as e:
        if switch == 0:
            en = re.sub('[^0-9]','', str(e.args))
            if en == '88':
                console.hud_alert('【取得制限エラー】','error')
                if first:
                    console.show_image('./src/limit_error.png')
        	
        switch = 2
        sys.exit(3)
        return False

def init_list_member(api,target_screen):
    global slug, my_screen_name
    global list_switch
    global old_list_tweet
    try:
        lists = api.lists_all(api.me().screen_name)
        for i in range(len(lists)):
            if lists[i].name == "guerrilla_list":
                slug = lists[i].slug
                my_screen_name = lists[i].user.screen_name
        if slug =="":
            list_switch = False
        else:
            list_members = api.list_members(owner_screen_name = my_screen_name, slug = slug)
            for member in list_members:
            	api.remove_list_member(owner_screen_name = my_screen_name, slug = slug, screen_name = member.screen_name)
            api.update_list(owner_screen_name = my_screen_name, slug = slug, mode="private")
            api.add_list_member(owner_screen_name = my_screen_name, slug = slug, screen_name = target_screen)
            api.update_list(owner_screen_name = my_screen_name, slug = slug, mode="public")
            old_list_tweet = list_tweet_get(api)[1]
            if len(api.list_members(owner_screen_name = my_screen_name, slug = slug)) > 0:
                list_switch = True
                print("***プラスモード起動***")
            else:
                list_switch = False
    except:
        list_switch = False

def list_tweet_get(twpy_api):
    global switch
    try:
        gtweets = twpy_api.list_timeline(owner_screen_name = my_screen_name, slug = slug, count = 1)
        return list_tweets2element(gtweets)
    except Exception as e:
        if switch == 0:
            en = re.sub('[^0-9]','', str(e.args))
            if en == '88':
                console.hud_alert('【取得制限エラー】','error')
        	
        switch = 2
        sys.exit(3)
        return False

def t_tweet_get(ttw_api, userid, lisg=False):
    global new
    if not lisg:
        newcan = tweet_get(ttw_api, userid)
    else:
        newcan = list_tweet_get(ttw_api)
    if not newcan[1] == 'err':
        new=newcan

def remove_room_vector(text):
    for room in roomidt:
        for vector in vectoridt:
            text = re.sub(room + vector + "[0-9０-９]+", '', text)
            text = re.sub(room + "[0-9０-９]+", '', text)

    return text


#if len(re.findall('[0-9]桁|[０-９]桁|[0-9]けた|[０-９]けた|[一-九]桁', twtext)) == 0:
def check_passtweet(twtext):
    if not twtext == "err":
        if not twtext[0:6] == "listtt":
            if oldtweet_text[:60] != twtext[:60]:
                return True
            return False
        else:
            if old_list_tweet[:60] != twtext[:60]:
                return True
            return False
    else:
        return False


def pass_auto(tweet_id, tweettext, img_url):
    global switch
    global error_script
    password = ''
    flag = False
    original=tweettext
    if img_mode == 'True':
        if img_url != '':
            tweettext = add_img(img_url, tweettext)
    tweettext = re.sub("listtt","",tweettext)
    if len(tweettext)<11:
        simn = re.findall('[0-9０-９]+',tweettext)
        if len(simn) == 2:
            if len(simn[0])+len(simn[1])>5:
                return simn[1]
    tweettext = re.sub(' |\u3000', '', tweettext)
    tweettext = '\n' + tweettext
#sqmmode off
    for i in range(len(idt)):
        tweettext = re.sub(idt[i], numidt[i], tweettext)
    tweettext = re.sub('https?://[\\w/:%#\\$&\\?\\(\\)~\\.=\\+\\-]+', '', tweettext)
    tweettext = re.sub('[0-9０-９]?[0-9０-９]:[0-9０-９][0-9０-９]?|[0-9０-９]?[0-9０-９]/[0-9０-９][0-9０-９]?|[0-9０-９]?[0-9０-９]時|[0-9０-９]?[0-9０-９]分|[0-9０-９]?[0-9０-９]日|[0-9０-９]?[0-9０-９]月|[0-9０-９]?[0-9０-９]回', '', tweettext)
    tweettext = re.sub('[0-9０-９]?[0-9０-９]組|[0-9０-９]?[0-9０-９]チーム|[0-9０-９]?[0-9０-９]キル|[0-9０-９]?[0-9０-９]位|[0-9０-９]?[0-9０-９]番|[0-9０-９]?[0-9０-９]枠|[0-9０-９]?[0-9０-９]人|[0-9０-９]?[0-9０-９]名', '', tweettext)
    tweettext = re.sub('GO|go|Go|START|start|Start|DM|dm|id|ID|Id|Just|JUST|just', '', tweettext)
    tweettext = re.sub('[0-9０-９]+円|@[0-9０-９a-zA-Z_]+', '', tweettext)
    tweettext = re.sub('500 ?× ?[0-9]|1000 ?× ?[0-9]|1500 ?× ?[0-9]|2000 ?× ?[0-9]|3000 ?× ?[0-9]|5000 ?× ?[0-9]|10000 ?× ?[0-9]|500 ?✖️ ?[0-9]|1000 ? ✖️ ?[0-9]|1500 ?✖️ ?[0-9]|2000 ?✖️ ?[0-9]|3000 ?✖️ ?[0-9]|5000 ?✖️ ?[0-9]|10000 ?✖️ ?[0-9]|[0-9]+×人数|[0-9]+✖️人数', '', tweettext)
    #数字探索
    match = re.findall('[0-9０-９]+', tweettext)
    if alpha_mode == 'True':
        tweettext = re.sub('GO|go|Go|START|start|Start|DM|dm|id|ID|Id|Just|JUST|just', '', tweettext)
        match = re.findall('[0-9０-９a-zA-Z]+', tweettext)
    tweettext = remove_room_vector(tweettext)
    bnnum = len(re.findall('\\W', tweettext))
    fddst = []
    for i in range(len(passch)):
        twfd = tweettext.find(passch[i])
        if twfd != -1:
            fddst = re.findall('[0-9０-９]+', tweettext[twfd:])
            if alpha_mode == 'True':
                fddst = re.findall('[0-9０-９a-zA-Z]+', tweettext[twfd + len(passch[i]):])
            if len(fddst) != 0:
                password = converter(fddst[0])
                return password
    if len(match) == 0:
        for i in range(len(sub_idt)):
            tweettext = re.sub(sub_idt[i], sub_numidt[i], tweettext)
        match = re.findall('[0-9０-９]+', tweettext)
    if len(match) == 1:
        password = converter(match[0])
        return password
    else:
        if len(match) >= 2:
            password = converter(match[1])
            return password
        console.hud_alert('取得失敗','error')
        sound.play_effect('digital:ZapThreeToneDown', 0.1)
        #console.show_image('./src/extract_error.png')
        try:
            mememe=tw_api[0].me()
            nowt = str(datetime.datetime.now())
            error_script =  "atweet_id x"+str(error_script.count('atweet_id'))+"   ltweet_id x"+str(error_script.count('ltweet_id'))+error_script
            error_script = re.sub("local variable 'atweet_id' referenced before assignment","",error_script)
            error_script = re.sub("local variable 'ltweet_id' referenced before assignment","",error_script)

            stext = nowt[:nowt.find(".")]+'\nリストスイッチ:'+str(list_switch)+"\nエラー文\n"+error_script+"\nuser:@"+mememe.screen_name+"\ntweet:"+oldtweet_name+"\n"+oldtweet_text+"\n処理前テキスト\n"+original+"\n処理後テキスト"+tweettext
            stext = urllib.parse.quote(stext)
            requests.get()
        except:
            pass
        switch = 5
        sys.exit(3)
        return False

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
            if num_i == 5:
                initt = threading.Thread(target=init_list_member, args=(api,idid))
                initt.start()
        except Exception as e:
            print(':::::No.'+str(num_i)+':::::')
            en = re.sub('[^0-9]','', str(e.args))
            if en == '88':
                print("取得制限(15分後に解除)")
            else:
                print(e)
    except:
        pass

def run_pass_auto():
    global oldimg_url
    global oldtweet_id
    global oldtweet_name
    global oldtweet_text
    global exrep
    global switch
    global new
    global error_script
    
    global alpha_mode,img_mode,speed
    try:
        with open('./.option.csv', 'r', encoding='utf8') as (f):
            reader = csv.reader(f)
            for i in reader:
                alpha_mode = i[0]
                img_mode = i[1]
                sleep_time = 0.21-float(i[2])*0.2
        print("***設定読み込み完了***")
        print("****オート起動****")

    except:
        console.alert('Pythonistaで先に設定して下さい。')
        sys.exit(3)
    
    try:
        f = open('.tw.txt', 'r')
        for row in f:
            settingtxt = row.strip()
        f.close()
        codes = re.split('#', settingtxt)
        au = convert_from_hash(codes[4])
    except:
        print('Twitter連携が無効です\n')
        sys.exit()
    if not au==str(send_code*33):
        print('購入者コードが無効です\n')
        sys.exit()
    
    userid = url2id(url)
    
    add_api(1,userid)
    for i in range(2,6):
        tt = threading.Thread(target=add_api, args=(i,userid))
        tt.start()
        time.sleep(0.15)
    tt.join()
    #print("****連携済み"+str(len(tw_api))+"個****")
    
    start_time = time.time()
    stpcount = 0
    
    if len(tw_api) == 0:
        print("連携不足エラー")
        sys.exit()

    old = tweet_get(tw_api[0], userid, True)
    while old[1] == 'err':
        old = tweet_get(tw_api[0], userid, True)
        stpcount += 1
        if stpcount == 5:
            print("ツイート取得できませんでした。")
            sys.exit()
    oldtweet_id = old[0]
    oldtweet_text = old[1]
    oldtweet_name = old[2]
    oldimg_url = old[3]
    print(oldtweet_name + 'のパスツイ待機中•••')
    new = tweet_get(tw_api[0], userid)
    mtweet_id = new[0]
    mtweet_text = new[1]
    mtweet_name = new[2]
    mimg_url = new[3]
    elapsed_time = 0
    api_switch = 0
    loop_count = 0
    list_get = False
    while switch == 0:
        api_switch = api_switch%len(tw_api)
        if list_switch:
            list_get = not list_get
        t = threading.Thread(target=t_tweet_get, args=(tw_api[api_switch], userid, list_get))
        t.start()
        mtweet_id = new[0]
        mtweet_text = new[1]
        mtweet_name = new[2]
        mimg_url = new[3]
        if not keyboard.is_keyboard():
            print(mtweet_text)
        flag = check_passtweet(mtweet_text)
        if flag:
            ps = pass_auto(mtweet_id, mtweet_text, mimg_url)
            if keyboard.is_keyboard():
                keyboard.backspace(10)
                keyboard.insert_text(ps)
                keyboard.insert_text('\n')
            print('****取得成功****\n' + ps)
            sound.play_effect('arcade:Coin_2', 0.10)
            switch = 1
            try:
                mememe=tw_api[0].me()
                nowt = str(datetime.datetime.now())
                error_script =  "atweet_id x"+str(error_script.count('atweet_id'))+"   ltweet_id x"+str(error_script.count('ltweet_id'))+error_script
                error_script = re.sub("local variable 'atweet_id' referenced before assignment","",error_script)
                error_script = re.sub("local variable 'ltweet_id' referenced before assignment","",error_script)
                stext = nowt[:nowt.find(".")]+'\nリストスイッチ:'+str(list_switch)+"\nエラー文\n"+error_script+"\nuser:@"+mememe.screen_name+"\nsleeptime:"+str(sleep_time)+"\ntweet:"+oldtweet_name+"\n"+oldtweet_text+"\n処理前テキスト\n"+mtweet_text+"\n処理後テキスト\n"+ps
                stext = urllib.parse.quote(stext)
                requests.get()
            except Exception as e:
                #print(e)
                pass
        api_switch+=1
        time.sleep(sleep_time)

run_pass_auto()
