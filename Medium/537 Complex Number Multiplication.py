{\rtf1\ansi\ansicpg949\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Monaco;}
{\colortbl;\red255\green255\blue255;\red238\green182\blue49;\red29\green30\blue26;\red255\green255\blue255;
\red143\green175\blue54;\red47\green173\blue251;\red243\green79\blue40;\red242\green68\blue154;}
{\*\expandedcolortbl;;\cssrgb\c94902\c75686\c24706;\cssrgb\c15294\c15686\c13333;\cssrgb\c100000\c100000\c100000;
\cssrgb\c62353\c72941\c27059;\cssrgb\c21176\c73725\c98824;\cssrgb\c97255\c40000\c20392;\cssrgb\c96863\c38039\c66667;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 class\cf4 \strokec4  Solution\cf5 \strokec5 :\cf4 \strokec4 \
    def \cf6 \strokec6 complexNumberMultiply\cf4 \strokec4 (self, num1\cf5 \strokec5 :\cf4 \strokec4  str, num2\cf5 \strokec5 :\cf4 \strokec4  str) \cf5 \strokec5 ->\cf4 \strokec4  str\cf5 \strokec5 :\cf4 \strokec4 \
        \cf7 \strokec7 A\cf5 \strokec5 =\cf4 \strokec4 re.\cf6 \strokec6 sub\cf4 \strokec4 (\cf8 \strokec8 '[^0-9-]'\cf4 \strokec4 ,\cf8 \strokec8 " "\cf4 \strokec4 ,num1).\cf6 \strokec6 split\cf4 \strokec4 ()\
        \cf7 \strokec7 B\cf5 \strokec5 =\cf4 \strokec4 re.\cf6 \strokec6 sub\cf4 \strokec4 (\cf8 \strokec8 '[^0-9-]'\cf4 \strokec4 ,\cf8 \strokec8 " "\cf4 \strokec4 ,num2).\cf6 \strokec6 split\cf4 \strokec4 ()\
 \
        \cf2 \strokec2 return\cf4 \strokec4  \cf6 \strokec6 str\cf4 \strokec4 (\cf6 \strokec6 eval\cf4 \strokec4 (\cf7 \strokec7 A\cf4 \strokec4 [\cf7 \strokec7 0\cf4 \strokec4 ]\cf5 \strokec5 +\cf8 \strokec8 '*'\cf5 \strokec5 +\cf7 \strokec7 B\cf4 \strokec4 [\cf7 \strokec7 0\cf4 \strokec4 ]\cf5 \strokec5 +\cf8 \strokec8 '-'\cf5 \strokec5 +\cf7 \strokec7 A\cf4 \strokec4 [\cf7 \strokec7 1\cf4 \strokec4 ]\cf5 \strokec5 +\cf8 \strokec8 '*'\cf5 \strokec5 +\cf7 \strokec7 B\cf4 \strokec4 [\cf7 \strokec7 1\cf4 \strokec4 ]))\cf5 \strokec5 +\cf8 \strokec8 '+'\cf5 \strokec5 +\cf4 \strokec4 \\\
               \cf6 \strokec6 str\cf4 \strokec4 (\cf6 \strokec6 eval\cf4 \strokec4 (\cf7 \strokec7 A\cf4 \strokec4 [\cf7 \strokec7 0\cf4 \strokec4 ]\cf5 \strokec5 +\cf8 \strokec8 '*'\cf5 \strokec5 +\cf7 \strokec7 B\cf4 \strokec4 [\cf7 \strokec7 1\cf4 \strokec4 ]\cf5 \strokec5 +\cf8 \strokec8 '+'\cf5 \strokec5 +\cf7 \strokec7 A\cf4 \strokec4 [\cf7 \strokec7 1\cf4 \strokec4 ]\cf5 \strokec5 +\cf8 \strokec8 '*'\cf5 \strokec5 +\cf7 \strokec7 B\cf4 \strokec4 [\cf7 \strokec7 0\cf4 \strokec4 ]))\cf5 \strokec5 +\cf8 \strokec8 'i'}