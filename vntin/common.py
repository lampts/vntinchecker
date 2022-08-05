def validate_tin(tin: str) -> int:
    """
    tin format: n1n2n3n4n5n6n7n8n9 n10 n11n12n13
    n10 is check sum
    
    returns 1 if valid else 0
    """
    if not isinstance(tin, str):
        raise ValueError("The input of tax identifier number needs to be a string.")

    if not tin.isdigit():
        raise ValueError("The input of tax identifier number needs to be digits")

    if len(tin) < 10:
        raise ValueError("Tax Identifier Number must have more 10 digits.")
        
    codes = tin[:10]
    weights = [31,29,23,19,17,13,7,5,3]
    checksum = 0
    for l1,l2 in zip(codes[:9], weights):
        checksum += int(l1) * int(l2)
    
    if int(codes[9]) == (10 - checksum % 11):
        return 1
    else:
        return 0