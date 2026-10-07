probe() {
  name="$1"; shift
  out=$(curl -sSL -m 45 -o ./b6.bin -w "%{http_code}|%{content_type}" "$@" 2>./e6.txt)
  echo "=== $name -> $out"
  [ -f ./b6.bin ] && { head -c 300 ./b6.bin | tr -d '\0' | tr -c '[:print:]' ' '; echo; echo "   bytes=$(wc -c < ./b6.bin)"; }
  echo "   err=$(head -c 120 ./e6.txt)"
  rm -f ./b6.bin
}
probe "airforce-chat-free" -X POST -H "Content-Type: application/json" -d '{"model":"ministral-3b-latest","messages":[{"role":"user","content":"Say hi in three words"}]}' "https://api.airforce/v1/chat/completions"
probe "streamlabs-tts" -X POST -H "Content-Type: application/json" -d '{"voice":"Brian","text":"hello from telegraph"}' "https://streamlabs.com/polly/speak"
probe "wikimedia-core-search" "https://api.wikimedia.org/core/v1/wikipedia/en/search/page?q=photosynthesis&limit=1"
probe "pollinations-get-retry" "https://text.pollinations.ai/What%20is%202%20plus%202?model=openai"
probe "pollinations-post-retry" -X POST -H "Content-Type: application/json" -d '{"model":"openai","messages":[{"role":"system","content":"You are terse."},{"role":"user","content":"What is the capital of Japan?"}]}' "https://text.pollinations.ai/openai"
probe "freetts-play" "https://freetts.com/Home/PlayAudio?Language=en-US&Voice=en-US-Standard-A&TextMessage=hello&type=0"
probe "fakeyou-tts" -X POST -H "Content-Type: application/json" -d '{"uuid_idempotency_token":"abc123","tts_model_token":"TM:ep8m3hjjw27b","inference_text":"hello"}' "https://api.fakeyou.com/tts/inference"
probe "ddg-chat-vqd" -H "x-vqd-accept: 1" "https://duckduckgo.com/duckchat/v1/status"
probe "openrouter-nokey" -X POST -H "Content-Type: application/json" -d '{"model":"meta-llama/llama-3.2-3b-instruct:free","messages":[{"role":"user","content":"hi"}]}' "https://openrouter.ai/api/v1/chat/completions"
probe "groq-nokey" -X POST -H "Content-Type: application/json" -d '{"model":"llama-3.1-8b-instant","messages":[{"role":"user","content":"hi"}]}' "https://api.groq.com/openai/v1/chat/completions"
