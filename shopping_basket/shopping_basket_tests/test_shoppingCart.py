import unittest
from shoppingCart import ShoppingCart
from shoppingCart import Shop


class ShoppingCartTestCases(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()
        self.shop = Shop()

    # To test the code when selected Items are Baked_Beans 4 and Biscuits 1 with present offer

    def test_basket1(self):

        Basket1 = {"Baked_Beans":4,"Biscuits":1}

        expected_bills = {"sub_total":"£5.16","discount":"£0.99","total":"£4.17"}

        # Adding the basket items using add_item finctions
        for item_name, quantity in Basket1.items():
            self.cart.add_item(item_name,quantity)

        # Calling the function to calculate the bill with current offer 

        actual_bills = self.cart.generate_bill()

        self.assertDictEqual(actual_bills, expected_bills)

    # To test the code when selected Items are Baked_Beans 2 , Biscuits 1 and Sardines 2 with present offer 

    def test_basket2(self):

        Basket2 = {"Baked_Beans":2,"Biscuits":1,"Sardines":2}

        expected_bills = {"sub_total":"£6.96","discount":"£0.95","total":"£6.01"}

        # Adding the basket items using add_item finctions
        for item_name, quantity in Basket2.items():
            self.cart.add_item(item_name,quantity)

        # Calling the function to calculate the bill with current offer 
        
        actual_bills = self.cart.generate_bill()

        self.assertDictEqual(actual_bills, expected_bills)

    # Test case for the offer of low cost items for free when total items selected are more than three
    def test_basket3(self):

        Basket3 = {"Shampoo_Large":3,"Shampoo_Medium":1,"Shampoo_Small":3}

        expected_bills = {"sub_total":"£19.00","discount":"£5.50","total":"£13.50"}

        # Adding the basket items using add_item finctions
        for item_name, quantity in Basket3.items():
            self.cart.add_item(item_name,quantity)

        # Calling the function to calculate the bill with offer "Buy 3 get lowest cost product free"

        actual_bills = self.cart.generate_bill_with_new_offer()

        self.assertDictEqual(actual_bills, expected_bills)

if __name__ == "__main__":
    unittest.main()

