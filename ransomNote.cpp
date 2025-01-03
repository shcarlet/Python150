class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char,int>hashh;
        for(char c : magazine)
        {
            hashh[c]++;
        }

        for(char c: ransomNote)
        {
            if(hashh[c]<=0)
            {
                return false;
            }
            hashh[c]--;

            
        }
        return true;
    }
};
