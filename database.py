import sqlite3

CREATE_RECIPES_TABLE = """CREATE TABLE recipes
            (recipe_id INTEGER PRIMARY KEY NOT NULL,
            name TEXT,
            ingredients TEXT,
            instructions TEXT);
            """

INSERT_RECIPE = """INSERT INTO recipes
            (name, ingredients, instructions)
            VALUES (?, ?, ?);
            """

GET_RECIPE_BY_ID = """SELECT * FROM recipes
            WHERE recipe_id IS ?;
            """

GET_ALL_INGREDIENTS = "SELECT recipe_id, ingredients FROM recipes;"

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

    def add_recipe(self, name, ingredients, instructions):
        with self.connection:
            self.connection.execute(INSERT_RECIPE, (name, ingredients, instructions))

    def get_random_recipe(self):
        with self.connection:
            recipe = self.connection.execute(GET_RANDOM_RECIPE).fetchall()

            self.recipe_name = recipe[0][1]
            self.recipe_ingredients = recipe[0][2]
            self.recipe_instructions = recipe[0][3]

    def get_all_ingredients(self):
        with self.connection:
            return self.connection.execute(GET_ALL_INGREDIENTS).fetchall()

    def get_user_ingridients(self, ingridients):
        user_ingridients = ingridients.split(",")
        user_ingridients = [s.strip().lower() for s in user_ingridients]

        return user_ingridients

    def get_recipe_by_id(self, id):
        with self.connection:
            recipe = self.connection.execute(GET_RECIPE_BY_ID, (id,)).fetchall()

            self.recipe_name = recipe[0][1]
            self.recipe_ingredients = recipe[0][2]
            self.recipe_instructions = recipe[0][3]

    def most_matches(self):
        all_ingridients = self.get_all_ingredients()
        user_ingridients = self.get_user_ingridients("Chicken meat, Noodles, Onion")
        most_matches = 0
        recipe_id = 0

        for recipe_index in range(len(all_ingridients)):
            current_ingridients = all_ingridients[recipe_index][-1].lower()
            matches = 0

            for user_ingridient in user_ingridients:
                if user_ingridient in current_ingridients:
                    matches += 1

            if matches > most_matches:
                most_matches = matches
                recipe_id = all_ingridients[recipe_index][0]

        self.get_recipe_by_id(recipe_id)


recipes1 = RecipeSuggester()

# recipes1.create_table()
# recipes1.add_recipe("Chicken Burrito", "Chicken meat, Tortilla, Cottage cheese, Greens, Onion, Corn", "Cook the chicken meat. Caramelize the onions. Put the chicken and corn in the pan with the onions. Heat the tortilla on a hot pan. Put the greens as a bed. Then the chicken with the corn and onions. Then put cottage cheese on top and any condiments of your choise. Enjoy!")
# recipes1.add_recipe("Turkey Burrito", "Turkey mince, Tortilla, Cottage cheese, Greens, Onion, Corn", "Cook the turkey mince. Caramelize the onions. Put the turkey mince and corn in the pan with the onions. Heat the tortilla on a hot pan. Put the greens as a bed. Then the turkey mince with the corn and onions. Then put cottage cheese on top and any condiments of your choise. Enjoy!")
# recipes1.add_recipe("Fusilli Bolognese", "Fusilli, Turkey mince, Tomato sauce, Garlic, Onion", "Boil the fusilli until they are al dente. Save a little of the water they boiled in for the sauce. Caramelize the onion and the garlic in a pan then add the turkey mince. Add Italian spices, salt and pepper. Add the tomato sauce, lower the heat and let it simmer for a few minutes. When the sauce is ready add the fusilli and a little bit of the water you boiled them in. Serve with cheese or by itself. Enjoy!")
# recipes1.add_recipe("Chicken Noodles with Spicy Peanut Sauce", "Chicken meat, Noodles, Onion, Peanut butter, Sriracha sauce, Vinegar, Soy sauce, Garlic, Sugar, Eggs", "Cook the chicken meat in the oven. Mince some garlic and put it in a pan. Add the sugar, soy sauce, vinegar, sriracha and peanut butter and heat until the sugar is dissolved and everything is combined. If the mix is too thick - add water. Set it aside. Heat some oil in a pan and add the onion and fry it until it turns golden. This is the moment to add any leftover vegetables from the fridge. Add the cooked chicken sliced in bite-sized pieces. Boil the noodles and add them to the pan. Crack the eggs on the side of the pan and combine with everything else once they start to set. Finally add the peanut sauce and stir until everything is well mixed. Serve with sesame seeds. Enjoy!")
# recipes1.add_recipe("Protein Oats", "Oatmeal, Protein powder, Cinnamon, Honey, Fruit, Nuts", "Cook the oats, protein powder and cinnamon. Once the mixture cools down a bit, add the honey, fruits and nuts. Enjoy!")
# recipes1.add_recipe("Chicken with Sweet Potatoes", "Chicken meat, Sweet potatoes, Vegetables, Onion", "Put some oil in a large cooking tray. Put the oven on high. Cut everything in bite-sized pieces and put it in the tray. Add spices and a glass of water, wine or beer and put the tray in the oven. Bake until golden brown. Enjoy!")

# recipes1.most_matches()
# recipes1.get_random_recipe()
# print()
# print(recipes1.recipe_name)
# print()
# print(recipes1.recipe_ingredients)
# print()
# print(recipes1.recipe_instructions)
