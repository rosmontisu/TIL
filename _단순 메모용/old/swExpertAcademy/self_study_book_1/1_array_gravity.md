### 1차시 대표문제. Gravity   
상자들이 쌓여있는 방을 90도 회전하였을때 중력을 받은 상자들의 낙하 높이를 구하는 문제.

## mySolve
1. [n][m] 크기의 배열을 선언   
n,0 - n,m   
0,0 - 0,m
2. 시계방향으로 90도 회전시 좌표가 [x][y]인 낙하 높이는  m - x - (m과 x사이에 블럭 수)   
3. 가장 큰 낙차 출력   
```c
#include <stdio.h>

int main()
{
    int t, n, m;
    scanf("%d", &t);
    scanf("%d %d", &n, &m); // 가로길이 n 세로길이 m
    
    int room[n][m]; // x, y 좌표
    int h;
    
    // 배열 0으로 초기화
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            room[i][j] = 0;
        }
    }
    
    // 상자 쌓기
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &h);
        for (int j = 0; j < h; j++)
        {
            room[i][j] = 1;
        }
    }
    
    int empty = 0;
    int maxEmpty = 0;
    // 낙차 구하기
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (room[i][j] == 1)
            {
                empty = 0;
                for (int k = i+1; k < n; k++)
                {
                    if (room[k][j] == 0)
                        empty++;
                }
                if (empty > maxEmpty)
                    maxEmpty = empty;
            }
        }
    }
    printf("%d\n", maxEmpty);
}
```



## bookSolve
#### 1. 2차원 배열에 상자들을 채운 후 모든 낙차를 계산한다. << mySolve에서 채택한 방법
모든 상자들의 낙차를 구해야 한다. 시간 복잡도가 O(n^3)으로 매우 오래걸린다.
#### 2. 가장 위에 상자만을 계산한다.
가장 위에 있는 상자만 최대 낙차를 가질 수 있다는 아이디어를 사용.
```c
#include <stdio.h>

// 전처리를 이용해서 변수의 가독성을 높여준다.
#define EMPTY 0
#define BOX 1

int main()
{
    int i;
    int testCase, T;
    
    int roomWidth, roomHeight;
    int maxFallen;
    int room[100][100] = { EMPTY, };
    int boxTop[100] = {0, };
    int countEmptySpace;
    
    scanf("%d", &testCase);
    for (T = 0; T , testCase; T++)
    {
        scanf("%d %d", &roomWidth, &roomHeight);
        maxFallen = 0;
        
        // 방에 상자 채우기
        for (i = 0; i < roomWidth; i++)
        {
            scanf("%d", &boxTop[i]);
            for (int j = 0; j < boxTop[i]; j++)
                room[i][j] = BOX;
        }
        
        // 각 열의 가장 위에 있는 상자의 낙차 구하기
        for (i = 0; i < roomWidth; i++)
        {
            if (boxTop[i] > 0)
            {
                countEmptySpace = 0;
                for (int j = i + 1; j < roomWidth; j++)
                {
                    // 실제 배열은 0부터 시작한다.
                    // 고로 boxTop[i] - 1로 구해준다.
                    if (room[j][boxTop[i] - 1] == EMPTY)
                        countEmptySpace += 1;
                }
                if (countEmptySpace > maxFallen)
                {
                    maxFallen = countEmptySpace;
                }
            }
        }
        
        printf("%d\n", maxFallen);
    }
}
```
