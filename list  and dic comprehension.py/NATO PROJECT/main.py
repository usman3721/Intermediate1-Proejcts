
import csv
import pandas as pd
nato_file=pd.read_csv("/Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel\list  and dic comprehension.py/NATO PROJECT/nato_phonetic_alphabet.csv")
phonetic_dict={row.letter:row.code for (index,row) in nato_file.iterrows()}
def generate_nato():  
    user_input=input("Enter a word: ").upper()
    try:
        output_list=[phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry only letters are required..")
        generate_nato()
    else:
        print(output_list)
generate_nato()