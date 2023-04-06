#Sample Solution for lab3 question 5
import arcpy

arcpy.env.workspace = ".\\"
arcpy.env.overwriteOutput = True

cityShp = "CITIES.shp"
citySelShp = "cities_250000.shp"

arcpy.Select_analysis(cityShp, citySelShp, "\"POP1990\" > 250000")

print("Completed.")
