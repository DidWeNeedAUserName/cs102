#from __future__ import annotations

#from typing import TYPE_CHECKING

#from common import util
#from common.event import EventType, GameEvent
#from common.types import COLLECTABLE_TYPES
from entities.movable_entity import MovableEntity
#from entities.player_inventory import PlayerInventory
#from worlds import world

needed_items_cnt = 3
class Bullet(MovableEntity):
    def __init__(self, damage, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.damage = damage
        #if world.player.count_inventory(COLLECTABLE_TYPES) >= needed_items_cnt:
            #self.damage = damage + 50