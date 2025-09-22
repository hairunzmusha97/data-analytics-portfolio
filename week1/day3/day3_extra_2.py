transactions = ["Apple","Banana","Apple","Milk","Banana","Orange","Milk","Apple"]
unique_items = set(transactions)
print(transactions)
print(f"Unique Items {unique_items}")

Item_count = {}

for items in transactions:
    if items in Item_count:
        Item_count[items] += 1
    else:
        Item_count[items] = 1

print(Item_count)
