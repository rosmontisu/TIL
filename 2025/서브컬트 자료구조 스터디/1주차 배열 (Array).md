## 1. 배열의 정의와 특징
##### 정의
동일한 타입의 데이터를 연속적인 메모리 공간에 저장하는 자료 구조

##### 특징
- 고정된 크기 : 배열은 선언 시 크기가 정해지며, 이후 변경할 수 없다.
- 동일한 데이터 타입 : 배열은 모두 같은 데이터 타입만을 저장한다.
- 연속된 메모리 공간 : 배열 요소들은 메모리에 연속적으로 배치된다.
- 인덱스를 통한 접근 : 배열의 데이터는 각각의 인덱스를 통해 접근한다.
    

#### 시간 복잡도
- 예외적으로 배열의 마지막 인덱스에 삽입/삭제는 O(1)의 시간복잡도를 가진다.

| 연산    | 시간 복잡도       |
| ----- | ------------ |
| 접근/변경 | O(1)         |
| 삽입/삭제 | O(n) (특정 위치) |
|       |              |

![[Pasted image 20250218014634.png]]
![[Pasted image 20250218014559.png]]
![[Pasted image 20250218014609.png]]

#### 캐시 히트

- 배열은 메모리에 연속적으로 데이터가 저장되기 때문에, 한번의 메모리 접근으로 근처 주소에 데이터가 함께 캐싱되어 캐시 히트 비율이 높다.
- 이때, 2차원 배열에서 캐시히트와 관련된 문제가 존재하는데
- ![[Pasted image 20250218014158.png]]
- 왼쪽 그림과 같이 데이터를 1번 그림처럼 순서데로 (0,1 - 0,2 - 0,3 ... 3,1 - 3,2 - 3,3) 접근하면 캐시히트 덕분에 빠른 데이터 접근이 가능하지만
- 오른쪽 그림처럼 데이터에 접근하면 캐시 히트에 실패하여(캐시 미스) 데이터에 접근하는 속도가 느려지게된다.


## 2. 배열의 구현

#### 배열 선언과 초기화

```cpp
int arr[5] = { 1, 2, 3, 4, 5 };
```

#### 배열 기능 구현
- 삽입
	- 데이터를 삽입할 위치 pos보다 큰 인덱스에 값들을 모두 +1칸 이동한다.
	- 그리고, pos 인덱스에 삽입할 데이터 value를 넣고 배열의 크기 size를 1 증가시킨다.
```cpp
void Insert(int arr[], int& size, int pos, int value) 
{
    for (int i = size; i > pos; i--) 
	    arr[i] = arr[i - 1];
	    
    arr[pos] = value;
    size += 1;
}
```
- 삭제
	- 지우려는 데이터의 위치 pos보다 큰 인덱스에 값들을 모두 -1칸 이동한다.
	- 배열의 크기 size를 1 감소시킨다.
```cpp
void Erase(int arr[], int& size, int pos) 
{
    for (int i = pos; i < size; i++) 
	    arr[i] = arr[i + 1];
	    
    size -= 1;
}
```


## 3. 배열 연습 문제
- 순수하게 배열 만을 사용하는 문제는 많지 않지만...
- 배열을 응용해서 스택, 큐, 인접행렬(그래프) 등등 다양한 자료구조를 구현 가능하고, 이를 통해 여러 알고리즘 문제 풀이가 가능해집니다.
- 개인적으로 길찾기나 최단거리와 관련된 알고리즘 문제에서 배열이 직관적이라 배열로 문제의 조건(미로나 그래프 등)을 구현하는걸 선호합니다.
```cpp
#include <iostream>
#include <queue>
#include <windows.h>
#include <conio.h>

using namespace std;

#define X first
#define Y second

enum Tile { WALL, PATH, VISITED, START, END };
const int mazeSize = 10;

// 콘솔 색상 설정
void SetColor(int color) 
{
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), color);
}

// 미로 초기화 (수동, 생성 알고리즘 미구현)
Tile maze[mazeSize][mazeSize] = 
{
    {WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL},
    {WALL, PATH, PATH, WALL, PATH, PATH, PATH, PATH, PATH, WALL},
    {WALL, WALL, PATH, WALL, PATH, WALL, WALL, PATH, WALL, WALL},
    {WALL, PATH, PATH, PATH, PATH, WALL, PATH, PATH, PATH, WALL},
    {WALL, PATH, WALL, WALL, WALL, WALL, WALL, WALL, PATH, WALL},
    {WALL, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, WALL},
    {WALL, WALL, WALL, PATH, WALL, WALL, WALL, WALL, PATH, WALL},
    {WALL, PATH, PATH, PATH, WALL, PATH, PATH, PATH, PATH, WALL},
    {WALL, PATH, WALL, PATH, PATH, PATH, WALL, WALL, PATH, WALL},
    {WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL}
};

pair<int, int> startPos = { 1, 1 };  // 시작 좌표
pair<int, int> endPos = { 8, 8 };    // 종료 좌표

// 미로 출력
void PrintMaze(bool isVisited[mazeSize][mazeSize]) 
{
    system("cls"); // 화면 지우기

    for (int i = 0; i < mazeSize; i++) 
    {
        for (int j = 0; j < mazeSize; j++) 
        {
            if (i == startPos.X && j == startPos.Y) 
            {
                SetColor(12); // 시작점 빨강
                cout << "S ";
            }
            else if (i == endPos.X && j == endPos.Y) 
            {
                SetColor(12); // 종료점 빨강
                cout << "E ";
            }
            else if (isVisited[i][j]) 
            {
                SetColor(12); // 방문한곳 빨강
                cout << "* ";
            }
            else if (maze[i][j] == WALL) 
            {
                SetColor(10); // 벽 초록
                cout << "■";
            }
            else 
            {
                SetColor(15); // 길 흰색
                cout << "  ";
            }
        }
        cout << '\n';
    }
    SetColor(15); // 색상 리셋
}

// BFS 탐색 함수
void BFS() 
{
    bool visited[mazeSize][mazeSize] = { false };
    queue<pair<int, int>> q;
    q.push(startPos);
    visited[startPos.first][startPos.Y] = true;

    int dx[] = { 0, 1, 0, -1 };
    int dy[] = { 1, 0, -1, 0 };

    while (!q.empty()) 
    {
        int size = q.size();
        for (int i = 0; i < size; i++) 
        {
            pair<int, int> current = q.front();
            q.pop();

            // 종료 지점 도달 시
            if (current == endPos) 
            {
                PrintMaze(visited);
                cout << "\n탐색 성공\n\n";
                return;
            }

            // 4방향 탐색
            for (int dir = 0; dir < 4; dir++) 
            {
                int nx = current.X + dx[dir];
                int ny = current.Y + dy[dir];

                if (nx < 0 || nx >= mazeSize || ny < 0 || ny >= mazeSize) continue;
                if (visited[nx][ny] || maze[nx][ny] == WALL) continue;

                visited[nx][ny] = true;
                q.push({ nx, ny });
            }
        }
        PrintMaze(visited);
        Sleep(500); // 0.5초 대기
    }
    cout << "\n탐색 실패\n\n";
}

int main() 
{
    cout << "2차원 배열로 생성한 미로에서 BFS를 시각적으로 보여줍니다.\n";
    cout << "출발지 S -> 도착지 E\n";
    cout << "키 입력으로 시작\n";
    _getch();

    BFS();
    return 0;
}
```
	
#### 백준 단계별로 풀어보기 : 1차원 배열, 2차원 배열
- [개수 세기](https://www.acmicpc.net/problem/10807)
- [알파벳 개수](https://www.acmicpc.net/problem/10808)
- [행렬 덧셈](https://www.acmicpc.net/problem/2738)
- [색종이](https://www.acmicpc.net/problem/2563)