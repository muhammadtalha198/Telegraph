probe() {
  name="$1"; shift
  out=$(curl -sSL -m 40 -o ./b7.bin -w "%{http_code}|%{content_type}" "$@" 2>./e7.txt)
  echo "=== $name -> $out"
  [ -f ./b7.bin ] && { head -c 260 ./b7.bin | tr -d '\0' | tr -c '[:print:]' ' '; echo; echo "   bytes=$(wc -c < ./b7.bin)"; }
  echo "   err=$(head -c 110 ./e7.txt)"
  rm -f ./b7.bin
}
probe "poll-intent-get" "https://text.pollinations.ai/Return%20only%20one%20label%20from%20book_flight%2C%20check_weather%2C%20play_music%20for%3A%20book%20me%20a%20flight%20to%20Paris"
probe "siputzx-gpt3" "https://api.siputzx.my.id/api/ai/gpt3?prompt=You%20are%20helpful&content=Say%20hi"
probe "paxsenix-gpt4o" "https://api.paxsenix.biz.id/ai/gpt4o?text=say%20hi"
probe "widipe-ai" "https://widipe.com/ai?text=say%20hi"
probe "ryzendesu" "https://api.ryzendesu.vip/api/ai/chatgpt?text=say%20hi"
probe "hf-router-nokey" -X POST -H "Content-Type: application/json" -d '{"inputs":"hello"}' "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
probe "cohere-nokey" -X POST -H "Content-Type: application/json" -d '{"texts":["hi"],"model":"embed-english-v3.0","input_type":"search_document"}' "https://api.cohere.com/v2/embed"
probe "nlpcloud-nokey" -X POST -H "Content-Type: application/json" -d '{"text":"hello"}' "https://api.nlpcloud.io/v1/paraphrase-multilingual-mpnet-base-v2/embeddings"
probe "mistral-nokey" -X POST -H "Content-Type: application/json" -d '{"model":"mistral-embed","input":["hi"]}' "https://api.mistral.ai/v1/embeddings"
probe "voyage-nokey" -X POST -H "Content-Type: application/json" -d '{"input":["hi"],"model":"voyage-3"}' "https://api.voyageai.com/v1/embeddings"
