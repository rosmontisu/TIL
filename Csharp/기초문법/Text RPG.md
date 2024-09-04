- 초안
```cs
bool selectedJob = false;
while(!selectedJob)
{
    Console.WriteLine("직업을 선택하세요.");
    Console.WriteLine("[1] 기사");
    Console.WriteLine("[2] 궁수");
    Console.WriteLine("[3] 법사");

    int userInput = int.Parse(Console.ReadLine());
    switch(userInput)
    {
        case 1:
            Console.WriteLine("기사"); selectedJob = true;
            break;
        case 2:
            Console.WriteLine("궁수"); selectedJob = true;
            break;
        case 3:
            Console.WriteLine("법사"); selectedJob = true;
            break;
        default:
            break;
    }
}
```