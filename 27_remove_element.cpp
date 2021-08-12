class Solution {
public:
    int removeElement(vector<int>& a, int val) {
        int n = a.size();
        int k = 0;

        for (int i = 0; i < n; i++)
        {
            if (a[i] != val)
            {
                a[k] = a[i];
                k++;
            }
        }
        return k;
    }
};
