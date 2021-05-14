from flask import Flask
from app import create_app
from config import server_port


app=create_app() #python app.py로 실행 가능하게 한다 
if __name__=='__main__': #시작점 의미 
    app.run(host='0.0.0.0',port=server_port) # 포트 변경