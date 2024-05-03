- 이진 트리에는 BFS/DFS뿐만 아니라 4가지 추가적인 순회가 가능하다
	- 레벨 순회 - BFS
- 전위/중위/후위 순회는 모두 재귀적이다
	- 전위 순회 - DFS
	- 중위 순회
	- 후위 순회
#### 레벨 순회
- 루트를 시작점으로 두고, BFS를 돌린 순회이다.
- { 1-2-3-4-5-6-7-8 }
```cpp
int lc[9] = { 0, 2, 4, 6, 0, 0, 0, 0, 0}
int rc[9] = { 0, 3, 5, 7, 0, 8, 0, 0, 0}
void bfs() {
	queue<int> q;
	q.push(1);
	while(!q.empty()) {
		int cur = q.front();
		q.pop();
		cout << cur << ' ';
		if (lc[cur]) q.push(lc[cur]);
		if (rc[cur]) q.push(rc[cur]);
	}
}
```
#### 전위 순회 (Preorder Traversal)
- DFS와 방문 순서가 같다.
- 자신을 출력, 왼쪽/오른쪽 자식 각각에 대해 존재할 경우 다시 전위 순회
	1. 현재 정점을 방문한다.
	2. 왼쪽 서브 트리를 전위 순회한다.
	3. 오른쪽 서브 트리를 전위 순회한다.
- 일단 방문 -> 왼쪽방문 -> 왼쪽이 없으면 이제 오른쪽
- { 1-2-4-5-8-3-6-7 }
```cpp
int lc[9] = { 0, 2, 4, 6, 0, 0, 0, 0, 0}
int rc[9] = { 0, 3, 5, 7, 0, 8, 0, 0, 0}
void preorder(int cur) {
	cout << cur << ' '; // 현재 정점 출력
	if (lc[cur] != 0) preorder(lc[cur]); // 좌측 전위 순회
	if (rc[cur] != 0) preorder(rc[cur]); // 우측 전위 순회
}
```
#### 중위 순회 (Inorder Traversal)
- 트리의 가장 왼쪽에 있는 것 부터 방문하는 순서와 같다.
- 그렇기에 만약 BST라면, 가장 작은 수 -> 큰 수로 탐색된다.
	1. 왼쪽 서브 트리를 중위 순회한다.
	2. 현재 정점을 방문한다.
	3. 오른쪽 서브 트리를 중위 순회한다.
- 최대한 왼쪽으로 가기 -> 방문 -> 왼쪽이 없으면 오른쪽
- { 4-2-5-8-1-6-3-7 }
```cpp
int lc[9] = { 0, 2, 4, 6, 0, 0, 0, 0, 0}
int rc[9] = { 0, 3, 5, 7, 0, 8, 0, 0, 0}
void inorder(int cur) {
	if (lc[cur] != 0) inorder(lc[cur]); // 좌측 중위 순회
	cout << cur << ' '; // 현재 정점 출력
	if (rc[cur] != 0) inorder(rc[cur]); // 우측 중위 순회
}
```
#### 후위 순회 (Postorder Traversal)
```cpp
int lc[9] = { 0, 2, 4, 6, 0, 0, 0, 0, 0}
int rc[9] = { 0, 3, 5, 7, 0, 8, 0, 0, 0}
void postorder(int cur) {
	if (lc[cur] != 0) postorder(lc[cur]);
	if (rc[cur] != 0) postorder[rc[cur]];
	cout << cur;
}
```
#### 예시문제
- [1991 트리 순회](https://www.acmicpc.net/problem/1991)