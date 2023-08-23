# Create your own exception
class LargeError(Exception):
    def __init__(self):
        pass

    def __str__(self) -> str:
        return 'Error:Invalid Marks'

def percentage(marks):
    if marks<=600:
        print((marks/600)*100)
    else:
        raise LargeError()

try:
    percentage(100)
    percentage(600)
    percentage(700)
except LargeError as e:
    print(e)