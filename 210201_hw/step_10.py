def infinite_palindromes():
    pal_gen = infinite_palindromes()
    for i in pal_gen:
        print(i)
        digits = len(str(i))
        if digits == 5:
            pal_gen.close()
        pal_gen.send(10 ** (digits))