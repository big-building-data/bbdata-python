from .exceptions import UnknownResponseException, ResourceException, ResourceUnchangedException


def handle_response(status_code: int, return_value):
    """
    Takes care of the error handling of a BBData's API
    response

    Args:
        status_code: the HTTP status code
        return_value: the value to return

    Returns:
        the object given in parameter or an exception

    """

    if status_code == 200:
        return return_value
    elif status_code == 304:
        raise ResourceUnchangedException
    elif status_code == 400:
        raise ResourceException
    else:
        raise UnknownResponseException
