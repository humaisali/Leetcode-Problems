class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        const int MAXX = 2048;

        bitset<MAXX> present;
        for (int x : nums)
            present.set(x);

        bitset<MAXX> pair;

        // All possible XORs of two values present in the array
        for (int a = 0; a < MAXX; a++) {
            if (!present[a]) continue;
            for (int b = 0; b < MAXX; b++) {
                if (present[b])
                    pair.set(a ^ b);
            }
        }

        bitset<MAXX> ans;

        // XOR each pair XOR with every value present
        for (int x = 0; x < MAXX; x++) {
            if (!pair[x]) continue;
            for (int a = 0; a < MAXX; a++) {
                if (present[a])
                    ans.set(x ^ a);
            }
        }

        return ans.count();
    }
};