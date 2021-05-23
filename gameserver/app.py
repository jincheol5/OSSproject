from flask import Flask, jsonify,request #flask 모듈에서 Flask class,jsonify(),request()함수 가져온다
from sqlalchemy import create_engine,text #create_engine 사용하여 db에 연결, text 사용하여 sql 실행
from config import db_url #config.py 파일에서 db_url가져온다 
import json

#집 데탑 기준 
def create_app():  
  app=Flask(__name__) 

  
  database=create_engine(db_url,encoding='utf-8',max_overflow=0)
  app.database=database
  
  #점수들을 내림차순으로 보여주는 함수 
  def showscore():
    sql="SELECT name,score FROM board ORDER BY score DESC limit 10;"
    result=app.database.execute(sql)
    row=result.fetchall()
    row=str(row).strip('[]') 
    return jsonify(row) 

  


  #값을 받아서 db에 추가 후 table을 보여주는 기능 
  @app.route("/input",methods=['POST'])
  def input():
    #post 는 form 형태로 data 받는다 
    re_name=request.form['name']
    re_score=request.form['score']
    sql="insert into board value(NULL,'%s',%d);"%(re_name,int(re_score))
    app.database.execute(sql)
    
    
    return showscore()

  
  
    
    
    

  return app
    



