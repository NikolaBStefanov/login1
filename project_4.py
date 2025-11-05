from project_5 import u_name, p_word

while True:
    username = input("Въведи потребителско име: ")

    if username == u_name:
        print("Потребителското име е вярно.")
        password = input("Въведи парола: ")

        if password == p_word:
            print("Добре дошли!")
            break
        else:
            print("Грешна парола. Опитай пак.\n")
    else:
        print("Грешно потребителско име. Опитай пак.\n")
    
