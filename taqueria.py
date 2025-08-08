def main():
    cash = 0
    items = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    while True :
        try:
            x = input('Item: ').title()
            if x in items:
                cash += items[x]
                print('Total: $',f'{cash:.2f}',sep='')
        except:
            return main

main()
