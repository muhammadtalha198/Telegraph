---
intent: EVENT_OUTCOME_RESOLUTION
slug: event-mlb-statsapi
status: pending_review
captured_at: 2026-10-05T09:29:35Z
request_url: https://statsapi.mlb.com/api/v1/schedule?sportId=1&date=2023-11-01
content_type: application/json
inputs: |
  {}
intent_description: |
  Resolves objective real-world event outcomes for prediction markets and conditional contracts using quorum oracles.
answer_requirement: |
  Must state the settled result of the real-world event asked (who won / final outcome).
capture_note: |
  golden-test PASS: MLB Stats API
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "copyright": "Copyright 2026 MLB Advanced Media, L.P.  Use of any content on this page acknowledges agreement to the terms posted here http://gdx.mlb.com/components/copyright.txt",
  "totalItems": 1,
  "totalEvents": 0,
  "totalGames": 1,
  "totalGamesInProgress": 0,
  "dates": [
    {
      "date": "2023-11-01",
      "totalItems": 1,
      "totalEvents": 0,
      "totalGames": 1,
      "totalGamesInProgress": 0,
      "games": [
        {
          "gamePk": 748534,
          "gameGuid": "f3f76a5b-9530-4e02-99f1-40d4ce443e8c",
          "link": "/api/v1.1/game/748534/feed/live",
          "gameType": "W",
          "season": "2023",
          "gameDate": "2023-11-02T00:03:00Z",
          "officialDate": "2023-11-01",
          "status": {
            "abstractGameState": "Final",
            "codedGameState": "F",
            "detailedState": "Final",
            "statusCode": "F",
            "startTimeTBD": false,
            "abstractGameCode": "F"
          },
          "teams": {
            "away": {
              "team": {
                "id": 140,
                "name": "Texas Rangers",
                "link": "/api/v1/teams/140"
              },
              "leagueRecord": {
                "wins": 4,
                "losses": 1,
                "ties": 0,
                "pct": ".800"
              },
              "score": 5,
              "isWinner": true,
              "splitSquad": false,
              "seriesNumber": 1
            },
            "home": {
              "team": {
                "id": 109,
                "name": "Arizona Diamondbacks",
                "link": "/api/v1/teams/109"
              },
              "leagueRecord": {
                "wins": 1,
                "losses": 4,
                "ties": 0,
                "pct": ".200"
              },
              "score": 0,
              "isWinner": false,
              "splitSquad": false,
              "seriesNumber": 1
            }
          },
          "venue": {
            "id": 15,
            "name": "Chase Field",
            "link": "/api/v1/venues/15"
          },
          "content": {
            "link": "/api/v1/game/748534/content"
          },
          "isTie": false,
          "gameNumber": 1,
          "publicFacing": true,
          "doubleHeader": "N",
          "gamedayType": "P",
          "tiebreaker": "N",
          "calendarEventID": "14-748534-2023-11-01",
          "seasonDisplay": "2023",
          "dayNight": "night",
          "description": "World Series Game 5",
          "scheduledInnings": 9,
          "reverseHomeAwayStatus": false,
          "inningBreakLength": 175,
          "gamesInSeries": 7,
          "seriesGameNumber": 5,
          "seriesDescription": "World Series",
          "recordSource": "S",
          "ifNecessary": "N",
          "ifNecessaryDescription": "Normal Game"
        }
      ],
      "events": []
    }
  ]
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
