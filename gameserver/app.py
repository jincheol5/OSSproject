from flask import Flask, jsonify,request #flask 모듈에서 Flask class,jsonify(),request()함수 가져온다
from sqlalchemy import create_engine,text #create_engine 사용하여 db에 연결, text 사용하여 sql 실행
from config import db_url #config.py 파일에서 db_url가져온다 
import json

def create_app():  
  app=Flask(__name__) 

  
  database=create_engine(db_url,encoding='utf-8',max_overflow=0)
  app.database=database
  
  
  @app.route("/score",methods=['GET'])
  def score():  
    result=app.database.execute("SELECT * FROM scoreboard ORDER BY score DESC;") 
    row=result.fetchall() 
    
    
    return jsonify(str(row)) #변환을 위해 str 사용

  @app.route("/input",methods=['POST'])
  def input():
    app.database.execute("insert into scoreboard value('jc',100);")

    return score()

  @app.route("/delete",methods=['POST'])
  def delete():
    app.database.execute("delete from scoreboard where id='jc';")

    return score()

  return app
    



