from pydantic import BaseModel, Field

class MainModel(BaseModel):
    """
    This is the description of the main model
    """

    name: str 
    email: str
    '''isAdmin: bool
    isWaiter: bool'''
    rol: str
