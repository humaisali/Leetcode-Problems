class Solution {
public:
    using ll = long long;
    static constexpr ll LIMIT = 2000000; // safely above max possible k (1e6)

    // Exact (or capped-at-LIMIT) count of distinct multiset permutations
    // of `freq`, with NO heap allocation.
    ll countWays(const array<int,26>& freq) {
        ll ans = 1;
        int used = 0;
        for (int f : freq) {
            if (f == 0) continue;
            int n = used + f;
            ll c = 1;
            for (int i = 1; i <= f; i++) {
                c = c * (n - f + i) / i;      // always exact: C(n-f+i, i)
                if (c > LIMIT) { c = LIMIT; break; } // monotone -> safe to cap
            }
            ans *= c;
            if (ans > LIMIT) return LIMIT;    // monotone -> safe to bail early
            used += f;
        }
        return ans;
    }

    string smallestPalindrome(string s, int k) {
        array<int,26> cnt{};
        for (char ch : s) cnt[ch - 'a']++;

        array<int,26> half{};
        string mid;
        int halfLen = 0;
        for (int i = 0; i < 26; i++) {
            half[i] = cnt[i] / 2;
            halfLen += half[i];
            if (cnt[i] & 1) mid.push_back(char('a' + i));
        }

        ll kk = k;
        if (countWays(half) < kk) return "";

        string left;
        left.reserve(halfLen);
        for (int pos = 0; pos < halfLen; pos++) {
            for (int c = 0; c < 26; c++) {
                if (half[c] == 0) continue;
                half[c]--;
                ll ways = countWays(half);
                if (ways >= kk) {
                    left.push_back(char('a' + c));
                    break;
                }
                kk -= ways;
                half[c]++;
            }
        }

        string right = left;
        reverse(right.begin(), right.end());
        return left + mid + right;
    }
};