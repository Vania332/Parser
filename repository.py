from abc import ABC, abstractmethod
from models import Source
<<<<<<< HEAD
from sqlalchemy.ext.asyncio import AsyncSession
=======
>>>>>>> database-realization


class SourceRepository(ABC):
    
    @abstractmethod
    async def add(self, source: Source) -> Source: ...
    
    @abstractmethod
    async def get(self, id: int) -> Source | None: ...
    
    @abstractmethod
    async def get_all(self) -> list[Source]: ...
    
    @abstractmethod
    async def delete(self, id: int) -> None: ...
    
    @abstractmethod
    async def find_by_name(self, keyword: str) -> list[Source]: ...
    
    @abstractmethod
    async def update(self, source: Source) -> Source: ...
    
    
class SQLSourceRepository(SourceRepository):
    """SQL implementation of SourceRepository interface."""
<<<<<<< HEAD
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def add(self, source: Source) -> Source: 
        self.session.add(source)
        
        
=======
    
>>>>>>> database-realization
    