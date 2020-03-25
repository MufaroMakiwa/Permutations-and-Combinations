def gen_combinations(iterable, r):

    if r > len(iterable):
        return
    
    def generator(iterable, index = 0, length = 0):
    
        indices = range(index, len(iterable))
        if length == r:
            yield []
        else:
            for ind in indices:
                for other in generator(iterable, ind + 1, length + 1):
                    yield [iterable[ind]] + other
            
    return generator(iterable)

if __name__ == "__main__":
    combin1 = []
    # for comb in gen_combinations(list(range(50)), 8):
    #     combin1.append(tuple(comb))

    combin2 =[]
    import time
    start = time.time()
    for comb in combinations(list(range(30)), 10):
        # combin2.append(comb)
        print(comb)
    print(time.time() - start)

    # assert(combin1==combin2)


 