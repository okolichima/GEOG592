# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2023-02-14 14:49:44
"""
import arcpy

def Model():  # Model

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    CITIES = "CITIES"
    intrstat_shp = "C:\\Users\\Chima Okoli\\OneDrive\\Desktop\\Lab3\\intrstat.shp"

    # Process: Select (Select) (analysis)
    intrstat_Select4 = "C:\\Users\\Chima Okoli\\OneDrive\\Desktop\\Lab3\\Geog592.gdb\\intrstat_Select4"
    arcpy.analysis.Select(in_features=intrstat_shp, out_feature_class=intrstat_Select4, where_clause="ROUTE_NUM = 'I90'")

    # Process: Buffer (Buffer) (analysis)
    intrstat_Select_Buffer4 = "C:\\Users\\Chima Okoli\\OneDrive\\Desktop\\Lab3\\Geog592.gdb\\intrstat_Select_Buffer4"
    arcpy.analysis.Buffer(in_features=intrstat_Select4, out_feature_class=intrstat_Select_Buffer4, buffer_distance_or_field="30 Miles", line_side="FULL", line_end_type="ROUND", dissolve_option="NONE", dissolve_field=[], method="PLANAR")

    # Process: Clip (Clip) (analysis)
    Buffer_Clip4 = "C:\\Users\\Chima Okoli\\OneDrive\\Desktop\\Lab3\\Geog592.gdb\\Buffer_Clip4"
    arcpy.analysis.Clip(in_features=CITIES, clip_features=intrstat_Select_Buffer4, out_feature_class=Buffer_Clip4, cluster_tolerance="")

    # Process: Summary Statistics (Summary Statistics) (analysis)
    sumtable4 = "C:\\Users\\Chima Okoli\\OneDrive\\Desktop\\Lab3\\Geog592.gdb\\sumtable4"
    arcpy.analysis.Statistics(in_table=Buffer_Clip4, out_table=sumtable4, statistics_fields=[["POP1990", "SUM"], ["HISPANIC", "SUM"]], case_field=[], concatenation_separator="")

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\Users\Chima Okoli\OneDrive\Desktop\Lab3\Geog592.gdb", workspace=r"C:\Users\Chima Okoli\OneDrive\Desktop\Lab3\Geog592.gdb"):
        Model()