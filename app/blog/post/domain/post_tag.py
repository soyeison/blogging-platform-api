from sqlalchemy import Table, Column, ForeignKey
from app.database import Base

post_tag_association = Table(
    "post_tag",
    Base.metadata,
    Column("post_id", ForeignKey("post.id")),
    Column("tag_id", ForeignKey("tag.id"))
)