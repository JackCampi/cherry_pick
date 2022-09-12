from pydantic import BaseModel, Field

class MainModel(BaseModel):
    """
    This is the description of the main model
    """
    email: str
    sueldo: str