# Project 3

For the email confirmation to work this environment variable needs to be set
export EMAIL_HOST_PASSWORD="testing321"

To use the app register and then login. At which point items can be added to the cart.

models.py contains all the menu components, such that the individual building blocks can be modified by an Admin

orders.js contains logic to handle dependant dropdowns for a Pizza and to show options for particular Subs

If there are items in the cart the user can confirm at which point they are sent an email.

Site admins can view orders by navigating to Carts in the admin page

