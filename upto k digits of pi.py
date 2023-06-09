import math
def pi(k):
    if k==0:
        return 3
    def sqrt(n, one):

        floating_point_precision = 10**16
        n_float = float((n * floating_point_precision) // one) / floating_point_precision
        x = (int(floating_point_precision * math.sqrt(n_float)) * one) // floating_point_precision
        n_one = n * one
        while 1:
            x_old = x
            x = (x + n_one // x) // 2
            if x == x_old:
                break
        return x

    def pi_chudnovsky_bs(digits):

        C = 640320
        C3_OVER_24 = C**3 // 24
        def bs(a, b):

            if b - a == 1:
                # Directly compute P(a,a+1), Q(a,a+1) and T(a,a+1)
                if a == 0:
                    Pab = Qab = 1
                else:
                    Pab = (6*a-5)*(2*a-1)*(6*a-1)
                    Qab = a*a*a*C3_OVER_24
                Tab = Pab * (13591409 + 545140134*a) # a(a) * p(a)
                if a & 1:
                    Tab = -Tab
            else:
                # Recursively compute P(a,b), Q(a,b) and T(a,b)
                # m is the midpoint of a and b
                m = (a + b) // 2
                # Recursively calculate P(a,m), Q(a,m) and T(a,m)
                Pam, Qam, Tam = bs(a, m)
                # Recursively calculate P(m,b), Q(m,b) and T(m,b)
                Pmb, Qmb, Tmb = bs(m, b)
                # Now combine
                Pab = Pam * Pmb
                Qab = Qam * Qmb
                Tab = Qmb * Tam + Pam * Tmb
            return Pab, Qab, Tab
        # how many terms to compute
        DIGITS_PER_TERM = math.log10(C3_OVER_24/6/2/6)
        N = int(digits/DIGITS_PER_TERM + 1)
        # Calclate P(0,N) and Q(0,N)
        P, Q, T = bs(0, N)
        one = 10**digits
        sqrtC = sqrt(10005*one, one)
        return (Q*426880*sqrtC) // T

    digits = k
    pi = pi_chudnovsky_bs(digits)
    return(pi)
