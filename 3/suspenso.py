def ins(e, ls):
    yield [e, *ls]
    if ls:
        for i in ins(e, ls[1:]):
            yield [ls[0], *i]

def take(n, it):
    if n == 0:
        yield []
    else:
        while True:
            try:
                yield [next(it) for i in range(n)]
            except StopIteration:
                break

def misterio(ls):
    if ls:
        for m in take(len(ls)-1, misterio(ls[1:])):
            for i in ins(ls[0], m):
                for j in i:
                    yield j

if __name__ == "__main__":
    for m in misterio([1, 2, 3]):
        print(m)
