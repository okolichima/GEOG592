# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2023-02-28 11:57:52
"""
import arcpy
from arcpy.sa import *

def SuitabilityModeling():  # SuitabilityModeling

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    # Check out any necessary licenses.
    arcpy.CheckOutExtension("3D")
    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("ImageAnalyst")

    # Model Environment settings
    with arcpy.EnvManager(extent="439952.113762345 200181.284694512 513122.113762345 253671.284694512 PROJCS["NAD_1983_StatePlane_Vermont_FIPS_4400",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-72.5],PARAMETER["Scale_Factor",0.9999642857142857],PARAMETER["Latitude_Of_Origin",42.5],UNIT["Meter",1.0]],VERTCS["Unknown VCS",VDATUM["Unknown"],PARAMETER["Vertical_Shift",0.0],PARAMETER["Direction",1.0],UNIT["Foot_US",0.3048006096012192]]"):
        Streams = "Streams"
        Elevation = arcpy.Raster("Elevation")
        LandUse = arcpy.Raster("LandUse")

        # Process: Distance Accumulation (Distance Accumulation) (sa)
        Distance_Streams = "C:\\Users\\Chima Okoli\\OneDrive\\Desktop\\GEOG592\\SuitabilityModeling\\Output.gdb\\Distance_Streams"
        Distance_Accumulation = Distance_Streams
        backRaster = "C:\\Users\\Chima Okoli\\OneDrive\\Desktop\\GEOG592\\SuitabilityModeling\\Output.gdb\\backRaster"
        Out_source_direction_raster = ""
        Out_source_location_raster = ""
        Distance_Streams = arcpy.sa.DistanceAccumulation(in_source_data=Streams, in_barrier_data="", in_surface_raster="", in_cost_raster="", in_vertical_raster="", vertical_factor="BINARY 1 -30 30", in_horizontal_raster="", horizontal_factor="BINARY 1 45", out_back_direction_raster=backRaster, out_source_direction_raster=Out_source_direction_raster, out_source_location_raster=Out_source_location_raster, source_initial_accumulation="", source_maximum_accumulation="", source_cost_multiplier="", source_direction="", distance_method="PLANAR")
        Distance_Streams.save(Distance_Accumulation)

        backRaster = arcpy.Raster(backRaster)

        # Process: Slope (Slope) (sa)
        SlopeRaster = "C:\\Users\\Chima Okoli\\OneDrive\\Desktop\\GEOG592\\SuitabilityModeling\\Output.gdb\\SlopeRaster"
        Slope = SlopeRaster
        SlopeRaster = arcpy.sa.Slope(in_raster=Elevation, output_measurement="PERCENT_RISE", z_factor=0.30480060960121924, method="PLANAR", z_unit="METER")
        SlopeRaster.save(Slope)


        # Process: Reclassify (Reclassify) (sa)
        Reclass_Slope = "C:\\Users\\Chima Okoli\\OneDrive\\Desktop\\GEOG592\\SuitabilityModeling\\Output.gdb\\Reclass_Slope"
        Reclassify = Reclass_Slope
        Reclass_Slope = arcpy.sa.Reclassify(in_raster=SlopeRaster, reclass_field="VALUE", remap="0 3 0;3 10 3;10 25 6;25 90 10", missing_values="DATA")
        Reclass_Slope.save(Reclassify)


        # Process: Reclassify (2) (Reclassify) (sa)
        Reclass_Landuse = "C:\\Users\\Chima Okoli\\OneDrive\\Desktop\\GEOG592\\SuitabilityModeling\\Output.gdb\\Reclass_Landuse"
        Reclassify_2_ = Reclass_Landuse
        Reclass_Landuse = arcpy.sa.Reclassify(in_raster=LandUse, reclass_field="VALUE", remap="1 1;2 1;3 1;4 2;5 8;6 10;7 10;8 10;9 6;10 2;11 10;12 1", missing_values="DATA")
        Reclass_Landuse.save(Reclassify_2_)


        # Process: Rescale by Function (Rescale by Function) (sa)
        Rescale_Dist2Stream = "C:\\Users\\Chima Okoli\\OneDrive\\Desktop\\GEOG592\\SuitabilityModeling\\Output.gdb\\Rescale_Dist2Stream"
        Rescale_by_Function = Rescale_Dist2Stream
        Rescale_Dist2Stream = arcpy.sa.RescaleByFunction(in_raster=Distance_Streams, transformation_function=[["MSSMALL", "", "", "", "", 1, 1, ""]], from_scale=1, to_scale=10)
        Rescale_Dist2Stream.save(Rescale_by_Function)


        # Process: Raster Calculator (Raster Calculator) (sa)
        SuitableSites = "c:\\Users\\chima okoli\\OneDrive\\Desktop\\GEOG592\\suitabilitymodeling\\Output.gdb\\SuitableSites"
        Raster_Calculator = SuitableSites
        SuitableSites =  (Reclass_Slope * 0.3) + (Reclass_Landuse * 0.3) + ( Rescale_Dist2Stream *0.4)
        SuitableSites.save(Raster_Calculator)


if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(cartographicCoordinateSystem="PROJCS["NAD_1983_StatePlane_Vermont_FIPS_4400",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-72.5],PARAMETER["Scale_Factor",0.9999642857142857],PARAMETER["Latitude_Of_Origin",42.5],UNIT["Meter",1.0]],VERTCS["Unknown VCS",VDATUM["Unknown"],PARAMETER["Vertical_Shift",0.0],PARAMETER["Direction",1.0],UNIT["Foot_US",0.3048006096012192]]", cellSize="Elevation", mask="Elevation", 
                          outputCoordinateSystem="PROJCS["NAD_1983_StatePlane_Vermont_FIPS_4400",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-72.5],PARAMETER["Scale_Factor",0.9999642857142857],PARAMETER["Latitude_Of_Origin",42.5],UNIT["Meter",1.0]],VERTCS["Unknown VCS",VDATUM["Unknown"],PARAMETER["Vertical_Shift",0.0],PARAMETER["Direction",1.0],UNIT["Foot_US",0.3048006096012192]]", scratchWorkspace=r"C:\Users\Chima Okoli\OneDrive\Desktop\GEOG592\SuitabilityModeling\Output.gdb", snapRaster="Elevation", 
                          workspace=r"C:\Users\Chima Okoli\OneDrive\Desktop\GEOG592\SuitabilityModeling\Output.gdb"):
        SuitabilityModeling()