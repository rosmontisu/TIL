#### 1. TextRpg 직업 고르기 
- enum 열거형
- main 함수 밖으로 빼내기
- enum 타입의 변수 사용하기
```cs
enum ClassType
{
    None = 0,
    Knight = 1,
    Archer = 2,
    Mage = 3
}
static ClassType ChooseClass()
{
    Console.WriteLine("직업 선택");
    Console.WriteLine("[1] 기사");
    Console.WriteLine("[2] 궁수");
    Console.WriteLine("[3] 법사");

    ClassType choice = ClassType.None;
    string input = Console.ReadLine();
    switch (input)
    {
        case "1":
            choice = ClassType.Knight;
            break;
        case "2":
            choice = ClassType.Archer;
            break;
        case "3":
            choice = ClassType.Mage;
            break;
    }
    return choice;
}
static void Main(string[] args)
{
    while(true)
    {
        ClassType choice = ChooseClass();
        if (choice != ClassType.None)
            break;
    }
}
```
#### 2. TextRpg 플레이어 생성

##### 2-1 각 변수를 out으로 구현
- hp, attack 2개의 변수를 반환해야 하는데
- out 키워드로 각 switch(choice)에 맞게 반환하면 되지 않을까?
```cs
static void CreatePlayer(ClassType choice, out int hp, out int attack)
{
    switch (choice)
    {
        case ClassType.Knight:
            hp = 100;
            attack = 10;
            break;
        case ClassType.Archer:
            hp = 75;
            attack = 12;
            break;
        case ClassType.Mage:
            hp = 50;
            attack = 15;
            break;
        case ClassType.None:
            hp = 0; attack = 0;
            break;
        default:
            hp = 0; attack = 0;
            break;
    }
}
static void Main(string[] args)
{
    while (true)
    {
        ClassType choice = ChooseClass();
        if (choice != ClassType.None)
        {
            // 캐릭터 생성
            CreatePlayer(choice, out int hp, out int attack);
            Console.WriteLine($"{hp}/{attack}");
            // 기사(100/10) 궁수(75/12) 법사(50/15)
        }
    }
}
```

##### 2-2 player 구조체로 변수 묶기
- 지금은 변수가 hp, attack 2개 뿐이지만
- 만약 변수의 갯수가 증가하면, 수정할 부분이 너무 많다.
- struct를 이용해보자.
```cs
struct Player
{
    public int hp;
    public int attack;
    //public ClassType type;
}
static void CreatePlayer(ClassType choice, out Player player)
{
    switch (choice)
    {
        case ClassType.Knight:
            player.hp = 100;
            player.attack = 10;
            break;
        case ClassType.Archer:
            player.hp = 75;
            player.attack = 12;
            break;
        case ClassType.Mage:
            player.hp = 50;
            player.attack = 15;
            break;
        case ClassType.None:
            player.hp = 0; player.attack = 0;
            break;
        default:
            player.hp = 0; player.attack = 0;
            break;
    }
}
static void Main(string[] args)
{
    while (true)
    {
        ClassType choice = ChooseClass();
        if (choice != ClassType.None)
        {
            // 캐릭터 생성 
            Player player;

            CreatePlayer(choice, out player);
            Console.WriteLine($"{player.hp}/{player.attack}");
        }
    }
}
```

#### 3. TextRpg 몬스터 생성
- 몬스터 구조체와 열거형 몬스터타입 생성
- CreateRandomMonster() 구현
```cs
enum MonsterType
{
    None = 0,
    Slime = 1,
    Orc = 2,
    Skeleton = 3
}
struct Monster
{
    public int hp;
    public int attack;
}

static void CreateRandomMonster(out Monster monster)
{
    // 랜덤으로 1~3 몬스터 중 하나 생성
    Random rand = new Random();
    int randMonster = rand.Next(1, 4);

    switch (randMonster)
    {
        case (int)MonsterType.Slime:
            Console.WriteLine("슬라임이 스폰되었습니다.");
            monster.hp = 20;
            monster.attack = 2;
            break;
        case (int)MonsterType.Orc:
            Console.WriteLine("오크이 스폰되었습니다.");
            monster.hp = 40;
            monster.attack = 4;
            break;
        case (int)MonsterType.Skeleton:
            Console.WriteLine("스켈레톤이 스폰되었습니다.");
            monster.hp = 30;
            monster.attack = 3;
            break;
        default:
            monster.hp = 0;
            monster.attack = 0;
            break;
    }

}
static void EnterFiled()
{
    Console.WriteLine("필드에 접속했습니다.");

    // 몬스터 생성 
    Monster monster;
    CreateRandomMonster(out monster);

    Console.WriteLine("[1] 전투");
    Console.WriteLine("[2] 도망");
    string input = Console.ReadLine();
    switch (input)
    {
    }
}
```
#### 4.TextRpg 전투
- 원본 player와 monster의 수정이 필요하므로, ref를 이용하자
```cs
static void Fight(ref Player player, ref Monster monster)
{
    while (true)
    {
        // 플레이어가 몬스터 공격
        monster.hp -= player.attack;
        if (monster.hp <= 0)
        {
            Console.WriteLine("승리");
            Console.WriteLine($"남은 체력 : {player.hp}");
            break;
        }

        // 몬스터 반격
        player.hp -= monster.attack;
        if (player.hp <= 0)
        {
            Console.WriteLine("패배");
            break;
        }
    }
}
static void EnterFiled(ref Player player)
{
    Console.WriteLine("필드에 접속했습니다.");

    // 몬스터 생성 
    Monster monster;
    CreateRandomMonster(out monster);

    Console.WriteLine("[1] 전투");
    Console.WriteLine("[2] 도망");
    string input = Console.ReadLine();
    switch (input)
    {
        case "1":
            Fight(ref player, ref monster);
            break;
        case "2":
            // 33% 확률로 도망 성공
            Random rand = new Random();
            int randValue = rand.Next(0, 101);
            if (randValue <= 33)
            {
                Console.WriteLine("도망 성공");
                return;
            }
            else
            {
                Fight(ref player, ref monster);
            }
            break;
        default:
            break;
    }
}
```

#### 코드 전문
```cs
enum ClassType 
{
    None = 0,
    Knight = 1,
    Archer = 2,
    Mage = 3
}
struct Player
{
    public int hp;
    public int attack;
    //public ClassType type;
}
enum MonsterType
{
    None = 0,
    Slime = 1,
    Orc = 2,
    Skeleton = 3
}
struct Monster
{
    public int hp;
    public int attack;
}

static ClassType ChooseClass()
{
    Console.WriteLine("직업 선택");
    Console.WriteLine("[1] 기사");
    Console.WriteLine("[2] 궁수");
    Console.WriteLine("[3] 법사");

    ClassType choice = ClassType.None;
    string input = Console.ReadLine();
    switch (input)
    {
        case "1":
            choice = ClassType.Knight;
            break;
        case "2":
            choice = ClassType.Archer;
            break;
        case "3":
            choice = ClassType.Mage;
            break;
    }
    return choice;
}
static void CreatePlayer(ClassType choice, out Player player)
{
    switch (choice)
    {
        case ClassType.Knight:
            player.hp = 100;
            player.attack = 10;
            break;
        case ClassType.Archer:
            player.hp = 75;
            player.attack = 12;
            break;
        case ClassType.Mage:
            player.hp = 50;
            player.attack = 15;
            break;
        case ClassType.None:
            player.hp = 0; player.attack = 0;
            break;
        default:
            player.hp = 0; player.attack = 0;
            break;
    }
}
static void CreateRandomMonster(out Monster monster)
{
    // 랜덤으로 1~3 몬스터 중 하나 생성
    Random rand = new Random();
    int randMonster = rand.Next(1, 4);

    switch (randMonster)
    {
        case (int)MonsterType.Slime:
            Console.WriteLine("슬라임이 스폰되었습니다.");
            monster.hp = 20;
            monster.attack = 2;
            break;
        case (int)MonsterType.Orc:
            Console.WriteLine("오크이 스폰되었습니다.");
            monster.hp = 40;
            monster.attack = 4;
            break;
        case (int)MonsterType.Skeleton:
            Console.WriteLine("스켈레톤이 스폰되었습니다.");
            monster.hp = 30;
            monster.attack = 3;
            break;
        default:
            monster.hp = 0;
            monster.attack = 0;
            break;
    }

}

static void Fight(ref Player player, ref Monster monster)
{
    while (true)
    {
        // 플레이어가 몬스터 공격
        monster.hp -= player.attack;
        if (monster.hp <= 0)
        {
            Console.WriteLine("승리");
            Console.WriteLine($"남은 체력 : {player.hp}");
            break;
        }

        // 몬스터 반격
        player.hp -= monster.attack;
        if (player.hp <= 0)
        {
            Console.WriteLine("패배");
            break;
        }
    }
}
static void EnterFiled(ref Player player)
{
    Console.WriteLine("필드에 접속했습니다.");

    // 몬스터 생성 
    Monster monster;
    CreateRandomMonster(out monster);

    Console.WriteLine("[1] 전투");
    Console.WriteLine("[2] 도망");
    string input = Console.ReadLine();
    switch (input)
    {
        case "1":
            Fight(ref player, ref monster);
            break;
        case "2":
            // 33% 확률로 도망 성공
            Random rand = new Random();
            int randValue = rand.Next(0, 101);
            if (randValue <= 33)
            {
                Console.WriteLine("도망 성공");
                return;
            }
            else
            {
                Fight(ref player, ref monster);
            }
            break;
        default:
            break;
    }
}
static void EnterGame(ref Player player)
{
    while (true)
    {
        Console.WriteLine("마을에 접속했습니다.");
        Console.WriteLine("[1] 필드로 간다");
        Console.WriteLine("[2] 로비로 돌아가기");

        string input = Console.ReadLine();

        switch (input)
        {
            case "1":
                EnterFiled(ref player);
                break;
            case "2":
                return;
            default:
                break;
        }
    }
}

static void Main(string[] args)
{
    while (true)
    {
        ClassType choice = ChooseClass();
        if (choice == ClassType.None)
            continue;

        // 캐릭터 생성 
        Player player;
        CreatePlayer(choice, out player);
        EnterGame(ref player);
    }
}
```