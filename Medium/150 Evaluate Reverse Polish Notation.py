class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        
        for token in tokens:
            if stack and token in '-+*/':
                num1=stack.pop()
                num2=stack.pop()
                stack.append(str(int(eval(num2+token+num1))))

            else:
                stack.append(token)
        return stack[-1]
