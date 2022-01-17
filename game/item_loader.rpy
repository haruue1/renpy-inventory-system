label item_loader:
    python:
        data = json.load(renpy.file("items.json"))
        item_factory = ItemFactory()

        item_factory.register("generic", Generic)
        item_factory.register("food", Food)
        
        for item in data["items"]:
            ITEMS[item["id"]] = item_factory.create(item) 

        Item  = SimpleNamespace(**ITEMS)

    return