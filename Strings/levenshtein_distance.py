from unittest import result
from wsgiref.validate import InputWrapper
from sympy import substitution
from webob import second


def levenshtein_distance(first_word: str, second_word: str) -> int:
    if len(first_word)<len(second_word):
        return levenshtein_distance(second_word, first_word)    
    if len(second_word)==0:
        return len(first_word)
    previous_row=list(range(len(second_word)+1))
    for i, c1 in enumerate(first_word):
        current_row=[i+1]
        for j, c2 in enumerate(second_word):
            insertions=previous_row[j+1]+1
            deletions=current_row[j]+1
            substitutions=previous_row[j]+(c1!=c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row=current_row
    return previous_row[-1]

if __name__=="__main__":
    first_word=input("Enter the first word:\n").strip()
    second_word=input("Enter the second word:\n").strip()
    result=levenshtein_distance(first_word, second_word)
    print(f"Levenshtein distance between {first_word} and {second_word} is {result}")