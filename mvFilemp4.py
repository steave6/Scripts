#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os, shutil, re

class Mvfile: # {{{
  def __init__(self, frompath, topath, checkname):
    """Myfile(from, to)"""
    self.frompath = self.__RelativetoAbs(frompath)
    self.topath = self.__RelativetoAbs(topath)
    self.reg = re.compile(checkname, re.I)


# {{ プライベートメソッド
  def __RelativetoAbs(self, relative):
    """from exefile to a specific file path by relative path"""
    root_abspath = os.path.abspath(os.path.dirname(__file__))
    relpath = os.path.join(root_abspath, relative)
    normpath = os.path.normpath(relpath)
    return normpath

  def __ifNOTExistdirMake(self):
    # もし移動先ディレクトリがなければ作成
    if os.path.isdir(self.topath) == False:
      os.mkdir(self.topath)
      print "%s is created" % self.topath
# }}

  def CheckSearch(self, file, checkext):
    """ CheckSearch(file, checkext)  
    file = 検索対象の文字列
    checkext = 検索する拡張子
    """
    name, ext = os.path.splitext(file)
    if ext in checkext and self.reg.findall(file) and file != __file__: # 順に拡張子、検索文字列、実行ファイルをチェック
      return True
    else:
      return False

  def Findfile(self):
    """スクリプトファイルのある全てのファイルを検索し、その中で条件に一致するものだけジェネレータで返す
    method-CheckSearchで詳しい検索を行う"""
    for file in os.listdir(self.frompath): # このファイルのディレクトリにあるデータごとにループ
      abs_file = os.path.join(self.frompath, file)
      if self.CheckSearch(file, '.mp4') and os.path.isfile(abs_file):
        yield abs_file

  def FindfileRec(self, exclude_folder):
    """root Directoryから再帰的にファイルを検索し、条件に一致したファイルのフルパスを返す"""
    for root, dirs, files in os.walk(self.frompath):
      # Actorディレクトリを除外
      if root.find(exclude_folder) != -1:
        continue
      for file in files: # root直下にファイルがあればループ
        if self.CheckSearch(file, '.mp4'):
          yield os.path.join(root, file) # ファイルのabspath

  def Move(self):
    """指定のディレクトリにあるファイルのうち条件に一致するものを移動
    移動元、移動先、検索文字列はインスタンス生成時に引数で渡す"""
    self.__ifNOTExistdirMake()
    for file in self.Findfile():
      filename = os.path.basename(file)
      shutil.move(file,self.topath) # ファイルを移動
      print('mv sucess:"%s" to %s' % (filename, self.topath)) # 実行結果を表示 file名 移動先ディレクトリ
  
  def MoveRec(self, exclude_folder):
    """指定のルートディレクトリから再帰的にファイルを検索し、条件に一致するものを移動
    ルートディレクトリ、移動先、検索文字列はインスタンス生成時に引数で渡す"""
    self.__ifNOTExistdirMake()
    for file in self.FindfileRec(exclude_folder):
      filename = os.path.basename(file)
      shutil.move(file,self.topath) # ファイルを移動
      print('mv sucess:"%s" to %s' % (filename, self.topath)) # 実行結果を表示 file名 移動先ディレクトリ
# }}}

"""
how to use
Mvfile(frompath, topath, checkname).Move()
or 
Mvfile(frompath, topath, checkname).MoveRec(exclude_folder)
"""
