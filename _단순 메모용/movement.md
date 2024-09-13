- CharacterContoller 컴포넌트로 편하게 구현 가능
- 2d처럼 직접 구현할 필요 x
```css
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    // 이동 속도를 조절하는 변수
    public float speed = 6.0f;
    // 중력 적용을 위한 변수
    public float gravity = -9.81f;
    // 점프 힘을 조절하는 변수
    public float jumpHeight = 1.0f;

    // CharacterController 컴포넌트를 저장하는 변수
    private CharacterController controller;
    // 현재 속도를 저장하는 변수
    private Vector3 velocity;
    // 바닥에 있는지 여부를 판단하는 변수
    private bool isGrounded;

    void Start()
    {
        // CharacterController 컴포넌트 가져오기
        controller = GetComponent<CharacterController>();
    }

    void Update()
    {
        // 바닥에 닿아 있는지 확인
        isGrounded = controller.isGrounded;

        if (isGrounded && velocity.y < 0)
        {
            // 바닥에 있으면 y축 속도 초기화
            velocity.y = -2f;
        }

        // 플레이어의 입력을 받아 이동 방향 설정
        float x = Input.GetAxis("Horizontal");
        float z = Input.GetAxis("Vertical");

        // 입력을 바탕으로 이동 방향 벡터 계산
        Vector3 move = transform.right * x + transform.forward * z;

        // CharacterController를 사용해 이동
        controller.Move(move * speed * Time.deltaTime);

        // 점프 입력 처리
        if (Input.GetButtonDown("Jump") && isGrounded)
        {
            velocity.y = Mathf.Sqrt(jumpHeight * -2f * gravity);
        }

        // 중력 적용
        velocity.y += gravity * Time.deltaTime;

        // y축 방향으로 이동 적용
        controller.Move(velocity * Time.deltaTime);
    }
}

```