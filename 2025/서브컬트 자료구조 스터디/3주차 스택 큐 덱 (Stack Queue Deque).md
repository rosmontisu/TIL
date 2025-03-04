## 1. 스택의 정의와 특징

##### 정의

후입선출(LIFO, Last-In-First-Out) 원칙에 따라 데이터를 관리하는 자료구조입니다.
##### 특징
- **동적 크기** : 데이터 추가/삭제에 따라 크기가 동적으로 변경됩니다.
- **제한된 접근** : 데이터는 스택의 맨 위(top)에서만 접근 가능합니다.
- **메모리 효율** : 연속된 메모리 공간을 사용하며, 캐시 지역성이 높습니다.

##### 시간복잡도

| 연산       | 시간복잡도 |
| -------- | ----- |
| 삽입(push) | O(1)  |
| 추출(pop)  | O(1)  |
| 탐색(top)  | O(1)  |
| 검색(특정 값) | O(N)  |

---

## 2. 큐의 정의와 특징

##### 정의

선입선출(FIFO, First-In-First-Out) 원칙에 따라 데이터를 관리하는 선형 자료구조입니다.

##### 특징

- **동적 크기** : 데이터 추가/삭제에 따라 크기가 동적으로 변경됩니다.
- **제한된 접근** : 데이터는 back에서 추가되고 front에서 삭제됩니다.
- **메모리 효율** : 원형 큐(Circular Queue)로 구현시 메모리 낭비를 줄일 수 있습니다.

##### 시간복잡도

| 연산          | 시간복잡도 |
| ----------- | ----- |
| 삽입(enqueue) | O(1)  |
| 추출(dequeue) | O(1)  |
| 탐색(front)   | O(1)  |
| 검색(특정 값)    | O(N)  |

---

## 3. 덱의 정의와 특징

##### 정의
양쪽 끝에서 삽입/삭제가 모두 가능한 자료구조로 Double-Ended Queue의 약자입니다.

##### 특징
- **유연한 연산**: front/back 양쪽에서 O(1) 시간에 삽입/삭제 가능합니다.
- **동적 배열 기반**: 일반적으로 블록 기반 할당으로 구현되어 확장성이 좋습니다.

##### 시간복잡도

| 연산                | 시간복잡도 |
| ----------------- | ----- |
| 앞쪽 삽입(push front) | O(1)  |
| 뒤쪽 삽입(push back)  | O(1)  |
| 앞쪽 추출(pop front)  | O(1)  |
| 뒤쪽 추출(pop back)   | O(1)  |
| 임의 접근(원칙적으로는 불가능) | O(1)¹ |

¹ 배열 기반 덱의 경우 인덱스 접근 가능합니다 (C++ STL `deque` 등..)

---

## 4. 구현과 C++ STL

##### 스택
- 구현
```cpp
int stk[N];
int pos = 0;

void push(int x) 
{
    stk[pos++] = x;
}

void pop() 
{
    if(pos > 0) pos--;
}

int top() 
{
    return stk[pos-1];
}
```
- STL
```cpp
#include <stack>
std::stack<int> s;

// 삽입
s.push(10);

// 추출
s.pop();

// 탐색
int top = s.top();

// 기타
bool isEmpty = s.empty();
int size = s.size();
```

##### 큐
- 구현
```cpp
int q[N];
int head = 0, tail = 0;

void push(int x) 
{ 
	q[tail++] = x; 
}
void pop() 
{ 
	head++; 
}
int front() 
{ 
	return q[head]; 
}
int back() 
{ 
	return q[tail-1]; 
}
```

- STL
```cpp
#include <queue>
std::queue<int> q;

// 삽입
q.push(20);

// 추출
q.pop();

// 탐색
int front = q.front();

// 기타
bool isEmpty = q.empty();
```

##### 덱
- 구현
```cpp
int dq[N*2]; // 양방향 확장을 위해 2배 할당
int head = N, tail = N;

void push_front(int x) 
{ 
	dq[--head] = x; 
}
void push_back(int x) 
{ 
	dq[tail++] = x; 
}
void pop_front() 
{ 
	head++; 
}
void pop_back() 
{ 
	tail--; 
}
int front() 
{ 
	return dq[head]; 
}
int back() 
{ 
	return dq[tail-1]; 
}
```
- STL
```cpp
#include <deque>
std::deque<int> dq;

// 양쪽 삽입
dq.push_front(5);
dq.push_back(15);

// 양쪽 추출
dq.pop_front();
dq.pop_back();

// 임의 접근
int val = dq[2];
```

---

## 5. 관련 알고리즘 & 활용 예시

##### 스택
- **DFS**(깊이 우선 탐색) : 재귀 대신 스택으로도 구현 가능합니다
- **괄호 쌍 검사** : `(){}[]` 와 같은 괄호들의 쌍을 검사하는 문제 풀이에 쓰입니다
	- 백준 단계별로 풀어보기 `스택` 단계에서 해당 유형의 연습 문제들입니다.
		- [boj 9012 괄호](https://www.acmicpc.net/problem/9012)
		- [boj 4949 균형잡힌 세상](https://www.acmicpc.net/problem/4949)



### 큐
- **BFS**(너비 우선 탐색) : 너비 우선 탐색시에 방문한 위치를 저장할때 사용합니다
- 단순 순차 처리
