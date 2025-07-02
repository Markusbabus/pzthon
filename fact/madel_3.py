def sequence(c, z = 0):

    while True :
        yield z
        z = z ** 2 + c

def mandelbrot(candidate):
    return sequence(c = candidate, z = 0)

def julia(candidate, parameter):
    return sequence(c = parameter, z = candidate)