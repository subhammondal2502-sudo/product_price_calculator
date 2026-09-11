#product price calculator......
product_name=input(" product name with model numbers : ")
original_price=float(input(" original price of your product : "))
discount=float(input("discount percentage : "))
discount_amount = original_price * discount / 100
final_price = original_price - discount_amount
print("product name :", product_name)
print("discount amount :", discount_amount)
print("final price :", final_price)
if final_price>=5000:
    print("category : premium product ")
elif final_price>=2000:
    print("category : mid range product")
