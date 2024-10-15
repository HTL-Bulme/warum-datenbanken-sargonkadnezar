fuhrwerk = {
    "brand": "Benz",
    "model": "AMG187",
	"year": "2004"
	"country": "Österreich"
	"performance": "500"
	
    "releasedate": "2024-01-01"
}

# opening a file this way is not best practice. but more intuitive for beginners ;-)
file = open("fuhrwerk.csv", "w")
file.write("{")

file.write(fuhrwerk["brand"] + ";" + fuhrwerk["model"] + ";" + fuhrwerk["releasedate"]+ ";" + fuhrwerk["performance"]+ ";" + fuhrwerk["country"]+ ";" + fuhrwerk["year"])
file.write("}")
file.close()
