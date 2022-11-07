from src.models.item_model import ItemModel
from src.repositories.item_repository import ItemRepository

class ItemService(object):
    repository: ItemRepository = ItemRepository()
    
    def __init__(self) -> None:
        pass
    
    def get(self):
        return self.repository.get()
    
    def create(self, item: ItemModel):
        self.repository.create(item)
        return item