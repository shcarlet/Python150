class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int i=digits.size()-1;
       while(i<=digits.size()-1)
        {
            if(digits[i]!=9)
            {
                digits[i]++;
                return digits;
            }
            else
            {
                digits[i]=0;
                
            }
            i--;
            
        }
        digits.push_back(0);
        digits[0]=1;
        return digits;
    }
};
