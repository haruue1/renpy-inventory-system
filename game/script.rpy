init python:
    import json
    from items.factory import ItemFactory
    from items.item import Generic, Food
    from types import SimpleNamespace
    from inventory.inventory import Inventory

define e = Character("Eileen")
default ITEMS = {}
default Item = {}
default inventory = Inventory() 

screen inventory_window():
    frame:
        xpadding 10
        ypadding 10
        xalign 0.5
        yalign 0.1
        vbox:
            for inventory_item in inventory.get_items():
                textbutton "[inventory_item.item.display_name] - [inventory_item.quantity]":
                    action NullAction()
                    tooltip inventory_item.item.description

screen tool_tip_window():
    frame:
        xalign 1.0
        hbox:
            $tooltip = GetTooltip()
            if tooltip:
                text "[tooltip]"


screen inventory_button():
    hbox:
        textbutton "Inventory" action ToggleScreen("inventory_window")

label start:

    scene bg room
    show eileen happy

    call load_items

    $ inventory.clear()
    $ inventory.add_item(Item.money, 1000)
    $ inventory.add_item(Item.banana, 10)

    show screen inventory_button
    show screen tool_tip_window

    "HELLO???"

    e "Once you add a story, pictures, and music, you can release it to the world!"

    return

label load_items:
    python:
        data = json.load(renpy.file("items.json"))
        item_factory = ItemFactory()

        item_factory.register("generic", Generic)
        item_factory.register("food", Food)
        
        for item in data["items"]:
            ITEMS[item["id"]] = item_factory.create(item) 

        Item  = SimpleNamespace(**ITEMS)

    return
