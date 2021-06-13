class ArithmeticOperationException(Exception):
    def __init__(self, message='Incorrect Arithmetic Operation Entered'):
        super().__init__(message)