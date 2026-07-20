from inventory_observer import InventoryObserver


class EmailNotificaton(InventoryObserver):
    
    def update(self, product: str):
        return print(f'Email: {product} voltou ao estoque.')