import env

CALENDAR = {
    2024: [
        1,
    ]
}


class Main:
    def __init__(self):
        pass

    def run(self):
        env_year = env.get_year()
        env_day = env.get_day()
        env_part = env.get_part()

        exit = False
        while not exit:
            print("============================================")
            print("Advent of Code")
            print("============================================")
            print("0. Exit")

            year = env_year
            if year is None:
                year = self.menu_year()

            if year is None or year not in CALENDAR.keys():
                continue

            day = env_day
            if day is None:
                day = self.menu_day(year)

            if day is None or day not in CALENDAR[year]:
                continue

            part = env_part
            if part is None:
                part = self.menu_part()

            if part is None or part not in [0, 1, 2]:
                continue

            modules = []

            if part == 0:
                modules.append(__import__(f"{year}.day{str(day).zfill(2)}.1", fromlist=["run"]))
                modules.append(__import__(f"{year}.day{str(day).zfill(2)}.2", fromlist=["run"]))
            else:
                modules.append(__import__(f"{year}.day{str(day).zfill(2)}.{part}", fromlist=["run"]))

            for module in modules:
                run_function = getattr(module, "run", None)

                if run_function is None:
                    print(f"Module day{day}.{part} does not have a 'run' function")
                else:
                    print()
                    run_function()

            if env_year is not None and env_day is not None and env_part is not None:
                exit = True

    def menu_year(self) -> int:
        # Select the year to run
        print("")
        print("Select the year to run:")
        for year in CALENDAR.keys():
            print(f"{year}. Year {year}")

        year = int(input("Enter the year: "))

        if year not in CALENDAR.keys():
            print("Invalid year")
            return None

        return year

    def menu_day(self, year: int) -> int:
        # Create a menu to select the day to run
        print("")
        print("Select the day to run:")
        for day in CALENDAR[year]:
            print(f"{day}. Day {day}")

        day = int(input("Enter the day number: "))
        if day not in CALENDAR[year]:
            print("Invalid day number")
            return None

        return day

    def menu_part(self) -> int:
        # Select the part to run (0, 1 or 2)
        print("")
        print("Select the part to run:")
        print("0. All parts")
        print("1. Part 1")
        print("2. Part 2")

        part = int(input("Enter the part number: "))
        if part not in [0, 1, 2]:
            print("Invalid part number")
            return None

        return part


if __name__ == "__main__":
    main = Main()
    main.run()
