# Задача №4. Брой думи
# Програмата прочита текст, който може да съдържа:
# — малки и главни латински букви;
# — интервали;
# — препинателни знаци: точка, запетая, удивителен и въпросителен знак;
# — символ –, който в някои случаи означава тире, а в други — дефис.
# Дума е последователност от латински букви и знаци дефис, ограниченая от двата края. Като ограничители се приемат начало на ред, край на ред строки, интервал, препинателен знак и тире. Тирето се отличава от дефиса по това, че отляво и отдясно на знака дефис се пишат букви, а поне от едната страна на тирето има или начало на ред, или край на ред, или интервал, или пррепинателен знак, или още едно тире.
# Напишете програма, определяща, колко са думите в даден ред от текста.
# Вход
# На единствения ред на стандартния вход се въвежда низ с неповече от 200 знака.
# Изход
# На стандартния изход изведете едно число — броя думи, които се съдържат във въведения текст.

import re

def count_words(text):
    # Използваме регулярен израз, за да намерим всички думи в текста
    words = re.findall(r'\b[\w-]+\b', text)
    return len(words)

# Четем входните данни от потребителя
input_text = input("Въведете текст: ")

# Извикваме функцията за броя на думите
word_count = count_words(input_text)

# Извеждаме резултата
print( word_count)
