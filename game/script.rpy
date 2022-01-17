define e = Character("Eileen")
default ITEMS = {}
default Item = {}
default inventory = Inventory() 


label start:

    scene bg room
    show eileen happy

    call item_loader 

    $ inventory.clear()
    $ inventory.add_item(Item.money, 1000)
    $ inventory.add_item(Item.banana, 10)

    show screen inventory_button
    show screen tool_tip_window

    "HELLO???"

    e "Once you add a story, pictures, and music, you can release it to the world!"

    return