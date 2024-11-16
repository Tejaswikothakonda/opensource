x = int(input())
discount_1 = x * 0.10
discount_2 = 100
maximum_discount = max(discount_1, discount_2)
amt = x - maximum_discount
print(int(amt))
