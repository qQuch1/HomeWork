answer = int(input("Введите любое количество секунд: "))
hours = answer // 3600
residue = answer % 3600
minutes = residue // 60
sec = residue % 60
print(f"{answer} секунд это - {hours}час:{minutes}мин:{sec}сек ")
