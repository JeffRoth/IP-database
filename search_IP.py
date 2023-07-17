# Import libraries
import os
import pandas as pd
import ipaddress
import matplotlib.pyplot as plt

# Read in agency IP ranges
agency_ip_ranges = pd.read_excel('Agency_IP_ranges.xlsx')
agency_ip_ranges = agency_ip_ranges.dropna(how='all')

# Read in list of unknown IPs
unknown_agencies = pd.read_excel('unknown_agencies.xlsx')
unknown_ips = unknown_agencies['IP']

# Define search function
def search_IP(ip, known_ips_list):
    """
    Searches list of known Agency IP ranges.
    
    Arguments:
        ip             : unknown IP address that you want to search for
        known_ips_list : Agency known IP list to search through
    Returns:
        If match is found, returns IP address with related agency information.
        If not match is found, returns None.
    """
    found_i = 0                                             # set 'found flag' to 0 (default)
    ip_address = ipaddress.ip_address(ip)                   # create ipaddress object for unknown IP
    for index, row in known_ips_list.iterrows():            # iterate through list of known agency IPs
        ip_range = ipaddress.ip_network(row['IP range'])    # if known agency IP is an IP range, create ip_network object
        if ip_address in ip_range:                          # test if unknown IP address exists within known agency IP range
            ip_sort = row['IP sort']
            agency = row['Agency']
            domain = row['Domain']
            description = row['Description']
            type = row['Type']
            city = row['City']
            address = row['Address']
            source = row['Source']
            found_i += 1                                    # found IP address.  Increment the 'found flag'
    if found_i != 0:
        return ip_address.compressed, ip_sort, agency, domain, description, type, city, address, source
    
# Loop through unknown IPs and search for matches
identified_ips_list = []                            # initialize list for identified IPs
unidentified_ips_list = []                          # initialize list of un-identified IPs
for ip in unknown_ips:                              # iterate through list of unknown IPs
    found_ip = search_IP(ip, agency_ip_ranges)      # call search_IP function to search through list of known IPs
    if found_ip is None:
        unidentified_ips_list.append(ip)            # if IP address is not found, add to list of unidentified IPs
    else:
        identified_ips_list.append(found_ip)        # otherwise, add to list of identified IPs

# Create a dataframe to hold known and unknown IPs
identified_ips_df = pd.DataFrame(identified_ips_list, columns=['IP', 'IP Sort', 'Agency', 'Domain', 'Description', 'Type', 'City', 'Address', 'Source'])
unidentified_ips_df = pd.DataFrame(unidentified_ips_list, columns=['IP'])

# Drop duplicate IPs
identified_ips_df.drop_duplicates(inplace=True, subset=['IP'])
unidentified_ips_df.drop_duplicates(inplace=True, subset=['IP'])

# Write out dataframes to CSV
identified_ips_df.to_csv("identified_ips_incl_defender.csv", index=False)
unidentified_ips_df.to_csv("unidentified_ips_incl_defender.csv", index=False)
