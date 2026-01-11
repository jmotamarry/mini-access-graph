"""
queries the aws iam api to list all users in the account 
(https://docs.aws.amazon.com/cli/latest/reference/iam/list-users.html)

takes that response and puts it in raw_data/raw_aws_data/iam_users.json



queries the aws s3 api to list all buckets in the account
(https://docs.aws.amazon.com/cli/latest/reference/s3api/list-buckets.html)

takes that response and puts it in raw_data/raw_aws_data/s3_buckets.json



queries each bucket from raw_aws_data/all_buckets.json to get its bucket policy
(https://docs.aws.amazon.com/cli/latest/reference/s3api/get-bucket-policy.html)

takes those responses and creates a json for each bucket in raw_data/raw_aws_data/bucket_policies/{bucket_name}.json
"""