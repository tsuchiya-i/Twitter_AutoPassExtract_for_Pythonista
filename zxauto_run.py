"""





######パス打ちオート起動用ファイル#######

①iPad(もしくはiPhone)の設定アプリを開いて
一般 
> キーボード 
> キーボード 
> 新しいキーボードを追加 
> Pythonista 
> PyKeys-Pythonista 
> フルアクセスの許可

②右上の▷ボタンを押して解説動画を
見ながら進めてください。

③設定完了後は右上の🔧マークを押して
Shortcuts > Pythonista Keyboard > +
> Add

#####################################

















































"""
#============================
#以下書き換えると動作しなくなります。
#============================
import sys
import master

try:
	ok = sys.argv[1]
	ov = sys.argv[2]
	try:
		sub = sys.argv[3]
	except:
		sub = "1"
	master.run(ok,ov,sub)
except:
	master.run()
