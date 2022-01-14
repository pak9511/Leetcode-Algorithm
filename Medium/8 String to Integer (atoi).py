class Solution:
    def myAtoi(self, s: str) -> int:
        idx, sign, output = 0, 1,  ""
        
        s=s.lstrip()   # 1번. 왼쪽의 공백 제거     
        if idx < len(s) and (s[idx] == "-" or s[idx] == "+"): # 2번. 부호 확인 후 sign 변수에 담아둠
            sign = int(s[idx] + "1")
            idx += 1
        
        while idx < len(s) and s[idx].isdigit(): # 3번. 숫자만 output에 담아둠.
            output += s[idx]
            idx += 1
           
        output = sign * int(output or 0) # 4번. output이 공백이면 0을 반환하고, sign을 참고해 부호를 변경함.
        
        if output <= -2 ** 31: # 5번. output의 범위를 확인해 반환함.
            return -2 ** 31
        elif output >= 2**31 - 1:
            return 2 ** 31 -1
			
        return output
