- ref를 이용한 원본 수정 vs 반환값을 이용한 값 수정
```cs
static void AddOne(ref int number)
{
    number = number + 1;
}

static int AddOne2(int number)
{
    return number + 1;
}

static void Main(string[] args)
{
    int a = 0;
    Program.AddOne(ref a); // 값 복사가 아닌 주소 참조 ref
    Console.WriteLine(a);

    // 디자인상 아래 방식이 더 좋음
    // 실제 값을 수정하지 않음(원본을 건들지 않아서 안전함)
    a = Program.AddOne2(a);
    Console.WriteLine(a);
}
```
- out을 이용한 여러개의 값 반환
```cs
static void Divide(int a, int b, out int result1, out int result2)
{
    // out 은 ref처럼 참조를 한다.
    result1 = a / b;
    result2 = a % b;
}

static void Main(string[] args)
{
    int num1 = 10;
    int num2 = 3;

    int res1;
    int res2;
    Divide(num1, num2, out res1, out res2);

    Console.WriteLine(res1);
    Console.WriteLine(res2);
}
```
