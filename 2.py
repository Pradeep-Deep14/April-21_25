fruit_stores={'apple':{'store1':1.0,'store2':1.5},
              'banana':{'store1':2.0,'store2':1.8}
}

#Need to write a Python function that takes inner dictionary lowest value and returns the outer dictionary key

#Example: {'apple':{'store1':1.0,'store2':1.5}} --> store1
#Example: {'banana':{'store1':2.0,'store2':1.8}} --> store2


def get_store_with_lowest_price(fruit_stores):
    result = {}
    for fruit, stores in fruit_stores.items():
        min_store = min(stores, key=stores.get)
        result[fruit] = min_store
    return result
print(get_store_with_lowest_price(fruit_stores))