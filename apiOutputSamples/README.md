# API output samples (Semantic Register V2)

One file per **intent × API/slug**.  
You (Talha) **manually** read each file and mark `approved` before any on-chain register.

```bash
# Capture
python3 scripts/capture_api_output.py \
  --intent WEATHER_CURRENT --slug example-api \
  --url 'https://api.example.com/…' \
  --note 'Open-Meteo current weather'

# After you read the file
python3 scripts/set_sample_status.py \
  --file apiOutputSamples/WEATHER_CURRENT/example-api.md \
  --status approved \
  --note 'Answer is clear: temperature present'
```

Statuses: `pending_review` | `approved` | `rejected`
