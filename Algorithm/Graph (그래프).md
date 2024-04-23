## 특징
> 정점(vertex/node)와 간선(edge)로 이루어진 자료구조
## 종류
- 순환 그래프 (Cyclic Graph)
- 비순환 그래프 (Acyclic Graph)
- 완전 그래프 (Complete Graph)
- 연결 그래프 (Connected Graph)
- 단순 그래프 (Simple Graph)

## 표현법
#### 인접 행렬
#### 리스트

## BFS
#### 구현

- 연결 그래프에서의 순회
```cpp
vector<int> adj[10]; // adjacency
bool vis[10];
void bfs()
{
	queue<int> q;
	q.push(1);
	vis[1] = true;
	while (!q.empty())
	{
		int cur = q.front();
		q.pop();
		cout << cur << ' ';
		for (auto nxt : adj[cur])
		{
			if (vis[nxt]) continue;
			q.push(nxt);
			vis[nxt] = true;
		}	
	}
}
```

    
- 1번 정점과의 거리 - dist
```cpp
vector<int> adj[10]; // adjacency
bool dist[10];
void bfs()
{
	fill(dist, dist + 10, -1);
	queue<int> q;
	q.push(1);
	dist[1] = 0;
	while (!q.empty())
	{
		int cur = q.front();
		q.pop();
		for (auto nxt : adj[cur])
		{
			if (dist[nxt] != -1) continue;
			q.push(nxt);
			dist[nxt] = dist[cur] + 1;
		}
	}
}
```


- 연결 그래프가 아닐때 { 1, 2, 3, 4 }, { 5, 6 }
```cpp
vector<int> adj[10]; // adjacency
bool vis[10];
int v = 9; // vertax
void bfs()
{
	queue<int> q;
	for (int i = 1; i <= v; i++)
	{
		if (vis[i]) continue;
		q.push(i);
		vis[i] = true;
		while (!q.empty())
		{
			int cur = q.front();
			q.pop();
			cout << cur << ' ';
			for (auto nxt : adj[cur])
			{
				if (vis[nxt]) continue;
				q.push(nxt);
				vis[nxt] = true;
			}
		}
	}
}
```

## DFS
> BFS에서는 큐를 사용했지만, DFS에서는 스택을 사용한다. 또한, 재귀를 이용하여 구현도 가능하다.
#### 구현
- 연결 그래프 순회, 비재귀
```cpp
vector<int> adj[10];
bool vis[10];
void dfs()
{
	stack<int> s;
	s.push(1);
	vis[1] = true;
	while (!s.empty())
	{
		int cur = s.top();
		s.pop();
		cout << cur << ' ';
		for (auto nxt : adj[cur])
		{
			if (vis[nxt]) continue;
			s.push(nxt);
			vis[nxt] = true;
		}
	}
}
```

- 연결 그래프 순회, 재귀
```cpp
vector<int> adj[10];
bool vis[10];
void dfs(int cur)
{
	vis[cur] = true;
	cout << cur << ' ';
	for (auto nxt : adj[cur])
	{
		if (vis[nxt]) continue;
		dfs(nxt);
	}
}
```




