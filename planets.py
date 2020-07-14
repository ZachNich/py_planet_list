planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])
planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")
planet_list.append("Pluto")
del planet_list[-1]

print(planet_list)