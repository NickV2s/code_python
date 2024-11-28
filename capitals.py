city = ["Ankara", "Brassilia", "Dhaka", "Lisbon", "Manilla", "Rome"]
country = ["Turkey", "Brasil", "Bangladesh", "Portugal", "Philippines", "Italy"]
a_dict = {}
for i in range(len(city)):
    a_dict[country[i]]=city[i]
country.sort()
city=[]
for c in country:
    city.append(a_dict[c])
print(city, country)
def mutatingSelectionSort(city,country):
    for i in range(0,len(country)):
        lowest = "z"
        smallest = 0
        for j in range(i,len(country)):
            if country[j]<lowest:
                lowest = country[j]
                smallest = j
        swapper = country[i]
        country[i]=country[smallest]
        country[smallest]=swapper
        swapper = city[i]
        city[i]=city[smallest]
        city[smallest]=swapper
    return city,country
print(mutatingSelectionSort(city,country))

