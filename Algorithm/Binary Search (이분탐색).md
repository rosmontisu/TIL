## 특징
- 정렬되어 있는 배열에서 특정 데이터를 찾기 위해 탐색 범위를 절반으로 줄여가며 찾는 기법
- 시간복잡도
	- 선형탐색은 O(NM)이나, 이분탐색은 O(NlogN + MlogN)이다.
	1. 정렬 : NlogN
	2. 탐색 : MlgN
	3. 실제 시간복잡도 : O(NlogN + MlogN)
## 구현
- start, middle, end 포인트를 저장하는 변수를 이용해 구현한다.
- 각 변수의 핵심 로직은 아래와 같다.
	- 초기 end = n-1
	- middle = (start+end)/2 
	- start = mid+1
	- end = mid-1
```cpp
#include <iostream>
using namespace std;
//vector<int> v;
int arr[100001];
int n;
int BinarySearch(int input)
{
	int st = 0; 
	int end = n - 1;
	while (st <= end)
	{
		int mid = (st + end) / 2;
		if (arr[mid] < input)
			st = mid + 1;
		else if (arr[mid] > input)
			end = mid - 1;
		else
			return 1;
	}
	return 0;
}
int main(void)
{
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> arr[i];
	sort(arr, arr + n);
	int m;
	cin >> m;
	while (m--)
	{
		int input; cin >> input;
		cout << BinarySearch(input) << '\n';
	}
}
```
## Parametric Search
- 최적화 문제 : 조건을 만족하는 최소/최댓값을 구하는 문제
- 최적화 문제를 결정 문제로 변환해 이분탐색을 수행하는 방법
- 예시 문제 [boj 1654 랜선 자르기](https://www.acmicpc.net/problem/1654)
- 변수를 가지고 함수를 세웠을 때 그 함수가 증가/감소 함수인 경우에 가능하다.
- ![[Pasted image 20240514171611.png]]위 그림과 같은 구조이다 [출처](https://blog.encrypted.gg/985)
- 문제에서 최소/최대에 대한 얘기가 나오고, 범위가 매우 큰 경우, 시간복잡도에서 값 하나(큰 변수 하나)를 로그로 떨구면 될때 parametric search의 사용을 고민해보자.
 