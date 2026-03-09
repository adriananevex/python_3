def main() -> None:
    print("=== Game Analytics Dashboard ===")

    players = [
        {
            "name": "alice",
            "score": 2300,
            "active": True,
            "region": "north",
            "achievements": [
                "first_kill",
                "level_10",
                "boss_slayer",
                "treasure_hunter",
                "speed_runner",
            ],
        },
        {
            "name": "bob",
            "score": 1800,
            "active": True,
            "region": "east",
            "achievements": ["first_kill", "level_10", "helper"],
        },
        {
            "name": "charlie",
            "score": 2150,
            "active": True,
            "region": "central",
            "achievements": [
                "first_kill",
                "boss_slayer",
                "collector",
                "explorer",
                "level_10",
                "pvp_win",
                "veteran",
            ],
        },
        {
            "name": "diana",
            "score": 20250,
            "active": False,
            "region": "north",
            "achievements": ["first_kill", "explorer"],
        },
    ]

    print("=== List Comprehension Examples ===")

    high_scores = [p["name"] for p in players if p["score"] > 2000]
    print("High scores (>2000):", high_scores)

    scores_doubled = [p["score"] * 2 for p in players]
    print("Scores doubled:", scores_doubled)

    active_players = [p["name"] for p in players if p["active"]]
    print("Active players:", active_players)

    print("=== Dict Comprehension Examples ===")

    player_scores = {p["name"]: p["score"] for p in players}
    print("Player scores:", player_scores)

    score_categories = {
        "high": len([p for p in players if p["score"] >= 2100]),
        "medium": len([p for p in players if 1900 <= p["score"] < 2100]),
        "low": len([p for p in players if p["score"] < 1900]),
    }
    print("Score categories:", score_categories)

    achievement_counts = {p["name"]: len(p["achievements"]) for p in players}
    print("Achievement counts:", achievement_counts)

    print("=== Set Comprehension Examples ===")

    unique_players = {p["name"] for p in players}
    print("Unique players:", unique_players)

    unique_achievements = {a for p in players for a in p["achievements"]}
    print("Unique achievements:", unique_achievements)

    active_regions = {p["region"] for p in players if p["active"]}
    print("Active regions:", active_regions)

    print("=== Combined Analytics ===")

    total_players = len(players)
    print("Total players:", total_players)

    total_unique_achievements = len(unique_achievements)
    print("Total unique achievements:", total_unique_achievements)

    scores = [p["score"] for p in players]
    avg_score = sum(scores) / len(scores)
    print("Average score:", avg_score)

    top_player = max(players, key=lambda p: p["score"])
    print(
        "Top performer:",
        top_player["name"],
        "(",
        top_player["score"],
        "points,",
        len(top_player["achievements"]),
        "achievements)",
    )


if __name__ == "__main__":
    main()
