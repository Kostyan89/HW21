y = 0
x = 0


while True:
    word = input()
    if word == "up":
        y += 1
    elif word == "down":
        y -= 1
    elif word == "right":
        x += 1
    elif word == "left":
        x -= 1
    elif word == "stop":
        break
print(x,y)