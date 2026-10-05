
def rev_count(n):
    if n == 0:
        return
    print(n)
    rev_count(n-1)
rev_count(10)
