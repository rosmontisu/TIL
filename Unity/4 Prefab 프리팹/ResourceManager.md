##### 코드상에서 프리팹을 컨트롤하는 방법
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
```cs
using UnityEngine;

public class ResourceManager : MonoBehaviour
{
    public T Load<T>(string path) where T : Object
    {
        return Resources.Load<T>(path);
    }

    public GameObject Instantiate(string path, Transform parent = null)
    {
        GameObject prefab = Load<GameObject>($"Prefabs/{path}");
        if (prefab == null)
        {
            Debug.Log($"Failed to load prefab : {path}");
            return null;
        }

        return Object.Instantiate(prefab, parent);
    }

    public void Destroy(GameObject obj)
    {
        if (obj == null)
        {
            return;
        }

        Object.Destroy(obj);
    }
}

```