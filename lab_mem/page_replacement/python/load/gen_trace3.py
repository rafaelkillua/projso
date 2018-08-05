from random import randint

n_refs = 1000000
n_pages = 1500000

for i in range(n_refs):
    number = randint(0, n_pages)
    n_mode = randint(0, 1)
    print number, "r" if n_mode == 0 else "w"
