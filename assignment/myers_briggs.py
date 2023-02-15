import sys


def show(personality_type):
    print(f"Your personality type is - >{personality_type}")


def question():
    questions_a: list = [
        "1. A. expend energy, enjoy groups ",
        "2. A. interpret literally ",
        "3. A. logical, thinking, questioning",
        "4. A. organized, orderly",
        "5. A. more outgoing, think out loud",
        "6. A. practical, realistic, experiential",
        "7. A. candid, straight forward, frank",
        "8. A. plan, schedule",
        "9. A. seek many tasks, public activities, interaction with others",
        "10. A. standard, usual, conventional",
        "11. A. firm, tend to criticize, hold the line ",
        "12. A. regulated, structured",
        "13. A. external, communicative, express yourself",
        "14. A. focus on here-and-now ",
        "15. A. tough-minded, just ",
        "16. A. preparation, plan ahead",
        "17. A. active, initiate",
        "18. A. facts, things, “what is”",
        "19 .A. matter of fact, issue-oriented",
        "20.  A. control, govern"
    ]
    questions_b: list = [
        "1. B. conserve energy, enjoy one on one",
        "2. B. look for meaning and possibilities",
        "3. B. empathetic, feeling, accommodating",
        "4. B. flexible, adaptable",
        "5. B. more reserved, think to yourself",
        "6. B. . imaginative, innovative, theoretical",
        "7. B. b. tactful, kind, encouraging",
        "8. B. unplanned, spontaneous",
        "9. B. seek private, solitary activities with quiet to concentrate",
        "10. B. gentle, tend to appreciate, conciliate",
        "11. B. easygoing, “live” and “let live” ",
        "12. B. internal, reticent, keep to yourself",
        "13. B. look to the future, global perspective, “big picture”",
        "14. B. tender-hearted, merciful",
        "15. B. go with the flow, adapt as you go",
        "16. B. reflective, deliberate",
        "17. B. ideas, dreams, “what could be,” philosophical",
        "18. B. ideas, dreams, “what could be,” philosophical",
        "19. B. sensitive, people-oriented, compassionate",
        "20. B. . latitude, freedom"
    ]

    count_a: int = 0
    count_b: int = 0
    personality: str = ''
    count = 0
    for i in range(len(questions_a)):
        print(questions_a[i] + '\t' + questions_b[i])
        answer = ''
        while not (answer == 'A' or answer == 'B'):
            count_a = 0
            count_b = 0
            try:
                answer = input(i).upper()
                if not (answer == 'A' or answer == 'B'):
                    raise ValueError("Invalid input")
            except ValueError as error:
                print(error)
            else:
                if answer == 'A':
                    count_a = count_a + 1
                if answer == 'B':
                    count_b = count_b + 1
                    count = count + 1

        if count == 5:
            if count_a > count_b:
                personality = personality + 'E'
            else:
                personality = personality + 'I'
        else:
            if count == 10:
                if count_a > count_b:
                    personality = personality + 'S'
                else:
                    personality = personality + 'N'
            else:
                if count == 15:
                    if count_a > count_b:
                        personality = personality + 'T'
                    else:
                        personality = personality + 'F'
                else:
                    if count == 20:
                        if count_a > count_b:
                            personality = personality + 'J'
                        else:
                            personality = personality + 'P'
    show(personality)


def exit_application():
    print("Exiting application....")
    sys.exit(0)


def main():
    user_input = input("""
    Welcome to the Meyers Briggs Personality Test
    Press 1 to take test
    Press 2 to exit application ->
    """)
    try:
        if not (user_input == "1" or user_input == "2"):
            raise ValueError("Invalid input")
    except ValueError as error:
        print(error)
    else:
        switcher = {
            "1": question(),
            "2": exit_application()
        }
        return switcher.get(user_input)()



if __name__ == '__main__':
    main()
