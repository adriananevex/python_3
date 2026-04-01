import sys


def parse_inventory(args):
    inventory = {}

    for token in args:
        if ":" not in token:
            print(f"Error - invalid parameter '{token}'")
            continue

        name, qty_str = token.split(":", 1)

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            qty = int(qty_str)
        except ValueError:
            print(
                f"Quantity error for '{name}': "
                f"invalid literal for int() with base 10: '{qty_str}'"
            )
            continue

        inventory[name] = qty

    return inventory


def main():
    print("=== Inventory System Analysis ===")

    inventory = parse_inventory(sys.argv[1:])

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")

    for name in inventory:
        qty = inventory[name]
        percent = (qty * 100) / total_qty if total_qty > 0 else 0
        print(f"Item {name} represents {percent:.1f}%")

    if inventory:
        most_name = None
        least_name = None

        for name in inventory:
            if most_name is None or inventory[name] > inventory[most_name]:
                most_name = name

            if least_name is None or inventory[name] < inventory[least_name]:
                least_name = name

        print(
            f"Item most abundant: {most_name} "
            f"with quantity {inventory[most_name]}"
        )
        print(
            f"Item least abundant: {least_name} "
            f"with quantity {inventory[least_name]}"
        )
    else:
        print("Item most abundant: none")
        print("Item least abundant: none")

    inventory.update({"magic_item": 1})
    print("Updated inventory:", inventory)


if __name__ == "__main__":
    main()
