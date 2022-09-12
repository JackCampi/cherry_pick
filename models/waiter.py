from pydantic import BaseModel, Field

class Waiter(BaseModel):
    """
    This is the description of the main model
    """
    email: str
    addres: str