# """
# 2. Напишите программу, которая будет бесконечно спрашивать у пользователя какое слово было загадано, пока тот не напишет это слово. Только когда правильное слово совпадает с загаданным цикл остановится. Также по желанию можно добавлять разные подсказки для пользователя.
# magic_word = “tester “
# """

# def guess_word():
#     magic_word = "tester"
#     while True:
#         guess = input("Угадайте загаданное слово: ")
#         if guess == magic_word:
#             print("Поздравляем! Вы угадали слово!")
#             break
#         else:
#             print("Попробуйте еще раз. Неправильное слово.")

# # Вызов функции для начала игры
# guess_word()

import random
import string
def generate_email_list():
    # 
    # Function generates a list of randomly generated email addresses.
    # Number of emails to generate is provided by user input.

    # :return: List of randomly generated email addresses.
    # :rtype: list
    # """
    
    # Get number of emails to generate from the user
    count = int(input("How many emails do you need? "))
    
    # Initialize an empty list to store the generated email addresses
    email_list = []
    
    # Generate the specified number of email addresses
    for _ in range(count):
        
        # Generate a random username
        # By iterating over a range of 6 characters, we generate a 6-character username
        # Each character is chosen randomly from the lowercase ASCII letters
        username = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
        
        # Choose a random domain from the list
        # The list contains popular email service providers
        domain = random.choice(['gmail.com', 'yahoo.com', 'hotmail.com'])
        
        # Construct the email address by combining the username and domain
        # The f-string is used to insert the username and domain into the email template
        email = f'{username}@{domain}'
        
        # Add the generated email address to the list
        email_list.append(email)
    
    # Return the list of generated email addresses
    return email_list
    return email_list

# Генерация списка email адресов
email_list = generate_email_list()

# Вывод списка email адресов
for email in email_list:
    print(email)

# Создание файла для сохранения email адресов
with open('email_list.txt', 'w') as file:
    for email in email_list:
        file.write(email + '\n')

print("Email list saved to email_list.txt")



# 1.Напишите программу которая запрашивает у пользователя два числа а затем рисует прямоугольник из символов * размером n строк на m столбцов
# Используется вложенные циклы (предположительно for)


# This program prompts the user for two numbers, then draws a rectangle of asterisks
# using nested for loops. The size of the rectangle is determined by the values entered
# for the number of rows and columns.

# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of columns: "))

# # Outer loop controls the number of rows
# for i in range(rows):
#     # Inner loop controls the number of columns
#     for j in range(cols):
#         # Prints an asterisk and moves to the next column
#         print("*", end=" ")
#     # Prints a new line after each row is complete
#     print()

# # Prints a new line after the entire rectangle is drawn
# print()

# #test upload
# #test upload
# #test upload
