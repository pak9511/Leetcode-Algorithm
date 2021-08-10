class Solution {
    public String addStrings(String num1, String num2) {
        String ans =new String();
        int i1=num1.length()-1;
        int i2=num2.length()-1;
        int carry = 0;
        int ascii='0';
        while (i1>=0 | i2>=0 | carry >0){
            if (i1>=0) {
                int i1Num=num1.charAt(i1);
                carry+=i1Num-ascii;
                i1--;
            }
            if (i2>=0){
                int i2Num=num2.charAt(i2);
                carry+=i2Num-ascii;
                i2--;
            }
            int tmp=(carry%10)+ascii;
            ans+=Character.toString(tmp);
            carry/=10;
        }
        return ( new StringBuffer(ans) ).reverse().toString();
    }
}
