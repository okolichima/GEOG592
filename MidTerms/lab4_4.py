#Jun Liang
#Lab 4 - Q4
import arcpy

arcpy.env.workspace = "T:\\Admin\\Lab4"
arcpy.env.overwriteOutput = True

#Read the text file
ptextFile = open("allLines.txt", "r")
allLines = ptextFile.readlines()

arcpy.CreateFeatureclass_management(arcpy.env.workspace, "polylineQ4.shp", "POLYLINE")
arcpy.AddField_management("polylineQ4.shp", "LineID", "TEXT","","",12)
polylineCursor = arcpy.da.InsertCursor("polylineQ4.shp", ["LineID","SHAPE@"])
pt = arcpy.Point()
array = arcpy.Array()
previousID = allLines[0].split()[0]
for aLine in allLines:
    aListValues = aLine.split()
    lineID = aListValues[0]
    x = float(aListValues[6])
    y = float(aListValues[5])
    pt.X = x
    pt.Y = y
    if lineID <> previousID:
        polyline = arcpy.Polyline(array)
        polylineCursor.insert([lineID, polyline])
        previousID = lineID
        array.removeAll()
    array.add(pt)
polyline = arcpy.Polyline(array)
polylineCursor.insertRow([lineID,polyline])

del polylineCursor
ptextFile.close()
print ("polylineQ4 has been created successfully.")

