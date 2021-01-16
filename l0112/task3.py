'''Task 3. Проверить, кто из списка людей является другом. Друзьями являются только те люди,
чьи имена состоят из 4 букв.'''

names = ['Sally', 'John', 'Martin', 'Alice', 'Maxim', 'Will']
for name in names:
    if len(name) == 4:
        print(f'{name} - friend!')