# Meraki: Update Network-wide SNMP Settings Across All Networks in an Organization
This prototype automates the updating of all SNMP configurations on all networks within an organization. It utilizes the Meraki Dashboard API to accomplish this at scale.

## Contacts
* Bradford Ingersoll (bingerso@cisco.com)

## Solution Components
* Python 3
* Meraki Dashboard API

## How to obtain a Meraki API Key

In order to use the Cisco Meraki API, you have to enable the API for your organization first. After having enabled API access, you can generate an API key. You can follow the following instructions on how to enable API access and how to generate an API key:

1. Log in to the Cisco Meraki dashboard

2. In the left-hand menu, go to `Organization > Settings > Dasbhoard API access`

3. Click on `Enable access to the Cisco Meraki Dashboard API`

4. Go to `Profile > API access`

5. Under `API access`, click on `Generate API key`

6. Save the API key in a safe place. Please note that the API key will be shown only once for security purposes. In case you lose the key, then you have to revoke the key and regenerate a new key. Moreover, there is a limit of only two API keys per profile. 

> For more information on how to generate an API key, please click here [here](https://documentation.meraki.com/General_Administration/Other_Topics/Cisco_Meraki_Dashboard_API)

> Note: Make sure this API key has write access to both the source and target organization. You can add your account as Full Organization Admin to both organizations by following the instructions [here](https://documentation.meraki.com/General_Administration/Managing_Dashboard_Access/Managing_Dashboard_Administrators_and_Permissions).

## Installation/Configuration

The following commands are executed in the terminal.

1. Create and activate a virtual environment for the project:
   
        # WINDOWS:
        $ py -3 -m venv [add_name_of_virtual_environment_here] 
        $ source [add_name_of_virtual_environment_here]/Scripts/activate
        # MAC:
        $ python3 -m venv [add_name_of_virtual_environment_here] 
        $ source [add_name_of_virtual_environment_here]/bin/activate
        
> For more information about virtual environments, please click [here](https://docs.python.org/3/tutorial/venv.html)

2. Access the created virtual environment folder

        $ cd [add_name_of_virtual_environment_here]

3. Clone this repository

        $ git clone https://github.com/totallybradical/meraki-update-all-networks-snmp.git

4. Access the folder `meraki-update-all-networks-snmp`

        $ cd gmeraki-update-all-networks-snmp

5. Install the dependencies:

        $ pip install -r requirements.txt

## Setup
1. Now it is time to launch the application! Simply type in the following command in your terminal:

        $ python change_snmp_across_org.py

2. Follow the prompts (API key, org selection, SNMP parameters) to execute