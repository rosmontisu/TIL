```cs
using System;
using System.Reflection;

public class ExampleClass
{
    public void PrintMessage(string message)
    {
        Console.WriteLine(message);
    }
}

public class ReflectionExample
{
    public static void Main()
    {
        // Type 객체 가져오기
        Type type = typeof(ExampleClass);

        // 인스턴스 생성
        object instance = Activator.CreateInstance(type);

        // 메서드 정보 가져오기
        MethodInfo methodInfo = type.GetMethod("PrintMessage");

        // 메서드 동적 호출
        methodInfo.Invoke(instance, new object[] { "Hello, Reflection!" });
    }
}

```