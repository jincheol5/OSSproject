import requests
import json
import re #문자열에서 숫자 추출을 위한 라이브러리 

url="http://192.168.55.138:5010/input"

def makeboard(r):
  #문자열에서 불필요한 요소들 제거
  r=r.replace(" ",'')
  r=r.replace(",",'')
  r=r.replace("(",'')
  r=r.replace(")",'')
  r=r.lstrip("'")
  #'로 문자열 분리 
  board=r.split("'")
  return board


#입력할 값 
datas={
  
  'name':'ojc',
  'score':100
  
}


response=requests.post(url,data=datas)
r=response.json()




board=makeboard(r)
name=[]
score=[]


for i in range(len(board)):
    if i%2==0: name.append(board[i])
    else: score.append(int(board[i]))

for i in range(len(name)):
  print("%2d 등 : %10s  -> 점수 : %d"%((i+1),name[i],score[i]))


