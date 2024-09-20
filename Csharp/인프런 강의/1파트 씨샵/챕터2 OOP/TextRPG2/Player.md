```cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharp
{
    public enum PlayerType
    {
        None = 0,
        Knight = 1,
        Archer = 2,
        Mage = 3
    }
    class Player : Creature
    {
        // 플레이어의 속성 (attribute)
        // 직업, 체력, 공격력
        protected PlayerType _type = PlayerType.None;
        protected int _hp = 0;
        protected int _attack = 0;
        
        // 자식에서 base로 부모의 생성자를 호출하며 상속받는 문법
        // 이런식으로 구현하지 않으면?
        // 자식에서 type이 없는 Player객체를 만들 가능성이 존재함
        protected Player(PlayerType type) : base(CreatureType.Player)
        {
            _type = type;
        }


        // 플레이어의 메서드
        // 초기 정보 설정
        public void SetInfo(int hp, int attack)
        {
            this._hp = hp;
            this._attack = attack;
        }

        // 반환 메서드
        // 직업/체력/공격력/생사여부
        public PlayerType GetPlayerType() { return _type; }
        public int GetHp() { return _hp; }
        public int GetAttack() { return _attack; }
        public bool IsDead() { return _hp <= 0; }

        // 피격판정
        public void OnDamaged(int damage) 
        {
            _hp -= damage;
            if (_hp < 0) _hp = 0;
        }
    }

    class Knight : Player
    {
        public Knight() : base(PlayerType.Knight) // 부모의 생성자를 호출
        {
            SetInfo(100, 10);
        }
    }

    class Archer : Player
    {
        public Archer() : base(PlayerType.Archer) 
        {
            SetInfo(75, 12);
        }
    }

    class Mage : Player
    {
        public Mage() : base(PlayerType.Mage)
        {
            SetInfo(50, 15);
        }
    }
}
```