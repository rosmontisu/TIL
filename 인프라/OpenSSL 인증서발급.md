```bash
genras -des3 -out private.pem 2048
```
- private.pem 이라는 이름의 pem 생성
	- -des3 가 적용되면 비밀번호(Key passphrase)필요
```bash
genras -out private.pem 2048
```
- 웹에서 사용할 인증서는 passphrase가 없어도 된다.