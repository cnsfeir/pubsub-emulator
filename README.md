<br>
<div align="center">
  <img src="https://github.com/cnsfeir/pubsub-emulator/assets/58790635/d39b8ed2-746e-462c-9a9c-c79ede421a63" width="506"/>
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
3. Provide a simple CRUD interface for managing topics and subscriptions locally.

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
Set an environment variable that points to the location of your JSON configuration file.
```bash
echo 'SERVICE_MAPPINGS_PATH=service-mappings.json' >> .env
```

<br>

# Setup

Ensure that all necessary dependencies are installed.
```bash
poetry install
```

Set the `PROJECT_ID` environment variable to your Google Cloud project ID.
```bash
echo 'PROJECT_ID=my-project' >> .env
```

Start the Pub/Sub emulator by executing this command in a new terminal tab or window. [^2]
```bash
gcloud beta emulators pubsub start
```

Set up the required environment variables for the Pub/Sub emulator connection to work. [^3]
```bash
$(gcloud beta emulators pubsub env-init)
```

<br>

# Usage

### Importing Cloud Pub/Sub Configuration

Synchronize your cloud configuration with the local emulator to ensure that your local environment mirrors the cloud setup with the appropriate local URLs.
```bash
make sync
```
### Running CLI Commands

Execute commands in `pubsub-emulator` through Poetry using the following syntax:
```bash
poetry run python pubsub_emulator <COMMAND>
```
Replace `<COMMAND>` with the specific command you wish to execute.<br>This method ensures that your commands run within the project's virtual environment.

### Accessing Help

To view a list of all available commands and their options in `pubsub-emulator`, you can use the `--help` option.
```bash
poetry run python pubsub_emulator --help
poetry run python pubsub_emulator <COMMAND> --help
```

### Reference Subscriptions Structure
When creating or updating a subscription with `pubsub-emulator`, it's necessary to pass a request object in JSON string format. To ensure you're using the correct structure for this request, refer to the latest subscription structure definitions in [Google's official Pub/Sub Library](https://github.com/googleapis/python-pubsub/blob/265f4106f499ec5d2d01a127ba192404c1836a28/google/pubsub_v1/types/pubsub.py#L589).

<br>

# License
This project is licensed under the [CC BY-NC 4.0 DEED](https://creativecommons.org/licenses/by-nc/4.0/deed.en) (Attribution-NonCommercial 4.0 International), which essentially means you are free to share and adapt the material in this repository, provided you give appropriate credit, indicate if changes were made, and, most importantly, **do not use it for commercial purposes**.

<br>

# Contact

Feel free to reach out through one of the following channels:

- 📧 hello@cristobalsfeir.com
- ✨ [Project Issues](https://github.com/cnsfeir/pubsub-emulator/issues)
- 💼 [LinkedIn](https://www.linkedin.com/in/cnsfeir/)

<br>
<br>

[^1]: I recommend using [Pyenv](https://github.com/pyenv/pyenv) for managing Python versions
[^2]: Since this command can't be executed in the background
[^3]: For more details about this command visit the [official Pub/Sub emulator guide](https://cloud.google.com/pubsub/docs/emulator?hl=en#env)

