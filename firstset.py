# coding=utf8
import ui, keyboard, clipboard, time, re, os,random,console
import datetime, sys,shutil
import requests_oauthlib
import tweepy
from requests_oauthlib import OAuth1Session
from urllib.parse import parse_qsl
import json,urllib,time
import webbrowser as wb
import notification

dirr = re.split('/', __file__)
send_code=0
send_code *= 1

#暗号→原文
def convert_from_hash(hash_text):
	return original_text
#原文→暗号
def convert_to_hash(text):
	return hash_text
#(原文→暗号)×3
def triple_to_hash(ck):
	return hhhck
#(暗号→原文)×3
def triple_from_hash(hhhck):
	return ck
#LINE送信コードコピーボタンで実行
def copy_code(sender):
	check_label = sender.superview['send_code']
	clipboard.set(check_label.text)
	PRINT_label = sender.superview['PRINT']
	PRINT_label.text="コピーしました。\n販売元にコードを送信し、\n購入者コードをお待ちください。"
def paste(sender):
	au_label = sender.superview['auth']
	au_label.text = clipboard.get()

#Twitter連携ボタンで実行
def link_twitter(sender):
	authc = sender.superview['auth'].text
	if convert_from_hash(authc) == str(send_code*33):
		sender.superview['PRINT'].text="購入者コード確認済"
	else:
		sender.superview['PRINT'].text="購入者コードが異なります"
		sys.exit(1)
	oauth_callback = ""
	request_token_url= "https://api.twitter.com/oauth/request_token"
	#暗号化ckとcsをスクレイピング
	f = urllib.request.urlopen('')
	for row in f:
		urltxt = row.strip()
	f.close()
	urltxt = urltxt.decode()
	#スクレイピした暗号を解読

	#Twitter連携用URL生成
	twitter = OAuth1Session(consumer_key, consumer_secret)
	response = twitter.post(request_token_url,params={'oauth_callback': oauth_callback})
	request_token = dict(parse_qsl(response.content.decode("utf-8")))
	#連携画面のURLを生成しブラウザで開く
	authenticate_url = "https://api.twitter.com/oauth/authenticate"
	authenticate_endpoint = '%s?oauth_token=%s' \
	% (authenticate_url, request_token['oauth_token'])
	v.close()
	wb.open_new(authenticate_endpoint)
	

#連携後ページから遷移してきた時に実行
def link(oauth_token,oauth_verifier,sub="1"):
	if sub == "1":
		f = urllib.request.urlopen('')
	else:
		f = urllib.request.urlopen('')
	for row in f:
		urltxt = row.strip()
	f.close()
	urltxt = urltxt.decode()
	urlckcs = re.split("",urltxt)
	consumer_key = triple_from_hash(urlckcs[0])
	consumer_secret = triple_from_hash(urlckcs[1])
	oauth_token = convert_from_hash(oauth_token)
	oauth_verifier = convert_from_hash(oauth_verifier)
	twitter = OAuth1Session(
		consumer_key,
		consumer_secret,
		oauth_token,
		oauth_verifier,
		)
	access_token_url = "https://api.twitter.com/oauth/access_token"
	response = twitter.post(access_token_url,params={'oauth_verifier': oauth_verifier})
	access_token = dict(parse_qsl(response.content.decode("utf-8")))
	
	CK = consumer_key
	CS = consumer_secret
	
	try:
		AT = access_token['oauth_token']
		AS = access_token['oauth_token_secret']
	except Exception as e:
		import traceback
		traceback.print_exc()
		print("__EX__")
		sys.exit()
	
	#暗号化して隠しファイルに保存
	CK = convert_to_hash(CK)
	CS = convert_to_hash(CS)
	AT = convert_to_hash(AT)
	AS = convert_to_hash(AS)
	au = convert_to_hash(str(send_code*33))
	
	if sub == "1" or sub == "10":
		f = open('.tw.txt','w')
	else:
		f = open('.tw'+sub+'.txt','w')
	f.write(CK+"#"+CS+"#"+AT +"#"+AS+"#"+au)
	f.close()

def run_ui(err_m=""):
	stre=str(err_m)
	if stre.count('Rate limit exceeded')>0:
		console.hud_alert('【制限エラー】15分後にお試しください')
		console.show_image('./src/limit_error.png')
		sys.exit()
	v.present('sheet')
	if stre.count('.tw.txt')>0:
		v['PRINT'].text="まだ設定されていません。"
	
	v['send_code'].text=str(send_code)

v = ui.load_view('./src/firstset.pyui')
