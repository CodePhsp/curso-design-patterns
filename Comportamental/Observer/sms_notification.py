from inventory_observer import InventoryObserver


class SmsNotificaton(InventoryObserver):
    
    def update(self, product: str):
        return print(f'SMS: {product} voltou ao estoque.')