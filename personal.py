person = {
    "first": "Brady",
    "last": "Pitt",
    "hiredate": "2024-09-24"
}

# opening a file this way is not best practice. but more intuitive for beginners ;-)
file = open("personal.csv", "w")
file.write(person["first"] + ";" + person["last"] + ";" + person["hiredate"])
file.close()