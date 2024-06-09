import json
import random
import time as Time


def up_temperature(info, settings):
    temp = info["temperature"]
    info["temperature"] = round(random.uniform(temp, settings["temperature"][1]), 2)
    print(f"Повышение температуры c {temp} до {info['temperature']} °C")


def less_temperature(info, settings):
    temp = info["temperature"]
    info["temperature"] = round(random.uniform(settings["temperature"][0], temp), 2)
    print(f"Понижение температуры c {temp} до {info['temperature']} °C")


def up_oxygen(info, settings):
    oxy = info["oxygen"]
    info["oxygen"] = round(random.uniform(oxy, settings["oxygen"][1]), 2)
    print(f"Повышение уровня кислорода в воде c {oxy} до {info['oxygen']} мг/л")


def less_oxygen(info, settings):
    oxy = info["oxygen"]
    info["oxygen"] = round(random.uniform(settings["oxygen"][0], oxy), 2)
    print(f"Понижение уровня кислорода в воде c {oxy} до {info['oxygen']} мг/л")


def up_ph(info, settings):
    ph = info["ph"]
    info["ph"] = round(random.uniform(ph, settings["ph"][1]), 2)
    print(f"Повышение уровня pH в воде c {ph} до {info['ph']}")


def less_ph(info, settings):
    ph = info["ph"]
    info["ph"] = round(random.uniform(settings["ph"][0], ph), 2)
    print(f"Понижение уровня pH в воде c {ph} до {info['ph']}")


def up_light(info, settings):
    light = info["light"]
    info["light"] = round(random.uniform(light, settings["light"][1]), 2)
    print(f"Повышение уровня освещенности с {light} до {info['light']} Вт/л")


def less_light(info, settings):
    light = info["light"]
    info["light"] = round(random.uniform(settings["light"][0], light), 2)
    print(f"Понижение уровня освещенности с {light} до {info['light']} Вт/л")


def feedings():
    print("кормление")


def first_setting(data):
    print("Выберите вид рыб, которые будут жить в аквариуме:")
    i = 0
    for name in list(data.keys()):
        i += 1
        print(f"{i}) {name}")
    while True:
        num = input(f"Введите только номер (от 1 до {i}): ")
        try:
            number = int(num)
            fish_name = list(data.keys())[number - 1]
        except ValueError:
            print("Вы ввели неправильное значение.")
        except IndexError:
            print("Вы ввели неправильное число.")
        else:
            break

    print()
    print(f"Вы выбрали {fish_name}")
    print()
    print("Рекомендуемые настройки аквариума для этого типа рыб:")
    print(f"Температура: {data[fish_name]['temperature'][0]} - {data[fish_name]['temperature'][1]} °C")
    print(f"Уровень кислорода: {data[fish_name]['oxygen'][0]} - {data[fish_name]['oxygen'][1]} мг/л")
    print(f"Уровень pH: {data[fish_name]['ph'][0]} - {data[fish_name]['ph'][1]}")
    print(f"Уровень освещённости: {data[fish_name]['light'][0]} - {data[fish_name]['light'][1]} Вт/л")
    print(f"Кормление: {data[fish_name]['feeding']} раз в день.")
    print("В ", end=" ")
    print(f"{data[fish_name]['hours'][0]}", end="")
    for j in range(1, data[fish_name]['feeding']):
        print(f", {data[fish_name]['hours'][j]}", end="")
    print(" часов.")
    print()
    answer = input("Установить рекомендуемые настройки (Yes / No): ")
    print()
    if answer.lower() in ("yes", "y", "да", "д"):
        settings = data[fish_name]
        print("Настройки успешно применены")
        print()
    else:
        settings = dict()
        settings["temperature"] = [0, 0]
        settings["oxygen"] = [0, 0]
        settings["ph"] = [0, 0]
        settings["light"] = [0, 0]
        print("Введите настройки для аквариума")
        print("Температура [20 - 30 °C]:")
        settings["temperature"][0] = int(input("Нижняя граница: "))
        settings["temperature"][1] = int(input("Верхняя граница: "))
        print("Кислород [1 - 10 мг/л]:")
        settings["oxygen"][0] = int(input("Нижняя граница: "))
        settings["oxygen"][1] = int(input("Верхняя граница: "))
        print("pH [5 - 9 pH]:")
        settings["ph"][0] = float(input("Нижняя граница: "))
        settings["ph"][1] = float(input("Верхняя граница: "))
        print("Освещение [0.1 - 1 Вт/л]:")
        settings["light"][0] = float(input("Нижняя граница: "))
        settings["light"][1] = float(input("Верхняя граница: "))
        settings["feeding"] = int(input("Сколько раз в день кормление: "))
        settings["hours"] = [int(i) for i in input("Введите часы кормления (через пробел): ").split()]
        print()
        print("Настройки успешно применены")
    return settings


def get_information():
    info = dict()
    info["temperature"] = round(random.uniform(20, 30), 2)
    info["oxygen"] = round(random.uniform(1, 10), 2)
    info["ph"] = round(random.uniform(5, 9), 2)
    info["light"] = round(random.uniform(0.1, 1), 2)
    return info


def control(settings):
    info = get_information()
    if info["temperature"] < settings["temperature"][0]:
        up_temperature(info, settings)
    elif info["temperature"] > settings["temperature"][1]:
        less_temperature(info, settings)
    else:
        print(f"Температура в норме, {info['temperature']} °C")

    if info["oxygen"] < settings["oxygen"][0]:
        up_oxygen(info, settings)
    elif info["oxygen"] > settings["oxygen"][1]:
        less_oxygen(info, settings)
    else:
        print(f"Уровень кислорода в норме, {info['oxygen']} мг/л")

    if info["ph"] < settings["ph"][0]:
        up_ph(info, settings)
    elif info["ph"] > settings["ph"][1]:
        less_ph(info, settings)
    else:
        print(f"Уровень pH в норме, {info['ph']}")

    if info["light"] < settings["light"][0]:
        up_light(info, settings)
    elif info["light"] > settings["light"][1]:
        less_light(info, settings)
    else:
        print(f"Уровень освещенности в норме, {info['light']} Вт/л")


if __name__ == "__main__":
    with open("Fish.json", "r") as file:
        data = json.load(file)
        settings = first_setting(data)

    start_time = Time.time()
    day = 0
    hour = 0
    while True:
        hour = round(Time.time() - start_time) // 2 % 24
        day = round(Time.time() - start_time) // 2 // 24
        print(f"day {day} time: {hour}:00")
        if hour in settings["hours"]:
            feedings()
        control(settings)
        print()
        Time.sleep(2)
