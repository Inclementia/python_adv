def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1

    pal_gen = infinite_palindromes()
    for i in pal_gen:
        digits = len(str(i))
        pal_gen.send(10 ** (digits))