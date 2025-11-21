def city_country(city, country, population=None, language=None):
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result

if __name__ == "__main__":
    # three calls for final screenshot
    print(city_country("santiago", "chile"))
    print(city_country("tokyo", "japan", 14000000))
    print(city_country("madrid", "spain", 3200000, "spanish"))
