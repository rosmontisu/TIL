- Socket == File
- Server == Process

- 서버에서 소켓에 접근한다 : RWX
- 읽는다?
	- Receive
- 쓴다?
	- Send
- 즉, 서버가 소켓에다가 I/O를 한다


- 2차 메모리 안에 파일이 있다.
	- HDD < A.bmp 
	- 위와 같은 데이터 구조일때 접근한다는건...

- Kernel mode
	- File System
	<->
	- Driver
- HDD

- Hdd 데이터의 용량이 매우크다.
	- 1.4MB
- 그렇다면 Memory는? 
	- 1.4MB는 작다
	- 64KB로 가정
