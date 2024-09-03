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