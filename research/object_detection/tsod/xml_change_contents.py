# Optional but DO NOT run this script without customizing main() function below

# for i in /path/to/xml_files/*.xml ; do python xml_change_contents.py -f $i ; done

# XML ElementTree does the bulk of the work
import xml.etree.ElementTree as ET

# argparse allows smoother automation and wide reproducability
import argparse


# Use argparse to declare new function options()
# OPTIONS() allows user to either input one filename or run as loop
def options():
    parser = argparse.ArgumentParser(description="Rewriting information in multiple XML files")
    parser.add_argument("-f", "--filename", help="Input name of file.", required=True)
    args = parser.parse_args()
    return args

  
# Don't forget to customize this part!! See below for more info.
def main():
    
    # Pull arguments from options() function
    args = options()
    
    # Pull filename from options() function
    mytree = ET.parse(args.filename)
    
    # Read XML data into environment
    myroot = mytree.getroot()

    # Begin customization
    
    fo = myroot.find("./folder")
    fn = myroot.find("./filename")
    p = myroot.find("./path")

    fo.text = ("folder_name_verify")

    p.text = ("/path_to/verify/" + fn.text)
    
    # End customization
    
    # Replace old XML file with updated XML file
    mytree.write(args.filename)

# Run contents of main()
if __name__ == '__main__':
    main()
