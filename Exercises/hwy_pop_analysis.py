# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2023-02-03 14:26:54
"""
import arcpy


# To allow overwriting outputs change overwriteOutput option to True.
# Set up environment variables
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "T:\\Admin\\Lab3\\lab3\\"

#Section for configuring input data sources
CITIES_SHP = "CITIES.SHP"
intrstat_shp = "intrstat.shp"

#Get user's input for two highway choices
hwyListStr = input("Please types two highways to analyze - Ex: I40 I80\n")
hwyList = hwyListStr.split()
hw1 = hwyList[0]
bufDistStr = input("Please input the buffer distance value here (in miles): Ex - 30\n")

for aHwy in hwyList:
    # Process: Select (Select) (analysis)
    hwy_sel_shp = "hwy_sel.shp"
    arcpy.analysis.Select(intrstat_shp, hwy_sel_shp, "ROUTE_NUM = '"+aHwy+"'")

    # Process: Buffer (Buffer) (analysis)
    hwySelBuf_shp = "hwySelBuf.shp"
    arcpy.analysis.Buffer(hwy_sel_shp, hwySelBuf_shp, bufDistStr+" Miles", "FULL","ROUND","NONE", [], "PLANAR")

    # Process: Clip (Clip) (analysis)
    CITIES_Clip = "CITIES_Clip.shp"
    arcpy.analysis.Clip(CITIES_SHP, hwySelBuf_shp, CITIES_Clip)

    # Process: Summary Statistics (Summary Statistics) (analysis)
    sum_table_dbf = "st"+aHwy+bufDistStr+".dbf"
    arcpy.analysis.Statistics(CITIES_Clip, sum_table_dbf, [["POP1990", "SUM"]])
    print(aHwy+ " just being completed.")
    sumFldName = "SUM_"+"POP1990"
    sumCursor = arcpy.da.SearchCursor(sum_table_dbf, ["FREQUENCY", sumFldName[:10]]) #ArcGIS Pro only keeps the first 10 characters of a field name
    for aRow in sumCursor:
        cityNum = aRow[0]
        sumResult = aRow[1]
        print("Total number of cities in the highway buffer is ", cityNum)
        print(sumFldName + " is ", sumResult)
print("All completed")