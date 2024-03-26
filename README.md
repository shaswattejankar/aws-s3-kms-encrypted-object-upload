# aws-s3-kms-encrypted-object-upload

This code is a boto3 implementatino that: encrypts the local json data file using a custom aws kms key, and uploads it to s3, also creates a copy locally, and performs decryption on it.

replace <code>OUR_SYMMETRIC_KEY_ID</code>, and <code>YOUR_BUCKET_NAME</code> accordingly
