import google.generativeai as genai

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Character Background Generator")
root.geometry("400x800")

# Create a title label
title_label = tk.Label(root, text="Character Background Generator", font=("Arial", 20))
title_label.pack(pady=20)

# Create the input labels and text boxes
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

lifestyle_label = tk.Label(root, text="Lifestyle (Ex: Poor, Modest, Comfortable, Wealthy, etc):")
lifestyle_label.pack()
lifestyle_entry = tk.Entry(root)
lifestyle_entry.pack()

race_label = tk.Label(root, text="Race (Ex: Human, Elf, Dwarf, Halfling, etc):")
race_label.pack()
race_entry = tk.Entry(root)
race_entry.pack()

class_label = tk.Label(root, text="Class (Ex: Barbarian, Rogue, Bard, Sorcerer, Normal, etc):")
class_label.pack()
class_entry = tk.Entry(root)
class_entry.pack()

personality_label = tk.Label(root, text="Personality (Ex: Cowardly, Friendly, Greedy, Hasty, etc):")
personality_label.pack()
personality_entry = tk.Entry(root)
personality_entry.pack()

background_label = tk.Label(root, text="Background (Ex: Acolyte, Charlatan, Criminal, Entertainer, etc):")
background_label.pack()
background_entry = tk.Entry(root)
background_entry.pack()

gender_label = tk.Label(root, text="Gender (Ex: Male, Female, Nonbinary, etc):")
gender_label.pack()
gender_entry = tk.Entry(root)
gender_entry.pack()

location_label = tk.Label(root, text="Location (Ex: Forest Village, Mountain Village, Mountain City, etc):")
location_label.pack()
location_entry = tk.Entry(root)
location_entry.pack()

# Create a function to save the values
def save_values0():
    global Name, Age, LifeStyle, Race, Personality, Background, Gender, Location

    Name = name_entry.get()
    Age = age_entry.get()
    LifeStyle = lifestyle_entry.get()
    Race = race_entry.get()
    Class = class_entry.get()
    Personality = personality_entry.get()
    Background = background_entry.get()
    Gender = gender_entry.get()
    Location = location_entry.get()

    genai.configure(api_key="AIzaSyCAH-mevjvRmPhwg-a1v0EdwfabNNVYBjo")

    # Set up the model
    generation_config = {
    "temperature": 1,
    "top_p": 0,
    "top_k": 1,
    "max_output_tokens": 1024,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    ]

    model = genai.GenerativeModel(model_name="gemini-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

    prompt_parts = [
    f"Make a background Story for a DND character whos name is {Name} and whos age is {Age} and whos gender is {Gender} and whos race is Human and whos class is {Class} and whos lifestyle is {LifeStyle} and whos background is {Background} and whos personality is {Personality} and whos location is {Location}. The background story should just be a basis and shouldn't have a whole story. It should simply be an introduction to the character's life. They don't have anything yet and have simply started their journey. Make it not a cliche\n",
    ]

    response = model.generate_content(prompt_parts)
    background_response = response.text

    second_window = tk.Toplevel(root)
    second_window.title("Generated Character Background")
    second_window.geometry("1400x1000")

    character_background_label = tk.Label(second_window, text=background_response, font=("Arial", 16), wraplength=root.winfo_width())
    character_background_label.pack(pady=20, fill=tk.BOTH, expand=True)

# Create a function to save the values
def save_values1():
    global Name, Age, LifeStyle, Race, Personality, Background, Gender, Location

    Name = name_entry.get()
    Age = age_entry.get()
    LifeStyle = lifestyle_entry.get()
    Race = race_entry.get()
    Class = class_entry.get()
    Personality = personality_entry.get()
    Background = background_entry.get()
    Gender = gender_entry.get()
    Location = location_entry.get()

    genai.configure(api_key="AIzaSyCAH-mevjvRmPhwg-a1v0EdwfabNNVYBjo")

    # Set up the model
    generation_config = {
    "temperature": 1,
    "top_p": 0,
    "top_k": 1,
    "max_output_tokens": 2048,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    ]

    model = genai.GenerativeModel(model_name="gemini-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

    prompt_parts = [
    f"Make a story for a DND character whos name is {Name} and whos age is {Age} and whos gender is {Gender} and whos race is Human and whos class is {Class} and whos lifestyle is {LifeStyle} and whos background is {Background} and whos personality is {Personality} and whos location is {Location}. They start without have anything yet and have simply started their journey. As the story develops, add a climax and everything else too. Make it not a cliche\n",
    ]

    response = model.generate_content(prompt_parts)
    background_response = response.text

    second_window = tk.Toplevel(root)
    second_window.title("Generated Character Background")
    second_window.geometry("1400x1000")

    character_background_label = tk.Label(second_window, text=background_response, font=("Arial", 12), wraplength=root.winfo_width())
    character_background_label.pack(pady=20, fill=tk.BOTH, expand=True)

# Create a save button
background_button = tk.Button(root, text="Generate Background", command=save_values0)
background_button.pack(pady=20)

story_button = tk.Button(root, text="Generate Complete Story", command=save_values1)
story_button.pack(pady=20)

# Start the main loop
root.mainloop()

#Second Part

#Name = input("What is the name of your character?: ")
#Age = input("What is the age of your character?: ")
#Lifestyle = input("What is the character's lifestyle? (Ex: Poor, Modest, Comfortable, Wealthy): ")
#Location = input("What is the character's currently located? (Ex: Forest Village, Mountain Village, Mountain City): ")
#Race = input("What is the character's race? (Ex: Human, Elf, Dwarf, Halfling): ")
#Class = input("What is the character's class? (Ex: Barbarian, Rogue, Bard, Sorcerer): ")
#Gender = input("What is the character's gender? (Ex: Male, Female, Nonbinary): ")
#Background = input("What is the character's background? (Ex: Acolyte, Charlatan, Criminal, Entertainer): ")
#Personality = input("What is the character's personality? (Ex: Cowardly, Friendly, Greedy, Hasty): ")

# genai.configure(api_key="AIzaSyCAH-mevjvRmPhwg-a1v0EdwfabNNVYBjo")

# # Set up the model
# generation_config = {
#   "temperature": 1,
#   "top_p": 0,
#   "top_k": 1,
#   "max_output_tokens": 2048,
# }

# safety_settings = [
#   {
#     "category": "HARM_CATEGORY_HARASSMENT",
#     "threshold": "BLOCK_ONLY_HIGH"
#   },
#   {
#     "category": "HARM_CATEGORY_HATE_SPEECH",
#     "threshold": "BLOCK_ONLY_HIGH"
#   },
#   {
#     "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
#     "threshold": "BLOCK_ONLY_HIGH"
#   },
#   {
#     "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
#     "threshold": "BLOCK_ONLY_HIGH"
#   },
# ]

# model = genai.GenerativeModel(model_name="gemini-pro",
#                               generation_config=generation_config,
#                               safety_settings=safety_settings)

# prompt_parts = [
#   f"Make a background Story for a DND character whos name is {Name} and whos age is {Age} and whos gender is {Gender} and whos race is Human and whos class is {Class} and whos lifestyle is {Lifestyle} and whos background is {Background} and whos personality is {Personality} and whos location is {Location}. The background story should just be a basis and shouldn't have a whole story. It should simply be an introduction to the character's life. They don't have anything yet and have simply started their journey. Make it not a cliche\n",
# ]

# response = model.generate_content(prompt_parts)
# print()
# print(response.text)
