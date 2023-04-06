#Jun Liang
#Lab 4 - Q2
import arcpy

arcpy.env.workspace = "T:\\Admin\\Lab4"
arcpy.env.overwriteOutput = True

points1Cursor = arcpy.da.SearchCursor("points1.shp", ["LocID","SHAPE@XY"])

arcpy.CreateFeatureclass_management(arcpy.env.workspace, "points2.shp", "Point")
arcpy.AddField_management("points2.shp", "LocID", "TEXT","","",10)

points2Cursor = arcpy.da.InsertCursor("points2.shp", ["LocID","SHAPE@XY"])
sumX,sumY = 0, 0
count = 0
for point in points1Cursor:
    locationID = point[0]
    x = point[1][0]
    y = point[1][1]
    sumX = sumX + x
    sumY = sumY + y
    count = count + 1

    points2Cursor.insertRow([locationID,(x,y)])

x = sumX/count
y = sumY/count
points2Cursor.insertRow(["MC",(x,y)])
del points2Cursor
del points1Cursor
print ("points2.shp has been created successfully.")

