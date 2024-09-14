import  random
# list of names
names = ['Массалов']
print("Рандомизатор экзаменационных билетов:")
# shuffle the list
random.shuffle(names)
# assign ticket numbers
ticket_numbers = list(range(1, len(names)+16))
random.shuffle(ticket_numbers)

# print the randomized list with ticket numbers
for i in range(len(names)):
    print(f" Билет N{ticket_numbers[i]}. {names[i]}")
print("Успешной защиты!")
