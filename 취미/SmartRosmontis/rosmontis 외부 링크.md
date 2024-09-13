#### 엔드포인트
gpt-3.5-turbo-instruct, babbage-002, davinci-002    
https://api.openai.com/v1/completions
gpt-4, gpt-4-turbo-preview, gpt-3.5-turbo
https://api.openai.com/v1/chat/completions
#### package.json
"type": "module",
상황에 맞게 추가하기

npm start 로 서버 실행하는데,    
ls web으로 폴더 옮기고 해야합니다

discord - bot - privileged Gateway Intents
1 2, (+3) 까지 켜줘야합니다
초대링크는 OA2 - bot - 권한 설정후 생성    
#### port 비정상 종료로 사용중일 경우?
netstat -a -o
taskkill /f /pid [pid번호]    
#### maa
엔드포인트 잘 찍어주세요
로컬기준으로는  
http://localhost:3000/url...  
#### port
bot - 80(http)
unity http - 3000
maa - 3001
web - 3005
(putty), unity ws, fz - 8080
->
sftp://45.119.146.143:8080
#### linux
nohup 으로 터미널이 끊겨도 돌아가게 가능(데몬에서 돌리기)    
& 로 백드라운드에서 돌아가게 가능    
ex) nohup node server_web.js > app.log &    

프로세스 확인  
ps -ef | grep node

프로세스 킬    
kill -9 {id}    

pop 으로 프로세스 확인 후    
pid입력으로 kill 도 가능  
pop, O COMMAND=python 등으로 특정 커맨드를 grep 가능

#### SSL
https://manage.sslforfree.com/dashboard
DA7... 으로 사용중