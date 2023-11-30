# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20231429 / w2051922
# Date: 04 December 2023

from graphics import *

credit_pass = []
credit_defer = []
credit_fail = []
credit_range = range(0, 121, 20)
count = 0
count_progress = 0
count_trailer = 0
count_retriever = 0
count_exclude = 0


while count < 1:
    while True:
        try:
            credit_pass = int(input('Please input the volume of credits at pass: '))
            if credit_pass in credit_range:
                break
            else:
                print('Out of range')
                print('')
        except ValueError:
            print('Integer required')
            print('')
    while True:
        try:
            credit_defer = int(input('Please input the volume of credits at defer: '))
            if credit_defer in credit_range:
                break
            else:
                print('Out of range')
                print('')
        except ValueError:
            print('Integer required')
            print('')
    while True:
        try:
            credit_fail = int(input('Please input the volume of credits at fail: '))
            if credit_fail in credit_range:
                break
            else:
                print('Out of range')
                print('')
        except ValueError:
            print('Integer required')
            print('')

    if credit_pass + credit_defer + credit_fail != 120:
        print('Total incorrect')
        continue
    elif credit_pass == 120:
        print('Progression Outcome --> Progress')
        count_progress += 1
    elif credit_pass == 100:
        print('Progression Outcome --> Progress (module trailer)')
        count_trailer += 1
    elif credit_fail >= 80:
        print('Progression Outcome --> Exclude')
        count_exclude += 1
    else:
        print('Progression Outcome --> Module retriever')
        count_retriever += 1

    repeatUntil = 0
    while repeatUntil < 1:
        print('\nWould you like to enter another set of data?')
        repeat = input("Enter 'y' for yes or 'q' for quit and view results: ").lower()
        if repeat == 'y':
            repeatUntil += 1
        elif repeat == 'q':
            count += 1
            repeatUntil += 1
        else:
            print('Please select the correct option!')


def histogram():
    win = GraphWin("Histogram", 610, 450)
    win.setBackground("Mint Cream")

    heading = Text(Point(150, 30), 'Histogram Results')
    heading.setSize(18)
    heading.setStyle('bold')
    heading.setFill(color_rgb(60, 60, 60))
    heading.draw(win)

    if count_progress or count_trailer or count_retriever or count_exclude < 15:
        height = 20
    else:
        height = 15

    rectangle1_height = 374 - count_progress*height
    rectangle1 = Rectangle(Point(50, 375), Point(170, rectangle1_height))
    rectangle1.setFill('pale green')
    rectangle1.draw(win)

    value1 = Text(Point(110, rectangle1_height-15), count_progress)
    value1.setFill('grey')
    value1.setSize(18)
    value1.setStyle('bold')
    value1.draw(win)

    rectangle2_height = 374 - count_trailer*height
    rectangle2 = Rectangle(Point(180, 375), Point(300, rectangle2_height))
    rectangle2.setFill(color_rgb(160, 198, 137))
    rectangle2.draw(win)

    value2 = Text(Point(240, rectangle2_height-15), count_trailer)
    value2.setFill('grey')
    value2.setSize(18)
    value2.setStyle('bold')
    value2.draw(win)

    rectangle3_height = 374 - count_retriever*height
    rectangle3 = Rectangle(Point(310, 375), Point(430, rectangle3_height))
    rectangle3.setFill(color_rgb(167, 188, 119))
    rectangle3.draw(win)

    value3 = Text(Point(370, rectangle3_height-15), count_retriever)
    value3.setFill('grey')
    value3.setSize(18)
    value3.setStyle('bold')
    value3.draw(win)

    rectangle4_height = 374 - count_exclude*height
    rectangle4 = Rectangle(Point(440, 375), Point(560, rectangle4_height))
    rectangle4.setFill('pink')
    rectangle4.draw(win)

    value4 = Text(Point(500, rectangle4_height-15), count_exclude)
    value4.setFill('grey')
    value4.setSize(18)
    value4.setStyle('bold')
    value4.draw(win)

    line = Line(Point(30, 375), Point(580, 375))
    line.draw(win)

    subheading1 = Text(Point(110, 390), 'Progress')
    subheading1.setSize(14)
    subheading1.setStyle('bold')
    subheading1.setFill('grey')
    subheading1.draw(win)

    subheading2 = Text(Point(240, 390), 'Trailer')
    subheading2.setSize(14)
    subheading2.setStyle('bold')
    subheading2.setFill('grey')
    subheading2.draw(win)

    subheading3 = Text(Point(370, 390), 'Retriever')
    subheading3.setSize(14)
    subheading3.setStyle('bold')
    subheading3.setFill('grey')
    subheading3.draw(win)

    subheading4 = Text(Point(500, 390), 'Excluded')
    subheading4.setSize(14)
    subheading4.setStyle('bold')
    subheading4.setFill('grey')
    subheading4.draw(win)

    num_outcomes = count_progress+count_trailer+count_retriever+count_exclude

    outcomes = Text(Point(180, 420), f'{num_outcomes} outcomes in total.')
    outcomes.setSize(18)
    outcomes.setStyle('bold')
    outcomes.setFill('grey')
    outcomes.draw(win)

    win.getMouse()
    win.close()


histogram()
