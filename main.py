import json
from datetime import datetime

while True:
    choice = int(input("\n1.Add Items 2.Sell 3.Exit : "))

    if choice == 1:
        fd = open("record.json", 'r')
        r = fd.read()
        fd.close()
        record = json.loads(r)
        new = {}
        id = str(input("\nEnter product id : "))
        name = str(input("Enter product's name : "))
        p = float(input("Enter product's price : "))
        q = int(input("Enter product's quantity : "))

        new[id] = {'name': name, 'price': p, 'quantity': q}

        for i in new:
            if str(i) in record:
                new[i]['quantity'] += record[str(i)]['quantity']
                record.update({str(i): new[i]})
            else:
                record[i] = new[i]
        print("\nItem added Successfully!!!\n")
        js = json.dumps(record)
        fd = open("record.json", 'w')
        fd.write(js)
        fd.close()

    elif choice == 2:
        fd = open("record.json", 'r')
        r = fd.read()
        fd.close()
        sell_record = json.loads(r)
        fd1 = open("sales.json", 'r')
        r1 = fd1.read()
        fd1.close()
        sales_record = json.loads(r1)
        new_sale={}
        check={}

        s_id = str(input("\nEnter product id : "))
        s_q = int(input("Enter product's quantity : "))
        check[s_id]={'quantity': s_q}
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        for i in check:
            if str(i) in sell_record:

                if s_q<=sell_record[s_id]['quantity']:

                    print("\nProduct: ", sell_record[s_id]['name'])
                    print("Price: ", sell_record[s_id]['price'])
                    print("Billing Amount: ", sell_record[s_id]['price']*s_q)
                    print("Date and Time =", dt_string)
                    print("Thanks for shopping!!\n")

                    new_sale[dt_string] = {'product_id': s_id, 'name': sell_record[s_id]['name'], 'quantity': s_q, 'price': sell_record[s_id]['price']*s_q}

                    for i in new_sale:
                        if str(i) in sales_record:
                            new_sale[i]['quantity'] += sales_record[str(i)]['quantity']
                            sales_record.update({str(i): new_sale[i]})
                        else:
                            sales_record[i] = new_sale[i]
                    js1 = json.dumps(sales_record)
                    fd1 = open("sales.json", 'w')
                    fd1.write(js1)
                    fd1.close()

                    sell_record[s_id]['quantity'] = sell_record[s_id]['quantity'] - s_q

                    js = json.dumps(sell_record)
                    fd = open("record.json", 'w')
                    fd.write(js)
                    fd.close()

                elif s_q>sell_record[s_id]['quantity']:
                    print(f'Sorry! The asked quantity is not available. Max quantity available is {sell_record[s_id]["quantity"]}')


            else:
                print("Sorry! Product not available\n")

    elif choice == 3:
        exit()

    else:
        print("\nChoose correct choice!!!!")