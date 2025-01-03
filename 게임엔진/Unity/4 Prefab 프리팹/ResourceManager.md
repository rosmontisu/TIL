##### 코드상에서 프리팹을 컨트롤하는 방법
- 매니저에는 아래 3가지 기능을 만들어준다.
	- Load
	- Instatiate
	- Destory
```cs
using UnityEngine;

public class PrefabTest : MonoBehaviour
{
    GameObject prefab;

    GameObject tank;
    void Start()
    {
        prefab = Resources.Load<GameObject>("Prefabs/Tank"); // 1. Load
        tank = Instantiate(prefab);                          // 2. Instantiate
        Destroy(tank, 3.0f);                                 // 3. Destroy
                                                             // 위 3개의 인터페이스를 manager에서 제공해보자
    }
}
```

##### 매니저에서 인터페이스를 만들어보자
- 이때 public T Load<T>(string path) where T : Object{}
	- 와 같이 Generic문법을 사용하는데...
	- where T : Object로 Generic에 Object제약을 줄거면 그냥
	- public Object Load(string path) 와 같이 만들면 되는거 아닌가?
- 만약 Object형을 반환하도록 메서드를 짜버리면..
	- 실 사용시 아래와 같이 형 변환을 해줘야 하는 등 여러 문제가 발생
- 또한, 유니티의 모든 객체는 UnityEngine.Object를 상속받으므로 상관없다
```cs
Object obj = ResourceManager.Load("Textures/MyTexture");
Texture myTexture = (Texture)obj;  // 캐스팅 필요
```
```cs
using UnityEngine;

public class RosourceManager : MonoBehaviour
{
    // 1. Load 기능 
    // 지정된 path에서 리소스를 로드 후, return 해준다.
    public T Load<T>(string path) where T : Object
    {
        return Resources.Load<T>(path);
    }

    // 2. Instantiate 기능
    public GameObject Instantiate(string path, Transform parent = null)
    {
        // 파일 구조에 따라 달라집니다.
        GameObject prefab = Load<GameObject>($"Prefabs/{path}");
        if (prefab == null)
        {
            Debug.Log($"Failed to load prefab : {path}");
            return null;
        }
        return Object.Instantiate(prefab, parent);
    }

    // 3. Destroy 기능 
    public void Destroy(GameObject obj)
    {
        if (obj == null)
            return;

        Object.Destroy(obj);
    }
}


```