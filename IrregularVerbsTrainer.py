import random


print("Welcome to my irregular verbs training")
play = input("Do you want to play? If you want write to yes: ")
if play.lower() != "yes":
    quit()

print("Oki, let's started! If you want escape game, please write to 'esc'")
score = 0

irregular_verbs_list =  {"jeść": ["eat", "ate", "eaten"],
                        "pić": ["drink", "drank", "drunk"],
                        "rysować": ["draw", "drew", "drawn"],
                        "kosztować": ["cost", "cost", "cost"],
                        "położyć": ["lay", "laid", "laid"], 
                        "odchodzić": ["leave, left, left"]} 
polish_verbs = list(irregular_verbs_list.keys())                       
random.shuffle(polish_verbs)
    
def checking_verbs(polish_verb, english_verbs):
    
    user_forms = []
    for i in range(3):
        form = input("Enter the {} form of the verb '{}': ".format(i + 1, polish_verb))
        if form == "esc":
             quit()
        user_forms.append(form)
    if user_forms == english_verbs:
        print("Congratulations, you are correct!")
        return True
    else:
       print("Unfortunately, that is incorrect. The correct forms are: {}".format(english_verbs))
       return False
for polish_verb in polish_verbs:
    correct = checking_verbs(polish_verb, irregular_verbs_list[polish_verb])
if correct:
         score += 1
print("You got {} out of {} verbs correct.".format(score, len(polish_verbs)))
