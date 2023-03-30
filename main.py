import os


class Loader:
    def __init__(self):
        self.folder_path = "files"

    def read_population_data(self, filename: str):
        """
        Функція для зчитування даних про популяцію з файлу
        """
        population_data = {}

        with open(os.path.join(self.folder_path, filename), 'r') as f:
            for line in f:
                country, year, population = line.strip().split(',')
                population = int(population)

                if country in population_data:
                    population_data[country].append((int(year), population))
                else:
                    population_data[country] = [(int(year), population)]

        return population_data

    def process_population_data_change(self, population_data):
        """
        Функція для обробки даних про популяцію з файлу
        """
        population_change = {}

        for country, data in population_data.items():
            data.sort()

            population_change[country] = []

            for i in range(1, len(data)):
                change = data[i][1] - data[i - 1][1]
                population_change[country].append((data[i][0], change))

        return population_change

    def show_data(self, data):
        for country, values in data.items():
            print(country)
            for year, population in values:
                print(f"Year: {year}, Population change: {population}")
            print()


def main():
    loader = Loader()
    filename = 'file.txt'
    population_data = loader.read_population_data(filename)
    population_change = loader.process_population_data_change(population_data)
    loader.show_data(population_change)


if __name__ == "__main__":
    main()
