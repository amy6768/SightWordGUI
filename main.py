import tkinter as tk
from tkinter import ttk
import random

# Define the different lists of sight words
sight_word_lists = {
    "Pre-K Dolch Sight Words": ['a', 'and', 'away', 'big', 'blue', 'can', 'come',
    'down', 'find', 'for', 'funny', 'go', 'help', 'here', 'I', 'in', 'is', 'it',
    'jump', 'little', 'look', 'make', 'me', 'my', 'not', 'one', 'play', 'red', 'run',
    'said', 'see', 'the', 'three', 'to', 'two', 'up', 'we', 'where', 'yellow', 'you'],

    "Kindergarten Dolch Sight Words": ['all', 'am', 'are', 'at', 'ate', 'be', 'black',
    'brown', 'but', 'came', 'did', 'do', 'eat', 'four', 'get', 'good', 'have', 'he',
    'into', 'like', 'must', 'new', 'no', 'now', 'on', 'our', 'out', 'please', 'pretty',
    'ran', 'ride', 'saw', 'say', 'she', 'so', 'soon', 'that', 'there', 'they', 'this', 
    'too', 'under', 'want', 'was', 'well', 'went', 'what', 'white', 'who', 'will', 'with',
     'yes'],

     "First Grade Dolch Sight Words": ['after', 'again', 'an', 'any', 'as', 'ask', 'by',
     'could', 'every', 'fly', 'from', 'give', 'going', 'had', 'has', 'her', 'him', 'his',
     'how', 'just', 'know', 'let', 'live', 'may', 'of', 'old', 'once', 'open', 'over', 'put',
     'round', 'some', 'stop', 'take', 'thank', 'them', 'then', 'think', 'walk', 'were', 'when'],
     
     "Second Grade Dolch Sight Words": ['always', 'around', 'because', 'been', 'before', 'best',
     'both', 'buy', 'call', 'cold', 'does', 'don’t', 'fast', 'first', 'five', 'found', 'gave',
     'goes', 'green', 'its', 'made', 'many', 'off', 'or', 'pull', 'read', 'right', 'sing', 'sit',
     'sleep', 'tell', 'their', 'these', 'those', 'upon', 'us', 'use', 'very', 'wash', 'which', 
     'why', 'wish', 'work', 'would', 'write', 'your'],

     "Third Grade Dolch Words": ['about', 'better', 'bring', 'carry', 'clean', 'cut', 'done', 'draw',
     'drink', 'eight', 'fall', 'far', 'full', 'got', 'grow', 'hold', 'hot', 'hurt', 'if', 'keep',
     'kind', 'laugh', 'light', 'long', 'much', 'myself', 'never', 'only', 'own', 'pick', 'seven',
     'shall', 'show', 'six', 'small', 'start', 'ten', 'today', 'together', 'try', 'warm'],

     "Noun Dolch Sight Words": ['apple', 'baby', 'back', 'ball', 'bear', 'bed', 'bell', 'bird',
     'birthday', 'boat', 'box', 'boy', 'bread', 'brother', 'cake', 'car', 'cat', 'chair', 'chicken',
     'children', 'Christmas', 'coat', 'corn', 'cow', 'day', 'dog', 'doll', 'door', 'duck', 'egg',
     'eye', 'farm', 'farmer', 'father', 'feet', 'fire', 'fish', 'floor', 'flower', 'game', 'garden',
     'girl', 'goodbye', 'grass', 'ground', 'hand', 'head', 'hill', 'home', 'horse', 'house', 'kitty',
     'leg', 'letter', 'man', 'men', 'milk', 'money', 'morning', 'mother', 'name', 'nest', 'night',
     'paper', 'party', 'picture', 'pig', 'rabbit', 'rain', 'ring', 'robin', 'Santa Claus', 'school',
     'seed', 'sheep', 'shoe', 'sister', 'snow', 'song', 'squirrel', 'stick', 'street', 'sun', 'table',
     'thing', 'time', 'top', 'toy', 'tree', 'watch', 'water', 'way', 'wind', 'window', 'wood']
     
     }

# Define the function to select a new word
def select_word():
    current_list = combo_list.get()
    words = sight_word_lists[current_list]
    current_word = random.choice(words)
    label_word.config(text=current_word, font=("Arial bold", 300))


# Create the GUI window
window = tk.Tk()
window.geometry("1200x850")
window.title("Sight Word Practice")

# Create the dropdown list for selecting the list of sight words
combo_list = ttk.Combobox(window, values=list(sight_word_lists.keys()))
combo_list.pack(pady=10)
combo_list.current(0)

# Create the "New Word" button
button = tk.Button(window, text="New Word", command=select_word)
button.pack()

# Create the label to display the selected word
label_word = tk.Label(window, text="")
label_word.pack(pady=50)

# Run the GUI window
window.mainloop()
