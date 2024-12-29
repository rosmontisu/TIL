#### 렌파이 script를 중심으로한 파일 구조 만져보기



- jump [label_name]으로 다른 aaa.rpy 파일 참조 가능

- 마찬가지로 ./폴더/aaa.rpy 파일 도 참조 가능

- 심각할정도로 다른 label에 쉽게 접근이 가능

- 만약 twice label 오류가 발생하면, 로그를 확인하고 겹치는 label의 이름을 수정 or 파일을 삭제 해줍시다
![[Pasted image 20240724173532.png]]
위와 같은 파일 구조일때
```py
jump good_ending 
```
으로 접근하는 good_ending label의 경로는
./endings/endings.rpy에
```py
label good_ending:
    "좋은 엔딩입니다."
return

label bad_ending:
	"좋지 않은 엔딩입니다."

return
```
위와 같은 식으로 정의해두면 접근 가능