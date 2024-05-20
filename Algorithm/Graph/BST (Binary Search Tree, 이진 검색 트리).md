## 특징
- 왼쪽 서브트리의 모든 값은 부모의 값보다 작고, 
- 오른쪽 서브트리의 모든 값은 부모의 값보다 크다.
- 원소가 크기순으로 정렬되어 있다.
- 이분되어 있으므로, 모든 연산은 n/2회 발생한다. 즉 시간복잡도는 O(log N)
- insert, erase, find, update -> O(log N)
## 자가 균형 트리
#### 필요성
 - root = 1 로 잡힌경우, 데이터가 완전히 순차적으로 들어오는 경우 등... 
 - 이진 트리가 한쪽방향으로 편향되게 그려질 경우 트리의 높이는?
	 정상적인 트리 : logN
	 편향된 트리 : n
- 이분 트리를 이용할 이유가 없어진다. (리스트와 다를바가 없기때문에)
- 그래서, 편향되지 않도록 해결해주는 트리 : 자가 균형 트리(Self-Binary Tree)
#### 구현과 원리
- 종류 : AVL Tree / Red Black Tree
- 구현난이도 : AVL < Red Black
- 성능 : AVL < Red Black
	 
## STL
- set, multiset, map 3가지로 구현이 가능하다.
- 직접 예제 코드를 작성하고, 분석해보자. ([예제 출처](https://blog.encrypted.gg/1013))
#### STL - set
```cpp
void set_example() {
	set<int> s;

	s.insert(-10); s.insert(100); s.insert(15); // { -10, 15, 100 }
	s.insert(-10); // { -10, 15, 100 }

	cout << s.erase(100) << '\n'; // { -10, 15 }, 1
	cout << s.erase(20) << '\n'; // { -10, 15 }, 0

	if (s.find(15) != s.end()) cout << "15 in s\n";
	else cout << "15 not in s\n";

	cout << s.size() << '\n'; // 2
	cout << s.count(50) << '\n'; // 0
	for (auto e : s) cout << e << ' ';
	cout << '\n';

	s.insert(-40); // {-40, -10, 15 }

	set<int>::iterator it1 = s.begin(); // begin() : 처음 원소의 iterator 반환
	it1++; // { -40, -10(<- it1), 15 }
	auto it2 = prev(it1); // { -40(<- it2), -10, 15 }	뒤로
	it2 = next(it1); // { -40, -10, 15(<- it2) }		앞으로
	advance(it2, -2); // { -40(<- it2), -10, 15 }		-2칸 전진

	auto it3 = s.lower_bound(-20); // { -40, -10(<- it3), 15) }
	auto it4 = s.find(15); // { -40, -10, 15(<- it4) }

	cout << *it1 << '\n'; // -10
	cout << *it2 << '\n'; // -40
	cout << *it3 << '\n'; // -10
	cout << *it4 << '\n'; // 15
}
```
#### STL - multiset
> set과 다른 몇가지 특징들이 있습니다
- 원소의 중복이 허용된다.
- erase(n) : 모든 n을 지웁니다.
- find(n) : n 원소중 무작위로 반환합니다.
```cpp
void multiset_example() {
	multiset<int> ms;
	ms.insert(-10); ms.insert(100); ms.insert(15); // { -10, 15, 100 }
	ms.insert(-10); ms.insert(15); // { -10, -10, 15, 15, 100 }
	cout << ms.size() << '\n'; // 5
	for (auto e : ms) cout << e << ' ';
	cout << '\n';
	cout << ms.erase(15) << '\n'; // { -10, -10, 100 }, 15가 번부 지워진다.
	ms.erase(ms.find(-10)); // { -10, 100 }, 1개만 찾아서 지운다.
	ms.insert(100); // { -10, 100, 100 }
	cout << ms.count(100) << '\n'; // 2

	auto it1 = ms.begin(); // { -10(<- it1), 100, 100 }
	auto it2 = ms.upper_bound(100); // { -10, 100, 100 } (<- it2)
	auto it3 = ms.find(100); // { -10, 100(<- it3), 100 }, 가장 좌측 100을 찾아준다

	cout << *it1 << '\n'; // -10
	cout << (it2 == ms.end()) << '\n'; // 1(true)
	cout << *it3 << '\n'; // 100
}
```
#### STL - map
> key : value 구조이다
```cpp
void map_example() {
	map<string, int> m;
	m["hi"] = 123;
	m["bkd"] = 1000;
	m["gogo"] = 165; 
	// ("bkd", 1000), ("gogo", 165), ("hi", 123)
	cout << m.size() << '\n'; // 3
	m["hi"] = -7; // ("bkd", 1000), ("gogo", 165), ("hi", -7)
	if (m.find("hi") != m.end()) cout << "hi in m\n";
	else cout << "hi not in m\n";
	m.erase("bkd"); // ("gogo", 165), ("hi", 123)
	for (auto e : m)
		cout << e.first << ' ' << e.second << '\n';
	auto it1 = m.find("gogo");
	cout << it1->first << ' ' << it1->second << '\n'; // gogo 165 (key : value)
}
```

## 주의점
- end() 함수는 마지막 원소 다음 주소의 iterator를 반환한다. 
  사용시 --end()/prev(end()) 등을 고려해보자
- 이진 검색 트리의 연산은 같은 O(logN) 중에서도 상당히 느리기때문에, 
  n=100만 이상인 연산을 수행할 경우 시간제한 1초는 부담된다.
## 연습문제
#### [boj 7662 : 이중 우선순위 큐](https://www.acmicpc.net/problem/7662)
- 최소값과 최대값만 수정하면 되는 문제입니다.
- 중복되는 원소가 존재하므로, STL multiset을 이용해서 풀이
##### 내 풀이
```cpp
#include <iostream>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t; cin >> t;
	while (t--)
	{
		multiset<int> ms;
		int k; cin >> k;
		while (k--)
		{
			// D 1	: 최댓값 삭제
			// D -1 : 최솟값 삭제
			// I n	: insert n
			char c; int num;
			cin >> c >> num;
			if (c == 'D' && ms.size() > 0 && num == 1) {
				multiset<int>::iterator itr = --ms.end();
				ms.erase(itr);
			}
			else if (c == 'D' && ms.size() > 0) {
				multiset<int>::iterator itr = ms.begin();
				ms.erase(itr);
			}
			else if (c == 'I') ms.insert(num);
		}

		if (ms.size() > 0)
		{
			auto it1 = ms.begin();
			auto it2 = --ms.end();
			cout << *it2 << ' ' << *it1 << '\n';
		}
		else cout << "EMPTY\n";
	}
}
```
#### [boj 1202 : 보석 도둑](https://www.acmicpc.net/problem/1202)

```cpp
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

multiset<int> bag; 
pair<int, int> jam[300001];

int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	int jamNum, bagNum;
	cin >> jamNum >> bagNum;

	for (int i = 0; i < jamNum; i++)
		cin >> jam[i].second >> jam[i].first; 
	// key를 value로 잡아야 검색이 가능하니까
	// cin >> 무게 >> 가치
	sort(jam, jam + jamNum);

	for (int i = 0; i < bagNum; i++)
	{
		int c;
		cin >> c; 
		bag.insert(c);
	}

	long long ans = 0;

	// 고가치부터 담아야 하므로 역순 루프
	for (int i = jamNum - 1; i >= 0; i--)
	{
		int m, v;
		m = jam[i].second;
		v = jam[i].first;

		auto it = bag.lower_bound(m);
		if (it == bag.end())
			continue;
		ans += v;
		bag.erase(it);
	}
	cout << ans;
	return 0;
}
```
