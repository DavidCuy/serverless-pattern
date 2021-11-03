from app.Core.Services.BaseService import BaseService
from app.Data.Models.Dump import Dump


class DumpService(BaseService):
    def __init__(self) -> None:
        super().__init__(Dump)