text='Hello brother, I am from bangladesh'

upper_text=text.upper()
lower_text=text.lower()
title_text=text.title()
capitalized_text=text.capitalize()
swap_text=text.swapcase()
replace_text = text.replace('Hello','Hi')
split_text= text.split(' ');

# print({upper_text,lower_text,title_text,capitalized_text})

text_2=['Hello', 'brother,', 'I', 'am', 'from', 'bangladesh']

print(" ".join(text_2))


# print(swap_text)
# print(replace_text)
# print(split_text)


text_3="         Hey Brother         "

print(text_3.strip())
print(text_3.rstrip())
print(text_3.lstrip())