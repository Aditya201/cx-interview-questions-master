import math
import locale

class ShoppingCart(object):


    #Price catalogue for the existing products
    catalogue={"Baked_Beans":0.99,"Biscuits":1.20,"Sardines":1.89,"Shampoo_Small":2.00,"Shampoo_Medium":2.50,"Shampoo_Large":3.50}

    # Offer products catalogue to make sure only listed products comes under offer.(For new offers)
    offer_catalogue ={"Shampoo_Large","Shampoo_Medium","Shampoo_Small"}

    # Both the catalogues be created by reading file data instead of hard-coding

    #Setting the locale for GBP representation

    locale.setlocale( locale.LC_ALL, 'en_GB.UTF-8' )
    
    def __init__(self):
        self.total = 0
        self.items = dict()
        self.sub_total=0
        self.discount=0

    # Function to add items in the item dictionary

    def add_item(self, item_name, quantity):
        if item_name != None and quantity >= 1:
            self.items.update({item_name: quantity})
    
    # Round off function to round up the digit 5 after 0. values
    # If the value is 0.945 then python round(0.945,2) returns 0.94
    # Below function is to fix the above issue

    def round_off(self,n, d=0):
        m = 10 ** d
        return math.ceil(n * m) / m


    # Calculation of sub total, discount and total amounts with normal ofers on Baked_Beans and Sardines

    def calculate(self):
        for item_name, quantity in self.items.items():
            price=self.catalogue[item_name]
            
            # Clculation of sub total amounts

            if quantity:
                self.sub_total += (quantity * price)

            # Discount calculation for Baked_Beans and Sardines 

            # This logic is to implement buy 2 get 1 offer on Baked_Beans
            if item_name=="Baked_Beans" and quantity:
                self.discount+= int(quantity/3)*price

            # This logic is to implement 25% discount on Sardines
            elif item_name=="Sardines" and quantity:
                self.discount+=quantity*price*0.25

        self.sub_total = self.round_off(self.sub_total,2)
        self.discount = self.round_off(self.discount,2)
        self.total = self.round_off(self.sub_total - self.discount,2)

    # Calculation of sub total, discount and total amounts for buy three get lowest cost item for free offer

    def calculate_with_new_offer(self):
        
        total_qty=0 #total quantity if the quantity doesn't exceed multiple of 3 for single item
        offer_price =0

        # Iterate through the whole dictionary of Items

        for item_name, quantity in self.items.items():
            price = self.catalogue[item_name]
            
            #Calculation Offer price at the beginning of each iteration to select the lower cost

            offer_price = price if offer_price==0 else min(price,offer_price)

            # Clculation of sub total amounts

            if quantity:
                self.sub_total += (quantity * price)

            # Discount calculation if the product present in offer catalogue(Defined above)
            # Re-calculation of total_qty depending on quantity of one item

            if(item_name in self.offer_catalogue):

                # Calculate discount of the same item if the quantity is 3+ and count rest in total items
                # The implementation is by assuming that the offer is "Buy 3 get lowest cost product free"
                
                if(quantity>2):
                    self.discount+= int(quantity/3)*price
                    total_qty += quantity-int(quantity/3)*quantity

                else:
                    total_qty += quantity
                    
                # Discount calculation if total quantity already exceeds 2
                if(total_qty>2):
                    self.discount += int(total_qty/3)*offer_price
                    total_qty -= int(total_qty/3)*total_qty

        self.sub_total = self.round_off(self.sub_total,2)
        self.discount = self.round_off(self.discount,2)
        self.total = self.round_off(self.sub_total - self.discount,2)



    # To create a dictionary of Sub_total, discount and total for for first offer of buy 2 Baked Beans get 1 free 
    # and 25% off on Sardines
    
    # In place of dictionary this can be represented as per requirement

    def generate_bill(self):
        self.calculate()
        return {"sub_total":locale.currency(self.sub_total),"discount":locale.currency(self.discount),"total":locale.currency(self.total)}

    # To create a dictionary of Sub_total, discount and total for for second offer of buy 3 Shampoo get the 
    # low cost one for free 
    
    # In place of dictionary this can be represented as per requirement

    def generate_bill_with_new_offer(self):
        self.calculate_with_new_offer()
        return {"sub_total":locale.currency(self.sub_total),"discount":locale.currency(self.discount),"total":locale.currency(self.total)}

    # Remove items function for the scenario if someone wants to remove any item
    
    def remove_item(self, item_name, quantity):
        try:
            if item_name in self.items and quantity >= self.items[item_name]:
                self.items.pop(item_name, None)
            self.items[item_name] -= quantity
        except(KeyError, RuntimeError):
            pass

    # Checkout function after payment

    def checkout(self, cash_paid):
        balance = 0
        if cash_paid < self.sub_total:
            return "Cash paid not enough"
        balance = cash_paid - self.sub_total
        return balance

# The class to add, remove items and to calcuate the bill amounts and to call checkout function after payment
class Shop(ShoppingCart):

    def __init__(self):
        self.quantity = 100
