from fastapi import APIRouter
from app.markdown.mark import Markdown
from typing import Optional
from pydantic import BaseModel


class Doc(BaseModel):
    data: str
    
   
router = APIRouter()


@router.post("/")
def convert(doc: Doc) -> str:
    """
    Convert Simple Markdown to HTML Markup
    """
    print(doc)
    return Markdown.render_html(doc.data)