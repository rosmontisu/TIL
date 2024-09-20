```cs
using System.Numerics;
using System.Runtime.CompilerServices;

namespace CSharp
{
    class Program
    {
        static void Main(string[] args)
        {
            Game gmae = new Game();
            
            while (true)
            {
                gmae.Process();
            }
        }
    }
}

```