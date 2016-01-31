class test:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def __eq__(self, instance):
        return instance.var1 == self.var1 and instance.var2 == self.var2

def main():
    a = test('foo', 1)
    b = test('bar', 2)
    c = test('foo', 1)

    print a == b
    print b == c
    print a == c

    alist = [a, b, c]
    print a in alist
    print ('foo', '1') in alist

main()
