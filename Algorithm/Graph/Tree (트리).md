## 특징
- 방향성이 없고, (Undirected)
- 사이클이 없는 연결 그래프 (Acyclic Connected Graph)
- 트리는 임의의 노드를 root로 만들 수 있다.
## BFS/DFS
- 루트가 아닌 정점은 부모를 제외한 자식 정점만 방문하면된다.
- 즉, 트리에서의 BFS는 자신의 자식만 전부 큐에 넣어주면된다.
	- visit[] 배열이 필요없다
#### BFS - 부모 배열 채우기
```cpp
vector<int> adj[10];
int p[10];
void bfs(int root) {
	queue<int> q;
	q.push (root); // root-node
	while (!q.empty()) {
		int cur = q.front();
		q.pop();
		cout << cur << ' ';
		for (int nxt : adj[cur]) {
			if (p.[cur] == nxt) continue; // cur의 부모가 nxt라면 생략
			q.push(nxt); // cur -> nxt 로 더 깊은 노드로 이동했으니
			p[nxt] = cur; // nxt의 부모는 상위 노드인 cur로 저장
		}
	}
	
}
```
- 시간복잡도는 O(V)
	- 트리의 E = V-1이므로 O(V+E) -> O(V)
- 각 정점의 부모 정보를 p[] 배열에 저장하므로, BFS한번으로 부모 정보를 쉽게 파악 가능

#### BFS - 부모와 depth 배열 채우기
```cpp
vector<int> adj[10];
int p[10];
int depth[10];
voic bfs(int root) {
	queue<int> q;
	q.push(root); // root-node
	while (!q.empty()) {
		int cur = q.front();
		q.pop();
		cout << cur << ' ';
		for (int nxt : adj[cur]) {
			if (p[cur] == nxt) continue;
			q.push(nxt);
			p[nxt] = cur; // nxt의 부모는 cur입니다.
			depth[nxt] = depth[cur] + 1; // 자식의 depth는 부모 + 1;
		}
	}
}
```

#### DFS - 부모와 depth 배열 채우기 (비재귀)
```cpp
vector<int> adj[10];
int p[10];
int depth[10];
void dfs (int root) {
	stack<int> s;
	s.push(root); // root-node
	while (!s.empty()) {
		int cur = s.top();
		s.pop(); 
		cout << cur << ' ';
		for (int nxt : adj[cur]) {
			if (p[cur] == nxt) continue; // 부모노드이므로, 생략
			s.push(nxt);
			p[nxt] = cur;
			depth[nxt] = depth[cur] + 1;
		}
	}
}
```
#### DFS - 부모와 depth 배열 채우기 (재귀)
```cpp
vector<int> adj[10];
int p[10];
int depth[10]
void dfs(int cur) {
	cout << cur << ' ';
	// adj[cur]로 마지막 정점에 도달하면 알아서 멈추므로, 재귀가 성립
	for (int nxt : adj[cur]) {
		if (p[cur] == nxt) continue;
		p[nxt] = cur;
		depth[nxt] = depth[cur] + 1;
		dfs(nxt);
	}
}
```
- dfs(node) 로 함수를 시작하면된다.
- 주의점 : 스택 메모리가 1MB제한일경우?
- V가 3만 이상이라면 일자트리 모양에서 스택 메모리 한계를 넘을 수 있다.
#### DFS - 단순 순회 (재귀)
```cpp
vector<int> adj[10];
void dfs(int cur) {
	cout << cur << ' ';
	for (int nxt : adj[cur]) {
		dfs(nxt);
	}
}
```


## [이진 트리](obsidian://open?vault=TIL&file=Algorithm%2FGraph%2FBinary%20Tree%20(%EC%9D%B4%EC%A7%84%20%ED%8A%B8%EB%A6%AC)
- 부모 노드의 자식이 항상 좌-우로 2개인 트리
