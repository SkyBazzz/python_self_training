def compound_interest(value: float, years: int, interest: int):
    list_result = list()
    result = value
    for i in range(years):
        result += result * interest / 100
        list_result.append(result * interest / 100)
        print(f"{result:.4f}")
    return list_result


def simple_interest(value: float, years: int, interest: int):
    list_result = list()
    result = value
    for i in range(years):
        result += value * interest / 100
        list_result.append(result * interest / 100)
        print(f"{result:.4f}")
    return list_result


base_line = 10
years = 20
interest = 10
compound_finale = compound_interest(base_line, years, interest)
finale = simple_interest(base_line, years, interest)

from PIL import Image, ImageDraw

img = Image.open('blank.png')
draw_img = ImageDraw.Draw(img)

x = 0

for i in finale:
    x = x + 30
    y = int(i)
    draw_img.line((x, 200, x, y), width=10, fill=(134, 0, 0, 134))

for i in compound_finale:
    x = x + 30
    y = int(i)
    draw_img.line((x, 200, x, y), width=10, fill=(255, 0, 0, 255))

img.show()