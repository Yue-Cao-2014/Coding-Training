import stock
import tableformat
import os
path_prefix = "Python_Mastery/"

def print_table(objects: list, attributes: list[str]):
    clm_wdth = 10
    # "%-10s" to print right-padded
    print(" ".join( "%10s"  % att for att in attributes))
    print((clm_wdth * "-" + " ")*len(attributes))

    for o in objects:
        print(" ".join("%10s" % getattr(o, att) for att in attributes))
