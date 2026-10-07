probe() {
  name="$1"; shift
  out=$(curl -sS -m 30 -o ./b2.bin -w "%{http_code}|%{content_type}" "$@" 2>./e2.txt)
  echo "=== $name -> $out"
  head -c 260 ./b2.bin | tr -d '\0' | tr -c '[:print:]' ' '
  echo; echo "   bytes=$(wc -c < ./b2.bin) err=$(head -c 120 ./e2.txt)"
  rm -f ./b2.bin
}
probe "hackclub-ai" -X POST -H "Content-Type: application/json" -d '{"messages":[{"role":"user","content":"Say hi in 3 words"}]}' "https://ai.hackclub.com/chat/completions"
probe "pollinations-openai-post" -X POST -H "Content-Type: application/json" -d '{"model":"openai","messages":[{"role":"user","content":"Say hi"}]}' "https://text.pollinations.ai/openai"
probe "omniroute-models" "https://omni-chat.13.237.89.59.sslip.io/v1/models"
probe "wikidata-search" "https://www.wikidata.org/w/api.php?action=wbsearchentities&search=photosynthesis&language=en&format=json"
probe "ddg-ia-retry" "https://api.duckduckgo.com/?q=photosynthesis&format=json&no_html=1&skip_disambig=1"
probe "conceptnet-retry" "https://api.conceptnet.io/relatedness?node1=/c/en/cat&node2=/c/en/dog"
probe "spotlight-demo" -H "Accept: application/json" "https://demo.dbpedia-spotlight.org/en/annotate?text=Barack%20Obama%20visited%20Berlin&confidence=0.5"
probe "popcat-chatbot" "https://api.popcat.xyz/v2/chatbot?msg=hello&owner=me&botname=bot"
probe "affiliateplus-chatbot" "https://api.affiliateplus.xyz/api/chatbot?message=hello&botname=Bot&ownername=Me&user=1"
probe "pollinations-models" "https://text.pollinations.ai/models"
