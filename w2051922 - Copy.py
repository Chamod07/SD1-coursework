# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20231429 / w2051922
# Date: 04 December 2023

from graphics import *

credit_range = range(0, 121, 20)
count_progress = 0
count_trailer = 0
count_retriever = 0
count_exclude = 0


def userInput(input_string):
    credit = int(input(f'{input_string}'))
    if credit not in credit_range:
        print('Out of range')
        print('')
        userInput(input_string)
    return credit


def checkProgress(pass_cr, defer_cr, fail_cr):
    if pass_cr + defer_cr + fail_cr != 120:
        print('Total incorrect')
        return
    if pass_cr == 120:
        outcome = 'Progress'
    elif pass_cr == 100:
        outcome = 'Progress (module trailer)'
    elif fail_cr >= 80:
        outcome = 'Exclude'
    else:
        outcome = 'Module Retriever'
    print(f'Progression Outcome --> {outcome}')


def repeatUserInput():
    count = 0
    print('\nWould you like to enter another set of data?')
    repeat = input("Enter 'y' for yes or 'q' for quit and view results: ").lower()
    while count < 1:
        if repeat == 'y':
            return True
        elif repeat == 'q':
            count += 1
            return True
        else:
            print('Please select the correct option!')
            return False
    histogram()


def histogram():
    # highest = max(count_exclude, count_retriever, count_trailer, count_progress)

    win = GraphWin("Histogram", 610, 450)
    win.setBackground("Mint Cream")

    heading = Text(Point(150, 30), 'Histogram Results')
    heading.setSize(18)
    heading.setStyle('bold')
    heading.setFill(color_rgb(60, 60, 60))
    heading.draw(win)

    # rectangle_highest = Rectangle(Point(x1, 375), Point(x2, 100))
    # rectangle_highest.draw(win)

    rectangle1_height = 375 - count_progress*20
    rectangle1 = Rectangle(Point(50, 375), Point(170, rectangle1_height))
    rectangle1.setFill('pale green')
    rectangle1.draw(win)

    value1 = Text(Point(110, rectangle1_height-15), count_progress)
    value1.setFill('grey')
    value1.setSize(18)
    value1.setStyle('bold')
    value1.draw(win)

    rectangle2_height = 375 - count_trailer*20
    rectangle2 = Rectangle(Point(180, 375), Point(300, rectangle2_height))
    rectangle2.setFill(color_rgb(160, 198, 137))
    rectangle2.draw(win)

    value2 = Text(Point(240, rectangle2_height-15), count_trailer)
    value2.setFill('grey')
    value2.setSize(18)
    value2.setStyle('bold')
    value2.draw(win)

    rectangle3_height = 375 - count_retriever*20
    rectangle3 = Rectangle(Point(310, 375), Point(430, rectangle3_height))
    rectangle3.setFill(color_rgb(167, 188, 119))
    rectangle3.draw(win)

    value3 = Text(Point(370, rectangle3_height-15), count_retriever)
    value3.setFill('grey')
    value3.setSize(18)
    value3.setStyle('bold')
    value3.draw(win)

    rectangle4_height = 375 - count_exclude*20
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


def main():
    credit_pass = userInput('\nPlease input the volume of credits at pass: ')
    credit_defer = userInput('Please input the volume of credits at defer: ')
    credit_fail = userInput('Please input the volume of credits at fail: ')
    checkProgress(credit_pass, credit_defer, credit_fail)
    repeatUserInput()


if __name__ == '__main__':
    main()
