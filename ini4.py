# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.

{
    a= 4349
    b= 9100
    print(sum(x for x in range(a,b+1) if x%2 == 1))
}

# 15976224
