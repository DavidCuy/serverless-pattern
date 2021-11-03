from typing import Dict, List
from sqlalchemy import Column, Integer, String
from app.Core.Data.BaseModel import BaseModel

class Example(BaseModel):
    """ Table Examples Database model

    Args:
        BaseModel (ORMClass): Parent class

    Returns:
        Person: Instance of model
    """

    __tablename__ = 'Examples'
    id = Column("IdExample", Integer, primary_key=True)
    Description = Column("Description", String, nullable=False)
    
    # This model path is used to know which path will raise the event
    model_path_name = "example"
    
    def property_map(self) -> Dict:
        return {
            "id": "IdExample"
        }
    
    def display_members(self) -> List[str]:
        return [
            "id", "Description"
        ]
