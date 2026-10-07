probe() {
  name="$1"; shift
  out=$(curl -sSL -m 40 -o ./b5.bin -w "%{http_code}|%{content_type}" "$@" 2>./e5.txt)
  echo "=== $name -> $out"
  [ -f ./b5.bin ] && { head -c 300 ./b5.bin | tr -d '\0' | tr -c '[:print:]' ' '; echo; echo "   bytes=$(wc -c < ./b5.bin)"; }
  echo "   err=$(head -c 120 ./e5.txt)"
  rm -f ./b5.bin
}
probe "airforce-models-L" "https://api.airforce/v1/models"
probe "semanticscholar-retry" "https://api.semanticscholar.org/graph/v1/paper/search?query=crispr&limit=1&fields=title,abstract,year"
probe "poll-get-classify" "https://text.pollinations.ai/Classify%20the%20intent%20of%20%22book%20me%20a%20flight%20to%20Paris%22%20as%20one%20of%20book_flight,%20check_weather,%20play_music.%20Answer%20with%20the%20label%20only."
probe "libretranslate-detect-L" -X POST -H "Content-Type: application/json" -d '{"q":"Bonjour le monde"}' "https://libretranslate.com/detect"
probe "typegpt" -X POST -H "Content-Type: application/json" -d '{"model":"gpt-4o-mini","messages":[{"role":"user","content":"hi"}]}' "https://chat.typegpt.net/v1/chat/completions"
probe "jina-embeddings-nokey" -X POST -H "Content-Type: application/json" -d '{"model":"jina-embeddings-v3","input":["hello"]}' "https://api.jina.ai/v1/embeddings"
probe "ores-legacy" "https://ores.wikimedia.org/v3/scores/enwiki?models=articletopic&revids=1255566234"
probe "kagi-fastgpt-nokey" -X POST -H "Content-Type: application/json" -d '{"query":"hi"}' "https://kagi.com/api/v0/fastgpt"
probe "conceptnet-query" "https://api.conceptnet.io/query?node=/c/en/cat&other=/c/en/dog"
probe "textprocessing-phrases" -X POST -d "text=Machine learning models for natural language processing are improving rapidly" "https://text-processing.com/api/phrases/"
