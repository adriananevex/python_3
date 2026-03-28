import math

Point3D = tuple[float, float, float]


def distance_3d(p1: Point3D, p2: Point3D) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def get_player_pos(prompt: str) -> Point3D:
    while True:
        coord_str = input(prompt)
        parts = coord_str.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        try:
            x, y, z = [float(p.strip()) for p in parts]
            return (x, y, z)
        except ValueError as e:
            for p in parts:
                try:
                    float(p.strip())
                except ValueError:
                    print(
                        f"Error on parameter '{p.strip()}': "
                        f"cound not convert string to float: '{p.strip()}'")


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    prompt = "Enter new coordinates as floats in format 'x,y,z': "
    first_pos = get_player_pos(prompt)
    print(f"Got a first tuple: {first_pos}")
    print(f"It includes: X={first_pos[0]}, Y={first_pos[1]}, Z={first_pos[2]}")

    center = (0.0, 0.0, 0.0)
    dist_to_center = distance_3d(first_pos, center)
    print(f"Distance to center: {round(dist_to_center, 4)}")
    print()
    print("Get a second set of coordinates")
    second_pos = get_player_pos(prompt)

    dist_between = distance_3d(first_pos, second_pos)
    print(
        "Distance between the 2 sets of coordinates: "
        f"{round(dist_between, 4)}"
    )


if __name__ == "__main__":
    main()
