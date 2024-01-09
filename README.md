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

## Motivation

The inspiration for `pubsub-emulator` stemmed from the challenges faced when integrating Pub/Sub into various projects. A key obstacle was the lack of an effective method to replicate the Pub/Sub setup locally. Although [Google Cloud's beta Pub/Sub emulator](https://cloud.google.com/pubsub/docs/emulator) was a step in the right direction, it started as an empty slate each time, missing the crucial topics and subscriptions needed for communication. To address this gap, this project was developed with three core functionalities:

1. Import topics and subscriptions from a GCP project to a local Pub/Sub environment.
2. Automatically translate production push endpoints into local URLs.
3. Provide a simple CRUD interface for managing topics and subscriptions.
