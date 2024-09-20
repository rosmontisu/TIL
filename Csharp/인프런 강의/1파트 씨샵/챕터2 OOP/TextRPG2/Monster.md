```cs
using System;

namespace CSharp
{
    public enum MonsterType
    {
        None = 0,
        Slime = 1,
        Orc = 2,
        Skeleton = 3
    }
    class Monster : Creature
    {
        protected MonsterType type = MonsterType.None;
        protected Monster(MonsterType type) : base(CreatureType.Monster)
        {
            this.type = type;
            
            int hp;
            int attack;
        }
        public MonsterType GetMonsterType() { return type; }
    }
    class Slime : Monster
    {
        public Slime() : base(MonsterType.Slime)
        {
            SetInfo(10, 1);
            this.type = MonsterType.Slime;
        }
    }
    class Orc : Monster
    {
        public Orc() : base(MonsterType.Orc)
        {
            SetInfo(20, 2);

            this.type = MonsterType.Orc;
        }
    }
    class Skeleton : Monster
    {
        public Skeleton() : base(MonsterType.Skeleton)
        {
            SetInfo(15, 5);
            this.type= MonsterType.Skeleton;
        }
    }
}


```