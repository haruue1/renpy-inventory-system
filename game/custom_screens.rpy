
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