1. 나한테 RigidBody가 있어야 한다. (IsKinematic : Off)
2. 나한테 collider가 있어야 한다. (IsTrigger : Off)
3. 상대한테 Collider가 있어야 한다. (IsTrigger : Off)
- TestCollision.cs
```cs
using UnityEngine;

public class TestCollision : MonoBehaviour
{
    // 실제 물리적인 충돌 (피격 판정 등..)

    // 1. 나 혹은 상대한테 RigidBody (IsKinematic : Off)
    // 2. 나한테 Collider (IsTrigger : Off)
    // 3. 상태한테 Collider (Istrigger : Off)
    private void OnCollisionEnter(Collision collision)
    {
        Debug.Log($"collision : @{collision.gameObject.name}");
    }
    
    // 범위 판단 등..
    
    // 1. 둘 다 Collider
    // 2. 둘 중 하나 이상 IsTrigger : On
    // 3. 둘 중 하나 이상 RigidBody
    private void OnTriggerEnter(Collider other)
    {
        Debug.Log($"Trigger @{other.gameObject.name} !");
    }
}

```

#### Trigger
![[Pasted image 20241116104019.png]]
- Rigidbody
	- IsTrigger = True
	- 유니티에서의 물리 엔진을 적용 시키지 않음.
- Collider의 물리적인 충돌은 부하가 상당하므로 존재하는 기능
- 응용방안이 상당히 많다
	- (단, 장판 스킬의 판단 등은 싱글베이스 게임이 아닌경우 서버에서 수학적으로 처리가 필요)
	- (물론 싱글 게임에서는 트리거로 처리하는것도 나쁘지 않음)
- .