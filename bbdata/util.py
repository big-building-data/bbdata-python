from .exceptions import UnknownResponseException, ResourceException, ResourceUnchangedException, UnauthorizedException


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
    else:
        handle_non_ok_status(status_code)


def handle_non_ok_status(status_code):
    """
    Takes care of raising the right exception according
    to a given HTTP status code

    Args:
        status_code: the integer reprensting the status code

    """
    if status_code == 304:
        raise ResourceUnchangedException("An error 304 was thrown")
    elif status_code == 400:
        raise ResourceException("An error 400 was thrown")
    elif status_code == 401:
        raise UnauthorizedException("An error 401 was thrown")
    elif status_code == 404:
        raise ResourceException("An error 404 was thrown")
    else:
        raise UnknownResponseException("WTF?!")
