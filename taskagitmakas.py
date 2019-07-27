import random

game_choices = {
    1: "taş",
    2: "kağıt",
    3: "makas"
}

def who_won(cpu_input, your_input):
    if (cpu_input == 1 and your_input == 2) or \
       (cpu_input == 2 and your_input == 3) or \
       (cpu_input == 3 and your_input == 1):
        return True
    elif cpu_input == your_input :
        return 
    else:
        return False

user_won, cmp_won = 0, 0

while cmp_won != 3 or user_won != 3:
    user_input = input("Taş için 1, Kağıt için 2, Makas için 3: ")
    user_input = int(user_input)
    cmp_input = random.choice(list(game_choices.keys()))
    won = who_won(cmp_input,user_input)

    if won:
        print("Bu el sen kazandın. Yine iyisin.")
        user_won += 1
    elif won is None :
        print("Berabere kaldık.")
    else:
        print("Ha haa ben kazandım.")
        cmp_won += 1

if cmp_won == 3:
    print("Computer Won.")
else:
    print("You won.")
   
