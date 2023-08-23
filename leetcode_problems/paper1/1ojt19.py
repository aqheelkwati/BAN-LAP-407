def trafficcolor(func):
    def message():
        color=input("Enter the color of traffic signal:").lower()
        if color in ("red","yellow","green"):
            func(color)
        else:
            print("invalid color")
    return message

@trafficcolor
def trafficsignal(color):
    if color=="red":
        print("STOP")
    elif color=="yellow":
        print("SLOW DOWN")
    else:
        print("GO")

trafficsignal()