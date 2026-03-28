import random


def main():
    print("=== Game Data Alchemist ===")

    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]
    print("Initial list of players:", players)

    all_capitalized = [p.capitalize() for p in players]
    print("New list with all names capitalized:", all_capitalized)

    only_capitalized = [p for p in players if p[0].isupper()]
    print("New list of capitalized names only:", only_capitalized)

    score_dict = {p: random.randint(50, 1000) for p in all_capitalized}
    print("Score dict:", score_dict)

    avg_score = sum(score_dict.values()) / len(score_dict)
    print("Score average is {:.2f}".format(avg_score))

    high_scores = {k: v for k, v in score_dict.items() if v > avg_score}
    print("High scores:", high_scores)


if __name__ == "__main__":
    main()
