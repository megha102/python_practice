def calculate_love_score(name1,name2):
    true_list = list("TRUE".lower())
    love_list = list("LOVE".lower())
    names = (name1 + name2).lower()

    count_true = 0
    count_love = 0
    for i in range(len(names)):
        if names[i] in true_list:
            count_true += 1
        if names[i] in love_list:
            count_love += 1

    love_score = str(count_true) + str(count_love)

    print(f"Love Score= {love_score}")

calculate_love_score(name1="Angela Yu", name2="Jack Bauer")
