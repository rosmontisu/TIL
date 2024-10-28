### 0. 궁금증
[Nginx Proxy Manager 사용기 블로그 글](https://docs.street-drop.com/blog/nginx-proxy-manager/)
- 위 글을 읽던중...
	- SSL 인증서 관련 의문점
### 1. **SSL 인증서 발급 방법**

글에서 언급된 여러 방법 중 SSL 인증서를 적용하는 세 가지 방법이 소개되었는데, 이 중 Nginx Proxy Manager(NPM)를 사용하는 방법이 주목할 만한 부분입니다.

NPM은 Nginx 서버의 복잡한 설정 과정을 단순화하여 웹 기반 인터페이스를 통해 SSL 인증서를 쉽게 발급받고 설정할 수 있도록 해줍니다.

### 2. **CLI 방식과 Nginx Proxy Manager(NPM)의 차이점**

- **CLI 방식(Nginx 설정 파일을 직접 수정)**:
    
    - 이 방법은 Let's Encrypt 같은 인증 기관에서 SSL 인증서를 발급받아 Nginx 설정 파일을 수동으로 수정하는 방식입니다.
    - 장점은 서버의 요구 사항에 맞게 세부적인 설정이 가능하다는 점입니다.
    - 하지만 초보자에게는 복잡하고 시간이 걸릴 수 있습니다.
- **Nginx Proxy Manager(NPM)**:
    
    - Nginx의 프록시 및 SSL 설정을 직관적인 웹 인터페이스로 처리할 수 있는 도구입니다.
    - Let's Encrypt를 통해 무료 SSL 인증서를 자동으로 발급받을 수 있고, 이를 NPM을 통해 쉽게 적용할 수 있습니다.
    - CLI 방식에 비해 설정이 훨씬 단순하며, 유지 보수도 용이합니다.

### 3. **AWS ELB와의 비교**

AWS ELB는 SSL 인증서를 쉽게 적용할 수 있지만, 서비스가 확장될수록 요금이 증가할 수 있는 단점이 있습니다. 이 때문에 손시연 님이 비용 절감의 방법으로 ELB 대신 Nginx Proxy Manager를 선택하셨다고 언급된 것입니다.

### 결론

Nginx Proxy Manager를 사용하면 복잡한 CLI 명령어 없이도 SSL 인증서를 쉽게 발급받고 적용할 수 있으며, 직관적인 웹 인터페이스로 관리할 수 있어 편리합니다.