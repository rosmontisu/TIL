- SmartRosmontis에 deploy-commands.js 코드를 보면 다음과 같은 방식으로 '/' command를 정의하고 있다.
```json
...
},

 {
   name: "이미지생성",
   type: 1,
   description: "특정 모델을 사용하여 이미지를 생성합니다.",
   options: [
     {
       name: 'prompt',
       description: '이미지 생성 프롬프트 입력',
       type: 3, // STRING type
       required: true
     }
   ]
 },
 
 {...
```
- 이때, type 변수의 값은 discord api docs에 나와있는데.. 아래와 같다.
- **1 SUB_COMMAND**
    - 하위 명령어를 나타냅니다. 이 옵션은 명령어에 대해 하위 명령어를 정의할 때 사용됩니다.
    - 예: `/image create`에서 `create`가 SUB_COMMAND가 됩니다.
- **2 SUB_COMMAND_GROUP**
    - 하위 명령어 그룹을 나타냅니다. 명령어에 여러 하위 명령어 그룹이 있을 경우 그룹화를 위해 사용됩니다.
    - 예: `/image admin create`에서 `admin`이 SUB_COMMAND_GROUP이 됩니다.
- **3 STRING**
    - 문자열 타입을 입력으로 받습니다.
    - 예: 이름, 텍스트, URL 등.
- **4 INTEGER**
    - 정수형 데이터를 입력으로 받습니다. 음수와 양수 모두 가능하며, 소수점 없는 정수만 허용됩니다.
    - 예: 나이, 개수 등.
- **5 BOOLEAN**
    - 참(True) 또는 거짓(False) 값을 입력으로 받습니다.
    - 예: on/off, yes/no.
- **6 USER**
    - Discord 사용자를 입력으로 받습니다. 사용자 ID를 선택할 수 있습니다.
    - 예: 특정 유저를 선택할 때.
- **7 CHANNEL**
    - Discord 채널을 입력으로 받습니다. 텍스트 채널, 음성 채널 등 다양한 채널을 선택할 수 있습니다.
    - 예: 알림을 보낼 채널 선택.
- **8 ROLE**
    - Discord 역할을 입력으로 받습니다. 서버 내 특정 역할을 선택할 수 있습니다.
    - 예: 관리자 역할을 지정할 때.
- **9 MENTIONABLE**
    - 언급할 수 있는 모든 대상을 입력으로 받습니다. 사용자, 역할 등 언급할 수 있는 모든 대상을 포함합니다.
    - 예: 특정 사용자 또는 역할을 언급할 때.
- **10 NUMBER**
    - 숫자형 데이터를 입력으로 받습니다. 정수 및 소수를 모두 포함합니다.
    - 예: 특정 값(예: 3.14)을 입력할 때.
- **11 ATTACHMENT**
    - 첨부 파일을 입력으로 받습니다. 이미지, 파일 등 사용자가 업로드할 수 있는 파일을 포함합니다.
    - 예: 이미지 파일을 업로드할 때.