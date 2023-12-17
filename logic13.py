def main(a):
    x1=a//10
    x2=a%10
    """
    Given a two-digit integer a,  check the following statement "All digits sum is even".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return (x1+x2)%2==0
print(main(45))