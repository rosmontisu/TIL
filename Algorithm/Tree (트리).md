## 특징
> 방향성이 없고, (Undirected)
> 사이클이 없는 연결 그래프 (Acyclic Connected Graph)
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
