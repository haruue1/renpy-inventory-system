from dataclasses import dataclass


@dataclass
class Generic:
    id: str
    display_name: str
    quest_item: bool
    description: str


@dataclass
class Food(Generic):
    health_increase: int
