
# 클래스 선언 / 상품명 - codetree, 상품코드 - 50 (초기화)
class product():
    def __init__ (self,product_item="codetree",product_code=50):
        self.product_item = product_item
        self.product_code = product_code

product_output = product()
print(f"product {product_output.product_code} is {product_output.product_item}")

product_item_new, product_code_new = tuple(input().split())
product_code_new = int(product_code_new)
product_new = product(product_item_new,product_code_new)
print(f"product {product_new.product_code} is {product_new.product_item}")