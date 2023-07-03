

import random
def generate_addition_question():
    num1 = random.randint(10, 99)
    num2 = random.randint(1, 9)
    question = f"{num1} + {num2}"
    answer = num1 + num2


    return question,answer

# question, answer = generate_addition_question()


import matplotlib.pyplot as plt

class Flashcard:
    def __init__(self, content):
        self.content = content

    def show(self):
        fig, ax = plt.subplots()
        ax.text(0.5, 0.5, self.content, ha='center', va='center', fontsize=20)
        ax.axis('off')
        plt.show()

# Example usage:
# flashcard = Flashcard(question)
# flashcard.show()

#Generate Images

from PIL import Image, ImageDraw, ImageFont

image = Image.open('Blank_Flashcard.png')
image = image.resize((200,200))

def draw(image,question,answer,colour):
    draw =ImageDraw.Draw(image)
    font = ImageFont.truetype('Nunito-Black.ttf',24)
    text_width, text_height = draw.textsize(question, font=font)
    image_width, image_height = image.size
    x = (image_width - text_width) // 2
    y = (image_height - text_height) // 2
    draw.text((x, y), question, font=font, align="left")
    image.show()


# draw(image,question,answer,(255,255,255))