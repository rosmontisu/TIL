```cs
using System;
using UnityEngine;
using UnityEngine.EventSystems;

public class InputManager
{
    // delegate
    public Action KeyAction = null; // 이벤트로 변수를 전파해준다 - 리스너 패턴
    public Action<Define.MouseEvent> MouseAction = null; // 마우스 전용 액션 대리자
        // Action 대리자 헷갈릴때를 위한 설명
        // Define.MouseEvent 라는 enum 타입의 인수를 받고, void 형을 반환하는 메서드를
        // 대리자로 사용한다는 의미.
        // 이런식으로 관리하면 enum으로 나중에 필요한 부분을 쉽게 추가 가능

    bool _pressed = false; // 마우스의 입력 상태

    public void OnUpdate() // Monobehaviour 비상속이므로 Update -> OnUpdate
    {
        // UI에 클릭이 들어갔는지 검사
        if (EventSystem.current.IsPointerOverGameObject())
        { return; }

        if (Input.anyKey && KeyAction != null)
            KeyAction.Invoke(); // 키입력 True 전파(Invoke)

        // 마우스 이벤트 press와 click을 관리하는 인터페이스
        // 이 안에서 press, click 외에도 나중에 필요한걸 구현하면된다.
            // ex) 드래그라거나?
        if (MouseAction != null)
        {
            // 마우스를 입력하면
            if (Input.GetMouseButton(0))
            {
                MouseAction.Invoke(Define.MouseEvent.Press); // Press 이벤트 발생
                _pressed = true; // 마우스의 입력이 감지되었음
            }
            else // 그리고, 마우스를 떼면
            {
                if (_pressed) // 만약 한번이라도 press를 했다면? Click 이벤트 발생
                    MouseAction.Invoke(Define.MouseEvent.Click);
                _pressed = false;
            }
        }
    }   
}
```