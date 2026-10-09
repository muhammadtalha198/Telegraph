---
intent: EVENT_OUTCOME_RESOLUTION
slug: event-espn-mlb-scoreboard
status: approved
captured_at: 2026-10-04T18:40:16Z
request_url: https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard?dates=20241030
content_type: application/json
inputs: |
  MLB World Series date
intent_description: |
  Resolves objective real-world event outcomes for prediction markets and conditional contracts using quorum oracles.
answer_requirement: |
  Must state the settled outcome/result of the event asked.
capture_note: |
  (none)
reviewer_note: "auto_review: [0.80|heuristic] Contains settled results / completed event"
reviewed_at: 2026-10-04T18:41:49Z
---

## Raw API output

```json
{
  "leagues": [
    {
      "id": "10",
      "uid": "s:1~l:10",
      "name": "Major League Baseball",
      "abbreviation": "MLB",
      "midsizeName": "MLB",
      "slug": "mlb",
      "season": {
        "year": 2024,
        "startDate": "2024-02-15T08:00Z",
        "endDate": "2024-12-11T07:59Z",
        "displayName": "2024",
        "type": {
          "id": "2",
          "type": 2,
          "name": "Regular Season",
          "abbreviation": "reg"
        }
      },
      "logos": [
        {
          "href": "https://a.espncdn.com/i/teamlogos/leagues/500/mlb.png",
          "width": 500,
          "height": 500,
          "alt": "",
          "rel": [
            "full",
            "default"
          ],
          "lastUpdated": "2023-03-29T12:34Z"
        },
        {
          "href": "https://a.espncdn.com/combiner/i?img=/i/teamlogos/leagues/500-dark/mlb.png&w=500&h=500&transparent=true",
          "width": 500,
          "height": 500,
          "alt": "",
          "rel": [
            "full",
            "dark"
          ],
          "lastUpdated": "2026-10-03T07:46Z"
        }
      ],
      "calendarType": "day",
      "calendarIsWhitelist": false,
      "calendarStartDate": "2024-02-15T08:00Z",
      "calendarEndDate": "2024-12-11T07:59Z",
      "calendar": [
        "2024-02-15T08:00Z",
        "2024-02-16T08:00Z",
        "2024-02-17T08:00Z",
        "2024-02-18T08:00Z",
        "2024-02-19T08:00Z",
        "2024-02-20T08:00Z",
        "2024-02-21T08:00Z",
        "2024-03-27T07:00Z",
        "2024-07-15T07:00Z",
        "2024-07-17T07:00Z",
        "2024-07-18T07:00Z",
        "2024-10-04T07:00Z",
        "2024-10-21T07:00Z",
        "2024-10-22T07:00Z",
        "2024-10-23T07:00Z",
        "2024-10-24T07:00Z",
        "2024-10-27T07:00Z",
        "2024-10-31T07:00Z",
        "2024-11-01T07:00Z",
        "2024-11-02T07:00Z",
        "2024-11-03T07:00Z",
        "2024-11-04T08:00Z",
        "2024-11-05T08:00Z",
        "2024-11-06T08:00Z",
        "2024-11-07T08:00Z",
        "2024-11-08T08:00Z",
        "2024-11-09T08:00Z",
        "2024-11-10T08:00Z",
        "2024-11-11T08:00Z",
        "2024-11-12T08:00Z",
        "2024-11-13T08:00Z",
        "2024-11-14T08:00Z",
        "2024-11-15T08:00Z",
        "2024-11-16T08:00Z",
        "2024-11-17T08:00Z",
        "2024-11-18T08:00Z",
        "2024-11-19T08:00Z",
        "2024-11-20T08:00Z",
        "2024-11-21T08:00Z",
        "2024-11-22T08:00Z",
        "2024-11-23T08:00Z",
        "2024-11-24T08:00Z",
        "2024-11-25T08:00Z",
        "2024-11-26T08:00Z",
        "2024-11-27T08:00Z",
        "2024-11-28T08:00Z",
        "2024-11-29T08:00Z",
        "2024-11-30T08:00Z",
        "2024-12-01T08:00Z",
        "2024-12-02T08:00Z",
        "2024-12-03T08:00Z",
        "2024-12-04T08:00Z",
        "2024-12-05T08:00Z",
        "2024-12-06T08:00Z",
        "2024-12-07T08:00Z",
        "2024-12-08T08:00Z",
        "2024-12-09T08:00Z",
        "2024-12-10T08:00Z"
      ]
    }
  ],
  "events": [
    {
      "id": "401701044",
      "uid": "s:1~l:10~e:401701044",
      "date": "2024-10-31T00:08Z",
      "name": "Los Angeles Dodgers at New York Yankees",
      "shortName": "LAD @ NYY",
      "season": {
        "year": 2024,
        "type": 3,
        "slug": "post-season"
      },
      "competitions": [
        {
          "id": "401701044",
          "uid": "s:1~l:10~e:401701044~c:401701044",
          "date": "2024-10-31T00:08Z",
          "attendance": 49263,
          "type": {
            "id": "17",
            "abbreviation": "FINAL"
          },
          "timeValid": true,
          "neutralSite": false,
          "conferenceCompetition": false,
          "playByPlayAvailable": true,
          "recent": false,
          "wasSuspended": false,
          "venue": {
            "id": "208",
            "fullName": "Yankee Stadium",
            "address": {
              "city": "Bronx",
              "state": "New York"
            },
            "indoor": false
          },
          "competitors": [
            {
              "id": "10",
              "uid": "s:1~l:10~t:10",
              "type": "team",
              "order": 0,
              "homeAway": "home",
              "winner": false,
              "team": {
                "id": "10",
                "uid": "s:1~l:10~t:10",
                "location": "New York",
                "name": "Yankees",
                "abbreviation": "NYY",
                "displayName": "New York Yankees",
                "shortDisplayName": "Yankees",
                "color": "132448",
                "alternateColor": "c4ced4",
                "isActive": true,
                "links": [
                  {
                    "rel": [
                      "clubhouse",
                      "desktop",
                      "team"
                    ],
                    "href": "https://www.espn.com/mlb/team/_/name/nyy/new-york-yankees",
                    "text": "Clubhouse",
                    "isExternal": false,
                    "isPremium": false
                  },
                  {
                    "rel": [
                      "roster",
                      "desktop",
                      "team"
                    ],
                    "href": "https://www.espn.com/mlb/team/roster/_/name/nyy/new-york-yankees",
                    "text": "Roster",
                    "isExternal": false,
                    "isPremium": false
                  },
                  {
                    "rel": [
                      "roster",
                      "sportscenter",
                      "app",
                      "team"
                    ],
                    "href": "sportscenter://x-callback-url/showClubhouse?uid=s:1~l:10~t:10&section=roster",
                    "text": "Roster",
                    "isExternal": false,
                    "isPremium": false
                  },
                  {
                    "rel": [
                      "stats",
                      "desktop",
                      "team"
                    ],
                    "href": "https://www.espn.com/mlb/team/stats/_/name/nyy/new-york-yankees",
                    "text": "Statistics",
                    "isExternal": false,
                    "isPremium": false
                  },
                  {
                    "rel": [
                      "stats",
                      "sportscenter",
                      "app",
                      "team"
                    ],
                    "href": "sportscenter://x-callback-url/showClubhouse?uid=s:1~l:10~t:10&section=stats",
                    "text": "Statistics",
                    "isExternal": false,
                    "isPremium": false
                  },
                  {
                    "rel": [
                      "schedule",
                      "desktop",
                      "team"
                    ],
                    "href": "https://www.espn.com/mlb/team/schedule/_/name/nyy",
                    "text": "Schedule",
                    "isExternal": false,
                    "isPremium": false
                  },
                  {
                    "rel": [
                      "schedule",
                      "sportscenter",
                      "app",
                      "team"
                    ],
                    "href": "sportscenter://x-callback-url/showClubhouse?uid=s:1~l:10~t:10&section=scores",
                    "text": "Schedule",
                    "isExternal": false,
                    "isPremium": false
                  }
                ],
                "logo": "https://a.espncdn.com/i/teamlogos/mlb/500/scoreboard/nyy.png"
              },
              "score": "6",
              "linescores": [
                {
                  "value": 3.0,
                  "displayValue": "3",
                  "period": 1
                },
                {
                  "value": 1.0,
                  "displayValue": "1",
                  "period": 2
                },
                {
                  "value": 1.0,
                  "displayValue": "1",
                  "period": 3
                },
                {
                  "value": 0.0,
                  "displayValue": "0",
                  "period": 4
                },
                {
                  "value": 0.0,
                  "displayValue": "0",
                  "period": 5
                },
                {
                  "value": 1.0,
                  "displayValue": "1",
                  "period": 6
                },
                {
                  "value": 0.0,
                  "displayValue": "0",
                  "period": 7
                },
                {
                  "value": 0.0,
                  "displayValue": "0",
                  "period": 8
                },
                {
                  "value": 0.0,
                  "displayValue": "0",
                  "period": 9
                }
              ],
              "statistics": [
                {
                  "name": "hits",
                  "abbreviation": "H",
                  "displayValue": "8"
                },
                {
                  "name": "runs",
                  "abbreviation": "R",
                  "displayValue": "6"
                },
                {
                  "name": "avg",
                  "abbreviation": "AVG",
                  "displayValue": ".235"
                },
                {
                  "name": "saves",
                  "abbreviation": "SV",
                  "displayValue": "0"
                },
                {
                  "name": "losses",
                  "abbreviation": "L",
                  "displayValue": "1"
                },
                {
                  "name": "wins",
                  "abbreviation": "W",
                  "displayValue": "0"
                },
                {
                  "name": "ERA",
                  "abbreviation": "ERA",
                  "displayValue": "2.00"
                },
                {
                  "name": "errors",
                  "abbreviation": "E",
                  "displayValue": "3"
                }
              ],
              "leaders": [
                {
                  "name": "avg",
                  "displayName": "Batting Average",
                  "shortDisplayName": "BA",
                  "abbreviation": "AVG",
                  "leaders": [
                    {
                      "displayValue": "2-3, HR, 2B, 2 RBI, R, 2 BB",
                      "value": 0.6666666865348816,
                      "athlete": {
                        "id": "33192",
                        "fullName": "Aaron Judge",
                        "displayName": "Aaron Judge",
                        "shortName": "A. Judge",
                        "links": [
                          {
                            "rel": [
                              "playercard",
                              "desktop",
                              "athlete"
                            ],
                            "href": "https://www.espn.com/mlb/player/_/id/33192"
                          }
                        ],
                        "headshot": "https://a.espncdn.com/i/headshots/mlb/players/full/33192.png",
                        "jersey": "99",
                        "position": {
                          "abbreviation": "RF"
                        },
                        "team": {
                          "id": "10"
                        },
                        "active": false
                      },
                      "team": {
                        "id": "10"
                      }
                    }
                  ]
                },
                {
                  "name": "homeRuns",
                  "displayName": "Home Runs",
                  "shortDisplayName": "HR",
                  "abbreviation": "HR",
                  "leaders": [
                    {
                      "displayValue": "1-4, HR, 2 RBI, R",
                      "value": 1.0,
                      "athlete": {
                        "id": "30583",
                        "fullName": "Giancarlo Stanton",
                        "displayName": "Giancarlo Stanton",
                        "shortName": "G. Stanton",
                        "links": [
                          {
                            "rel": [
                              "playercard",
                              "desktop",
                              "athlete"
                            ],
                            "href": "https://www.espn.com/mlb/player/_/id/30583"
                          }
                        ],
                        "headshot": "https://a.espncdn.com/i/headshots/mlb/players/full/30583.png",
                        "jersey": "27",
                        "position": {
                          "abbreviation": "DH"
                        },
                        "team": {
                          "id": "10"
                        },
                        "active": true
                      },
                      "team": {
                        "id": "10"
                      }
                    }
                  ]
                },
                {
                  "name": "RBIs",
                  "displayName": "Runs Batted In",
                  "shortDisplayName": "RBI",
                  "abbreviation": "RBI",
                  "leaders": [
                    {
                      "displayValue": "1-4, HR, 2 RBI, R",
                      "value": 2.0,
                      "athlete": {
                        "id": "30583",
                        "fullName": "Giancarlo Stanton",
                        "displayName": "Giancarlo Stanton",
                        "shortName": "G. Stanton",
                        "links": [
                          {
                            "rel": [
                              "playercard",
                              "desktop",
                              "athlete"
                            ],
                            "href": "https://www.espn.com/mlb/player/_/id/30583"
                          }
                        ],
                        "headshot": "https://a.espncdn.com/i/headshots/mlb/players/full/30583.png",
                        "jersey": "27",
                        "position": {
                          "abbreviation": "DH"
                        },
                        "team": {
                          "id": "10"
                        },
                        "active": true
                      },
                      "team": {
                        "id": "10"
                      }
                    }
                  ]
                },
                {
                  "name": "MLBRating",
                  "displayName": "MLB Rating",
                  "shortDisplayName": "RAT",
                  "abbreviation": "RAT",
                  "leaders": [
                    {
                      "displayValue": "2-3, HR, 2B, 2 RBI, R, 2 BB",
                      "value": 70.25,
                      "athlete": {
                        "id": "33192",
                        "fullName": "Aaron Judge",
                        "displayName": "Aaron Judge",
                        "shortName": "A. Judge",
                        "links": [
                          {
                            "rel": [
                              "playercard",
                              "desktop",
                              "athlete"
                            ],
                            "href": "https://www.espn.com/mlb/player/_/id/33192"
                          }
                        ],
                        "headshot": "https://a.espncdn.com/i/headshots/mlb/players/full/33192.png",
                        "jersey": "99",
                        "position": {
                          "abbreviation": "RF"
                        },
                        "team": {
                          "id": "10"
                        },
                        "active": false
                      },
                      "team": {
                        "id": "10"
                      }
                    }
                  ]
                },
                {
                  "name": "MLBRating",
                  "displayName": "MLB Rating",
                  "shortDisplayName": "MLB",
                  "abbreviation": "MLB",
                  "leaders": [
                    {
                      "displayValue": "2-3, HR, 2B, 2 RBI, R, 2 BB",
                      "value": 70.25,
                      "athlete": {
                        "id": "33192",
                        "fullName": "Aaron Judge",
                        "displayName": "Aaron Judge",
                        "shortName": "A. Judge",
                        "links": [
                          {
                            "rel": [
                              "playercard",
                              "desktop",
                              "athlete"
                            ],
                            "href": "https://www.espn.com/mlb/player/_/id/33192"
                          }
                        ],
                        "headshot": "https://a.espncdn.com/i/headshots/mlb/players/full/33192.png",
                        "jersey": "99",
                        "position": {
                          "abbreviation": "RF"
                        },
                        "team": {
                          "id": "10"
                        },
                        "active": false
                      },
                      "team": {
                        "id": "10"
                      }
                    }
                  ]
                }
              ],
              "probables": [
                {
                  "name": "probableStartingPitcher",
                  "displayName": "Probable Starting Pitcher",
                  "shortDisplayName": "Starter",
                  "abbreviation": "SP",
                  "playerId": 32081,
                  "athlete": {
                    "id": "32081",
                    "fullName": "Gerrit Cole",
                    "displayName": "Gerrit Cole",
                    "shortName": "G. Cole",
                    "links": [
                      {
                        "rel": [
                          "playercard",
                          "desktop",
                          "athlete"
                        ],
                        "href": "https://www.espn.com/mlb/player/_/id/32081"
                      }
                    ],
                    "headshot": "https://a.espncdn.com/i/headshots/mlb/players/full/32081.png",
                    "jersey": "45",
                    "position": "SP",
                    "team": {
                      "id": "10"
                    }
                  },
                  "statistics": [
                    {
                      "name": "saves",
                      "abbreviation": "SV",
                      "displayValue": "0",
                      "rankDisplayValue": "Tied-15th"
                    },
                    {
                      "name": "losses",
                      "abbreviation": "L",
                      "displayValue": "0",
                      "rankDisplayValue": "Tied-39th"
                    },
                    {
                      "name": "wins",
                      "abbreviation": "W",
                      "displayValue": "1",
                      "rankDisplayValue": "Tied-8th"
                    },
                    {
                      "name": "ERA",
                      "abbreviation": "ERA",
                      "displayValue": "2.17",
                      "rankDisplayValue": "16th"
                    },
                    {
                      "name": "errors",
                      "abbreviation": "E",
                      "displayValue": "0",
                      "rankDisplayValue": "Tied-25th"
                    }
                  ],
                  "record": "(1-0, 2.17)"
                }
              ],
              "hits": 8,
              "errors": 3,
              "record": "1-4",
              "records": [
                {
                  "name": "overall",
                  "abbreviation": "Total",
                  "type": "total",
                  "summary": "94-68"
                },
                {
                  "name": "Home",
                  "abbreviation": "Home",
                  "type": "home",
                  "summary": "44-37"
                },
                {
                  "name": "Road",
                  "abbreviation": "AWAY",
                  "type": "road",
                  "summary": "50-31"
                }
              ]
            },
            {
              "id": "19",
              "uid": "s:1~l:10~t:19",
              "type": "team",
              "order": 1,
              "homeAway": "away",
              "winner": true,
              "team": {
                "id": "19",
                "uid": "s:1~l:10~t:19",
                "location": "Los Angeles",
                "name": "Dodgers",
                "abbreviation": "LAD",
                "displayName": "Los Angeles Dodgers",
                "shortDisplayName": "Dodgers",
                "color": "005a9c",
                "alternateColor": "ffffff",
                "isActive": true,
                "links": [
                  {
                    "rel": [
                      "clubhouse",
                      "desktop",
                      "team"
                    ],
                    "href": "https://www.espn.com/mlb/team/_/name/lad/los-angeles-dodgers",
                    "text": "Clubhouse",
                    "isExternal": false,
                    "isPremium": false
                  },
                  {
                    "rel": [
                      "roster",
                      "desktop",
                      "team"
                    ],
                    "href": "https://www.espn.com/mlb/team/roster/_/name/lad/los-angeles-dodgers",
                    "text": "Roster",
                    "isExternal": false,
                    "isPremium": false
                  },
                  {
                    "rel": [
                      "roster",
                      "sportscenter",
                      "app",
                      "team"
                    ],
                    "href": "sportscenter://x-callback-url/showClubhouse?uid=s:1~l:10~t:19&section=roster",
                    "text": "Roster",
                    "isExternal": false,
                    "isPremium": false
                  },
                  {
                    "rel": [
                      "stats",
                      "desktop",
                      "team"
                    ],
                    "href": "https://www.espn.com/mlb/team/stats/_/name/lad/los-angeles-dodgers",
                    "text": "Statistics",
                    "isExternal": false,
                    "isPremium": false
                  },
                  {
                    "rel": [
                      "stats",
                      "sportscenter",
                      "app",
                      "team"
                    ],
                    "href": "sportscenter://x-callback-url/showClubhouse?uid=s:1~l:10~t:19&section=stats",
                    "text": "Statistics",
                    "isExternal": false,
                    "isPremium": false
                  },
                  {
                    "rel": [
                      "schedule",
                      "desktop",
                      "team"
                    ],
                    "href": "https://www.espn.com/mlb/team/schedule/_/name/lad",
                    "text": "Schedule",
                    "isExternal": false,
                    "isPremium": false
                  },
                  {
                    "rel": [
                      "schedule",
                      "sportscenter",
                      "app",
                      "team"
                    ],
                    "href": "sportscenter://x-callback-url/showClubhouse?uid=s:1~l:10~t:19&section=scores",
                    "text": "Schedule",
                    "isExternal": false,
                    "isPremium": false
                  }
                ],
                "logo": "https://a.espncdn.com/i/teamlogos/mlb/500/scoreboard/lad.png"
              },
              "score": "7",
              "linescores": [
                {
                  "value": 0.0,
                  "displayValue": "0",
                  "period": 1
                },
                {
                  "value": 0.0,
                  "displayValue": "0",
                  "period": 2
                },
                {
                  "value": 0.0,
                  "displayValue": "0",
                  "period": 3
                },
                {
                  "value": 0.0,
                  "displayValue": "0",
                  "period": 4
                },
                {
                  "value": 5.0,
                  "displayValue": "5",
                  "period": 5
                },
                {
                  "value": 0.0,
                  "displayValue": "0",
                  "period": 6
                },
                {
                  "value": 0.0,
                  "displayValue": "0",
                  "period": 7
                },
                {
                  "value": 2.0,
                  "displayValue": "2",
                  "period": 8
                },
                {
                  "value": 0.0,
                  "displayValue": "0",
                  "period": 9
                }
              ],
              "statistics": [
                {
                  "name": "hits",
                  "abbreviation": "H",
                  "displayValue": "7"
                },
                {
                  "name": "runs",
                  "abbreviation": "R",
                  "displayValue": "7"
                },
                {
                  "name": "avg",
                  "abbreviation": "AVG",
                  "displayValue": ".206"
                },
                {
                  "name": "saves",
                  "abbreviation": "SV",
                  "displayValue": "1"
                },
                {
                  "name": "losses",
                  "abbreviation": "L",
                  "displayValue": "0"
                },
                {
                  "name": "wins",
                  "abbreviation": "W",
                  "displayValue": "1"
                },
                {
                  "name": "ERA",
                  "abbreviation": "ERA",
                  "displayValue": "6.00"
                },
                {
                  "name": "errors",
                  "abbreviation": "E",
                  "displayValue": "0"
                }
              ],
              "leaders": [
                {
                  "name": "avg",
                  "displayName": "Batting Average",
                  "shortDisplayName": "BA",
                  "abbreviation": "AVG",
                  "leaders": [
                    {
                      "displayValue": "2-4, 2 R, BB",
                      "value": 0.5,
                      "athlete": {
                        "id": "31358",
                        "fullName": "Enrique Hernandez",
                        "displayName": "Enrique Hernandez",
                        "shortName": "E. Hernandez",
                        "links": [
                          {
                            "rel": [
                              "playercard",
                              "desktop",
                              "athlete"
                            ],
                            "href": "https://www.espn.com/mlb/player/_/id/31358"
                          }
                        ],
                        "headshot": "https://a.espncdn.com/i/headshots/mlb/players/full/31358.png",
                        "jersey": "8",
                        "position": {
                          "abbreviation": "3B"
                        },
                        "team": {
                          "id": "19"
                        },
                        "active": true
                      },
                      "team": {
                        "id": "19"
                      }
                    }
                  ]
                },
                {
                  "name": "homeRuns",
                  "displayName": "Home Runs",
                  "shortDisplayName": "HR",
                  "abbreviation": "HR",
                  "leaders": [
                    {
                      "displayValue": "0-0",
                      "value": 0.0,
                      "athlete": {
                        "id": "30189",
                        "fullName": "Ryan Brasier",
                        "displayName": "Ryan Brasier",
                        "shortName": "R. Brasier",
                        "links": [
                          {
                            "rel": [
                              "playercard",
                              "desktop",
                              "athlete"
                            ],
                            "href": "https://www.espn.com/mlb/player/_/id/30189"
                          }
                        ],
                        "headshot": "https://a.espncdn.com/i/headshots/mlb/players/full/30189.png",
                        "jersey": "51",
                        "position": {
                          "abbreviation": "RP"
                        },
                        "team": {
                          "id": "19"
                        },
                        "active": false
                      },
                      "team": {
                        "id": "19"
                      }
                    }
                  ]
                },
                {
                  "name": "RBIs",
                  "displayName": "Runs Batted In",
                  "shortDisplayName": "RBI",
                  "abbreviation": "RBI",
                  "leaders": [
                    {
                      "displayValue": "1-4, 2 RBI, R, BB, K",
                      "value": 2.0,
                      "athlete": {
                        "id": "30193",
                        "fullName": "Freddie Freeman",
                        "displayName": "Freddie Freeman",
                        "shortName": "F. Freeman",
                        "links": [
                          {
                            "rel": [
                              "playercard",
                              "desktop",
                              "athlete"
                            ],
                            "href": "https://www.espn.com/mlb/player/_/id/30193"
                          }
                        ],
                        "headshot": "https://a.espncdn.com/i/headshots/mlb/players/full/30193.png",
                        "jersey": "5",
                        "position": {
                          "abbreviation": "1B"
                        },
                        "team": {
                          "id": "19"
                        },
                        "active": true
                      },
                      "team": {
                        "id": "19"
                      }
                    }
                  ]
                },
                {
                  "name": "MLBRating",
                  "displayName": "MLB Rating",
                  "shortDisplayName": "RAT",
                  "abbreviation": "RAT",
                  "leaders": [
                    {
                      "displayValue": "2-4, 2B, 2 RBI, BB, K",
                      "value": 65.5,
                      "athlete": {
                        "id": "33377",
                        "fullName": "Teoscar Hernandez",
                        "displayName": "Teoscar Hernandez",
                        "shortName": "T. Hernandez",
                        "links": [
                          {
                            "rel": [
                              "playercard",
                              "desktop",
                              "athlete"
                            ],
                            "href": "https://www.espn.com/mlb/player/_/id/33377"
                          }
                        ],
                        "headshot": "https://a.espncdn.com/i/headshots/mlb/players/full/33377.png",
                        "jersey": "37",
                        "position": {
                          "abbreviation": "LF"
                        },
                        "team": {
                          "id": "19"
                        },
                        "active": true
                      },
                      "team": {
                        "id": "19"
                      }
                    }
                  ]
                },
                {
                  "name": "MLBRating",
                  "displayName": "MLB Rating",
                  "shortDisplayName": "MLB",
                  "abbreviation": "MLB",
                  "leaders": [
                    {
                      "displayValue": "2-4, 2B, 2 RBI, BB, K",
                      "value": 65.5,
                      "athlete": {
                        "id": "33377",
                        "fullName": "Teoscar Hernandez",
                        "displayName": "Teoscar Hernandez",
                        "shortName": "T. Hernandez",
                        "links": [
                          {
                            "rel": [
                              "playercard",
                              "desktop",
                              "athlete"
                            ],
                            "href": "https://www.espn.com/mlb/player/_/id/33377"
                          }
                        ],
                        "headshot": "https://a.espncdn.com/i/headshots/mlb/players/full/33377.png",
                        "jersey": "37",
                        "position": {
                          "abbreviation": "LF"
                        },
                        "team": {
                          "id": "19"
                        },
                        "active": true
                      },
                      "team": {
                        "id": "19"
                      }
                    }
                  ]
                }
              ],
              "probables": [
                {
                  "name": "probableStartingPitcher",
                  "displayName": "Probable Starting Pitcher",
                  "shortDisplayName": "Starter",
                  "abbreviation": "SP",
                  "playerId": 33837,
                  "athlete": {
                    "id": "33837",
                    "fullName": "Jack Flaherty",
                    "displayName": "Jack Flaherty",
                    "shortName": "J. Flaherty",
                    "links": [
                      {
                        "rel": [
                          "playercard",
                          "desktop",
                          "athlete"
                        ],
                        "href": "https://www.espn.com/mlb/player/_/id/33837"
                      }
                    ],
                    "headshot": "https://a.espncdn.com/i/headshots/mlb/players/full/33837.png",
                    "jersey": "9",
                    "position": "SP",
                    "team": {
                      "id": "19"
                    }
                  },
                  "statistics": [
                    {
                      "name": "saves",
                      "abbreviation": "SV",
                      "displayValue": "0",
                      "rankDisplayValue": "Tied-15th"
                    },
                    {
                      "name": "losses",
                      "abbreviation": "L",
                      "displayValue": "2",
                      "rankDisplayValue": "Tied-1st"
                    },
                    {
                      "name": "wins",
                      "abbreviation": "W",
                      "displayValue": "1",
                      "rankDisplayValue": "Tied-8th"
                    },
                    {
                      "name": "ERA",
                      "abbreviation": "ERA",
                      "displayValue": "7.36",
                      "rankDisplayValue": "37th"
                    }
                  ],
                  "record": "(1-2, 7.36)"
                }
              ],
              "hits": 7,
              "errors": 0,
              "record": "4-1",
              "records": [
                {
                  "name": "overall",
                  "abbreviation": "Total",
                  "type": "total",
                  "summary": "98-64"
                },
                {
                  "name": "Home",
                  "abbreviation": "Home",
                  "type": "home",
                  "summary": "52-29"
                },
                {
                  "name": "Road",
                  "abbreviation": "AWAY",
                  "type": "road",
                  "summary": "46-35"
                }
              ]
            }
          ],
          "notes": [
            {
              "type": "event",
              "headline": "World Series - Game 5"
            }
          ],
          "status": {
            "clock": 0.0,
            "displayClock": "0:00",
            "period": 9,
            "type": {
              "id": "3",
              "name": "STATUS_FINAL",
              "state": "post",
              "completed": true,
              "description": "Final",
              "detail": "Final",
              "shortDetail": "Final"
            },
            "featuredAthletes": [
              {
                "name": "winningPitcher",
                "displayName": "Winning Pitcher",
                "shortDisplayName": "Win",
                "abbreviation": "WP",
                "playerId": 32185,
                "athlete": {
                  "id": "32185",
                  "fullName": "Blake Treinen",
                  "displayName": "Blake Treinen",
                  "shortName": "B. Treinen",
                  "links": [
                    {
                      "rel": [
                        "playercard",
                        "desktop",
                        "athlete"
                      ],
                      "href": "https://www.espn.com/mlb/player/_/id/32185"
                    }
                  ],
                  "headshot": "https://a.espncdn.com/i/headshots/mlb/players/full/32185.png",
                  "jersey": "49",
                  "position": "RP",
                  "team": {
                    "id": "19"
                  }
                },
                "team": {
                  "id": "19"
                },
                "statistics": [
                  {
                    "name": "hits",
                    "abbreviation": "H",
                    "displayValue": "0"
                  },
                  {
                    "name": "runs",
                    "abbreviation": "R",
                    "displayValue": "0"
                  },
                  {
                    "name": "avg",
                    "abbreviation": "AVG",
                    "displayValue": ".000"
                  },
                  {
                    "name": "saves",
                    "abbreviation": "SV",
                    "displayValue": "3"
                  },
                  {
                    "name": "losses",
                    "abbreviation": "L",
                    "displayValue": "0"
                  },
                  {
                    "name": "wins",
                    "abbreviation": "W",
                    "displayValue": "2"
                  },
                  {
                    "name": "ERA",
                    "abbreviation": "ERA",
                    "displayValue": "2.19"
                  },
                  {
                    "name": "errors",
                    "abbreviation": "E",
                    "displayValue": "0"
                  }
                ]
              },
              {
                "name": "losingPitcher",
                "displayName": "Losing Pitcher",
                "shortDisplayName": "Loss",
                "abbreviation": "LP",
                "playerId": 31867,
                "athlete": {
                  "id": "31867",
                  "fullName": "Tommy Kahnle",
                  "displayName": "Tommy Kahnle",
                  "shortName": "T. Kahnle",
                  "links": [
                    {
                      "rel": [
                        "playercard",
                        "desktop",
                        "athlete"
                      ],
                      "href": "https://www.espn.com/mlb/player/_/id/31867"
                    }
                  ],
                  "headshot": "https://a.espncdn.com/i/headshots/mlb/players/full/31867.png",
                  "jersey": "46",
                  "position": "RP",
                  "team": {
                    "id": "10"
                  }
                },
                "team": {
                  "id": "10"
                },
                "statistics": [
                  {
                    "name": "hits",
                    "abbreviation": "H",
                    "displayValue": "0"
                  },
                  {
                    "name": "runs",
                    "abbreviation": "R",
                    "displayValue": "0"
                  },
                  {
                    "name": "avg",
                    "abbreviation": "AVG",
                    "displayValue": ".000"
                  },
                  {
                    "name": "saves",
                    "abbreviation": "SV",
                    "displayValue": "1"
                  },
                  {
                    "name": "losses",
                    "abbreviation": "L",
                    "displayValue": "1"
                  },
                  {
                    "name": "wins",
                    "abbreviation": "W",
                    "displayValue": "1"
                  },
                  {
                    "name": "ERA",
                    "abbreviation": "ERA",
                    "displayValue": "2.08"
                  },
                  {
                    "name": "errors",
                    "abbreviation": "E",
                    "displayValue": "0"
                  }
                ]
              },
              {
                "name": "savingPitcher",
                "displayName": "Saving Pitcher",
                "shortDisplayName": "Save",
                "abbreviation": "S",
                "playerId": 39251,
                "athlete": {
                  "id": "39251",
                  "fullName": "Walker Buehler",
                  "displayName": "Walker Buehler",
                  "shortName": "W. Buehler",
                  "links": [
                    {
                      "rel": [
                        "playercard",
                        "desktop",
                        "athlete"
                      ],
                      "href": "https://www.espn.com/mlb/player/_/id/39251"
                    }
                  ],
                  "headshot": "https://a.espncdn.com/i/headshots/mlb/players/full/39251.png",
                  "jersey": "10",
                  "position": "SP",
                  "team": {
                    "id": "19"
                  }
                },
                "team": {
                  "id": "19"
                },
                "statistics": [
                  {
                    "name": "hits",
                    "abbreviation": "H",
                    "displayValue": "0"
                  },
                  {
                    "name": "runs",
                    "abbreviation": "R",
                    "displayValue": "0"
                  },
                  {
                    "name": "avg",
                    "abbreviation": "AVG",
                    "displayValue": ".000"
                  },
                  {
                    "name": "saves",
                    "abbreviation": "SV",
                    "displayValue": "1"
                  },
                  {
                    "name": "losses",
                    "abbreviation": "L",
                    "displayValue": "1"
                  },
                  {
                    "name": "wins",
                    "abbreviation": "W",
                    "displayValue": "1"
                  },
                  {
                    "name": "ERA",
                    "abbreviation": "ERA",
                    "displayValue": "3.60"
                  },
                  {
                    "name": "errors",
                    "abbreviation": "E",
                    "displayValue": "0"
                  }
                ]
              }
            ]
          },
          "broadcasts": [
            {
              "market": "national",
              "names": [
                "FOX"
              ]
            }
          ],
          "leaders": [
            {
              "name": "MLBRating",
              "displayName": "MLB Rating",
              "shortDisplayName": "RAT",
              "abbreviation": "RAT",
              "leaders": [
                {
                  "displayValue": "2-3, HR, 2B, 2 RBI, R, 2 BB",
                  "value": 70.25,
                  "athlete": {
                    "id": "33192",
                    "fullName": "Aaron Judge",
                    "displayName": "Aaron Judge",
                    "shortName": "A. Judge",
                    "links": [
                      {
                        "rel": [
                          "playercard",
                          "desktop",
                          "athlete"
                        ],
                        "href": "https://www.espn.com/mlb/player/_/id/33192"
                      }
                    ],
                    "headshot": "https://a.espncdn.com/i/headshots/mlb/players/full/33192.png",
                    "jersey": "99",
                    "position": {
                      "abbreviation": "RF"
                    },
                    "team": {
                      "id": "10"
                    },
                    "active": false
                  },
                  "team": {
                    "id": "10"
                  }
                },
                {
                  "displayValue": "1-4, HR, 2 RBI, R",
                  "value": 66.5,
                  "athlete": {
                    "id": "30583",
                    "fullName": "Giancarlo Stanton",
                    "displayName": "Giancarlo Stanton",
                    "shortName": "G. Stanton",
                    "links": [
                      {
                        "rel": [
                          "playercard",
                          "desktop",
                          "athlete"
                        ],
                        "href": "https://www.espn.com/mlb/player/_/id/30583"
                      }
                    ],
                    "headshot": "https://a.espncdn.com/i/headshots/mlb/players/full/30583.png",
                    "jersey": "27",
                    "position": {
                      "abbreviation": "DH"
                    },
                    "team": {
                      "id": "10"
                    },
                    "active": true
                  },
                  "team": {
                    "id": "10"
                  }
                }
              ]
            }
          ],
          "format": {
            "regulation": {
              "periods": 9
            }
          },
          "startDate": "2024-10-31T00:08Z",
          "series": {
            "type": "playoff",
            "title": "Playoff Series",
            "summary": "LAD win series 4-1",
            "completed": true,
            "totalCompetitions": 7,
            "competitors": [
              {
                "id": "10",
                "uid": "s:1~l:10~t:10",
                "wins": 1,
                "ties": 0,
                "href": "http://sports.core.api.espn.pvt/v2/sports/baseball/leagues/mlb/seasons/2024/teams/10?lang=en&region=us"
              },
              {
                "id": "19",
                "uid": "s:1~l:10~t:19",
                "wins": 4,
                "ties": 0,
                "href": "http://sports.core.api.espn.pvt/v2/sports/baseball/leagues/mlb/seasons/2024/teams/19?lang=en&region=us"
              }
            ]
          },
          "broadcast": "FOX",
          "geoBroadcasts": [
            {
              "type": {
                "id": "5",
                "shortName": "Radio"
              },
              "market": {
                "id": "1",
                "type": "National"
              },
              "media": {
                "shortName": "ERADM"
              },
              "lang": "en",
              "region": "us"
            },
            {
              "type": {
                "id": "1",
                "shortName": "TV"
              },
              "market": {
                "id": "1",
                "type": "National"
              },
              "media": {
                "shortName": "FOX"
              },
              "lang": "en",
              "region": "us"
            }
          ],
          "headlines": [
            {
              "type": "Recap",
              "description": "— You gotta hand it to Freddie Freeman, Shohei Ohtani and the Los Angeles Dodgers.",
              "shortLinkText": "Dodgers win World Series in 5 games, overcome 5-run deficit with help of errors to beat Yankees 7-6"
            }
          ],
          "highlights": []
        }
      ],
      "links": [
        {
          "language": "en-US",
          "rel": [
            "summary",
            "desktop",
            "event"
          ],
          "href": "https://www.espn.com/mlb/game/_/gameId/401701044/dodgers-yankees",
          "text": "Gamecast",
          "shortText": "Gamecast",
          "isExternal": false,
          "isPremium": false
        },
        {
          "language": "en-US",
          "rel": [
            "boxscore",
            "desktop",
            "event"
          ],
          "href": "https://www.espn.com/mlb/boxscore/_/gameId/401701044",
          "text": "Box Score",
          "shortText": "Box Score",
          "isExternal": false,
          "isPremium": false
        },
        {
          "language": "en-US",
          "rel": [
            "pbp",
            "desktop",
            "event"
          ],
          "href": "https://www.espn.com/mlb/playbyplay/_/gameId/401701044",
          "text": "Play-by-Play",
          "shortText": "Play-by-Play",
          "isExternal": false,
          "isPremium": false
        },
        {
          "language": "en-US",
          "rel": [
            "recap",
            "desktop",
            "event"
          ],
          "href": "https://www.espn.com/mlb/recap?gameId=401701044",
          "text": "Recap",
          "shortText": "Recap",
          "isExternal": false,
          "isPremium": false
        }
      ],
      "status": {
        "clock": 0.0,
        "displayClock": "0:00",
        "period": 9,
        "type": {
          "id": "3",
          "name": "STATUS_FINAL",
          "state": "post",
          "completed": true,
          "description": "Final",
          "detail": "Final",
          "shortDetail": "Final"
        }
      }
    }
  ],
  "provider": {
    "id": "100",
    "name": "Draft Kings",
    "displayName": "Draft Kings",
    "priority": 1
  }
}
```

## Why this matches (or not)

_[0.80|heuristic] Contains settled results / completed event_
