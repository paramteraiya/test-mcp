def add_two_numbers(a, b):
    """
    Add two numbers together and return the result.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    # Convert inputs to float if they are strings
    if isinstance(a, str):
        a = float(a)
    if isinstance(b, str):
        b = float(b)
    
    return a + b  

# Example usage
if __name__ == "__main__":
    num1 = 5    
    num2 = 10
    result = add_two_numbers(num1, num2)
    print("The sum of", num1, "and", num2, "is", result)
