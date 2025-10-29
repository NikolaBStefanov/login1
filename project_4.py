u_name = "123_user_123"
p_word = "123456789"

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


