from ecommerce.sales import calc_shipping, calc_tax # imports specific methods / objects

import ecommerce.sales # imports ENTIRE module as an object
# you can call by using sales.calc_tax()
# ecommerce.sales.calc_shipping()

calc_tax()

calc_shipping()