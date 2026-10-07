probe() {
  name="$1"; shift
  out=$(curl -sS -m 40 -o ./b3.bin -w "%{http_code}|%{content_type}" "$@" 2>./e3.txt)
  echo "=== $name -> $out"
  [ -f ./b3.bin ] && { head -c 260 ./b3.bin | tr -d '\0' | tr -c '[:print:]' ' '; echo; echo "   bytes=$(wc -c < ./b3.bin)"; }
  echo "   err=$(head -c 120 ./e3.txt)"
  rm -f ./b3.bin
}
probe "pollinations-audio" "https://text.pollinations.ai/Hello%20world?model=openai-audio&voice=alloy"
probe "soundoftext" -X POST -H "Content-Type: application/json" -d '{"engine":"Google","data":{"text":"hello world","voice":"en-US"}}' "https://api.soundoftext.com/sounds"
probe "tiktok-tts" -X POST -H "Content-Type: application/json" -d '{"text":"hello world","voice":"en_us_001"}' "https://tiktok-tts.weilnet.workers.dev/api/generation"
probe "ttsmp3" -X POST -d "msg=hello world&lang=Brian&source=ttsmp3" "https://ttsmp3.com/makemp3_new.php"
probe "relatedwords" "https://relatedwords.org/api/related?term=cat"
probe "deepinfra-minilm" -X POST -H "Content-Type: application/json" -d '{"inputs":["hello world"]}' "https://api.deepinfra.com/v1/inference/sentence-transformers/all-MiniLM-L6-v2"
probe "poll-vision" -X POST -H "Content-Type: application/json" -d '{"model":"openai","messages":[{"role":"user","content":[{"type":"text","text":"Caption this image in one sentence."},{"type":"image_url","image_url":{"url":"https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/320px-Cat_November_2010-1a.jpg"}}]}]}' "https://text.pollinations.ai/openai"
probe "marytts-public" "http://mary.dfki.de:59125/process?INPUT_TEXT=hello&INPUT_TYPE=TEXT&OUTPUT_TYPE=AUDIO&AUDIO=WAVE_FILE&LOCALE=en_US"
probe "airforce" -X POST -H "Content-Type: application/json" -d '{"model":"llama-3.1-70b","messages":[{"role":"user","content":"hi"}]}' "https://api.airforce/v1/chat/completions"
probe "wikifier-nokey" -X POST -d "text=Barack Obama visited Berlin&lang=en" "http://www.wikifier.org/annotate-article"
