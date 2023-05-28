def median(pool):
    copy = sorted(pool)
    size = len(copy)
    if size % 2 == 1:
        return copy[int((size - 1) / 2)]
    else:
        return (copy[int(size/2 - 1)] + copy[int(size/2)]) / 2
class Stock():
    def __init__(self, name, price):
        self.name = name
        self.price = price

if __name__ == '__main__':
    test = Stock("sam", 25)
    print(test.price)
    median(25)
    Stock()

    asdf