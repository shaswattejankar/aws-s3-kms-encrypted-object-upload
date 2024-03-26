import boto3
import json
import base64

def encrypt_data(kms_key_id, data):
    
    kms_client = boto3.client('kms')
    response = kms_client.encrypt(
        KeyId = kms_key_id,
        Plaintext=json.dumps(data)
    )
    b64_encrypted_blob = base64.b64encode(response["CiphertextBlob"])

    # create a local file for encrypted_data.json
    with open('encrypted_data.json', 'wb') as file:
        file.write(b64_encrypted_blob)

    return b64_encrypted_blob

# to decrypt the locally stored blob and print it
def local_decrypt(kms_key_id):

    kms_client = boto3.client('kms')

    with open('encrypted_data.json', 'r') as file:
        _encoded_ = file.read()

    response = kms_client.decrypt(CiphertextBlob=base64.b64decode(_encoded_),KeyId=kms_key_id)
    data = json.loads(response['Plaintext'].decode('utf-8'))
    # print('\njson data : ', data)

def upload_to_s3(data_blob, bucket_name, object_key):
    
    s3_client = boto3.client('s3')
    s3_client.put_object(
        Bucket=bucket_name,
        Key=object_key,
        Body=data_blob
    )

def main():
    kms_key_id=YOUR_SYMMETRIC_KEY_ID
    bucket_name=YOUR_BUCKET_NAME
    file_path="./data.json"
    object_key="encrypted_data.json"

    # read data from file
    with open(file_path, 'r') as file:
        data = file.read()

    # encrypt data
    b64_encrypted_data_blob = encrypt_data(kms_key_id, data)

    # # decrypt locally created data file and print it
    # local_decrypt(kms_key_id)

    # upload the data
    upload_to_s3(b64_encrypted_data_blob, bucket_name, object_key)

if __name__ == "__main__":
    main()
