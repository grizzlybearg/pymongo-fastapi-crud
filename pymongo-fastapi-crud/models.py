"""
Create models for API requests and responses
MongoDB has a flexible schema model which allows having documents 
with different structure within the same collection. 
In practice, the documents in a collection 
usually share the same structure. 
If needed, you can even enforce 
validation rules per collection. 
We won't cover database validation 
in our PyMongo tutorial. 
Instead, we'll ensure that data passing 
through the REST API is valid before storing it in the database.

We'll create a couple of models for the API 
requests and responses and let FastAPI do 
the heavy lifting for us. 
The framework will take care of the validation, 
converting to the correct data types, 
and even generating the API documentation. 
Open the models.py file and add the following:

We're extending the BaseModel from the pydantic 
package and adding the fields for our models. 
For the Book model, we've got four required 
fields: id, title, author, and synopsis. T
he id field is automatically populated with a UUID.
We also have an example for the Book model 
that will be displayed in the API documentation.

The fields in the BookUpdate model are optional. 
That will allow us to do partial updates. 
We don't have an id field in the BookUpdate model 
because we don't want to 
allow the user to update the id.
"""

import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Book(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    author: str = Field(...)
    synopsis: str = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "Don Quixote",
                "author": "Miguel de Cervantes",
                "synopsis": "..."
            }
        }


class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    synopsis: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Don Quixote",
                "author": "Miguel de Cervantes",
                "synopsis": "Don Quixote is a Spanish novel by Miguel de Cervantes..."
            }
        }
