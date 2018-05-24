products = [
    {'id':1,'name':'Apple','price':45000},
    {'id':2,'name':'Vivo','price':22000},
    {'id':3,'name':'Redmi','price':15000},
    {'id':4,'name':'Samsung','price':55000},
    {'id':5,'name':'Apple','price':85000},
    ]

p = input("Enter the product : ")
for data in products:
    if data['name'] == p:
        print(data)





        
