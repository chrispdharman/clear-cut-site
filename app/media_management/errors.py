class ClearCutLambdaError(Exception):
    """
    Raised when the clear cut lambda errors, including timing out
    """
    message = 'Error occured in the Clear Cut lambda API. This includes the possibility of a timeout.'
