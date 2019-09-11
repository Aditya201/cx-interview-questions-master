# Shopping Basket

## Requirements

You have been asked to implement a "shopping basket" pricing library for a supermarket.

This is a component which if given a "basket" of products chosen by a customer, a "catalogue" of products available in a supermarket and a list of special offers, can calculate the price of goods including any applicable discounts. In other words, the basket component is responsible for working out which offers are applicable to products and applying those offers to work out the final price. 

This is to be a component of a much bigger system. It could be used in a number of different ways by other developers, for example in an online-shop or in the supermarket's cash-registers. For this reason, it needs to be designed to be reusable. 

For any given basket, catalogue and offers your solution should return the sub-total, discount and total, all accurate to at least two decimal places. Prices can be returned as floating point numbers. 

### Definitions

* **sub-total**: The undiscounted cost of items in a basket.
* **discount**: The amount of money which must be subtracted from the subtotal in order to calculate the final price of the goods in the basket.
* **total**: The final price of goods in the basket once the discount has been applied.
* **offers**: These are pricing rules which under some circumstances may cause one or more items in the basket to be discounted, and consequently change the final price of the basket. 
* **catalogue**: The products currently sold by the supermarket. This component requires that products have a unique name and a price. At minimum, the catalogue maps product names onto non-discounted prices.

### Behavior

* A basket can contain zero or more products.
* A basket is mutable - that is to say products an be added to it.
* An empty basket has a sub-total, discount and total each of zero.
* Baskets cannot have a negative price.
* The discount and therefore the total price is determined by the contents of the basket, the undiscounted price of the goods and the applicable offers.
* As with all supermarkets, the prices of goods and the offers applicable to those goods may change from day to day and therefore cannot be hard-coded into this component.
* Catalogue and offers are maintained by two different teams. It's possible that there are offers on products which are no longer in the catalogue. It's also possible that there are items in the catalogue with no offers, or multiple offers.

#### Other considerations

* We are only interested in the behavior of the shopping basket pricer component. You do not need to build an API, web-interface or database. Try to stay focused on implementing the shopping basket, and especially the part which figures out which offers are applicable to a given basket.
* You can use 3rd party components if you think it will be helpful, for example in your testing. Use the included Pipfile to identify any dependencies your component needs. 
* Provide some documentation that will help us run your submission. You can put your documentation in [the readme file](./readme.md)
* You can assume all prices are in £GBP, no need to consider any other currencies. 
* For this exercise, a floating point number is good enough to represent a money value, but if you have a better way to represent money, feel free to use it.

### Catalogue

This is an example catalogue, provided as a demonstration:

* **Baked Beans** £0.99
* **Biscuits** £1.20
* **Sardines** £1.89
* **Shampoo (Small)** £2.00
* **Shampoo (Medium)** £2.50
* **Shampoo (Large)** £3.50

## Examples

Examples of what would be expected for a couple of different baskets...

### Offers

The supermarket currently has these offers:

* ***Baked Beans***: buy 2 get 1 free
* ***Sardines***: 25% discount

### Basket 1

* Baked Beans x 4
* Biscuits x 1

Should give the results:

* sub-total: £5.16
* discount: £0.99
* total: £4.17

### Basket 2

* Baked Beans x 2
* Biscuits x 1
* Sardines x 2

Should give:

* sub-total: £6.96
* discount: £0.95
* total: £6.01

## Bonus Question 1

The supermarket wants to implement a new kind of offer: "Buy N of {X}, get the cheapest one for free", where N is a number of products that must be bought, and {X} is a subset of products from the catalogue that this offer is applicable to.

The supermarket is keen that the discounts should be applied fairly, so the rule must be interpreted to calculate the maximum possible discount given the set of applicable chosen products. This is complicated by the fact that a user may buy any number of products from the set {X}.

### Example

The Supermarket currently has the following offer:

Buy three, get the cheapest one for free with any of the following:

* Shampoo (Large)
* Shampoo (Medium)
* Shampoo (Small)

Given that the basket contains:

* Shampoo (Large) * 3
* Shampoo (Medium) x 1
* Shampoo (Small) x 2

Should give:

* sub-total: £17.0
* discount: £5.5
* total: 11.5

The customer has got 1 large and 1 small shampoo for free.

