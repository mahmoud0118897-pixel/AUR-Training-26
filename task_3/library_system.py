from abc import ABC , abstractmethod
from enum import Enum
import os

class Itemstatus(Enum):
    AVAILABLE = "AVAILABLE"
    CHECKED_OUT = "CHECKED_OUT"
    LOST = "LOST"
class Isbn_Validator:
    @staticmethod
    def validator (isbn: str):
        isbn=isbn.replace(" ","").replace("-","")
        if not isbn.isdigit() or len(isbn) !=13:
            return False
        total=0
        for i,char in enumerate(isbn):
            if i%2==0:
                total+=int(char)
            else:
                total+=int(char)*3
        return total%10==0
class LibraryItem(ABC):
    _registry={}
    def __init__(self,title,status):
        self.title = title
        self._status = status
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._registry[cls.__name__] = cls
    @property
    def status(self):
        return self._status
    def checkout(self):
        if self._status != Itemstatus.AVAILABLE :
           raise ValueError(f"Item '{self.title}' cannot be checked out because its status is {self._status.name}.")
        self._status = Itemstatus.CHECKED_OUT 
    def return_items(self):
        if self._status == Itemstatus.AVAILABLE :
               raise ValueError(f"Item '{self.title}' is already available")
        self._status = Itemstatus.AVAILABLE
    def mark_lost (self):
        self._status = Itemstatus.LOST       
   
    @property
    @abstractmethod
    def loan_period(self):
        pass
    def __lt__(self, other):
        if isinstance(other,LibraryItem):
            return self.title.lower() < other.title.lower()
        return NotImplemented
    def __repr__(self):
        return f"{self.__class__.__name__}(title='{self.title}', status={self._status.name})"
    def __str__(self):
        return f"{self.title} ({self.__class__.__name__}) - {self._status.value}" 
    @classmethod
    def from_dict(cls, data: dict):
        item_type = data.get("type")
        subclass = cls._registry.get(item_type)
        if not subclass:
            raise ValueError(f"Unknown item type: {item_type}")
        return subclass._from_dict_impl(data)
    @classmethod
    @abstractmethod
    def _from_dict_impl(cls, data: dict):
        pass
class Book(LibraryItem):
    def __init__(self, title, status, author, isbn):
        super().__init__(title, status)
        self.author = author
        if not Isbn_Validator.validator(isbn):
            raise ValueError(f"Invalid ISBN: {isbn}")
        self.isbn = isbn
    @classmethod
    def _from_dict_impl(cls, data: dict):
        return cls(
            title=data.get("title"),
            author=data.get("author"),
            isbn=data.get("isbn"),
            status=Itemstatus(data.get("status", "AVAILABLE"))
        )
    @property
    def loan_period(self):
        return 21
class DVD(LibraryItem):
    def __init__(self, title: str, director: str, status):
        super().__init__(title, status)
        self.director = director
    @property
    def loan_period(self) -> int:
        return 5
    @classmethod
    def _from_dict_impl(cls, data: dict):
        return cls(
            title=data.get("title"),
            director=data.get("director"),
            status=Itemstatus(data.get("status", "AVAILABLE"))
        )
class Magazine(LibraryItem):
    def __init__(self, title: str, issue: str, status):
        super().__init__(title, status)
        self.issue = issue
    @property
    def loan_period(self) -> int:
        return 14
    @classmethod
    def _from_dict_impl(cls, data: dict):
        return cls(
            title=data.get("title"),
            issue=data.get("issue"),
            status=Itemstatus(data.get("status", "AVAILABLE"))
        )
class Database:
    def __init__(self, filepath="database.txt"):
        self.filepath = filepath

    def load_items(self) -> list:
        items = []
        if not os.path.exists(self.filepath):
            return items

        with open(self.filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                
                data = {}
                parts = line.split("|")
                for part in parts:
                    if "=" in part:
                        key, value = part.split("=", 1)
                        data[key.strip()] = value.strip()
                
                if "type" in data:
                    try:
                        item = LibraryItem.from_dict(data)
                        items.append(item)
                    except Exception as e:
                        print(f"Error parsing line: {e}")
        return items

    def save_items(self, items: list):
        with open(self.filepath, "w", encoding="utf-8") as f:
            for item in items:
                line_parts = [f"type={item.__class__.__name__}", f"title={item.title}"]
                
                if isinstance(item, Book):
                    line_parts.append(f"author={item.author}")
                    line_parts.append(f"isbn={item.isbn}")
                elif isinstance(item, DVD):
                    line_parts.append(f"director={item.director}")
                elif isinstance(item, Magazine):
                    line_parts.append(f"issue={item.issue}")
                
                line_parts.append(f"status={item.status.value}")
                
                f.write("|".join(line_parts) + "\n")
class Library:
    def __init__(self, database: Database):
        self.database = database
        self.items = self.database.load_items()

    def add_item(self, item: LibraryItem):
        self.items.append(item)
        self.database.save_items(self.items)

    def checkout_item(self, title: str):
        for item in self.items:
            if item.title.lower() == title.lower():
                item.checkout()
                self.database.save_items(self.items)
                return True
        raise ValueError(f"Item with title '{title}' not found.")

    def return_item(self, title: str):
        for item in self.items:
            if item.title.lower() == title.lower():
                item.return_item()
                self.database.save_items(self.items)
                return True
        raise ValueError(f"Item with title '{title}' not found.")

    def find_by_title(self, title: str) -> list:
        return [item for item in self.items if title.lower() in item.title.lower()]

    def list_available(self) -> list:
        return [item for item in self.items if item.status == Itemstatus.AVAILABLE]

    def get_sorted_items(self) -> list:
        return sorted(self.items)
