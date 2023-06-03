from wtforms import Form, BooleanField, StringField, PasswordField, validators
#
# Users/Customer table:


class Customer:
    pass


# Products table:
class Products:
    pass


# Categories table:
class Categories:
    pass


# Orders table:
class Orders:
    pass


# Order Items table:
class Items:
    pass


# Wishlist table:
class Wishlist:
    pass


# Reviews table:
class Reviews:
    pass


# Shopping Cart table:
class Shopping:
    pass


# Payments table:
class Payments:
    pass


# Coupons/Promotions table:
class Coupons:
    pass

#
# Users/Customer table: Stores information about registered users/customers, including their name, email, password,
# shipping address, billing address, and contact information.
#
# Products table: Stores information about the jewelry products available for sale, including attributes such as
# product ID, name, description, price, quantity in stock, and image URL.
#
# Categories table: Stores information about the different categories or types of jewelry products available,
# such as necklaces, earrings, bracelets, etc. This table helps organize and classify products.
#
# Orders table: Stores information about the orders placed by customers, including attributes like order ID,
# customer ID, order date, shipping details, and order status.
#
# Order Items table: A junction table that connects the Orders table and Products table. It stores information about
# the products included in each order, such as the product ID, quantity ordered, and the price at the time of purchase.
#
# Wishlist table: Stores information about products that customers have added to their wishlist for future reference
# or purchase.
#
# Reviews table: Stores customer reviews and ratings for specific products. This table may include attributes such as
# review ID, product ID, customer ID, review content, and rating.
#
# Shopping Cart table: Stores temporary information about the items a customer has added to their shopping cart,
# including the product ID, quantity, and any applied discounts.
#
# Payments table: Stores information about the payment transactions made by customers, including payment ID,
# order ID, payment method, transaction details, and payment status.
#
# Coupons/Promotions table: Stores information about available coupons or promotional offers, including coupon codes,
# discount percentages, expiry dates, and any restrictions or conditions.
#

