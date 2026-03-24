import random

def gen_player_achievements(all_achievements: list[str]) -> set[str]:
    """Gera um conjunto aleatório de achievements para um jogador"""
    num = random.randint(3, len(all_achievements))
    return set(random.sample(all_achievements, num))

def main():
    print("=== Achievement Tracker System ===")

    all_achievements = [
        "Crafting Genius", "World Savior", "Master Explorer", "Collector Supreme",
        "Untouchable", "Boss Slayer", "Strategist", "Speed Runner", "Survivor",
        "Treasure Hunter", "First Steps", "Sharp Mind", "Unstoppable", "Hidden Path Finder"
    ]

    players = ["Alice", "Bob", "Charlie", "Dylan"]

    player_achievements = {}

    for player in players:
        player_achievements[player] = gen_player_achievements(all_achievements)
        print(f"Player {player}: {player_achievements[player]}")

    all_distinct = set().union(*player_achievements.values())
    print("All distinct achievements:", all_distinct)

    common = set.intersection(*player_achievements.values())
    print("Common achievements:", common)

    for player in players:
        others = set().union(*(v for k, v in player_achievements.items() if k != player))
        unique = player_achievements[player].difference(others)
        print(f"Only {player} has:", unique)

    for player in players:
        missing = all_distinct.difference(player_achievements[player])
        print(f"{player} is missing:", missing)

if __name__ == "__main__":
    main()