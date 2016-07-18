#! /usr/bin/env python3
# -*- coding: utf-8 -*-
""" [NAME] に続くScriptの簡易説明文

[DESCRIPTION] Scriptの詳細説明文
"""

__author__ = "steav <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "01 November 2011"

import os
import shutil
 
# 指定パスのファイル一覧を取得し1件ずつ出力
def movefile(to, checkext):
  """
  Description: スクリプトのある場所のファイルを検索し該当するファイルを指定のフォルダへ移動させることができます。
  このスクリプトを実行するときは、かならずスクリプトのフォルダまでcdしてから実行してください。
  そうでない場合、思わぬファイル移動が生じるおそれがあります。
  """
  frompath = os.path.abspath(os.path.dirname(__file__)) # 現在のスクリプトがあるディレクトリ
  topath = os.path.join(frompath, to) # 移動先のディレクトリ
  topath = os.path.normpath(topath) # ノーマルパスに整形
  # もし移動先ディレクトリがなければ作成
  if os.path.isdir(topath) == False:
    os.mkdir(topath)

  # スクリプトファイルのあるフォルダのファイルにつきループ
  for file in os.listdir(frompath): # このファイルのディレクトリにあるデータごとにループ
    if os.path.isfile(file) and file != __file__: # fileと実行ファイルであるかを確認
      name, ext = os.path.splitext(file)
      if ext in checkext: # 拡張子のチェック
        fromfile = os.path.join(frompath, file) # 移動元ファイルの絶対パス生成
        shutil.move(fromfile,topath) # ファイルを移動
        print('mv sucess:%s to %s' % (file, topath)) # 実行結果を表示 file名 移動先ディレクトリ

if __name__ == '__main__':
  # 使い方
  # movefile(移動先dir<相対パス>, 検索する拡張子（配列可）)
  movefile('ziprar', ['.zip', '.rar'])
  movefile('debfile', '.deb')
  movefile('msoffice', ['.docx', '.xlsx'])
  movefile('../Videos', ['.mp4', '.vlc'])

