# Subjects : B157

shops, vegetables = list(map(int, input().split()))
price_list_shop = [list(map(int, input().split())) for _ in range(shops)]

cart_list = [[0] * shops for _ in range(vegetables)]

for i in range(vegetables):
    for j in range(shops):
        cart_list[i][j] = price_list_shop[j][i] # make taples by vegetable

sum = 0
count = 0
shop = set()

for i in range(vegetables):
    vegi = min(cart_list[i])
    for j in range(shops):
        if cart_list[i][j] == vegi:
            shop.add(j)
print(len(shop))
