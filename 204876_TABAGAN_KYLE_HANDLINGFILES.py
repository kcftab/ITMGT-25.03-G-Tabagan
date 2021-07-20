products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    return products[code]

def get_property(code,property):
    return get_product(code)[property]

def main():
    total = 0
    orderdict = {
        "americano":{"quantity":0},
        "brewedcoffee":{"quantity":0},
        "cappuccino":{"quantity":0},
        "dalgona":{"quantity":0},
        "espresso":{"quantity":0},
        "frappuccino":{"quantity":0},
    }
    while True:
        code = input("Input the order code or type '/' to exit. ")
        if code == "/":
            print("Receipt will now be printed.")
            break
        elif code == "americano" or code == "brewedcoffee" or code == "cappuccino" or code == "dalgona" or code == "espresso" or code == "frappuccino":
            orderdict[code]["quantity"] += 1
        else:
            print("Please enter a valid input.")
    
    
    with open("receipt.txt.","w") as f:
        f.write('''
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL
''')
        for code in list(orderdict.keys()):
            if orderdict[code]["quantity"] > 0:
                f.write(code+"\t\t")
                f.write(get_property(code,"name")+"\t\t")
                f.write(str(orderdict[code]["quantity"])+"\t\t\t\t")
                f.write(str(get_property(code,"price")*orderdict[code]["quantity"])+"\n")
                total += get_property(code,"price")*orderdict[code]["quantity"]
        
        f.write(f'''

Total:\t\t\t\t\t\t\t\t\t\t{total}
==
''')

main()