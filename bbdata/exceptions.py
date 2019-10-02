class ResourceUnchangedError(RuntimeError):
    """Exception raised when a query didn't modify the resource

    Attributes:
        expression -- input expression in which the error occurred e.g.: HTTP status code
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class ResourceError(RuntimeError):
    """Exception raised when a resource:
         - isn't found
         - you don't have access to it
         - the request is malformed

    Attributes:
        expression -- input expression in which the error occurred e.g.: HTTP status code
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class UnknownResponseError(RuntimeError):
    """Exception raised when the response to an API call is unknown

    Attributes:
        message -- explanation of the error
    """