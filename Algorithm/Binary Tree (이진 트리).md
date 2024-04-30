- 이진 트리에는 BFS/DFS뿐만 아니라 4가지 추가적인 순회가 가능하다
	- 레벨 순회 - BFS
- 전위/중위/후위 순회는 모두 재귀적이다
	- 전위 순회 - DFS
	- 중위 순회
	- 후위 순회
#### 레벨 순회
- 루트를 시작점으로 두고, BFS를 돌린 순회이다.
- {1-2-3-4-5-6-7-8}
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
```cpp
int lc[9] = { 0, 2, 4, 6, 0, 0, 0, 0, 0}
int rc[9] = { 0, 3, 5, 7, 0, 8, 0, 0, 0}
void preorder(int cur) {
	cout << cur << ' ';
	if (lc[cur] != 0) preorder(lc[cur]);
	if (rc[cur] != 0) preorder(rc[cur]);
}
```
#### 중위 순회 (Inorder Traversal)
```cpp
int lc[9] = { 0, 2, 4, 6, 0, 0, 0, 0, 0}
int rc[9] = { 0, 3, 5, 7, 0, 8, 0, 0, 0}
void inorder(int cur) {
	if (lc[cur] != 0) inorder(lc[cur]);
	cout << cur << ' ';
	if (rc[cur] != 0) inorder(rc[cur]);
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