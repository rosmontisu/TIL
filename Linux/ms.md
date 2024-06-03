#### swap
- free -h
	- 사용중인 메모리, 스왑 메모리 표기
- swapon --show
#### grub
- grub2의 설정 파일 위치
	- /boot/grub2/grub.cfg :: 읽기 전용(실제 파일 위치)
	- /etc/grub2.cfg :: 링크 파일
	- /etc/default/grub :: 수정 가능 파일
	- /etc/grub.d :: 수정 가능 파일
- 아래 설정들을 수정 후 grub2-mkconfig 로 저장
- ![[Pasted image 20240527170625.png]]
#### df
- disk free 의 약자
- 디스크의 상태를 확인한다.
- df -h (G/M/K byte)단위로 디스크 상태 확인
- ![[Pasted image 20240531194602.png]]
- df -i (I-node 의 수를 확인)
- ![[Pasted image 20240531194644.png]]

#### A
- 