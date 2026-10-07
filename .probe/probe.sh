probe() {
  name="$1"; shift
  out=$(curl -sS -m 30 -o ./body.bin -w "%{http_code}|%{content_type}" "$@" 2>./err.txt)
  echo "=== $name -> $out"
  head -c 240 ./body.bin | tr -d '\0' | tr '\n' ' '
  echo; echo "   bytes=$(wc -c < ./body.bin) err=$(head -c 120 ./err.txt)"
}
probe "streamelements-tts" "https://api.streamelements.com/kappa/v2/speech?voice=Brian&text=Hello%20from%20Telegraph"
probe "google-translate-tts" -A "Mozilla/5.0" "https://translate.google.com/translate_tts?ie=UTF-8&q=hello%20world&tl=en&client=tw-ob"
probe "pollinations-text-get" "https://text.pollinations.ai/What%20is%20the%20capital%20of%20France?model=openai"
probe "conceptnet-relatedness" "https://api.conceptnet.io/relatedness?node1=/c/en/cat&node2=/c/en/dog"
probe "ddg-instant-answer" "https://api.duckduckgo.com/?q=isaac%20newton&format=json&no_html=1"
probe "wikipedia-summary" "https://en.wikipedia.org/api/rest_v1/page/summary/Photosynthesis"
probe "dbpedia-spotlight" -H "Accept: application/json" "https://api.dbpedia-spotlight.org/en/annotate?text=Barack%20Obama%20visited%20Berlin%20to%20discuss%20climate%20policy&confidence=0.5"
probe "text-processing-sentiment" -X POST -d "text=great product i love it" "https://text-processing.com/api/sentiment/"
probe "umbc-sts" "http://swoogle.umbc.edu/StsService/GetStsSim?operation=api&phrase1=dog%20runs&phrase2=puppy%20sprints"
probe "datamuse-ml" "https://api.datamuse.com/words?ml=ringing+in+the+ears&max=5"
