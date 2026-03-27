import random
from typing import Generator, Tuple

def gen_event() -> Generator[Tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "jump", "sleep", "grab", "move", "climb", "swim", "release", "use"]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(events: list[Tuple[str, str]]) -> Generator[Tuple[str, str], None, None]:
    while events:
        index = random.randrange(len(events))
        yield events.pop(index)


def main():
    print("=== Game Data Stream Processor ===")
    
    event_gen = gen_event()
    
    for i in range(1000):
        player, action = next(event_gen)
        print(f"Event {i}: Player {player} did action {action}")
    
    event_list = [next(event_gen) for _ in range(10)]
    print("Built list of 10 events:", event_list)
    
    for e in consume_event(event_list):
        print("Got event from list:", e)
        print("Remains in list:", event_list)


if __name__ == "__main__":
    main()
