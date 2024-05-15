
countries_capitals = {
    'Россия': 'Москва',
    'США': 'Вашингтон',
    'Франция': 'Париж',
    'Германия': 'Берлин',
    'Италия': 'Рим'
}

print("a) Перечень стран и их столиц:")
for country, capital in countries_capitals.items():
    print(f"{country}: {capital}")

country_input = input("b) Введите название страны: ")
if country_input in countries_capitals:
    print(f"Столица {country_input}: {countries_capitals[country_input]}")
else:
    print("Такая страна не найдена в списке.")

sorted_countries = sorted(countries_capitals.keys())
print("\nc) Содержимое словаря, отсортированное по названиям стран:")
for country in sorted_countries:
    print(f"{country}: {countries_capitals[country]}")
