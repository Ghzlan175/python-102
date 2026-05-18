from datetime import datetime
import calendar

people = []
birth_days = []

today = datetime(2021, 1, 1)

while True:
    data = input()

    if data.strip() == "":
        break

    try:
        name, birth = data.split(",")

        name = name.strip().capitalize()
        birth = birth.strip()

        day, month, year = birth.split("-")

        # التحقق من أن القيم أرقام موجبة
        if not (day.isdigit() and month.isdigit() and year.isdigit()):
            print(f"{name}: Invalid date")
            continue

        day = int(day)
        month = int(month)
        year = int(year)

        # التحقق من صحة التاريخ
        birth_date = datetime(year, month, day)

        # حساب العمر
        age = today.year - year

        if (today.month, today.day) < (month, day):
            age -= 1

        # اسم اليوم
        day_name = calendar.day_name[birth_date.weekday()]

        print(f"{name} is {age} years old and she/he was born on {day_name}")

        people.append((name, age))

        # مواليد الأحد
        if day_name == "Sunday":
            birth_days.append(name)

    except:
        print(f"{name}: Invalid date")

# أكبر وأصغر شخص
if len(people) > 1:

    oldest = max(people, key=lambda x: x[1])
    youngest = min(people, key=lambda x: x[1])

    print(f"The oldest one is {oldest[0]}")
    print(f"The youngest one is {youngest[0]}")

else:
    print("There is no oldest or youngest person")

# عدد الأشخاص
print(f"Total People: {len(people)}")

# ترتيب الأشخاص من الأكبر للأصغر
print("\nPeople sorted from oldest to youngest:")

sorted_people = sorted(people, key=lambda x: x[1], reverse=True)

for person in sorted_people:
    print(person[0], "-", person[1])

# طباعة المدخلات بشكل عكسي
print("\nReversed order:")

for person in reversed(people):
    print(person[0])

# الأشخاص المولودون يوم الأحد
print("\nPeople born on Sunday:")

for person in birth_days:
    print(person)