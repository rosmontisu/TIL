1. 나한테 RigidBody가 있어야 한다. (IsKinematic : Off)
2. 나한테 collider가 있어야 한다. (IsTrigger : Off)
3. 상대한테 Collider가 있어야 한다. (IsTrigger : Off)
- TestCollision.cs
```cs
using UnityEngine;

public class TestCollision : MonoBehaviour
{
    private void OnCollisionEnter(Collision collision)
    {
        Debug.Log("Collision !");
    }

    private void OnTriggerEnter(Collider collider)
    {
        Debug.Log("Collider !");
    }
}

```