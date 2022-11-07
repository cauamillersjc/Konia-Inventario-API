from datetime import datetime

from src.models.item_model import ItemModel

class ItemRepository(object):
    _items = []
    
    def __init__(self) -> None:
        pass
    
    def get(self):
        return self._items
    
    def create(self, item: ItemModel):
        item.id += len(self._items)
        item.created_at = datetime.today()
        self._items.append(item)