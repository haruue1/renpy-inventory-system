from typing import Any
from items.item import Generic


class ItemFactory:
    def __init__(self):
        self._registered_items: dict[str, Generic] = {}

    def register(self, item_type: str, item_creation_func: Generic) -> None:
        self._registered_items[item_type] = item_creation_func

    def unregister(self, item_type: str) -> None:
        del self._registered_items[item_type]

    def create(self, args: dict[str, Any]) -> Generic:
        args_copy = args.copy()
        item_type = args_copy.pop("type", None)
        try:
            item_creation_func = self._registered_items[item_type]
            return item_creation_func(**args_copy)
        except KeyError:
            raise ValueError(f"Uknown type {item_type!r}")
