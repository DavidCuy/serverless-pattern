from typing import Dict, List
from sqlalchemy import Column, Integer, String
from app.Core.Data.BaseModel import BaseModel

class Dump(BaseModel):
    """ Table Dumps Database model

    Args:
        BaseModel (ORMClass): Parent class

    Returns:
        Dump: Instance of model
    """

    __tablename__ = 'Dumps'
    id = Column("IdDump", Integer, primary_key=True)
    Description = Column("Description", String, nullable=False)
    
    model_path_name = "dump"
    
    def property_map(self) -> Dict:
        return {
            "id": "IdDump"
        }
    
    def display_members(self) -> List[str]:
        return [
            "id", "Description"
        ]
