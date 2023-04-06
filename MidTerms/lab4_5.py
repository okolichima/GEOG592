#Jun Liang
#Lab 4 - Q5
import arcpy

arcpy.env.workspace = "T:\\Admin\\Lab4"
arcpy.env.overwriteOutput = True
shpFile = "states2010.shp"
numericalFields = arcpy.ListFields(shpFile, '', 'Double') + arcpy.ListFields(shpFile, '', 'Integer')+ arcpy.ListFields(shpFile, '', 'Float')
counter = 0
for aFld in numericalFields:
    print ("<%d>" % counter + aFld.name)
    counter += 1

iChoice = int(raw_input("Please choose a field by typing the corresponding index number.\n"))

statCursor = arcpy.da.SearchCursor(shpFile, [numericalFields[iChoice].name])
total = 0
maximum = -999999999
for aRow in statCursor:
    value = aRow[0]
    total = total + value
    if value > maximum:
        maximum = value
print( maximum)

#Delete cursor objects, calcualte mean, print out results
del aRow,statCursor

#Search for popchg field, if found, do nothing, otherwise, create popchg field, and populate the field
def findField(fieldList, fieldName):
    for fld in fieldList:
        if fld.name == fieldName:
            return True
    return False

# Test to see if the "popchg" field exists
if findField(numericalFields, "popchg"):
    print ("popchg field already exists, deleting .. ")
    arcpy.DeleteField_management(shpFile, ["popchg"])
# Please add a float field named "popchg" here
arcpy.AddField_management(shpFile, "popchg", "FLOAT","10","3")
rows = arcpy.da.UpdateCursor(shpFile, ["POP2000","POP2010","popchg"])
for row in rows:      
    # Please get values for pop2000 and pop2010 using row object
    pop2010 = row[1]
    pop2000 = row[0]
    row[2] = (pop2010-pop2000)* 100.0 / pop2000
    rows.updateRow(row)
del row, rows
 

    


