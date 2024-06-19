## 특징
 - pop을 할 때 가장 먼저 들어온 원소가 나오는 대신, 
 - 우선순위가 가장 높은 원소가 나오는 큐
##### 시간복잡도
1. 원소의 추가 O(logN) - binary tree를 계속 이분하면서 heap[1] -> heap[n] 하므로 최악이 logN
2. 우선순위가 가장 높은 원소의 확인 O(1)
3. 우선순위가 가장 높은 원소의 제거 O(logN) - binary tree를 계속 이분하면서 heap[n] -> heap[1] 하므로 logN    
## 구현 
> 배열을 이용한 구현이 가능하다.

백준에 [최소힙](https://www.acmicpc.net/problem/1927)문제를 풀면서 아래의 연산을 직접 구현해보자.
- insert(x)
1. heap[size] = x; 힙의 최하단에 x를 넣는다.
2. if (heap[size/2] > heap[size]) ? swap(heap[size/2], heap[size]) : berak; x와 x의 부모를 비교 후 swap or break 한다.
3. if (size == 1) ? break  : continue; 만약 x가 root(size==1)에 도달하면 break한다.

- top()    
1. size == 0이면 아직 그래프가 없는것이다.
2. size > 0이면 return heap[1];로 최상층을 전달한다.

- pop() / 반환이 void일때로 가정할때 구현        
-- root를 제거하고, 가장 하단의 vertex를 root로 올린 후 구현한다.    
1. heap[1] = heap[size] // root에 최하단 vertex 올리기
2. size--; // size줄이기 - 실제 구현시 1번과 통합 가능합니다.
-- 이분트리이므로 왼쪽 자식과 오른쪽 자식을 구분해서, 더 작은 자식과 부모간의 자리를 교환한다. 
3. minChild = lc // 임시 초기화 
3-1. lc = cur * 2, rc = cur * 2 + 1 // 왼쪽 오른쪽 자식 설정
3-2. if (lc > rc) minChild = rc // 양쪽 자식 크기 비교 후, minChild 재지정
3-3. if (heap[cur] > heap[minChild]) swap // 자식이 더 작다면 swap후 계속 반복    
3-4. swap(heap[cur], heap[minChild]), cur = minChild;


```cpp
#include <iostream>
using namespace std;

int heap[100005];
int sz = 0; // heap에 들어있는 원소의 수

void push(int x) {
	sz++;
	heap[sz] = x;

	int cur = sz;
	while (cur != 1) {
		if (heap[cur / 2] <= heap[cur]) break;
		swap(heap[cur / 2], heap[cur]);
		cur /= 2;
	}
}

int top() {
	if (sz == 0)
		return 0;
	return heap[1];
}

void pop() {
	if (sz == 0)
		return;


	heap[1] = heap[sz--];
	int cur = 1;
	while (cur * 2 <= sz) {
		int lc = 2 * cur;	// 왼쪽 자식
		int rc = 2 * cur + 1; // 오른쪽 자식

		int min_child = lc; // 자식 중 더 작은 자식
		if (rc <= sz && heap[rc] < heap[lc])
			min_child = rc;
		if (heap[cur] <= heap[min_child]) break;
		swap(heap[cur], heap[min_child]);
		cur = min_child;
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int n; cin >> n;
	int x, cnt = 0;
	while (n--)
	{
		cin >> x;
		if (x > 0)
			push(x);
		else {
			cout << top() << '\n';
			pop();
		}
	}
}
```