from inventory import Inventory
from email_notification import EmailNotificaton
from sms_notification import SmsNotificaton


inventory = Inventory()


email = EmailNotificaton()
sms = SmsNotificaton()

inventory.add_observer(email)
inventory.add_observer(sms)

product = inventory.new_product('Papel A4')

print(product)

inventory.remove_observer(email)