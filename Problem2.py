# ach new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.
suma=0
FibNumb=1
FibNumb2=2
while FibNumb<4000000 and FibNumb2<4000000:
    if FibNumb%2==0:
        suma+=FibNumb
    FibNumb+=FibNumb2
    if FibNumb2%2==0:
        suma+=FibNumb2
    FibNumb2+=FibNumb
print(suma)