from dataclasses import dataclass
from items.item import Generic


@dataclass
class InventoryItem:
    item: Generic
    quantity: int

    def __eq__(self, other):
        return True if self.item.id == other.id else False


class Inventory:
    def __init__(self):
        self._inventory_items: list[InventoryItem] = []

    def add_item(self, item: Generic, quantity: int) -> None:
        new_item = InventoryItem(item, quantity)
        self._inventory_items.append(new_item)

    def remove_item(self, item: Generic, quantity: int = 1) -> None:
        for inventory_item in self._inventory_items:
            if inventory_item.item == item:
                inventory_item.quantity -= quantity
                if inventory_item.quantity <= 0:
                    self._inventory_items.remove(inventory_item)

    def get_items(self) -> list[InventoryItem]:
        return self._inventory_items

    def clear(self) -> None:
        del self._inventory_items[:]
