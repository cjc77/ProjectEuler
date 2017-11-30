#############################################
# The arithmetic used in sum_of_mults       #
# is derived from: n/2 * ( 2a + d(n-1) )    #
# the arithmetic series summation formula   #
# where a = "first term", d = "step"        #
# and n = " number of terms to sum"         #
# To find n: (N - 1) / d                    #
#############################################

def sum_of_mults(N):
    # Find n, n = (N - 1) / step
    n3 = (N - 1) // 3
    n5 = (N - 1) // 5
    n15 = (N - 1) // 15
    # Hang on to the sum
    tot = 0

    # Use arithmetic series summation formula
    # n/2 * ( 2a + d(n-1) )

    # Count mults of 3
    tot += (n3 * (6 + 3 * (n3 - 1))) // 2
    # Count mults of 5
    tot += (n5 * (10 + 5 * (n5 - 1))) // 2
    # Subtract mults of 15 i.e. mults of 3 and 5
    tot -= (n15 * (30 + 15 * (n15 - 1))) // 2
    print(tot)


def main():
    T = int(input().strip())
    for i in range(T):
        sum_of_mults(int(input().strip()))


if __name__ == '__main__':
    main()
