import uvicorn
from fastapi import FastAPI, Form
import requests
import random

from starlette.responses import HTMLResponse

app = FastAPI()

url = ""

film_by_age = {

    "children": ["Frozen", "Toy Story", "Finding Nemo", "Moana", "Zootopia", "Coco", "The Lion King", "Inside Out",
                 "How to Train Your Dragon", "Kung Fu Panda", "Spirited Away", "My Neighbor Totoro", "Up", "Luca",
                 "Ratatouille", "The Incredibles", "WALL-E", "Ponyo", "Madagascar",
                 "Charlie and the Chocolate Factory"],

    "teens": ["Spider-Man", "The Hunger Games", "Harry Potter", "The Maze Runner", "Divergent", "Percy Jackson",
              "Twilight", "The Fault in Our Stars", "Jurassic World", "Guardians of the Galaxy",
              "To All the Boys I've Loved Before", "The Perks of Being a Wallflower", "Lady Bird", "The Princess Bride",
              "Mean Girls", "The Breakfast Club", "John Wick", "Mad Max: Fury Road", "Black Panther",
              "Scott Pilgrim vs. the World"],

    "adults": ["Inception", "The Godfather", "The Shawshank Redemption", "12 Angry Men", "Schindler's List",
               "The Dark Knight", "The Lord of the Rings: The Fellowship of the Ring", "Pulp Fiction", "Fight Club",
               "Parasite", "Seven", "The Silence of the Lambs", "The Matrix", "No Country for Old Men", "Memento",
               "City of God", "Goodfellas", "The Departed", "The Green Mile", "Oldboy"]

}

html_form = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Film Önerisi</title>
    <style>
        body {
            font-family: sans-serif;
            margin: 20px;
        }

        h1 {
            text-align: center;
            margin-bottom: 20px;
        }

        form {
            max-width: 400px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        label {
            display: block;
            margin-bottom: 10px;
        }

        input[type="number"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 3px;
        }

        button[type="submit"] {
            background-color: #007bff;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Film Önerisi Sistemi 🎥</h1>
    <form action="/recommend" method="post">
        <label for="age">Yaşınızı girin:</label>
        <input type="number" id="age" name="age" required>
        <button type="submit">Film Öner</button>
    </form>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def home():
    return html_form


@app.post("/recommend", response_class=HTMLResponse)
def recommend(age: int = Form(...)):
    if age < 13:
        category = "children"
    elif 13 <= age < 18:
        category = "teens"
    else:
        category = "adults"

    film = random.choice(film_by_age[category])
    return f"<h1>Size önerimiz: {film} 🎬</h1>"


if __name__ == "__main__":
    uvicorn.run("main.app", host="0.0.0.0", port=8000, reload=True)