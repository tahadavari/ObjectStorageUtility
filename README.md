# ObjectStorageUtility

ObjectStorageUtility is a Python utility for transferring objects between two Amazon S3 buckets. It provides functionalities to compare objects between the source and destination buckets, and transfer objects from the source bucket to the destination bucket.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/ObjectStorageUtility.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Before using ObjectStorageUtility, make sure to set up the configuration file `config.ini`. You can use the provided `config.ini.example` file as a template. Fill in the necessary values for the source and destination buckets.

```ini
[TRANSFER]
SRC_ACCESS_KEY_ID=your_source_access_key_id
SRC_SECRET_ACCESS_KEY=your_source_secret_access_key
SRC_ENDPOINT=your_source_endpoint
SRC_BUCKET_NAME=your_source_bucket_name

DST_ACCESS_KEY_ID=your_destination_access_key_id
DST_SECRET_ACCESS_KEY=your_destination_secret_access_key
DST_ENDPOINT=your_destination_endpoint
DST_BUCKET_NAME=your_destination_bucket_name
```

## Usage

### 1. compare_objects.py

This script compares objects between the source and destination buckets.

```bash
python compare_objects.py
```

### 2. transfer_object.py

This script transfers objects from the source bucket to the destination bucket.

```bash
python transfer_object.py
```

## Files

1. **compare_objects.py**: Compares objects between the source and destination buckets.
2. **get_list_of_bucket_object.py**: Provides functions to retrieve a list of objects from a bucket.
3. **transfer_object.py**: Transfers objects from the source bucket to the destination bucket.
4. **config.ini.example**: Example configuration file. Rename it to `config.ini` and fill in the required values.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)
