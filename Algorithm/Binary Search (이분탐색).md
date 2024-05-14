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