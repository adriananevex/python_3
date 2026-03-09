import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for token in args:
        if ":" not in token:
            continue
        name, qty_str = token.split(":", 1)
        if not name:
            continue
        if not qty_str.isdigit():
            continue

        qty = int(qty_str)
        current = inventory.get(name, 0)
        inventory.update({name: current + qty})

    return inventory


def main() -> None:
    inventory = parse_inventory(sys.argv[1:])

    print("=== Inventory System Analysis ===")

    total_items = 0
    for qty in inventory.values():
        total_items += qty

    print("Total items in inventory:", total_items)
    print("Unique item types:", len(inventory.keys()))

    print("=== Current Inventory ===")
    ordered_items = sorted(
        inventory.items(),
        key=lambda entry: entry[1],
        reverse=True,
    )
    for name, qty in ordered_items:
        percentage = 0.0
        if total_items > 0:
            percentage = (qty * 100) / total_items
        print(f"{name}: {qty} units ({percentage: .1f}%)")

    print("=== Inventory Statictics ===")
    if len(inventory) > 0:
        most_name = None
        most_qty = -1
        least_name = None
        least_qty = None

        for name, qty in inventory.items():
            if qty > most_qty:
                most_name = name
                most_qty = qty
            if least_qty is None or qty < least_qty:
                least_name = name
                least_qty = qty

        print(f"Most abundant: {most_name} ({most_qty} units)")
        print(f"Least abundant: {least_name} ({least_qty} units)")
    else:
        print("Most abundant: none")
        print("Least abundant: none")

    print("=== Item Categories ===")
    categories = {
        "Abundant": {},
        "Moderate": {},
        "Scarce": {},
    }

    for name, qty in inventory.items():
        if qty >= 8:
            categories["Abundant"].update({name: qty})
        elif qty >= 5:
            categories["Moderate"].update({name: qty})
        else:
            categories["Scarce"].update({name: qty})

    for category_name, category_items in categories.items():
        if len(category_items) > 0:
            print(f"{category_name}: {category_items}")

    print("=== Management Suggestions ===")
    restock_needed = []
    for name, qty in inventory.items():
        if qty <= 1:
            restock_needed.append(name)
    print("Restock needed:", restock_needed)

    print("=== Dictionay Properties Demo ===")
    print("Dictionary keys:", list(inventory.keys()))
    print("Dictionary values:", list(inventory.values()))
    print("Sample lookup - sword' in inventory:", "sword" in inventory)


if __name__ == "__main__":
    main()
