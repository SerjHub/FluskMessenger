status = "status"
data = "data"
details = "details"

success = {
    status: True,
    data: None,
    details: None
}

fail = {
    status: False,
    data: None,
    details: None
}


def xSuccess(r_data=None, r_details=None):
    Success = fail.copy()
    Success[data] = r_data
    Success[details] = r_details
    return Success


def xFail(r_data=None, r_details=None):
    Fail = fail.copy()
    Fail[data] = r_data
    Fail[details] = r_details
    return Fail
