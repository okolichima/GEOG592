#Jun Liang
#Lab 4 - Q1
import arcpy

arcpy.env.workspace = "T:\\Admin\\Lab4"
arcpy.env.overwriteOutput = True

locationFile = open("locations.txt","r")
allLines = locationFile.readlines()[1:]

arcpy.CreateFeatureclass_management(arcpy.env.workspace, "points1.shp", "Point")
arcpy.AddField_management("points1.shp", "LocID", "TEXT","","",10)

locationCursor = arcpy.da.InsertCursor("points1.shp", ["LocID","SHAPE@XY"])

for aLine in allLines:
    aListValues = aLine.split(",")
    locationID = aListValues[0]
    x = float(aListValues[1])
    y = float(aListValues[2])

    locationCursor.insertRow([locationID,(x,y)])

del locationCursor
locationFile.close()
print ("points1.shp has been created successfully.")

