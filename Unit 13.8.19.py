ticket_price = 0
ticket_amount = input('Введите количество билетов: ')
ticket_amount = int(ticket_amount)
for i in range(ticket_amount):
    i += 1
    participant_age = input(f'Сколько лет {i}-му участнику? ')
    participant_age = int(participant_age)
    if participant_age < 18:
        print('Билет бесплатный')
    elif 25 > participant_age >= 18:
        ticket_price += 990
        print('Стоимость билета: 990 руб.')
    else:
        ticket_price += 1390
        print('Стоимость билета: 1390 руб.')
if ticket_amount > 3:
    if ticket_price > 0:
        ticket_price = ticket_price - ((ticket_price / 100) * 10)
        print(f'Приятная новость! За заказ больше 3-х билетов дарим скидку 10% на сумму заказа.')
        print(f'Итого к оплате: {ticket_price} руб.')
else:
    print(f'Итого к оплате: {ticket_price} руб.')
