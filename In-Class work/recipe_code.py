class Rational:
    def __init__(self, n, d):
        self.num = n
        self.denom = d

    def __mul__(self, other):
        assert isinstance(other, Rational)
        return Rational(self.num * other.num, self.denom * other.denom)


class Ingredient:
    def __init__(self, inp_name, inp_amount, inp_unit):
        self.name = inp_name
        self.amount = inp_amount
        self.unit = inp_unit

    def scale(self, scale_factor):
        """
        scales quantity by scale_factor
        """
        self.amount *= scale_factor

class Recipe:
    def __init__(self, name, ingredient_list):
        self.name = name
        self.ingredients = ingredient_list

    def scale(self, scale_factor):
        """
        scales all ingredients by scale_factor
        """
        list(map(lambda ingredient : ingredient.scale(scale_factor), self.ingredients))
    def print_ingredient_names(self):
        def print_name(ingredient):
             print("Name: " + ingredient.name)
        list(map(print_name, self.ingredients))



class VegetarianRecipe(Recipe):
    pass

quarter = Rational(1, 4)
lentils = Ingredient("lentil", quarter, "cup")
butter = Ingredient("butter", Rational(1,1), "tbsp")
spice = Ingredient("cumin", Rational(1,1), "tsp")
tomato = Ingredient("tomato", Rational(1,2), None)

vr = VegetarianRecipe("dahl", [lentils, butter, tomato, spice])
vr.scale(Rational(3,1))
vr.print_ingredients()


   
    
