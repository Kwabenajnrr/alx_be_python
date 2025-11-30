class SimpleCalculator:
    """A simple calculator class that performs basic arithmetic operations."""

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
        """Divide a by b and return the result. Returns None if b is zero."""
        if b == 0:
            return None
        return a / b
