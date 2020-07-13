# Nazarii Klymok.
# June 30th.
# Project Capstone, Option №1, Major Indecision.
# Helps students to decide on their major.

best = "No results"
stats = "No stats"


def main():
    start()
    menu()


def test():
    s = 0
    t = 0
    e = 0
    a = 0
    m = 0
    questions = get_questions()
    for question in questions:
        print(question)

        answer = ""
        while (not str(answer).isdigit()) or (int(answer) < 0 or int(answer) > 5):
            answer = input(question + "(0 to 5)")
        answer = int(answer)

        if question[0] == 's':
            s = s + answer
        elif question[0] == 't':
            t = t + answer
        elif question[0] == 'e':
            e = e + answer
        elif question[0] == 'a':
            a = a + answer
        elif question[0] == 'm':
            m = m + answer
    print("Congratulations! You finished the test.")
    evaluate(s, t, e, a, m)
    results()


def evaluate(s, t, e, a, m):
    global best
    global stats

    best = ""
    stats = ""
    max_score = 25

    if max(s, t, e, a, m) == s:
        best = best + " Science;"
    if max(s, t, e, a, m) == t:
        best = best + " Technology;"
    if max(s, t, e, a, m) == e:
        best = best + " Engineering;"
    if max(s, t, e, a, m) == a:
        best = best + " Arts;"
    if max(s, t, e, a, m) == m:
        best = best + " Maths;"

    science_score = "Science: " + str(s) + " out of " + str(max_score) + "\n"
    tech_score = "Technology: " + str(t) + " out of " + str(max_score) + "\n"
    engineering_score = "Engineering: " + str(e) + " out of " + str(max_score) + "\n"
    arts_score = "Arts: " + str(a) + " out of " + str(max_score) + "\n"
    maths_score = "Mathematics: " + str(m) + " out of " + str(max_score) + "\n"
    stats = science_score + tech_score + engineering_score + arts_score + maths_score


def results():
    print("Your test results say that the best course(s) for you is/are: ")
    print(best)
    print("display all results? If no, go to main menu: (y/n) ")
    choice = input("display all results? If no, go to main menu: (y/n) ")
    while choice != 'y' and choice != 'n':
        choice = input("display all results? If no, go to main menu: (y/n) ")
    if choice == 'y':
        print_research()

    menu()


def print_research():
    print(stats)
    if "Science" in best:
        print("Examples of jobs for science are scientist, geologist, economist, biochemist, physicist")
    if "Technology" in best:
        print("Examples of jobs for technology are Computer programmer, Web developer, Cybersecurity, Data analysis, "
              "Pentesting")
    if "Engineering" in best:
        print("Examples of jobs for engineering are engineer, technician, Designer, Audio engineer, PC Hardware "
              "engineer")
    if "Arts" in best:
        print("Examples of jobs for arts are animator, art director, architect, illustrator, curator")
    if "Maths" in best:
        print("Examples of jobs for maths are statistician, financial analyst, cryptologist, physicist, astronomer")


def get_questions():
    output = ["s-1: Do you like chemistry experiments?",
              "s-2: Have you ever liked studying organisms?",
              "s-3: Do you enjoy studying other cultures and nations?",
              "s-4: Have you ever wondered if its possible to describe events with formulas?",
              "s-5: Are you fascinated about Astronomy or/and space?",
              "t-1: Have you ever wanted to create your own computer program?",
              "t-2: Do you enjoy working with computers?",
              "t-3: Do you try, sometimes, to automate some job you do?",
              "t-4: Do you enjoy working in teams?",
              "t-5: Have you ever been inspired by hackers on your favorite TV series?",
              "e-1: Do you think it's cool to build cars/aeroplanes/other kind of transportation?",
              "e-2: Do you like (find it interesting) working with blueprints?",
              "e-3: Do you ever find yourself watching Space-X rocket launches with your jaw dropped?",
              "e-4: Have you ever done and did you enjoy doing DIYs?",
              "e-5: Do you like/ would like to start programming?",
              "a-1: Do you like drawing?",
              "a-2: Do you think you can describe the world visually better than in any other way?",
              "a-3: Do you think graphical aspect in data representation is important?",
              "a-4: Have anyone ever told you your drawings are great?",
              "a-5: Did you know that each pencil has a different parameter for its lead?",
              "m-1: Do you love working with formulas?",
              "m-2: Have you ever found math incredibly beautiful?",
              "m-3: Are you attentive to details?",
              "m-4: Are you a good critical thinker?",
              "m-5: Are you in analytical thinking?"]
    return output


def menu():
    print("Main menu (make a choice 1-3):")
    print("╟ 1. Take a test")
    print("╟ 2. See the results")
    print("╟ 3. Exit")
    choice = -1
    while (not str(choice).isdigit()) or (int(choice) < 1 or int(choice) > 3):
        choice = input("Make a choice from 1 to 3:")

    choice = int(choice)
    if choice == 1:
        test()
    elif choice == 2:
        if best != "No results":
            results()
        else:
            print("please, finish the test first!")
            menu()
    elif choice == 3:
        return


def start():
    print("╔" + ("═" * 35) + "╗")
    print("╟    Welcome to the MyMajor Test!   ╢")
    print("╚" + ("═" * 35) + "╝")
    print("We'll help you to decide on your major.")


main()
