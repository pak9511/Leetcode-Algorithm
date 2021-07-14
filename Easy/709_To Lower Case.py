class Solution:
    def toLowerCase(self, s: str) -> str:
        return ''.join([chr(ord(i)+32) if 64<ord(i)<96  else i for i in s])
