from fastapi import APIRouter
from app.markdown import mark
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
    pass
    return mark.Markdown.render_html(doc.data)