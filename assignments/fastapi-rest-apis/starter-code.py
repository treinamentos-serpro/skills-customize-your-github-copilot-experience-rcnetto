from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Book API")


class Book(BaseModel):
    id: int
    title: str
    author: str


class BookInput(BaseModel):
    title: str
    author: str


books = [
    Book(id=1, title="The Hobbit", author="J. R. R. Tolkien"),
    Book(id=2, title="Pride and Prejudice", author="Jane Austen"),
]


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    # TODO: Return all books.
    pass


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    # TODO: Find and return a book, or raise HTTPException with status 404.
    pass


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_input: BookInput) -> Book:
    # TODO: Create a unique ID, store the book, and return it.
    pass


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_input: BookInput) -> Book:
    # TODO: Update the matching book, or raise HTTPException with status 404.
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int) -> Response:
    # TODO: Remove the matching book, return an empty Response, or raise HTTPException with status 404.
    pass
