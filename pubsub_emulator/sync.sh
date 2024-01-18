echo "\n 🚧 Setting up Pub/Sub emulator"
$(gcloud beta emulators pubsub env-init)

echo "\n 🔎 Fetching topics"
topics=$(gcloud pubsub topics list --format=json)

echo "\n 🔎 Fetching subscriptions"
subscriptions=$(gcloud pubsub subscriptions list --format=json)

echo "\n 💾 Saving data"
data=$(jq -n --argjson topics "$topics" --argjson subscriptions "$subscriptions" '{topics: $topics, subscriptions: $subscriptions}')
echo "$data" > configuration.json

echo "\n 🔄 Syncing..."
poetry run python pubsub_emulator load configuration.json --translate

rm configuration.json
echo "\n ✅ Done! \n"
