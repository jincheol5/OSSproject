from flask import Flask, jsonify,request #flask 모듈에서 Flask class,jsonify(),request()함수 가져온다
from sqlalchemy import create_engine,text #create_engine 사용하여 db에 연결, text 사용하여 sql 실행
from config import db_url,server_port #config.py 파일에서 db_url,server_port가져온다 

def create_app(): #flask run 했을 경우 자동 실행 
  app=Flask(__name__) 
  #Flask class 객체화 -> 이  app 변수가 Flask 웹 API애플리케이션이다 
  #app 변수에 API설정과 엔드포인트들을 추가하면 APi 완성
  
  database=create_engine(db_url,encoding='utf-8',max_overflow=0)
  app.database=database
  
  
  @app.route("/score",methods=['GET'])
  #Flask의 route 데코레이터 사용해서 엔드포인트 등록. score함수를 엔드포인트 함수로 등록 
  #고유주소=score,method=GET 
  def score(): #user table을 보여주는 함수 
    result=app.database.execute(text("""SELECT * FROM scoreboard;"""))
    row=result.fetchone()
    
    return jsonify(row._mapping['id'])

  
  return app

app=create_app() #python app.py로 실행 가능하게 한다 

if __name__=='__main__':
    app.run(host='0.0.0.0',port=server_port) # 포트 변경