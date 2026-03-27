import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for token in args:
        if ":" not in token:
            print(f"Error - invalid parameter '{token}'")
            continue
        name, qty_str = token.split(":", 1)
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        if not qty_str.isdigit():
            print(f"Quantity error for '{name}': invalid literal for int() with base 10: '{qty_str}'")
            continue

        inventory[name] = int(qty_str)

    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = parse_inventory(sys.argv[1:])

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items:", total_qty)

    for name, qty in inventory.items():
        percent = (qty * 100) / total_qty if total_qty > 0 else 0
        print(f"Item {name} represents {percent:.1f}%")

    if inventory:
        most_name = max(inventory, key=lambda k: inventory[k])
        least_name = min(inventory, key=lambda k: inventory[k])
        print(f"Item most abundant: {most_name} with quantity {inventory[most_name]}")
        print(f"Item least abundant: {least_name} with quantity {inventory[least_name]}")
    else:
        print("Item most abundant: none")
        print("Item least abundant: none")

    inventory["magic_item"] = 1
    print("Updated inventory:", inventory)

if __name__ == "__main__":
    main()
