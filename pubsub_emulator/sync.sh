echo "\n 🚧 Setting up Pub/Sub emulator"
$(gcloud beta emulators pubsub env-init)

echo "\n 🔎 Fetching topics"
gcloud pubsub topics list --format=json > topics.json

echo "\n 🔎 Fetching subscriptions"
gcloud pubsub subscriptions list --format=json > subscriptions.json

echo "\n 🔄 Syncing..."
poetry run python pubsub_emulator sync

rm topics.json
rm subscriptions.json
echo "\n ✅ Done! \n"
