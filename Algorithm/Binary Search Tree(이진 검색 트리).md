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
	 
#### STL
- set, multiset, map 3가지가 구현되어있다.
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



