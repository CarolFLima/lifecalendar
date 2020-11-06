from PIL import Image
import os
import math
import datetime


def age_in_weeks(birthdate):
    
    currentDate = datetime.datetime.now()
    deadlineDate= datetime.datetime.strptime(birthdate,'%m/%d/%Y')
    daysLeft = currentDate - deadlineDate
    weeks = ((daysLeft.total_seconds())/(7*24*3600))
    weeksInt=int(weeks)
    return weeksInt


def create_calendar(birthdate, expectancy):

    square_size = 9
    height = square_size * 52
    width = square_size * math.ceil(expectancy)

    past_weeks = age_in_weeks(birthdate)
    x_limit = (past_weeks // 52) * square_size
    y_limit = (past_weeks % 52) * square_size

    image = Image.new("RGB", (width, height), (244, 244, 244))

    past_color = (222, 146, 146)
    future_color = (222, 222, 222)
    for i in range(width):
        for j in range(height):
            if i < x_limit:
                if i % square_size != 0 and j % square_size != 0:
                    image.putpixel((i, j), past_color)
            elif i < x_limit+square_size and j < y_limit:
                if i % square_size != 0 and j % square_size != 0:
                    image.putpixel((i, j), past_color)
            else:
                if i % square_size != 0 and j % square_size != 0:
                    image.putpixel((i, j), future_color)

    image.show()

if __name__ == "__main__":
    create_calendar("02/11/1994", 75)
