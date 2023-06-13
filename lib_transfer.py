import xml.etree.ElementTree as ET
import copy
import re
import pandas as pd

def get_comp_rt_list(sum_report_fname):
    '''
    get compound name list and retention time list from summary report
    sum_report_fname: summary report from Mass Omics
    '''
    df = pd.read_csv(sum_report_fname)

    cmp_name_list = df['Name'].tolist()
    cmp_rt_list = df['RT.median'].tolist()

    return cmp_name_list, cmp_rt_list

def replace_multiple_spaces(string):
    pattern = r'\s+'
    return re.sub(pattern, ' ', string.strip())

def get_elem_spec_copy(root_elem, cmp_name, cmp_rt, new_id=None):
    '''
    cmp_rt: retention time as float
    new_id: compound id in new library
    
    return (None, None) if not hit
    return (comppound element copy, spectrum element copy) if found a hit
    '''
    if "split peak" in cmp_name:
        lib_cmp_name = cmp_name[:cmp_name.index("split")-1].strip()
    else:
        lib_cmp_name = cmp_name.strip()
        
    lib_cmp_name = replace_multiple_spaces(lib_cmp_name)
        
    
    cmp_elem_list = root_elem.findall(".//*[.='{}']..".format(lib_cmp_name))
    if len(cmp_elem_list) > 0: # Check if returns a hit
        cmp_elem = cmp_elem_list[0]

        cmp_id = cmp_elem[1].text
        spec_elem = root_elem.findall(".//{{Quantitation.LibraryDatabase}}Spectrum[{{Quantitation.LibraryDatabase}}CompoundID ='{}']"
                            .format(cmp_id))[0]
        
        # make a copy of the compound element and spectrum element
        cmp_elem_copy = copy.deepcopy(cmp_elem)
        spec_elem_copy = copy.deepcopy(spec_elem)

    else:
        print (cmp_name, "not found in library")
        # no hit found in library, use the first compound in the library and change name and rt
        # add "required manual spectrum entry" in Description
        cmp_elem = root_elem[1]
        cmp_id = cmp_elem[1].text
        spec_elem = root_elem.findall(".//{{Quantitation.LibraryDatabase}}Spectrum[{{Quantitation.LibraryDatabase}}CompoundID ='{}']"
                            .format(cmp_id))[0]
        # make a copy of the compound element and spectrum element
        cmp_elem_copy = copy.deepcopy(cmp_elem)
        spec_elem_copy = copy.deepcopy(spec_elem)
        cmp_elem_copy[3].text = cmp_name
        cmp_elem_copy[4].text = "Required manual spectrum entry"
        
    # replace retention time
    rt_str = "{}".format(cmp_rt)

    cmp_elem_copy[9].text = rt_str
    cmp_elem_copy[3].text = cmp_name
    if new_id:
        cmp_elem_copy[1].text = "{}".format(new_id)
        spec_elem_copy[1].text = "{}".format(new_id)

    return (cmp_elem_copy, spec_elem_copy)

def create_library_from_summary(mass_hunter_lib, summary_report, output_file):
    summary_report_df = pd.read_csv(summary_report)
    mslib_file = mass_hunter_lib
    lib_tree = ET.parse(mslib_file)
    lib_root = lib_tree.getroot()

    cmp_name_list = summary_report_df['Name'].tolist()
    rt_list = summary_report_df['RT.median'].tolist()

    cmp_elem_list = []
    spec_elem_list = []

    for i in range(len(cmp_name_list)):
        cmp_name = cmp_name_list[i]
        cmp_rt = rt_list[i]
        cmp_elem_copy, spec_elem_copy = get_elem_spec_copy(lib_root, cmp_name, cmp_rt, i+1)
        cmp_elem_list.append(cmp_elem_copy)
        spec_elem_list.append(spec_elem_copy)

    # Create new element tree and remove anything under root
    new_tree = copy.deepcopy(lib_tree)
    new_root = new_tree.getroot()

    for child in list(new_root):
        new_root.remove(child)
        
    # copy the first library element to new tree
    new_root.append(copy.deepcopy(lib_root[0]))

    # append all the compound and spectrum elements
    for elem in cmp_elem_list:
        new_root.append(elem)
        
    for spec in spec_elem_list:
        new_root.append(spec)

    new_tree.write(output_file)


# create_library_from_summary("SVB_Total_20160414.mslibrary.xml", "Summary report_NIST_curated.csv", "test_output.xml")