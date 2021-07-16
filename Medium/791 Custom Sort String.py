class Solution:
    def customSortString(self, order: str, str: str) -> str:
        ans=""
        string=list(str)

        for char in order:
            if char in string:
                # if there are some duplicate chars 
                while char in string:
                    string.remove(char)
                    ans+=char

        return ans+''.join(string)
