- 코드
```cpp
#inlucde <stdio.h>

int main(int argc, char* argv[])
{
	int i;
	for (int i = 0; i < argc; i++)
		fputws(grgv[i], stdout);
	return 0;
}
```