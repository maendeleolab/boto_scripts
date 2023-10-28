#!/usr/bin/env python3

import boto3, sys

# Creating a boto3 object for the client to interact with
# the ec2 service in aws
ec2 = boto3.client('ec2', region_name='us-east-1')

# This is a function to describe resources
def describe_resources(name):
  try:
    resources = ec2.describe_vpcs(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': [
                    name,
                ]
            },
        ]
    )
    for item in resources['Vpcs'][0]['Tags']:
      return item['Value']
      #print(resources)
  except Exception as err:
      print(f'Error found: {err}...')

def describe_some():
  resources = ec2.describe_vpcs(
  )
  print(resources)
#describe_some()

# This is a function to describe the resources ids
def describe_ids(name):
  resources = ec2.describe_vpcs(
      Filters=[
	  {
	      'Name': 'tag:Name',
	      'Values': [
		  name,
	      ]
	  },
      ]
  )
  for item in resources['Vpcs']:
      return item['VpcId']
         

#describe_ids()

# This is a function to create resources
def create_resources(name, cidr):
  results = describe_resources(name)
  if results == name:
    print('resource already exists...')
    pass
  elif results != name:
    resources = ec2.create_vpc(
        CidrBlock=cidr,
        #AmazonProvidedIpv6CidrBlock=True|False,
        #Ipv6Pool='string',
        #Ipv6CidrBlock='string',
        #Ipv4IpamPoolId='string',
        #Ipv4NetmaskLength=123,
        #Ipv6IpamPoolId='string',
        #Ipv6NetmaskLength=123,
        #DryRun=True|False,
        InstanceTenancy='default',
        #Ipv6CidrBlockNetworkBorderGroup='string',
        TagSpecifications=[
            {
                'ResourceType': 'vpc',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': name
                    },
                ]
            },
        ]
    )
    return resources

#create_resources()

# This function modifies resources attributes
def modify_resources(resource):
  resources = ec2.modify_vpc_attribute(
      EnableDnsHostnames={
          'Value': True #True|False
      },
      EnableDnsSupport={
          'Value': True #True|False
      },
      VpcId=resource,
      EnableNetworkAddressUsageMetrics={
          'Value': True #True|False
      }
  )
#modify_resources(describe_ids())

# This is a function to delete resources
def delete_resources(resource):
  resources = ec2.delete_vpc(
      VpcId=resource,
      #DryRun=True|False
  )

#delete_resources(describe_ids())
