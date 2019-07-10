import functools

# // purchaseItem(
# //   emptyUserCart,
# //   buyItem,
# //   applyTaxToItems,
# //   addItemToCart
# // )(user, {name: 'laptop', price: 50})

user = {
    "name":"Kim",
    "active":True,
    "cart":[],
    "purchases":[]
}


def add_item_to_cart(user,item):
    new_user = user_deep_clone(user)
    new_user["cart"] = [item]
    return new_user


def apply_tax_to_items(user):
    new_user = user_deep_clone(user)
    tax = 1.3
    for item in new_user["cart"]:
        item['price'] = item['price']*tax
    return new_user


def buy_item(user):
    new_user = user_deep_clone(user)
    new_user["purchases"] = user["cart"][:]
    return new_user

 
def empty_user_cart(user):
    new_user = user_deep_clone(user)
    new_user["cart"] = []
    return new_user


def user_deep_clone(user):
    new_user = user.copy()
    new_user["cart"] = user["cart"][:]
    new_user["purchases"] = user["purchases"][:]
    return new_user


def compose2(f, g):
    return lambda *a, **kw: f(g(*a, **kw))

def compose(*fs):
    return functools.reduce(compose2, fs)


purchase_item = compose(empty_user_cart,buy_item, apply_tax_to_items, add_item_to_cart)

print(purchase_item(user,{'name': 'laptop', 'price': 50}))
print(purchase_item(user,{'name': 'laptop2', 'price': 100}))
print(compose(empty_user_cart,buy_item, apply_tax_to_items, add_item_to_cart)(user,{'name': 'laptop3', 'price': 345}))


