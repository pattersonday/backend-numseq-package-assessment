from numseq.fib import fib
from numseq.geo import square, triangle, cubed
from numseq.prime import prime, is_prime

author = "pattersonday w/guidance from perrymw"


def main():
    print("Fibonacci")
    for i in range(0, 10):
        print("{}: {}".format(i, fib(i)))
    print("Geometric numbers (square, triangle, cube)")
    for i in range(10):
        print("{}: {} {} {}".format(i, square(i), triangle(i), cubed(i)))
    print("Primes")
    prime_list = prime(1000)
    for p in prime_list[-10:]:
        print(p)
    print("Is 999981 prime? {}".format(is_prime(999981)))
    print("Is 999983 prime? {}".format(is_prime(999983)))


if __name__ == "__main__":
    main()
