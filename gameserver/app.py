from flask import Flask, jsonify,request #flask 모듈에서 Flask class,jsonify(),request()함수 가져온다
from sqlalchemy import create_engine,text #create_engine 사용하여 db에 연결, text 사용하여 sql 실행
from config import db_url #config.py 파일에서 db_url가져온다 
import json

def create_app(): #flask run 했을 경우 자동 실행 
  app=Flask(__name__) 
  #Flask class 객체화 -> 이  app 변수가 Flask 웹 API애플리케이션이다 
  #app 변수에 API설정과 엔드포인트들을 추가하면 APi 완성
  
  database=create_engine(db_url,encoding='utf-8',max_overflow=0)
  app.database=database
  
  #Flask의 route 데코레이터 사용해서 엔드포인트 등록. score함수를 엔드포인트 함수로 등록 
  #고유주소=score,method=GET 
  #@라고 되어 있는 부분은 파이썬에서 *데코레이터(decorator) 라고 하고 
  #이를 사용하여 app의 객체의 route함수에 request 인자를 넘기면서 HTTP요청을 처리 합니다.
  @app.route("/score",methods=['GET'])
  def score(): #user table을 보여주는 함수 
    result=app.database.execute("SELECT * FROM scoreboard ORDER BY score DESC;") #내림차순 정렬
    row=result.fetchall() #튜플로 저장
    
    
    return jsonify(str(row)) #변환을 위해 str 사용



  return app
    



