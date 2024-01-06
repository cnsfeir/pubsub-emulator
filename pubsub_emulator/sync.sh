$(gcloud beta emulators pubsub env-init)

gcloud pubsub topics list --format=json > topics.json
gcloud pubsub subscriptions list --format=json > subscriptions.json

poetry run python pubsub_emulator/sync.py

rm topics.json
rm subscriptions.json

poetry run python pubsub_emulator fetch-topics
poetry run python pubsub_emulator fetch-subscriptions
