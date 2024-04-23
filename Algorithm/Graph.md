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

```


