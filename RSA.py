from flask import Flask, request
import random
import math

app = Flask(__name__)


def prime_generator(end):
    for n in range(900, end):     # n starts from 2 to end
        for x in range(2, n):   # check if x can be divided by n
            if n % x == 0:      # if true then n is not prime
                break
        else:                   # if x is found after exhausting all values of x
            yield n             # generate the prime

@app.route('/')
def index():
    dict = {' ':27,'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    text = request.form.get('text')
    g = prime_generator(random.randint(900,10000))
    j1 = (list(g)[-3:-1])
    j2 = j1[0]
    j3 = j1[1]
    n = j3 * j2
    jh = (j3-1)*(j2-1)
    e = 1
    while jh%e == 0:
        e = random.randint(1,10)
    k = random.randint(0,10)
    d = int((k * jh + 1) / e)
    val = ""
    for i in text:
        vall = str(dict[i.lower()])

        val = val + vall
    val = int(val)

    CC = int(math.pow(val,e)%n)

    return str(CC)



if __name__ == '__main__':
    app.debug = True
    app.run()