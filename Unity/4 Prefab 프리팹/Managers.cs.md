```cs
using System.Resources;
using UnityEngine;

public class Managers : MonoBehaviour
{
    // Manager. 으로 이것저것 접근하도록 하기 위해서
    // 싱글톤 + 프로퍼티
    static Managers s_instance; // 유일성이 보장된다.
    static Managers Instance { get { Init(); return s_instance; } } // 유일한 매니저를 가져온다.

    // 이 아래로 우리가 만든 하위 매니져를 추가합니다.
    InputManager _input = new InputManager(); 
    ResourceManager _resource = new ResourceManager();

    public static InputManager Input { get { return Instance._input; } }
    public static ResourceManager Resource { get { return Instance._resource; } }

    void Start()
    {
        Init();
    }

    void Update()
    {
        _input.OnUpdate();
    }

    public static void Init()
    {
        GameObject go = GameObject.Find("@Managers");
        if (go == null)
        {
            go = new GameObject { name = "@Managers", tag = "Manager" };
            go.AddComponent<Managers>();
        }

        DontDestroyOnLoad(go);
        s_instance = go.GetComponent<Managers>();
    }
}
```