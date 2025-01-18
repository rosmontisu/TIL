- 문자열(문자)이 처음으로 나타나는 위치(시작하는 위치의 인덱스)를 반환해줌
- 만약 포함되어 있지 않다면 -1 반환
```cs
string example = "MyObject(Clone)";
int index = example.IndexOf("(Clone)");
// index는 8을 반환합니다.
```