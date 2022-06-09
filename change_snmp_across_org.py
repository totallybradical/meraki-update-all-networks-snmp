import getpass
import meraki


# This function loops through org_networks and calls the updateNetworkSnmp API with the appropriate parameters
def updateNetworkSnmp(dashboard, org_networks, access, communityString=None, users=None):
    for network in org_networks: # For each network in org_networks...
        print("Updating SNMP settings for network: {network_name}...".format(network_name=network["name"]))
        # Submit the appropriate updateNetworkSnmp API call
        if access == "none":
            dashboard.networks.updateNetworkSnmp(
                networkId=network["id"],
                access=access
            )
        elif access == "community":
            dashboard.networks.updateNetworkSnmp(
                networkId=network["id"],
                access=access,
                communityString=communityString
            )
        elif access == "users":
            dashboard.networks.updateNetworkSnmp(
                networkId=network["id"],
                access=access,
                users=users
            )


#########
# MAIN
#########
if __name__ == "__main__":
    try:
        API_KEY = getpass.getpass(prompt="Enter API key: ") # Prompt for API key WITHOUT echoing to terminal
        
        # Configure Dashboard object using API_KEY
        dashboard = meraki.DashboardAPI(
            API_KEY,
            suppress_logging=True
        ) 

        orgs = dashboard.organizations.getOrganizations() # Get available organizations
        print()
        print("List of organizations:")
        for idx, org in enumerate(orgs):
            print("{num}) {name}".format(num=(idx+1), name=org["name"])) # List all organizations that user's API key has access to
        
        print()
        user_org_input = input("Which org is being edited? [Type the name as it appears above]: ") # Prompt user for specific org

        # Use user_org_input to select appropriate org from the list
        target_org = None
        for org in orgs:
            if org["name"] == user_org_input.strip():
                target_org = org
        if not target_org:
            raise Exception("Org name [{user_org_input}] not found.".format(user_org_input=user_org_input)) 

        # Get all networks within target_org
        org_networks = dashboard.organizations.getOrganizationNetworks(target_org["id"])

        # Get SNMP Parameters
        print()
        print("Enter SNMP parameters that will be used: ")
        # Prompt user for type of SNMP access
        snmp_access = input("Type of SNMP access? ['none' (disabled), 'community' (V1/V2c), or 'users' (V3)]: ").lower()
        snmp_communitystring = None
        snmp_users_list = None
        if snmp_access not in ["none", "community", "users"]: # Validate user input
            raise Exception("Invalid SNMP access selection [{snmp_access}]".format(snmp_access=snmp_access))
        elif snmp_access == "community": # If SNMP access is community (v1/v2), prompt user for community string
            snmp_communitystring = input("SNMP v1/v2 community string: ")
        elif snmp_access == "users": # If SNMP access is users (v3), prompt user for list of users+passphrases
            snmp_users_list = []
            while True:
                snmp_user_username = input("Enter next SNMP username [leave blank if finished]: ")
                if not snmp_user_username.strip():
                    break
                snmp_user_passphrase = input("Enter SNMP passphrase for user {snmp_user_username}: ".format(snmp_user_username=snmp_user_username))
                snmp_user = {
                    "username": snmp_user_username,
                    "passphrase": snmp_user_passphrase
                }
                snmp_users_list.append(snmp_user)


        # #################
        # WARNING MESSAGE
        # #################
        print()
        print("WARNING: This will edit settings on {total_networks} networks!".format(total_networks=len(org_networks)))
        proceed = input("Proceed? [y/n]: ").lower()
        if proceed != "y":
            raise Exception("User cancelled configuration change.")
        print()
        
        # Call function to loop through networks, and update SNMP based on selections
        updateNetworkSnmp(
            dashboard=dashboard, # Pass dashboard object
            org_networks=org_networks, # Pass list of networks
            access=snmp_access, # Pass snmp_access string
            communityString=snmp_communitystring, # Pass community string (if needed)
            users=snmp_users_list # Pass list of snmp users (if needed)
        )

        print()
        print("SNMP settings updated successfully!")
    # Wrap everything in try/except to catch any errors/exceptions    
    except Exception as error:
        print('ERROR: ', error)
