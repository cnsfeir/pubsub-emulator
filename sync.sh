$(gcloud beta emulators pubsub env-init)

gcloud pubsub topics list --format=json > topics.json
gcloud pubsub subscriptions list --format=json > subscriptions.json

poetry run python sync.py

rm topics.json
rm subscriptions.json

poetry run python main.py fetch-topics
poetry run python main.py fetch-subscriptions
