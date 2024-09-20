```cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharp
{
    public enum CreatureType
    {
        None,
        Player = 1,
        Monster = 2
    }
    class Creature
    {
        CreatureType type;
        protected Creature(CreatureType type)
        {
            this.type = type;
        }
        protected int _hp = 0;
        protected int _attack = 0;

        public void SetInfo(int hp, int attack)
        {
            this._hp = hp;
            this._attack = attack;
        }

        public int GetHp() { return _hp; }
        public int GetAttack() { return _attack; }

        public bool IsDead() { return _hp <= 0; }

        public void OnDamaged(int damage)
        {
            _hp -= damage;
            if (_hp < 0) 
                _hp = 0;
        }
    }
}

```