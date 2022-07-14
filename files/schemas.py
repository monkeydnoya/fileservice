from pydantic import BaseModel


class FileSave(BaseModel):
    id:int
    eventid:int
    filename:str
    link:str

    class Config:
        orm_mode = True