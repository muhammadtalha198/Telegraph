---
intent: EVENT_OUTCOME_RESOLUTION
slug: event-thesportsdb-last
status: approved
captured_at: 2026-10-02T07:46:12Z
request_url: https://www.thesportsdb.com/api/v1/json/3/eventslast.php?id=133602
content_type: application/json
inputs: |
  team id 133602
intent_description: |
  Resolves objective real-world event outcomes for prediction markets and conditional contracts using quorum oracles.
answer_requirement: |
  Must state the settled outcome/result of the event asked.
capture_note: |
  sports events only
reviewer_note: "auto_review: [0.80] Contains settled results / completed event"
reviewed_at: 2026-10-02T12:49:15Z
---

## Raw API output

```json
{
  "results": [
    {
      "idEvent": "2594454",
      "idAPIfootball": "1635563",
      "strTimestamp": "2026-09-15T19:00:00",
      "strEvent": "Liverpool vs Tottenham Hotspur",
      "strEventAlternate": "Tottenham Hotspur @ Liverpool",
      "strFilename": "EFL Cup 2026-09-15 Liverpool vs Tottenham Hotspur",
      "strSport": "Soccer",
      "idLeague": "4570",
      "strLeague": "EFL Cup",
      "strLeagueBadge": "https://r2.thesportsdb.com/images/media/league/badge/x1va771565372556.png",
      "strSeason": "2026-2027",
      "strDescriptionEN": "",
      "strHomeTeam": "Liverpool",
      "strAwayTeam": "Tottenham Hotspur",
      "intHomeScore": "3",
      "intHomeScoreExtra": null,
      "intAwayScoreExtra": null,
      "intRound": "32",
      "intAwayScore": "1",
      "intSpectators": null,
      "strOfficial": "",
      "strWeather": "",
      "dateEvent": "2026-09-15",
      "dateEventLocal": "2026-09-15",
      "strTime": "19:00:00",
      "strTimeLocal": "20:00:00",
      "strGroup": "",
      "idHomeTeam": "133602",
      "strHomeTeamBadge": "https://r2.thesportsdb.com/images/media/team/badge/kfaher1737969724.png",
      "idAwayTeam": "133616",
      "strAwayTeamBadge": "https://r2.thesportsdb.com/images/media/team/badge/dfyfhl1604094109.png",
      "intScore": null,
      "intScoreVotes": null,
      "strResult": "",
      "idVenue": "15407",
      "strVenue": "Anfield",
      "strCountry": "England",
      "strCity": "",
      "strPoster": "",
      "strSquare": "",
      "strFanart": null,
      "strThumb": "https://r2.thesportsdb.com/images/media/event/thumb/x31a4g1788782656.jpg",
      "strBanner": "",
      "strMap": null,
      "strTweet1": "",
      "strVideo": "https://www.youtube.com/watch?v=Z2EXAkCRtvY",
      "strStatus": "FT",
      "strPostponed": "no",
      "strLocked": "unlocked"
    }
  ]
}
```

## Why this matches (or not)

_[0.80] Contains settled results / completed event_
