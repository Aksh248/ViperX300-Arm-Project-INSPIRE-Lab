import robot_func2
import identify_unkown
import weight_check_func
import shelve_meds

# Identify and pick up the new bottle
identify_unkown.identify_new()

# Check the weight of the bottle
weight_check_func.check_weight()

# Place the bottle on the Monday slot
shelve_meds.shelf_meds("Monday")