- 2d 화면에서 3d 오브젝트를 클릭하는 상황을 생각해보자.

#### TransformDirection()
- 로컬 좌표계에서 월드 좌표계로 변환하는데 사용한다.
- Physics.Raycast()로 raycast를 구현
	- Debug.DrawRay()로 raycast를 시각적으로 디버깅 가능
- Physics.RaycastAll() 을 사용하면 RaycastHit[] 형태로 여러개의 물체도 감지 가능
```cs
private void Update()
{
    // local space to world space
    Vector3 look = transform.TransformDirection(Vector3.forward); 

    Debug.DrawRay(transform.position + Vector3.up, look * 10, Color.red);

    RaycastHit[] hitInfos;
    hitInfos = Physics.RaycastAll(transform.position, Vector3.forward, 10);

    foreach (RaycastHit hit in hitInfos)
    {
        Debug.Log($"Raycast : {hit.collider.gameObject.name}");
    }
}
```
- 여러가지로 응용이 가능한 기능
	- 예시로, 와우나 파판같은 TPS시점의 게임에서 카메라와 플레이어 사이의 벽이 있는 경우
	- 레이케스트로 카메라와 유저 사이의 물체가 있는지 검사하는 방식으로도 구현 가능