from typing import Dict, Tuple
FOOD_DB: Dict[str, Tuple[float, float, float, float]] = {
    "apple": (52, 0.26, 0.17, 13.81),
    "banana": (96, 1.29, 0.33, 22.84),
    "orange": (47, 0.94, 0.12, 11.75),
    "strawberry": (33, 0.67, 0.3, 7.68),
    "grapes": (69, 0.72, 0.16, 18.1),
    "blueberry": (57, 0.74, 0.33, 14.49),
    "watermelon": (30, 0.61, 0.15, 7.55),
    "pineapple": (50, 0.54, 0.12, 13.12),
    "mango": (60, 0.82, 0.38, 15.0),
    "pear": (57, 0.36, 0.14, 15.0),
    "chicken breast (cooked)": (165, 31.0, 3.6, 0.0),
    "egg (whole)": (155, 13.0, 11.0, 1.1),
    "salmon (cooked)": (208, 20.4, 13.4, 0.0),
    "tuna (canned in water)": (132, 28.0, 1.0, 0.0),
    "tofu (firm)": (76, 8.0, 4.8, 1.9),
    "milk (whole)": (60, 3.2, 3.3, 4.8),
    "yogurt (plain)": (59, 10.0, 0.4, 3.6),
    "cheddar cheese": (403, 24.9, 33.1, 1.3),
    "bread (white)": (265, 9.0, 3.2, 49.0),
    "bread (brown)": (247, 13.0, 4.2, 41.0),
    "rice (white, cooked)": (130, 2.4, 0.2, 28.0),
    "rice (brown, cooked)": (111, 2.6, 0.9, 23.0),
    "pasta (cooked)": (131, 5.0, 1.1, 25.0),
    "potato (boiled)": (87, 1.87, 0.1, 20.13),
    "sweet potato": (86, 1.6, 0.1, 20.1),
    "lentils (cooked)": (116, 9.0, 0.4, 20.0),
    "chickpeas (cooked)": (164, 8.9, 2.6, 27.4),
    "black beans (cooked)": (132, 8.9, 0.5, 23.7),
    "almonds": (579, 21.15, 49.93, 21.55),
    "peanut butter": (588, 25.0, 50.0, 20.0),
    "walnuts": (654, 15.23, 65.2, 13.71),
    "olive oil": (884, 0.0, 100.0, 0.0),
    "butter": (717, 0.85, 81.11, 0.06),
    "avocado": (160, 2.0, 14.7, 8.5),
    "broccoli": (34, 2.82, 0.37, 6.64),
    "spinach": (23, 2.86, 0.39, 3.63),
    "carrot": (41, 0.93, 0.24, 9.58),
    "tomato": (18, 0.88, 0.2, 3.9),
    "cucumber": (16, 0.65, 0.11, 3.63),
    "onion": (40, 1.1, 0.1, 9.34),
    "garlic": (149, 6.36, 0.5, 33.06),
    "beef (lean, cooked)": (250, 26.1, 15.0, 0.0),
    "pork (cooked)": (242, 27.0, 14.0, 0.0),
    "paneer": (321, 18.0, 25.0, 1.2),
    "oats (dry)": (389, 16.9, 6.9, 66.3),
    "chia seeds": (486, 16.5, 30.7, 42.1),
    "quinoa (cooked)": (120, 4.4, 1.9, 21.3),
    "banana chips": (519, 2.3, 31.0, 58.9),
    "sugar (white)": (387, 0.0, 0.0, 100.0),
    "dark chocolate (70%)": (598, 7.8, 42.6, 46.0),
    "pizza (average)": (266, 11.0, 10.0, 33.0),
    "burger (average)": (295, 17.0, 12.0, 30.0),
    "soft drink (cola)": (39, 0.0, 0.0, 10.6),
    "almond milk (unsweetened)": (15, 0.4, 1.1, 0.3)
}

def find_food(name: str):
    key = name.strip().lower()
    if key in FOOD_DB:
        return key
    for k in FOOD_DB:
        if k.startswith(key) or key in k:
            return k
    return None

def scale_nutrients(nutr, grams: float):
    factor = grams / 100.0
    return tuple(round(x * factor, 2) for x in nutr)

def pretty(n):
    return f"{n:.2f}"

def main():
    print("Calorie & Nutrition Tracker (CLI)")
    daily = {"cal": 0.0, "protein": 0.0, "fat": 0.0, "carbs": 0.0}
    log = []

    while True:
        print("\nOptions: [add] food, [list] foods, [show] totals, [save] log, [help], [exit]")
        cmd = input("Enter option: ").strip().lower()
        if cmd == "add":
            item = input("Food name (e.g. apple, chicken breast): ").strip().lower()
            found = find_food(item)
            if not found:
                print("Food not found in database. Try a different name or add custom entry (type 'custom').")
                cont = input("Add custom food? (y/n): ").strip().lower()
                if cont == "y":
                    name = input("Custom food name: ").strip().lower()
                    try:
                        cal = float(input("Calories per 100g (kcal): ").strip())
                        protein = float(input("Protein per 100g (g): ").strip())
                        fat = float(input("Fat per 100g (g): ").strip())
                        carbs = float(input("Carbs per 100g (g): ").strip())
                        FOOD_DB[name] = (cal, protein, fat, carbs)
                        found = name
                        print(f"Custom food '{name}' added to database.")
                    except ValueError:
                        print("Invalid numbers. Aborting custom entry.")
                        continue
                else:
                    continue
            try:
                grams = float(input("Enter quantity in grams: ").strip())
                if grams <= 0:
                    print("Quantity must be positive.")
                    continue
            except ValueError:
                print("Invalid number for grams.")
                continue
            nutr = scale_nutrients(FOOD_DB[found], grams)
            daily["cal"] += nutr[0]
            daily["protein"] += nutr[1]
            daily["fat"] += nutr[2]
            daily["carbs"] += nutr[3]
            entry = {"food": found, "grams": grams, "nutr": nutr}
            log.append(entry)
            print(f"Added: {found} ({grams} g) -> {pretty(nutr[0])} kcal, P:{pretty(nutr[1])}g, F:{pretty(nutr[2])}g, C:{pretty(nutr[3])}g")
        elif cmd == "list":
            print("Available foods (sample):")
            keys = list(FOOD_DB.keys())
            for i, k in enumerate(keys[:60], 1):
                print(f"{i}. {k}")
            print(f"... total items in DB: {len(keys)}")
        elif cmd == "show":
            print("\nToday's totals:")
            print(f"Calories: {pretty(daily['cal'])} kcal")
            print(f"Protein: {pretty(daily['protein'])} g")
            print(f"Fat: {pretty(daily['fat'])} g")
            print(f"Carbs: {pretty(daily['carbs'])} g")
            advice = []
            cal = daily["cal"]
            if cal == 0:
                print("No food logged yet.")
            else:
                if cal < 1500:
                    advice.append("Calories seem low. Ensure you eat enough for your activity level.")
                elif cal > 3000:
                    advice.append("Calorie intake is high. Monitor portions and avoid excess processed foods.")
                else:
                    advice.append("Calorie intake appears within a typical range.")
                if daily["protein"] < 50:
                    advice.append("Protein intake is low. Consider adding lean protein sources.")
                if daily["fat"] > 90:
                    advice.append("Fat intake is high. Prefer healthy fats (olive oil, nuts) in moderation.")
                if daily["carbs"] > 350:
                    advice.append("Carbohydrate intake is high. Reduce refined carbs and sugary drinks.")
                print("\nSuggestions:")
                for a in advice:
                    print("- " + a)
        elif cmd == "save":
            fname = input("Filename to save log (default: foodlog.txt): ").strip() or "foodlog.txt"
            try:
                with open(fname, "w") as f:
                    f.write("Food log\n")
                    for e in log:
                        f.write(f"{e['food']}\t{e['grams']}g\t{e['nutr'][0]}kcal\tP:{e['nutr'][1]}g\tF:{e['nutr'][2]}g\tC:{e['nutr'][3]}g\n")
                    f.write("\nTotals:\n")
                    f.write(f"Calories: {daily['cal']}\nProtein: {daily['protein']}\nFat: {daily['fat']}\nCarbs: {daily['carbs']}\n")
                print(f"Log saved to {fname}")
            except Exception as ex:
                print("Error saving log:", ex)
        elif cmd == "help":
            print("Commands:\n add - add food entry\n list - show available foods\n show - display today's totals and advice\n save - save food log to a file\n exit - quit program")
        elif cmd == "exit":
            print("Exiting. Remember to save your log if you need it.")
            break
        else:
            print("Unknown command. Type 'help' for options.")

if __name__ == '__main__':
    main()
