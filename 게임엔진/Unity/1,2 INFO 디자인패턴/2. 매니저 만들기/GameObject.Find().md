```cs
using System.Collections;
using System.Collections.Generic;

using UnityEngine;

public class Player : MonoBehaviour
{
    void Start()
    {
	    // 1. Scene에 포함된 GameObject 중에서 @managers를 찾기
        GameObject go = GameObject.Find("@Managers");
        // 2. @Managers GameObject안에 Component중에서 Managers 찾기
        Managers mg = go.GetComponent<Managers>();
    }

    void Update()
    {
        
    }
}
```
- 단, 이런식으로 직접 GameObject.Find()시 부하가 심함
- 싱글톤 패턴을 활용해보자.