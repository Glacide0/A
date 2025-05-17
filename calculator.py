class Calculator:
    """A simple calculator class providing basic and advanced mathematical operations."""
    
    def add(self, a, b):
        """Add two numbers and return the result."""
        return a + b
    
    def subtract(self, a, b):
        """Subtract b from a and return the result."""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers and return the result."""
        return a * b
    
    def divide(self, a, b):
        """Divide a by b and return the result.
        
        Args:
            a: Numerator
            b: Denominator
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, a, b):
        """Calculate a raised to the power of b.
        
        Args:
            a: Base
            b: Exponent
        """
        return a ** b
    
    def square_root(self, a):
        """Calculate the square root of a.
        
        Args:
            a: Input number
            
        Raises:
            ValueError: If a is negative
        """
        if a < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return a ** 0.5
    
    def modulo(self, a, b):
        """Get the remainder of division of a by b.
        
        Args:
            a: Dividend
            b: Divisor
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot perform modulo with zero")
        return a % b
    
    def floor_division(self, a, b):
        """Perform integer division of a by b.
        
        Args:
            a: Dividend
            b: Divisor
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a // b