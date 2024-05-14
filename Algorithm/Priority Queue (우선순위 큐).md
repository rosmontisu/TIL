## 특징
 - pop을 할 때 가장 먼저 들어온 원소가 나오는 대신, 
 - 우선순위가 가장 높은 원소가 나오는 큐
##### 시간복잡도
1. 원소의 추가 O(logN)
2. 우선순위가 가장 높은 원소의 확인 O(1)
3. 우선순위가 가장 높은 원소의 제거 O(logN)
## 구현 
> 배열을 이용한 구현이 가능하다.

백준에 [최소힙](https://www.acmicpc.net/problem/1927)문제를 풀면서 아래의 연산을 직접 구현해보자.
- insert(x)
- top()
- pop()
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