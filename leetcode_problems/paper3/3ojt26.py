
def is_iterator(l):
    if hasattr(l,'__iter__') and hasattr(l,'__next__'):
        return True
    else:
        return False
print(is_iterator(iter([1,2])))
print(is_iterator([1,2,3]))