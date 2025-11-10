from datetime import datetime, date
import random
from .models import Publisher, Author, Book  # replace 'yourapp' with your actual app name

# --- Create Publishers ---
pub_names = ["Penguin Books", "HarperCollins", "O'Reilly Media", "Springer", "MIT Press"]
pub_locations = ["New York", "London", "San Francisco", "Berlin", "Cambridge"]

publishers = []
for name, loc in zip(pub_names, pub_locations):
    p = Publisher.objects.create(name=name, location=loc)
    publishers.append(p)

# --- Create Authors ---
author_names = [
    "Alice Walker", "George Orwell", "Isaac Asimov", "J.K. Rowling",
    "Mark Twain", "Ernest Hemingway", "Jane Austen", "Leo Tolstoy"
]

authors = []
for n in author_names:
    dob = date(random.randint(1940, 1995), random.randint(1, 12), random.randint(1, 28))
    a = Author.objects.create(name=n, DOB=dob)
    authors.append(a)

# --- Create Books ---
titles = [
    "The Future of AI", "Deep Learning Simplified", "Journey to the Unknown",
    "Worlds Beyond", "Modern Python", "Tales of Tomorrow", "Echoes of Time",
    "Digital Dreams"
]

for t in titles:
    price = round(random.uniform(10, 100), 2)
    qty = random.randint(1, 50)
    pubdate = datetime(2020 + random.randint(0, 4), random.randint(1, 12), random.randint(1, 28))
    rating = random.randint(1, 5)
    publisher = random.choice(publishers)
    b = Book.objects.create(
        title=t,
        price=price,
        quantity=qty,
        pubdate=pubdate,
        rating=rating,
        publisher=publisher
    )

    # Add 1–3 random authors
    b.authors.set(random.sample(authors, random.randint(1, 3)))
