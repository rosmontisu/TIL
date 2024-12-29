- 형 변환에 실패하면 null을 반환하는 연산자
```cs
object obj = "Hello, World!";
string str = obj as string;

if (str != null)
{
    Console.WriteLine(str);
}
else
{
    Console.WriteLine("형변환 실패");
}

```