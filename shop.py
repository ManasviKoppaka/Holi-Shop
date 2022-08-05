def insert(user,user_list):
    customer = {}
    db = open("customer.txt", "r")
    for i in db:
        u,p = i.split(":")
        customer[u]=p


    products = []
    for i in user_list:
        product = []
        product.append(i[0])
        product.append(i[2])
        products.append(product)
    strProducts = "["
    for i in products:
        strProduct="["+str(i[0])+","+str(i[1])+"],"
        strProducts+=strProduct
    strProducts+="]"
    ustrproducts = f"{user}:{strProducts}"

    flag = 0
    for i in customer.keys():
        if i == user:
            customer[i]+=ustrproducts
            flag = 1
    if flag == 0:
        customer[user]=ustrproducts


    db = open("customer.txt", "w")
    for i in customer.keys():
        record = f"{i}:{customer[i]}"
        db.write(record)
    db.close()