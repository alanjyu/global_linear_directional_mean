#!/usr/bin/env python2#-------------------------------------------------------------------------------
"""
Description:

Created by: Alan Yu
"""

import os, arcpy

def main(sourceWorkSpace):
	arcpy.env.overwriteOutput = True
	arcpy.env.workspace = sourceWorkSpace
 	split_shp = arcpy.ListFeatureClasses(feature_type='Arc')

	if not (arcpy.Exists(sourceWorkSpace + '\\ldm')):
		arcpy.CreateFolder_management(sourceWorkSpace, 'ldm')

	ldm_op_list = []

	# linear directional mean for all shape files in source folder
	for shp in split_shp:
		ldm_op = sourceWorkSpace + '\\ldm\\ldm_' + shp  # ldm output
		ldm_op_list.append(ldm_op) # add output to list for merge
		arcpy.DirectionalMean_stats(shp, ldm_op)
		arcpy.AddMessage(shp + ' is mean\'d.')

	# merge
	merge_op = sourceWorkSpace + '\\merged.shp'
	arcpy.AddMessage(merge_op)
	arcpy.Merge_management(ldm_op_list, merge_op)


### -------------------------------- ###

if __name__ == '__main__':
	sourceWorkSpace = arcpy.GetParameterAsText(0)

	# run the script
	main(sourceWorkSpace)
