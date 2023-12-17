def main(a):
    x1=a//100
    x2=a//10%10
    x3=a%10
    y=(x1+x2+x3)%2==0
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return y
print(main(152))