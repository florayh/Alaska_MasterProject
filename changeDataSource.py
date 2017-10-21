# open the mxd file first
mxd = arcpy.mapping.MapDocument("CURRENT")
# adjust path as necessary
mxd.findAndReplaceWorkspacePaths(r"E:\GIS\IRP_Project\IRP.gdb", r"Q:\WcurrieLab\AlaskaProject\IRP_Project\IRP.gdb")
mxd.save()
del mxd
arcpy.RefreshTOC()
arcpy.RefreshActiveView()
