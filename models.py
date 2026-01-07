from pydantic import BaseModel
from typing import Optional


# Request body model
class URLRequest(BaseModel):
    url: str
    custom_code: Optional[str] = None


# Response body model
class URLResponse(BaseModel):
    short_code: str
    original_url: str
