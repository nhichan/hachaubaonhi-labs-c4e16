from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    list_text = [shape['text'] for shape in shapes]
    list_color = [shape['color'] for shape in shapes]
    return [
                choice(list_text),
                choice(list_color),
                randint(0, 1) # 0 : meaning, 1: color
            ]

def is_inside(pt, rect):
    x, y = pt
    a, b, width, height = rect
    if a < x < a + width and b < y < b + height:
        return True
    return False

def mouse_press(x, y, text, color, quiz_type):
    for shape in shapes:
        if is_inside([x, y], shape['rect']):
            if (quiz_type == 0): # meaning
                return (shape['text'] == text)
            else:
                return (shape['color'] == color)
    return False
