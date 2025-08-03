import boto3

# Replace with your specific values
ami_id = 'ami-0abcdef1234567890'  # Example: ami-02d55cb47e83a99a0 for Ubuntu 20.04 in ap-south-1
instance_type = 't2.micro'
key_pair_name = 'my-ec2-key'
security_group_ids = ['sg-0abcdef1234567890'] # Example: sg-08e1234567890abcde

try:
    ec2 = boto3.resource('ec2')

    instances = ec2.create_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        MinCount=1,
        MaxCount=1,
        KeyName=key_pair_name,
        SecurityGroupIds=security_group_ids
    )

    for instance in instances:
        print(f"New EC2 instance created with ID: {instance.id}")
        # You can add tags, wait for instance to be running, etc.
        instance.wait_until_running()
        print(f"Instance {instance.id} is now running.")

except Exception as e:
    print(f"Error creating EC2 instance: {e}")
