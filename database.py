import sqlite3

CREATE_RECIPES_TABLE = """CREATE TABLE recipes
            (recipe_id INTEGER PRIMARY KEY NOT NULL,
            name TEXT,
            ingridients TEXT,
            instructions TEXT);
            """

INSERT_RECIPE = """INSERT INTO recipes
            (name, ingridients, instructions)
            VALUES (?, ?, ?);
            """

GET_ALL_RECIPES = "SELECT * FROM recipes;"

GET_RANDOM_RECIPE = """SELECT * FROM recipes
            ORDER BY RANDOM()
            LIMIT 1;
            """

class RecipeSuggester:

    def __init__(self):
        self.connection = sqlite3.connect("recipes")
        
    def create_table(self):
        with self.connection:
            self.connection.execute(CREATE_RECIPES_TABLE)

    def add_recipe(self, name, ingridients, instructions):
        with self.connection:
            self.connection.execute(INSERT_RECIPE, (name, ingridients, instructions))

    def get_random_recipe(self):
        with self.connection:
            return self.connection.execute(GET_RANDOM_RECIPE).fetchall()

recipes1 = RecipeSuggester()
# recipes1.create_table()
# recipes1.add_recipe("Chicken Burrito", "Chicken meat, Tortilla, Cottage cheese, Greens, Onion, Corn", "Cook the chicken meat. Caramelize the onions. Put the chicken and corn in the pan with the onions. Heat the tortilla on a hot pan. Put the greens as a bed. Then the chicken with the corn and onions. Then put cottage cheese on top and any condiments of your choise. Enjoy!")
print(recipes1.get_random_recipe())
