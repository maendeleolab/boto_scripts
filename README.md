

## [Description](#Description)

We are building modular scripts to build, monitor and manage cloud network infrastructures.<br>
Check out our project board [here](https://github.com/users/maendeleolab/projects/3/views/1?pane=info)

## [Prerequisites](#Prerequisites)

**Note: Must have AWS CLI installed and configured on your system.**<br>
[Follow this link to install awscli v2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) <br>
Create a folder, access the folder then create your virtual environment and activate it.
```
# Create folder
mkdir project
cd project
# Create a virtual environment named "labs"
python3 -m ven labs
# Activate it
source labs/bin/activate
```

Clone the project.
```
git clone https://github.com/maendeleolab/rubiconcloudnetwork.git
# Access your folder
cd rubiconcloudnetwork
```

Install the prerequisites
```
pip install -r requirements.txt
```

## [Folders_structure](#Folders_structure)

```
├── LICENSE
├── README.md
├── aws_org
│   └── template.py
├── network_prerequisites
│   ├── account_profiles.py
│   ├── delete_resources.py
│   ├── network_access_lists_api_calls.py
│   ├── prefix_lists_api_calls.py
│   ├── route_tables_api_calls.py
│   ├── security_groups_api_calls.py
│   ├── subnets_api_calls.py
│   ├── vpcs_api_calls.py
│   └── vpc_template.py
└── requirements.txt
```

## [Usage](#Usage)

Access the network_prerequisites folder to test the available scripts.<br>
Only two scripts are currently available.<br>
1 - vpc_template.py (Deploys a VPC with its prerequisites. Cidr, subnets, route tables and etc...)<br>
2 - delete_resources.py (Deletes all the resources created with the script above.
Check the [wiki page](https://github.com/maendeleolab/rubiconcloudnetwork/wiki).

## [Heads_up!](#Heads_up!)
Updates are done daily. Remember to always perform a "git pull" to get the latest updates.<br> 
Happy rubiconcloudnetworking! 



