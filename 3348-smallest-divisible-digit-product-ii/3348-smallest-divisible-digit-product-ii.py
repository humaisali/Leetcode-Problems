from collections import Counter

class Solution:
    DIGIT_FACTORS = {d: Counter() for d in range(10)}
    DIGIT_FACTORS[2] = Counter({2: 1})
    DIGIT_FACTORS[3] = Counter({3: 1})
    DIGIT_FACTORS[4] = Counter({2: 2})
    DIGIT_FACTORS[5] = Counter({5: 1})
    DIGIT_FACTORS[6] = Counter({2: 1, 3: 1})
    DIGIT_FACTORS[7] = Counter({7: 1})
    DIGIT_FACTORS[8] = Counter({2: 3})
    DIGIT_FACTORS[9] = Counter({3: 2})
    PRIMES = (2, 3, 5, 7)

    def _sub(self, a, b):
        return {p: max(0, a.get(p, 0) - b.get(p, 0)) for p in self.PRIMES}

    def _is_subset(self, need, have):
        return all(have.get(p, 0) >= v for p, v in need.items())

    def _factor_count(self, need):
        c2, c3, c5, c7 = need.get(2, 0), need.get(3, 0), need.get(5, 0), need.get(7, 0)
        n8, r2 = divmod(c2, 3)
        n9, n3 = divmod(c3, 2)
        n4, n2 = divmod(r2, 2)
        if n2 == 1 and n3 == 1:
            n2, n3, n6 = 0, 0, 1
        else:
            n6 = 0
        if n3 == 1 and n4 == 1:
            n2, n6, n3, n4 = 1, 1, 0, 0
        return {2: n2, 3: n3, 4: n4, 5: c5, 6: n6, 7: c7, 8: n8, 9: n9}

    def _construct(self, fac):
        return ''.join(str(d) * fac.get(d, 0) for d in range(2, 10))

    def _total(self, fac):
        return sum(fac.values())

    def smallestNumber(self, num: str, t: int) -> str:
        need, tt = {}, t
        for p in self.PRIMES:
            cnt = 0
            while tt % p == 0:
                tt //= p
                cnt += 1
            need[p] = cnt
        if tt != 1:
            return "-1"

        n = len(num)
        base_fac = self._factor_count(need)
        if self._total(base_fac) > n:
            return self._construct(base_fac)

        prime_prefix = {2: 0, 3: 0, 5: 0, 7: 0}
        for ch in num:
            for p, v in self.DIGIT_FACTORS[int(ch)].items():
                prime_prefix[p] += v

        first_zero = num.find('0')
        if first_zero == -1:
            first_zero = n
            if self._is_subset(need, prime_prefix):
                return num

        for i in range(n - 1, -1, -1):
            d = int(num[i])
            for p, v in self.DIGIT_FACTORS[d].items():
                prime_prefix[p] -= v
            space = n - 1 - i
            if i > first_zero:
                continue
            for bigger in range(d + 1, 10):
                needed = self._sub(self._sub(need, prime_prefix), self.DIGIT_FACTORS[bigger])
                fac = self._factor_count(needed)
                if self._total(fac) <= space:
                    fill = space - self._total(fac)
                    return num[:i] + str(bigger) + '1' * fill + self._construct(fac)

        fac = self._factor_count(need)
        return '1' * (n + 1 - self._total(fac)) + self._construct(fac)