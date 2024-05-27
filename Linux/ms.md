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