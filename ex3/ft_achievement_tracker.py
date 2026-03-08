def main() -> None:
    print("=== Achievement Tracker System ===")

    alice = {
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demion",
    }
    bob = {
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector",
    }
    charlie = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfeccionist",
    }

    print("Player alice achievements:", alice)
    print("Player bob achievements:", bob)
    print("Player charlie achievements:", charlie)

    print("=== Achievement ANalytics ===")

    all_unique = alice.union(bob).union(charlie)
    print("All unique achievements:", all_unique)
    print("Total unique achievements:", len(all_unique))

    common_all = alice.intersection(bob).intersection(charlie)
    print("Common to all players:", common_all)

    alice_unique = alice.difference(bob.union(charlie))
    bob_unique = bob.difference(alice.union(charlie))
    charlie_unique = charlie.difference(alice.union(bob))
    rare = alice_unique.union(bob_unique).union(charlie_unique)
    print("Rare achievements (1 player):", rare)

    alice_bob_common = alice.intersection(bob)
    print("Alice vs Bob common:", alice_bob_common)

    print("Alice unique:", alice.difference(bob))
    print("Bob unique:", bob.difference(alice))


if __name__ == "__main__":
    main()
