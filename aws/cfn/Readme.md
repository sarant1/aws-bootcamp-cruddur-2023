## Architecture Guide

Before you run any templates, be sure to create an s3 bucket to contain all artifacts for cloudformation

```
aws s3 mk s3://cfn-artifacts
export CFN_BUCKET="cfn-artifacts-sda"
```

# Bucket names are unique