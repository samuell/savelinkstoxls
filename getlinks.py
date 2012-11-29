import xlwt, urllib, re, sys, optparse

parser = optparse.OptionParser()
parser.add_option("-u","--url",help="The URL from which to scrap links")
parser.add_option("-o","--outfile",help="The filename where to save links (Excel format)")

(options,args) = parser.parse_args()

import sys
if options.url == None:
        sys.exit("You have to specify an URL! Use the -h flag to view options!")
if options.outfile == None:
        sys.exit("You have to specify an outfile! Use the -h flag to view options!")
if not options.outfile.endswith((".xls", ".xlsx")):
        sys.exit("You have to name the outfile with .xls or .xlsx as extension!")

urlopener = urllib.FancyURLopener()
urlobject = urlopener.open(options.url)
data = urlobject.read()
links = re.findall("(http(s)?:\/\/[^\"\'\ \<\>]+)",data)

wb = xlwt.Workbook()
wb.add_sheet("links")
sheet = wb.get_sheet(0)
    
i = 0
for link in links:
    row = sheet.row(i)
    row.set_cell_text(0,link[0])
    i += 1
    
wb.save(options.outfile)
