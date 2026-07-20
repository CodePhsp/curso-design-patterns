from inventory_observer import InventoryObserver


class Inventory:
    
    def __init__(self):
        self._observers= []
        self.shelf = []
        
    
    def new_product(self, product: str):
        self.shelf.append(product)
        
        self._notify_observers()
        
        return self.shelf
    
    
    def add_observer(self, observer: InventoryObserver):
        self._observers.append(observer)
    
    
    def remove_observer(self, observer: InventoryObserver):
        self._observers.remove(observer)
    
    
    def _notify_observers(self):
        for observer in self._observers:
            observer.update(self.shelf)
    