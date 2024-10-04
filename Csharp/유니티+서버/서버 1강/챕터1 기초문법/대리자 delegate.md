- C++의 함수 포인터와 비슷한 역할
	- 함수 자체를 인자로 넘겨줄수도 있다
- CallBack 예제
```cs
using System.Numerics;
using System.Runtime.CompilerServices;

namespace CSharp
{
    class Program
    {
        delegate int OnClicked();
        // void를 받고 int를 리턴하는
        // '형식' 자체로 분석하기

        static void ButtonPressed(OnClicked clickedFunction /*함수 자체를 인자로 넘겨주고*/)
        {
            clickedFunction(); /*넘겨 받은 함수를 호출*/
        }

        static int TestDelegate()
        {
            Console.WriteLine("Hello Delegate");
            return 0;
        }

        static void Main(string[] args)
        {
            ButtonPressed(TestDelegate);

        }
    }
}
```