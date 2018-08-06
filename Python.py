Hello, Python!
## Syntax, Variables, and Numbers 
The // operator gives us a result that's rounded down to the next integer.
print(5 // 2)
3

Order of operations
PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

pi = 3.14159 # approximate
diameter = 3
radius=1.50
area= pi*radius**2

# Swapping values
a = [1, 2, 3]
b = [3, 2, 1]
tmp = a
a = b
b = tmp
another solution 
a, b = b, a

##  Working with the [QuickDraw dataset] of doodled sketches and we want to visualize 
##  several sketches at once in a grid-like arrangement
import random
from matplotlib import pyplot as plt
from learntools.python.quickdraw import random_category, sample_images_of_category, draw_images_on_subplots

## Step 1: Sample some sketches
# How many sketches to view - a random number from 2 to 20
n = random.randint(2, 20)
# Choose a random quickdraw category
category = random_category()
imgs = sample_images_of_category(n, category)
## Step 2: Choose the grid properties
rows = n // 8 + min(1, n % 8)
cols = min(n, 8)
# The height and width of the whole grid, measured in inches.
height = rows * 2
width = cols * 2
## Step 3: Create the grid
grid = plt.subplots(rows, cols, figsize=(width, height))
## Step 4: Draw the sketches in the grid
draw_images_on_subplots(imgs, grid)
