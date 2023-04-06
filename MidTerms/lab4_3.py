#Jun Liang
#Lab 4 - Q3
import arcpy

arcpy.env.workspace = "T:\\Admin\\Lab4"
arcpy.env.overwriteOutput = True

#Read the text file
ptextFile = open("oneline.txt", "r")
allLines = ptextFile.readlines()

arcpy.CreateFeatureclass_management(arcpy.env.workspace, "polylineQ3.shp", "POLYLINE")
arcpy.AddField_management("polylineQ3.shp", "LineID", "TEXT","","",12)

polylineCursor = arcpy.da.InsertCursor("polylineQ3.shp", ["LineID","SHAPE@"])
pt = arcpy.Point()
array = arcpy.Array()

for aLine in allLines:
    aListValues = aLine.split()
    lineID = aListValues[0]
    x = float(aListValues[6])
    y = float(aListValues[5])
    pt.X = x
    pt.Y = y
    array.add(pt)

polyline = arcpy.Polyline(array)
polylineCursor.insertRow([lineID,polyline])

del polylineCursor
ptextFile.close()
print ("polylineQ3 has been created successfully.")

