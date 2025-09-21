from fastapi import HTTPException

class NotFoundError(HTTPException):
    def __init__(self, detail="Not found"):
        super().__init__(status_code=404, detail=detail)

class ConflictError(HTTPException):
    def __init__(self, detail="Conflict"):
        super().__init__(status_code=409, detail=detail)


from fastapi import HTTPException, status

def not_found(detail="Not found"):
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

def forbidden(detail="Forbidden"):
    return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=detail)
