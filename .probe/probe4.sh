probe() {
  name="$1"; shift
  out=$(curl -sS -m 40 -o ./b4.bin -w "%{http_code}|%{content_type}" "$@" 2>./e4.txt)
  echo "=== $name -> $out"
  [ -f ./b4.bin ] && { head -c 280 ./b4.bin | tr -d '\0' | tr -c '[:print:]' ' '; echo; echo "   bytes=$(wc -c < ./b4.bin)"; }
  echo "   err=$(head -c 120 ./e4.txt)"
  rm -f ./b4.bin
}
probe "yake-inesctec" "http://yake.inesctec.pt/yake/v2/extract_keywords?content=Machine%20learning%20models%20for%20natural%20language%20processing%20are%20improving%20rapidly&max_ngram_size=2&number_of_keywords=5"
probe "semanticscholar" "https://api.semanticscholar.org/graph/v1/paper/search?query=photosynthesis%20efficiency&limit=2&fields=title,abstract,year,url"
probe "openalex" "https://api.openalex.org/works?search=photosynthesis&per-page=2"
probe "stackexchange" "https://api.stackexchange.com/2.3/search/advanced?order=desc&sort=relevance&q=how%20to%20reverse%20a%20list%20in%20python&site=stackoverflow&filter=withbody&pagesize=1"
probe "lift-wing-articletopic" -X POST -H "Content-Type: application/json" -d '{"rev_id": 1234567890}' "https://api.wikimedia.org/service/lw/inference/v1/models/enwiki-articletopic:predict"
probe "libretranslate-de-detect" -X POST -H "Content-Type: application/json" -d '{"q":"Bonjour le monde"}' "https://libretranslate.de/detect"
probe "voicevox-tts-quest" "https://api.tts.quest/v3/voicevox/synthesis?text=hello&speaker=1"
probe "airforce-models" "https://api.airforce/models"
probe "textprocessing-tag" -X POST -d "text=Machine learning improves natural language processing" "https://text-processing.com/api/tag/"
probe "eutils-pubmed" "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=crispr&retmode=json&retmax=2"
