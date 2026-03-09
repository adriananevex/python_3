def game_event_stream(n):
    players = ("alice", "bob", "charlie", "diana", "eve")
    types = ("killed monster", "found treasure", "leveled up")

    i = 0
    while i < n:
        player = players[i % len(players)]
        level = (i * 7) % 20 + 1
        event_type = types[(i * 3) % len(types)]
        yield (i + 1, player, level, event_type)
        i += 1


def fibonacci_stream():
    a = 0
    b = 1
    while 1:
        yield a
        tmp = a + b
        a = b
        b = tmp


def prime_stream():
    n = 2
    while 1:
        d = 2
        is_prime = 1
      while d* d <= n:
          if n % d == 0:
              is_prime = 0
              break
          d += 1

      if is_prime == 1:
          yield n
      n += 1


def main():
    n = 1000

    print("=== Game Data Stream Processor ===")
    print("Processing", n, "game events...")

    total_events = 0
    high_level = 0
    treasure_events = 0

    for event in game_event_stream(n):
        event_id = event[0]
        player = event[1]
        level = event[2]
        event_type = event [3]

        if event_id <= 3:
            print("Event", event_id, ": Player", player, "(level", level, ")", event_type)
            if event_id == 3:
                print("...")

        total_events += 1
        if level >= 10:
            high_level += 1
        if event_type == "found treasure":
            treasure_events += 1
        if event_type == "leveled up":
            level_up_events += 1

    print("=== Stream Analytics ===")
    print("Total events processed:", total_events)
    print("High-level players (10+):", high_level)
    print("Treasure events:", treasure_events)
    print("Level-up events:", level_up_events)
    print("Memory usage: Constant (streaming)")
    print("Processing time: (not measured)")
    print("Processing time: (not measured)")

    print("=== Generator Demonstration ===")

    fib = iter(fibonacci_stream())
    print("Fibonacci sequence (first 10):", end=" ")
    i = 0
    while 1 < 10:
        v = next(fib)
        if i == 9:
            print(v)
        else:
            print(v, end=" ")
        i += 1


if __name__ == "__main__":
    main()
