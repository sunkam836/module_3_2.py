def send_email(message, recipient, *, sender = 'sunkam@rambler.ru') :
    x = "@"
    while 1 > 0:
        if recipient.endswith(('.com', '.ru', '.net')) and sender.endswith((".com", ".ru", ".net")):
            if x not in recipient and sender:
                print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
                break
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
            break
        if sender == recipient:
            print('Нельзя отправить письмо самому себе')
            break
        if sender == 'sunkam@rambler.ru':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
            break
        elif sender != recipient:
            print(f'ВИМАНИЕ! Письмо отправлено с {sender} на {recipient}')
            break

send_email('Это сообщение для проверки связи', 'sunkam@mail.ru')
send_email('Пожалуйста, исправьте задание', 'sunkam@mail.ru', sender='moonlight@rambler.ru')
send_email('Если вы видите это сообщение - все правильно!', 'urban.fanmail.ru', sender='sunkam@rambler.ru')
send_email('Напоминаю самому себе о вебинаре', 'sunkam@rambler.ru', sender='sunkam@rambler.ru')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
