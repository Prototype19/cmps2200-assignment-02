def iterate(f, x, a):
    """
    Params:
      f.....function to apply
      x.....return when a is empty
      a.....input sequence
    """
    #print('iterate: calling %s x=%s a=%s' % (f.__name__, x, a))
    if len(a) == 0:
        return x
    else:
        return iterate(f, f(x, a[0]), a[1:])

def reduce(f, id_, a):
    # print('a=%s' % a) # for tracing
#     print(id_)
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel
        return f(reduce(f, id_, a[:len(a)//2]),
                 reduce(f, id_, a[len(a)//2:]))

def plus(x, y):
    return x + y