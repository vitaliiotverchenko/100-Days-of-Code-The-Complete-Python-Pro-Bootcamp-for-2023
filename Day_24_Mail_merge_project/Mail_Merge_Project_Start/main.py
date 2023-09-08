#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    

with open("Day_24_Mail_merge_project/Mail_Merge_Project_Start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Day_24_Mail_merge_project/Mail_Merge_Project_Start/Input/Letters/starting_letter.txt") as letter_file:
    blueprint = letter_file.read()

for name in names:
    name = name.strip()
    new_letter = blueprint.replace("[name]", name)
    with open(f"Day_24_Mail_merge_project/Mail_Merge_Project_Start/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_letter_file:
        new_letter_file.write(new_letter)


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp