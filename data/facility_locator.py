import csv

def load_facilities(file_path):
    facilities = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            facilities.append(row)
    return facilities


def find_facilities_by_city(facilities, city_name):
    results = []
    for facility in facilities:
        if facility['city'].lower() == city_name.lower():
            results.append(facility)
    return results


def main():
    facilities = load_facilities('data/health_facilities.csv')
    city = input("Enter city name: ")

    matches = find_facilities_by_city(facilities, city)

    if not matches:
        print("No health facilities found for this city.")
    else:
        print(f"\nHealth facilities in {city}:")
        for facility in matches:
            print(f"- {facility['name']} ({facility['type']})")


if __name__ == "__main__":
    main()
