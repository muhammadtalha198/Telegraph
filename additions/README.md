# MinerCreator additions (from collaborator zip)

Copied from `Downloads/files (1)/` on 2026-10-02.

| File | Role |
|------|------|
| `candidates.json` | 27 GET-only API candidates (gaps vs FX/weather/crypto which are already covered) |
| `make_capture_script.py` | Writes `../capture_all.sh` skipping existing `intentYamls/` slugs + `FILL_` URLs |
| `GAP_REPORT.md` | Coverage table |

**Already generated:** `MinerCreator/capture_all.sh` (24 captures; 3 cross-chain skipped until you supply tx hashes).

**Next:** run `bash capture_all.sh` from `MinerCreator/`, then manually review `apiOutputSamples/`, then approve.

**Secrets:** Do not zip or commit `.env`. Rotate keys if they were in a shared zip.
