---
intent: EVENT_OUTCOME_RESOLUTION
slug: event-thesportsdb-lookup
status: approved
captured_at: 2026-10-04T18:40:12Z
request_url: https://www.thesportsdb.com/api/v1/json/3/lookupevent.php?id=1036723
content_type: application/json
inputs: |
  event id 1036723
intent_description: |
  Resolves objective real-world event outcomes for prediction markets and conditional contracts using quorum oracles.
answer_requirement: |
  Must state the settled outcome/result of the event asked.
capture_note: |
  pick a finished event id if this one rotates
reviewer_note: "auto_review: [0.75|heuristic] Sports event results present"
reviewed_at: 2026-10-04T18:42:20Z
---

## Raw API output

```json
{
  "events": [
    {
      "idEvent": "1036723",
      "idAPIfootball": "319492",
      "strTimestamp": "2020-09-05T00:30:00",
      "strEvent": "Club Guaraní vs Sportivo Luqueño",
      "strEventAlternate": "Sportivo Luqueño @ Club Guaraní",
      "strFilename": "Paraguayan Primera Division 2020-09-04 Club Guaraní vs Sportivo Luqueño",
      "strSport": "Soccer",
      "idLeague": "4687",
      "strLeague": "Paraguayan Primera Division",
      "strLeagueBadge": "https://r2.thesportsdb.com/images/media/league/badge/k1sbmx1652126723.png",
      "strSeason": "2020",
      "strDescriptionEN": null,
      "strHomeTeam": "Club Guaraní",
      "strAwayTeam": "Sportivo Luqueño",
      "intHomeScore": "3",
      "intHomeScoreExtra": null,
      "intAwayScoreExtra": null,
      "intRound": "18",
      "intAwayScore": "0",
      "intSpectators": null,
      "strOfficial": "",
      "strWeather": null,
      "dateEvent": "2020-09-04",
      "dateEventLocal": null,
      "strTime": "23:30:00",
      "strTimeLocal": null,
      "strGroup": null,
      "idHomeTeam": "138293",
      "strHomeTeamBadge": null,
      "idAwayTeam": "138300",
      "strAwayTeamBadge": null,
      "intScore": null,
      "intScoreVotes": null,
      "strResult": null,
      "idVenue": "18446",
      "strVenue": "Estadio Defensores del Chaco",
      "strCountry": "Paraguay",
      "strCity": null,
      "strPoster": null,
      "strSquare": null,
      "strFanart": null,
      "strThumb": null,
      "strBanner": null,
      "strMap": null,
      "strTweet1": null,
      "strVideo": null,
      "strStatus": "FT",
      "strPostponed": "no",
      "strLocked": "unlocked"
    }
  ]
}
```

## Why this matches (or not)

_[0.75|heuristic] Sports event results present_
