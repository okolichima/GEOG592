# Sample Solution for Lab3, Question 4
import arcpy

arcpy.env.workspace = ".\\"
arcpy.env.overwriteOutput = True

durhamOrangeShp = "orange_durham.shp"
cityShp = "CITIES.shp"
doCitiesShp = "cities_clip.shp"
cityBufShp = "city_buf.shp"

arcpy.Clip_analysis(cityShp, durhamOrangeShp, doCitiesShp)

arcpy.Buffer_analysis(doCitiesShp, cityBufShp, "3 Miles", "FULL", "ROUND", "NONE", "", "PLANAR")

arcpy.Delete_management(doCitiesShp)

print("Completed")
