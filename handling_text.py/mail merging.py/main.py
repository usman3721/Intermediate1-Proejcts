
PLACEHOLDER="[name]"

with open("/Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel\handling_text.py\mail merging.py\input.py/letters/starting_letter.txt") as starting_letter:
    letter=starting_letter.read()
    print(letter)

with open("/Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel\handling_text.py\mail merging.py\input.py/names/invited_names.txt") as invited_guest:
    guest=invited_guest.readlines()
    
    
    for name in guest:
        stripped_name=name.strip()
        print(type(name))
        changed_name=letter.replace(PLACEHOLDER,stripped_name)
        with open(f"/Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel\handling_text.py\mail merging.py\ouput.py/letter_to_{stripped_name}", mode="w") as ready_to_send:
            ready_to_send.write(changed_name)
            


# with open(f"/Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel\handling_text.py\mail merging.py\ouput.py/ReadyToSend/letter_to_{stripped_name}", mode="w") as ready_to_send:
    



  

