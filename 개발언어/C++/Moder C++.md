#### C++11
- **자동 타입 추론 (auto)**: 변수의 타입을 자동으로 추론합니다.
   ```
   auto x = 10; // x는 int 타입으로 추론됨
   ```
    
- **람다 표현식**: 익명 함수(람다)를 작성할 수 있습니다.
   ```
   auto add = [](int a, int b) { return a + b; };
   ```
- **범위 기반 for 루프**: 컬렉션을 반복하는 새로운 방법.
   ```
   for (int x : v) {     // v는 std::vector<int>와 같은 컬렉션 }
   ```
- **스마트 포인터**: `std::unique_ptr`과 `std::shared_ptr`을 통해 메모리 관리가 쉬워졌습니다.
   ```
   std::unique_ptr<int> p(new int(10));
   ```
- **rvalue 참조 및 이동 시맨틱**: 성능 향상을 위해 객체의 이동을 지원합니다.
    ```
    std::vector<int> v1 = {1, 2, 3}; std::vector<int> v2 = std::move(v1); // v1의 내용을 v2로 이동
    ```

#### C++14
- 제너릭 람다: 람다 표현식에서 템플릿 사용 가능.
```
auto add = [](auto a, auto b) { return a + b; };
```
- 이중 변수 선언: 변수 선언 시 중복을 줄임.
```
int x = 5;
decltype(x) y = 10; // y는 int 타입
```
- std::make_unique: std::unique_ptr의 안전한 생성.
```
auto p = std::make_unique<int>(10);
```
#### C++17
- 구조적 바인딩: 복합 타입을 더 간단하게 다룰 수 있습니다.
```
std::tuple<int, double> t(1, 2.3);
auto [i, d] = t; // i는 1, d는 2.3
```
- if 초기화 문: if 문에서 초기화를 지원.
```
if (int x = foo(); x > 0) {
    // x 사용 가능
}
```
- std::optional: 값이 존재할 수도 있고 없을 수도 있는 타입.
```
std::optional<int> opt = 5;
if (opt) {
    // opt가 값을 가짐
}
```
#### C++20
- 코루틴: 비동기 프로그래밍을 지원.
```
std::future<int> async_add(int a, int b) {
    co_return a + b;
}
```
- 개념 (Concepts): 템플릿 파라미터의 요구사항을 명시.
```
template<typename T>
concept Addable = requires(T a, T b) {
    { a + b } -> std::convertible_to<int>;
};
```
- 범위 (Ranges): 더 간결하고 읽기 쉬운 범위 기반 알고리즘.
```
std::vector<int> v = {1, 2, 3, 4};
auto result = v | std::views::filter([](int i) { return i % 2 == 0; });
```
- 우주선 연산자 (<=>): 세 가지 비교를 한 번에 처리하는 연산자.
```
auto result = (a <=> b); // a가 b보다 작으면 < 0, 같으면 == 0, 크면 > 0
```