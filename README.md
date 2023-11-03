# search_IP

Python script for searching unknown IP addresses in a (Excel-based) catalog of known IP addresses.  IP addresses in catalog can either be single IP addresses, or can be an IP range in CIDR (slash) notation.

## Requirements
 
 * pandas
 * ipaddress

## To Install
* Install Python on your machine.
* Install libraries by running `pip install -r requirements.txt`
* This script, and the Agency IP address catalog 'Agency_IP_ranges.xlsx' should both exist in the same folder.

## To Search for unknown IP addresses
* Place an excel workbook with the list of unknown IP addresses in the same folder as this script and the Agency IP address catalog 'Agency_IP_ranges.xlsx'.
* Ensure that the unknown IP addresses are in a column with the header 'IP'.
* Make note of the workbook name, as well as the sheet name in the workbook with the unknown IP addresses.
* Open a windows terminal in the folder.
* Run `python search_IP.py` in the terminal window.
* You will be prompted for the name of the Excel workbook. Type in the name of the file (don't forget to add '.xlsx)
* You will be prompted for the name of the worksheet. Make sure you type it in exactly.
* After processing, 2 new files will be generated: one for identified IP addresses, and one for unidentified IP addresses.
