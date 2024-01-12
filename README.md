<br>
<div align="center">
  <img src="https://github.com/cnsfeir/pubsub-emulator/assets/58790635/cb2b4707-e4a5-40c3-a302-2313167a1e99" width="506"/>
</div>

<br>
<p align="center">
    <em>
      An easy-to-use CLI app for effortlessly managing your local Pub/Sub environment <br> and automatically syncing it with your Google Cloud Pub/Sub configuration.
    </em>
</p>
<br>
<br>

# Motivation

The inspiration for `pubsub-emulator` stemmed from the challenges faced when integrating Pub/Sub into various projects. A key obstacle was the lack of an effective method to replicate the Pub/Sub setup locally. Although [Google Cloud's beta Pub/Sub emulator](https://cloud.google.com/pubsub/docs/emulator) was a step in the right direction, it started as an empty slate each time, missing the crucial topics and subscriptions needed for communication. To address this gap, this project was developed with three core functionalities:

1. Import topics and subscriptions from a GCP project to a local Pub/Sub environment.
2. Automatically translate production push endpoints into local URLs.
3. Provide a simple CRUD interface for managing topics and subscriptions.

<br>

# Prerequisites

- Python `≥3.11` [^1]
- [Poetry](https://python-poetry.org/)
- [Google Cloud Pub/Sub emulator](https://cloud.google.com/pubsub/docs/emulator)

<br>

# Configuring Service Mappings

### 1. Create the JSON File
Start by creating a new JSON file in your project directory.<br>You can name it `service-mappings.json` (or any name you prefer).

### 2.  Define the Mappings
In this file, you'll define a series of key-value pairs where each key is the URL of a cloud service, and the corresponding value is the localhost port to which it should be mapped. For example, if your service URL is `https://some-service-k4caugryxh-cha.run.app` and the corresponding local URL is `localhost:8080`, then your `service-mappings.json` should look like this:
```json
{
  "some-service-k4caugryxh-cha.run.app": 8080
}
```

### 3.  Set the Environment Variable
Set an environment variable to point to the location of your JSON configuration file.
```bash
echo 'SERVICE_MAPPINGS_PATH=service-mappings.json' >> .env
```

<br>

# Setup

### 1. Install Dependencies
Ensure that all necessary dependencies are installed.
```bash
poetry install
```

### 2. Set Project ID Environment Variable
Set the `PROJECT_ID` environment variable to your Google Cloud project ID.
```bash
echo 'PROJECT_ID=my-project' >> .env
```

### 3. Google Cloud Authentication (Optional)
Optionally, if you need to select the correct project in your gcloud CLI and authenticate, run this command:
```bash
make login
```

### 4. Start the Emulator
Open a new terminal tab or window (since this command can't be executed in the background) and start the Pub/Sub emulator.
```bash
make start
```

### 5. Sync Cloud Configuration
Import your Pub/Sub configuration into your local emulator.
```bash
make sync
```

<br>

## Usage

<br>

## License

<br>

## Contact

[^1]: I recommend using [Pyenv](https://github.com/pyenv/pyenv) for managing Python versions

