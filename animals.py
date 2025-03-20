animals = [
    {'name': 'Cat', 'group': 'Mammals', 'number_of_legs': 4, 'skills': ['climbing', 'hunting']},
    {'name': 'Dog', 'group': 'Mammals', 'number_of_legs': 4, 'skills': ['fetching', 'guarding']},
    {'name': 'Eagle', 'group': 'Birds', 'number_of_legs': 2, 'skills': ['flying', 'hunting']},
    {'name': 'Fish', 'group': 'Fish', 'number_of_legs': 0, 'skills': ['swimming']},
    {'name': 'Snake', 'group': 'Reptiles', 'number_of_legs': 0, 'skills': ['slithering', 'climbing']}
]



class Animal:
    def __init__(self, name, group, number_of_legs, skills):
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills

    def __str__(self):
        return f"Name: {self.name}, Group: {self.group}, Legs: {self.number_of_legs}, Skills: {', '.join(self.skills)}"

cat = Animal('Cat', 'Mammals', 4, ['Climbing', 'Jumping'])
dog = Animal('Dog', 'Mammals', 4, ['Running', 'Swimming'])
bird = Animal('Bird', 'Aves', 2, ['Flying', 'Singing'])
fish = Animal('Fish', 'Fish', 0, ['Swimming'])
snake = Animal('Snake', 'Reptiles', 0, ['Slithering', 'Climbing'])


animals = [cat, dog, bird, fish, snake]


for animal in animals:
    print(animal)
