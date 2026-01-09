import random
import time
import json  # 用于演示文件操作


# --- 第1部分：类与面向对象 (Classes & OOP) ---
class Character:
    """所有角色的基类"""

    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_power = attack_power

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f" > {self.name} 受到了 {damage} 点伤害！剩余血量: {self.hp}/{self.max_hp}")


class Hero(Character):
    """玩家控制的英雄类，继承自Character"""

    def __init__(self, name):
        # 调用父类的初始化方法
        super().__init__(name, hp=100, attack_power=15)
        self.inventory = ["恢复药水", "强力药水"]  # 列表 (List)

    def heal(self):
        if self.inventory:
            potion = self.inventory.pop(0)  # 列表操作
            heal_amount = 30
            self.hp = min(self.hp + heal_amount, self.max_hp)
            print(f"✨ {self.name} 使用了 {potion}，恢复了 {heal_amount} 点血量！")
        else:
            print("❌ 背包空了，没有药水了！")


class Monster(Character):
    """怪物类"""

    def __init__(self, name, difficulty):
        hp = difficulty * 20
        atk = difficulty * 5
        super().__init__(name, hp, atk)


# --- 第2部分：函数与流程控制 (Functions & Control Flow) ---
def battle(hero, monster):
    print(f"\n🔥 遭遇战！{hero.name} VS {monster.name} 🔥")
    print("-" * 30)

    # while 循环
    while hero.is_alive() and monster.is_alive():
        print(f"\n当前状态: [{hero.name} HP:{hero.hp}] vs [{monster.name} HP:{monster.hp}]")
        action = input("你的行动？(1.攻击 2.治疗 3.逃跑): ")

        # if-elif-else 条件判断
        if action == "1":
            # 随机攻击力波动 (模块使用)
            dmg = random.randint(hero.attack_power - 2, hero.attack_power + 5)
            print(f"⚔️ 你发起了攻击！")
            monster.take_damage(dmg)
        elif action == "2":
            hero.heal()
        elif action == "3":
            print("🏃 你试图逃跑...")
            if random.random() > 0.5:
                print("成功逃脱！")
                return False  # 战斗未胜利，但结束了
            else:
                print("逃跑失败！被怪物绊倒了！")
        else:
            print("❓ 无效指令，浪费了一回合！")

        # 怪物回合
        if monster.is_alive():
            time.sleep(0.5)  # 模拟思考时间
            dmg = random.randint(monster.attack_power - 2, monster.attack_power + 2)
            print(f"👿 {monster.name} 发起了反击！")
            hero.take_damage(dmg)

    # 战斗结算
    if hero.is_alive():
        print(f"\n🎉 胜利！你击败了 {monster.name}！")
        return True
    else:
        print("\n💀 你被打败了... 游戏结束。")
        return False


# --- 第3部分：文件操作与异常处理 (Files & Exceptions) ---
def save_score(name, score):
    """将最高分记录保存到文件"""
    data = {"player": name, "score": score}  # 字典 (Dictionary)
    try:
        with open("score_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
        print("💾 游戏记录已保存。")
    except IOError:
        print("⚠️ 保存文件时出错！")


# --- 第4部分：主程序入口 ---
def main():
    print("欢迎来到 Python 练手大冒险！")
    player_name = input("请输入勇者的名字: ")
    player = Hero(player_name)

    monsters_list = ["史莱姆", "哥布林", "恶龙"]
    score = 0

    # 遍历列表生成敌人
    for i, m_name in enumerate(monsters_list):
        difficulty = i + 1
        enemy = Monster(m_name, difficulty)

        # 开始战斗
        victory = battle(player, enemy)

        if not victory and not player.is_alive():
            break  # 死了就跳出循环

        if victory:
            score += 100 * difficulty
            print("休息一下，继续前进...")
            time.sleep(1)

    print(f"\n🏁 冒险结束！最终得分: {score}")
    save_score(player_name, score)


if __name__ == "__main__":
    main()