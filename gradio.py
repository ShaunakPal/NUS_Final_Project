import random
import gradio

def greet(name):
    myList = ["This is positive","This is negative","This is neutral"]
    random_element = random.choice(myList)
    return random_element

demo = gradio.Interface(fn=greet, inputs="text", outputs="text")

demo.launch()