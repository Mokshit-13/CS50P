def main():
    txt = input('camelCase: ')
    print(snake(txt))

def snake(txt):
    snake = ''
    for char in txt:
        if char.isupper():
            if snake:
                snake += '_'
                snake += char.lower()
        else:
            snake += char
    return snake

main()
