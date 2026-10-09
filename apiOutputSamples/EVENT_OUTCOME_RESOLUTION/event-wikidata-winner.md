---
intent: EVENT_OUTCOME_RESOLUTION
slug: event-wikidata-winner
status: pending_review
captured_at: 2026-10-08T04:42:36Z
request_url: https://www.wikidata.org/w/api.php?action=wbgetentities&sites=enwiki&titles=2022_FIFA_World_Cup&props=claims&format=json
content_type: application/json
inputs: |
  {}
intent_description: |
  Resolves objective real-world event outcomes for prediction markets and conditional contracts using quorum oracles.
answer_requirement: |
  Must state the settled result of the real-world event asked (who won / final outcome). Pins: wc22_final = 2022 FIFA World Cup final, 2022-12-18, Argentina beat France 3-3 a.e.t., 4-2 on penalties; nba_f5 = 2024 NBA Finals Game 5, 2024-06-17, Boston Celtics 106 - Dallas Mavericks 88.
capture_note: |
  (none)
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "entities": {
    "Q284163": {
      "type": "item",
      "id": "Q284163",
      "claims": {
        "P373": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P373",
              "hash": "a8277517480188289d9157450ee597c0e55bd757",
              "datavalue": {
                "value": "2022 FIFA World Cup",
                "type": "string"
              },
              "datatype": "string"
            },
            "type": "statement",
            "id": "q284163$AE55A807-9A5D-4CFB-BFE9-A4C534B70123",
            "rank": "normal"
          }
        ],
        "P664": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P664",
              "hash": "4df16ce520946f6a6929c40690aa6310d9d66c5c",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 253414,
                  "id": "Q253414"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$6616675a-4908-8418-1601-9e867989695d",
            "rank": "normal"
          }
        ],
        "P646": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P646",
              "hash": "62f93d4ce701eb94d7bc1f3f86247abdcf848808",
              "datavalue": {
                "value": "/m/0fp_8fm",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$F4FE786A-EBF2-48EE-939B-F3E580D4A07D",
            "rank": "normal",
            "references": [
              {
                "hash": "2b00cb481cddcac7623114367489b5c194901c4a",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "a94b740202b097dd33355e0e6c00e54b9395e5e0",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 15241312,
                          "id": "Q15241312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P577": [
                    {
                      "snaktype": "value",
                      "property": "P577",
                      "hash": "fde79ecb015112d2f29229ccc1ec514ed3e71fa2",
                      "datavalue": {
                        "value": {
                          "time": "+2013-10-28T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P248",
                  "P577"
                ]
              }
            ]
          }
        ],
        "P641": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P641",
              "hash": "1624e15e061523279bc14bb6497168e45caacb32",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 2736,
                  "id": "Q2736"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$CCFF8B92-762B-49B5-A1CD-3A6E5C486467",
            "rank": "normal",
            "references": [
              {
                "hash": "63fa4774b7d79f13d3a854256f3b8e727df733df",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "d1d1b10a05a8f3fc5d26bb4aeb6849617ad81fc7",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 5375741,
                          "id": "Q5375741"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P1417": [
                    {
                      "snaktype": "value",
                      "property": "P1417",
                      "hash": "44b6c4c71c3a2ea6d9eb346854dedc8ae8f5a1be",
                      "datavalue": {
                        "value": "sports/2022-FIFA-World-Cup",
                        "type": "string"
                      },
                      "datatype": "external-id"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7f0dfa43261621a38524db1db96fcb200ea2361d",
                      "datavalue": {
                        "value": {
                          "time": "+2026-07-01T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P248",
                  "P1417",
                  "P813"
                ]
              }
            ]
          }
        ],
        "P17": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P17",
              "hash": "8ba99c078ab46e426c8a6170c2a536bb5fd188c4",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 846,
                  "id": "Q846"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$a9d747b7-4099-b646-75c9-9aedf9da6a88",
            "rank": "normal",
            "references": [
              {
                "hash": "63fa4774b7d79f13d3a854256f3b8e727df733df",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "d1d1b10a05a8f3fc5d26bb4aeb6849617ad81fc7",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 5375741,
                          "id": "Q5375741"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P1417": [
                    {
                      "snaktype": "value",
                      "property": "P1417",
                      "hash": "44b6c4c71c3a2ea6d9eb346854dedc8ae8f5a1be",
                      "datavalue": {
                        "value": "sports/2022-FIFA-World-Cup",
                        "type": "string"
                      },
                      "datatype": "external-id"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7f0dfa43261621a38524db1db96fcb200ea2361d",
                      "datavalue": {
                        "value": {
                          "time": "+2026-07-01T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P248",
                  "P1417",
                  "P813"
                ]
              }
            ]
          }
        ],
        "P3417": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3417",
              "hash": "399e7f80d9c5f3ce2416374a8281cce9b6cbe37c",
              "datavalue": {
                "value": "2022-FIFA-World-Cup",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$9004AD71-70A4-4D09-A0BC-23FE70DB4CA3",
            "rank": "normal"
          }
        ],
        "P3450": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3450",
              "hash": "9111ecae047643187ba89846e9d80edd403ace73",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 19317,
                  "id": "Q19317"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P155": [
                {
                  "snaktype": "value",
                  "property": "P155",
                  "hash": "108887613999ac8be2ecf64ab262263519bcfc16",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 170645,
                      "id": "Q170645"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ],
              "P156": [
                {
                  "snaktype": "value",
                  "property": "P156",
                  "hash": "343b720ecfe6b31ddc9e339644bfc435999925e5",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 5020214,
                      "id": "Q5020214"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P155",
              "P156"
            ],
            "id": "Q284163$06EE0983-AE23-4B50-8814-83B8BD64D77B",
            "rank": "normal"
          }
        ],
        "P31": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P31",
              "hash": "de4b3ac238f47284a2dc0a6e30bf5d5e84a4a62f",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 500834,
                  "id": "Q500834"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$EF665A11-6B8F-4CC4-923B-CBD17AE11AFF",
            "rank": "normal",
            "references": [
              {
                "hash": "63fa4774b7d79f13d3a854256f3b8e727df733df",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "d1d1b10a05a8f3fc5d26bb4aeb6849617ad81fc7",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 5375741,
                          "id": "Q5375741"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P1417": [
                    {
                      "snaktype": "value",
                      "property": "P1417",
                      "hash": "44b6c4c71c3a2ea6d9eb346854dedc8ae8f5a1be",
                      "datavalue": {
                        "value": "sports/2022-FIFA-World-Cup",
                        "type": "string"
                      },
                      "datatype": "external-id"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7f0dfa43261621a38524db1db96fcb200ea2361d",
                      "datavalue": {
                        "value": {
                          "time": "+2026-07-01T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P248",
                  "P1417",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P31",
              "hash": "58e4840c7f6c4af442e84f4f9a60711e9287c6a1",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1478437,
                  "id": "Q1478437"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$94d5f8bd-450f-1f20-ed27-5e0fd3f3c2eb",
            "rank": "normal",
            "references": [
              {
                "hash": "63fa4774b7d79f13d3a854256f3b8e727df733df",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "d1d1b10a05a8f3fc5d26bb4aeb6849617ad81fc7",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 5375741,
                          "id": "Q5375741"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P1417": [
                    {
                      "snaktype": "value",
                      "property": "P1417",
                      "hash": "44b6c4c71c3a2ea6d9eb346854dedc8ae8f5a1be",
                      "datavalue": {
                        "value": "sports/2022-FIFA-World-Cup",
                        "type": "string"
                      },
                      "datatype": "external-id"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7f0dfa43261621a38524db1db96fcb200ea2361d",
                      "datavalue": {
                        "value": {
                          "time": "+2026-07-01T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P248",
                  "P1417",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P31",
              "hash": "ecbb916a7543708b066e45ad27981718c3e43d13",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 27020041,
                  "id": "Q27020041"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$f3483304-4491-846a-dfe4-704997d75c55",
            "rank": "normal"
          }
        ],
        "P585": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P585",
              "hash": "2158d4b68f82b8f36f47c98bd3609a99913faa59",
              "datavalue": {
                "value": {
                  "time": "+2022-00-00T00:00:00Z",
                  "timezone": 0,
                  "before": 0,
                  "after": 0,
                  "precision": 9,
                  "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                },
                "type": "time"
              },
              "datatype": "time"
            },
            "type": "statement",
            "id": "Q284163$8B9D196E-A1D9-4A6F-8B49-60B24A78C767",
            "rank": "normal"
          }
        ],
        "P580": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P580",
              "hash": "f612e9605a4b64745a135c4d20d628f0cac89583",
              "datavalue": {
                "value": {
                  "time": "+2022-11-20T00:00:00Z",
                  "timezone": 0,
                  "before": 0,
                  "after": 0,
                  "precision": 11,
                  "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                },
                "type": "time"
              },
              "datatype": "time"
            },
            "type": "statement",
            "id": "Q284163$e52e5b7c-4159-3a16-95eb-366ee6bdacea",
            "rank": "normal",
            "references": [
              {
                "hash": "63fa4774b7d79f13d3a854256f3b8e727df733df",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "d1d1b10a05a8f3fc5d26bb4aeb6849617ad81fc7",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 5375741,
                          "id": "Q5375741"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P1417": [
                    {
                      "snaktype": "value",
                      "property": "P1417",
                      "hash": "44b6c4c71c3a2ea6d9eb346854dedc8ae8f5a1be",
                      "datavalue": {
                        "value": "sports/2022-FIFA-World-Cup",
                        "type": "string"
                      },
                      "datatype": "external-id"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7f0dfa43261621a38524db1db96fcb200ea2361d",
                      "datavalue": {
                        "value": {
                          "time": "+2026-07-01T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P248",
                  "P1417",
                  "P813"
                ]
              }
            ]
          }
        ],
        "P582": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P582",
              "hash": "bc5d1bcb85b9e14b7bc60b8add988ee55c367d30",
              "datavalue": {
                "value": {
                  "time": "+2022-12-18T00:00:00Z",
                  "timezone": 0,
                  "before": 0,
                  "after": 0,
                  "precision": 11,
                  "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                },
                "type": "time"
              },
              "datatype": "time"
            },
            "type": "statement",
            "id": "Q284163$5b79d2ff-4c71-cfc3-0497-c9ecb711d8a0",
            "rank": "normal",
            "references": [
              {
                "hash": "63fa4774b7d79f13d3a854256f3b8e727df733df",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "d1d1b10a05a8f3fc5d26bb4aeb6849617ad81fc7",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 5375741,
                          "id": "Q5375741"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P1417": [
                    {
                      "snaktype": "value",
                      "property": "P1417",
                      "hash": "44b6c4c71c3a2ea6d9eb346854dedc8ae8f5a1be",
                      "datavalue": {
                        "value": "sports/2022-FIFA-World-Cup",
                        "type": "string"
                      },
                      "datatype": "external-id"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7f0dfa43261621a38524db1db96fcb200ea2361d",
                      "datavalue": {
                        "value": {
                          "time": "+2026-07-01T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P248",
                  "P1417",
                  "P813"
                ]
              }
            ]
          }
        ],
        "P1132": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1132",
              "hash": "33e8d18c02d070be5ede08f7813f012f2160f4f4",
              "datavalue": {
                "value": {
                  "amount": "+32",
                  "unit": "1"
                },
                "type": "quantity"
              },
              "datatype": "quantity"
            },
            "type": "statement",
            "id": "Q284163$48f5d18b-4e10-2491-b520-4032ec6c440a",
            "rank": "normal",
            "references": [
              {
                "hash": "63fa4774b7d79f13d3a854256f3b8e727df733df",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "d1d1b10a05a8f3fc5d26bb4aeb6849617ad81fc7",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 5375741,
                          "id": "Q5375741"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P1417": [
                    {
                      "snaktype": "value",
                      "property": "P1417",
                      "hash": "44b6c4c71c3a2ea6d9eb346854dedc8ae8f5a1be",
                      "datavalue": {
                        "value": "sports/2022-FIFA-World-Cup",
                        "type": "string"
                      },
                      "datatype": "external-id"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7f0dfa43261621a38524db1db96fcb200ea2361d",
                      "datavalue": {
                        "value": {
                          "time": "+2026-07-01T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P248",
                  "P1417",
                  "P813"
                ]
              }
            ]
          }
        ],
        "P393": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P393",
              "hash": "160c8e2a851a5bad6bb911e089cc319a6cb40eef",
              "datavalue": {
                "value": "22",
                "type": "string"
              },
              "datatype": "string"
            },
            "type": "statement",
            "id": "Q284163$bbb1f49c-4b90-d375-f10c-deef70f92cf2",
            "rank": "normal"
          }
        ],
        "P910": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P910",
              "hash": "51c01d645ef98f7537c6aff779b4e74965e7649a",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 8204865,
                  "id": "Q8204865"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$7f10e7e1-4275-672a-df97-9a54a2cce061",
            "rank": "normal"
          }
        ],
        "P154": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P154",
              "hash": "630d8c3317f52b740b8ed0b579a60d9af00c613c",
              "datavalue": {
                "value": "2022 FIFA World Cup Qatar (Wordmark).svg",
                "type": "string"
              },
              "datatype": "commonsMedia"
            },
            "type": "statement",
            "id": "Q284163$570d6ea9-49a5-adde-f0f8-f7a998541ae3",
            "rank": "normal"
          }
        ],
        "P2094": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P2094",
              "hash": "6c137752b3b79bad9a00b5fae9d171a795a357df",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 31930761,
                  "id": "Q31930761"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$5C765D66-A52A-45A6-8629-9742FBACC153",
            "rank": "normal"
          }
        ],
        "P276": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P276",
              "hash": "879f553fb3d3ae19582f7ef4649325a25869434f",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1186333,
                  "id": "Q1186333"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$a2e501b9-4237-bd52-e5b0-3b4019a5673b",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P276",
              "hash": "1626522436a888d43f1f5f150435a61522df0241",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1050220,
                  "id": "Q1050220"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$048d35e7-426e-0a5d-fd0c-7ff4d24b74bf",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P276",
              "hash": "9526ac4f67806a010b858c76c35ccd77cb516a56",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1134439,
                  "id": "Q1134439"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$5f216ad6-48cd-9dc3-01aa-656df285ed20",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P276",
              "hash": "65eee40664663d08372cf21ee56da250f77deaad",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 39049425,
                  "id": "Q39049425"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$3a608092-4c45-011a-81af-4855f350146a",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P276",
              "hash": "50d565571e7705b560bdbdf966955da1c74f5e17",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1048774,
                  "id": "Q1048774"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$2f56ffba-49c3-0a63-1a92-b7b98ca0e67d",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P276",
              "hash": "6c1842dba0d1d986360334d6eb07c0519304fc1e",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 401643,
                  "id": "Q401643"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$5a973eca-4d79-b7d6-0175-098623a1ed03",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P276",
              "hash": "1e4671a79811127e314df47516185074e3f97d36",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 772988,
                  "id": "Q772988"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$3f81acac-4efa-eaaf-6138-3798719cb2c1",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P276",
              "hash": "29f2dde6fbcb9ea8efc2e689fe30b5eca80e2223",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 285531,
                  "id": "Q285531"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$67c5ffef-4816-9aa6-d70f-b0757ce8d10e",
            "rank": "normal"
          }
        ],
        "P8885": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P8885",
              "hash": "d7ce84eecad1d57ca022b053cfbb30876fcbce85",
              "datavalue": {
                "value": "2022 FIFA 월드컵 카타르",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$2aab1684-4d9a-ec9e-58d8-e883971b9d13",
            "rank": "normal"
          }
        ],
        "P1424": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1424",
              "hash": "e48d15e57ce5ffc8959debc0b79a4e42198c2660",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 53910818,
                  "id": "Q53910818"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$03774158-4cf8-3cfd-f5ac-14cab6ea56f7",
            "rank": "normal"
          }
        ],
        "P10234": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P10234",
              "hash": "3979d295c9a196efde5acce2eb4b1f1856aba114",
              "datavalue": {
                "value": "fussball_wm_2022",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$d3ee63c6-4b83-d26c-539d-30278b049128",
            "rank": "normal"
          }
        ],
        "P9346": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P9346",
              "hash": "823804dd798b65eeb1e48b067a1ac5764b653fbb",
              "datavalue": {
                "value": "mondial-2022",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$67629123-4fe3-85f1-df75-0db70420610c",
            "rank": "normal"
          }
        ],
        "P9347": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P9347",
              "hash": "83c4c65045fcaa69246a5c73d13a6da820b96506",
              "datavalue": {
                "value": "2022-fifa-world-cup",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$3057f03b-4327-6cb5-bd86-31d60b81da64",
            "rank": "normal"
          }
        ],
        "P9348": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P9348",
              "hash": "5fc321012d2d99b40f60af2f0d6fb3eabf5b4209",
              "datavalue": {
                "value": "mundial-qatar-2022",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$9118a863-4e3e-82cb-2ca4-0d9d5a23fddf",
            "rank": "normal"
          }
        ],
        "P9349": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P9349",
              "hash": "451a959aeff3bfecf20a2cbb6b3ee1574ee13b4b",
              "datavalue": {
                "value": "كأس-العالم-2022",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$6dcdafa7-4e3e-74cc-6cd3-d45f9c32a795",
            "rank": "normal"
          }
        ],
        "P822": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P822",
              "hash": "29dd8efc141d882f5cec36d0abbe3a3c3a8268c2",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111450544,
                  "id": "Q111450544"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$b875a2e9-458d-4013-2e12-b1acc11ea0e9",
            "rank": "normal"
          }
        ],
        "P527": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "4cd2d16ac498443ae632261a55cce695c5f4aa43",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111435465,
                  "id": "Q111435465"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$885d22a8-49d1-647e-5105-e3c2bcc85374",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "89c69f84b29088d8530df8c699593a7599bddbd8",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111435467,
                  "id": "Q111435467"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$97be8147-4e26-1dfd-0930-3d467d3efdfc",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "ae21b96afc827ae93978544f1dba27128a77ca58",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111435469,
                  "id": "Q111435469"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$c839bbdb-4673-eff8-943c-b656c1b1e22f",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "23d01815475eb9ac8d355e23beddef2a8b31ef81",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111435473,
                  "id": "Q111435473"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$5ee302cb-420e-2035-dd73-cd7d348f5425",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "a94af30c378fc7c6b07bdb91c3c46fc7ffa6ddc7",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111435477,
                  "id": "Q111435477"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$03b310d7-4570-811b-1711-c76a0d41f8a7",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "cddc3ff20697ca8ab84eb688336e345f54dfab54",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111435479,
                  "id": "Q111435479"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$b588f235-4d03-039c-583b-31f686183c56",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "9be034f9d97c089227b33959197b3f7aa95e4905",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111435481,
                  "id": "Q111435481"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$1dac0e5c-494f-a741-af11-58858e061208",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "7867fdcf4d63cb393c9c4d977d388a57f81418f9",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111435483,
                  "id": "Q111435483"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$bb3a84dc-499a-e02e-c384-7f61cad7d40f",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "61409fdc2e3e97399b7e7b11926de295897fb5c2",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111435490,
                  "id": "Q111435490"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$0cd2e086-4977-c56f-4297-c75fef32f33b",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "13994d4768514f832eb58a84415a3db6c0153f69",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111496223,
                  "id": "Q111496223"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$C51C3CEE-6C7A-4B28-A89C-267CAB0F4079",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "872a95e37e6f2320b84a64ac1e1bb0bf5bb91063",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111499762,
                  "id": "Q111499762"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$7ACDEAC4-7978-46C9-89B8-32ACBE7AEC8C",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "31d0b6be246b0fd295e4b773b4a61a14009469fb",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111507044,
                  "id": "Q111507044"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$9E6572DB-E2AA-4281-B287-BDAA259872E7",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "2c8c2fe225af4ed61546cea67fe4ec721a469b3f",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111510956,
                  "id": "Q111510956"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$78177B9A-E3C5-47B5-B695-81942AB8783D",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "6e822dfd6a776c6649e7b8d688707874527d8bde",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111511872,
                  "id": "Q111511872"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$DBE7D204-4F5D-4D8F-8181-9DB4BF4C193E",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "952600922621e33a50dbe6a95c5a29966d2a9a5a",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111512848,
                  "id": "Q111512848"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$DD01D8D0-4391-454E-A220-71828752AB0A",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "86edddfecf680e4a5c77a2016ef108343be17105",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111514511,
                  "id": "Q111514511"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$46A87152-A455-48FC-9E8A-A5E7C8752D92",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "0d637cdba6b5c3f02cda3086f226b5e7cab2502e",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111523325,
                  "id": "Q111523325"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$4917B368-B788-420C-8089-744C9ADCA99A",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "6e42b7a109f809ee8e0846f12ca429a66a6adf7c",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535583,
                  "id": "Q111535583"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$3C1A3E84-6BE3-46AF-9064-D933DE1E1841",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "c9cbe8a35e76cf2f9b475ca7eca3991e8809d859",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535574,
                  "id": "Q111535574"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$89CCFC12-8317-4AB4-BA0B-AEDCD28A4EEF",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "585386b8732a0770bc9dca8ab1cae440d576cc8f",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535592,
                  "id": "Q111535592"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$A6DF79DE-45D9-4675-98D5-83FDA77EB359",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "42df9709224bafbe83d362dd73e0d5cbdddd5cc9",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535589,
                  "id": "Q111535589"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$43247D9A-03D6-4084-B241-ABC6DA8C78A6",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "dd39826c8fce1d46712447d35ce86816aa58634c",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535594,
                  "id": "Q111535594"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$A480FF87-0E39-4841-9237-08604AA4BAEE",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "d9cc9dbd4b35544fe0fdbd8cb0dad28da3fc0eca",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535598,
                  "id": "Q111535598"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$10D713CD-9CB1-41C9-8F3E-C74F0958D2CB",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "ec9cfb9e10034c79fbd6c5537269a655e9ba7402",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535585,
                  "id": "Q111535585"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$5F0CB912-A16B-4133-8586-CC31006CC597",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "76cfbadd861e73a8f650c7e246e8c645d28c6a11",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535576,
                  "id": "Q111535576"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$EED6905B-E5D5-496A-B8C5-99CA6515C040",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "b66dd3051f8becbd2eb0561eb8ec2b85f705840c",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535593,
                  "id": "Q111535593"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$19322FAB-71A1-46E2-9087-E932A7215650",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "303b6597ed558f78f81bab05bd5e392695e59f62",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535571,
                  "id": "Q111535571"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$210440B2-114F-4161-9BB7-22BF3221CD92",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "0c058b93be314e9eafd01317371491658566bdab",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535579,
                  "id": "Q111535579"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$903DE92B-5C40-4F82-9FD9-14556A68055F",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "bad6285a669453631871426b59d2753aebc36623",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535588,
                  "id": "Q111535588"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$A7CBB50B-D64A-4D13-AF84-35973D2CC9FC",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "4162b065cbd4076b2e41e7a0ace65ab099c7f3ae",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535572,
                  "id": "Q111535572"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$DD5D8650-EEED-43CA-8E58-78DE1B240053",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "eb75c0326d93958b51449d9a9c28fa6bd0425275",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535573,
                  "id": "Q111535573"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$D398F2BF-5902-476F-8C2A-8ADDC5DFC91A",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "f49390098034f43ee3a2c5ebaafdfb01474c543b",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535577,
                  "id": "Q111535577"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$8DD41EC2-20C4-4AE3-8FA4-D6EDDB20EBE4",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "7e981d3b0400a2892a655ae40bab57817a757e1e",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535590,
                  "id": "Q111535590"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$28407C2C-487F-4212-A20B-6C85559F0F0A",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "dfc5c3cb479df86e7a6e0679f8c449b79fffabd9",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535586,
                  "id": "Q111535586"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$CD0F7B4C-10F1-484B-9049-6C0E487792DE",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "a15686ec3bed56eeb04ebfe3f9c878005c6f2daf",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535595,
                  "id": "Q111535595"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$DE1813D2-42CA-4CEB-987F-CD21CCA1A39F",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "e77b91c9ebb946ff7f5cb9d20e184f94719ac0d6",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 86670164,
                  "id": "Q86670164"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$EA3BED38-4561-438F-80CA-7A29E90759B0",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "a109851410a87f3b802c2ca8dd59636f7b0d0176",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 112265366,
                  "id": "Q112265366"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$27014670-9391-4368-A6F0-E0977314D0DA",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "8391722a3c8eed6c3100d7f4cbb90a6888d1e40d",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 112572853,
                  "id": "Q112572853"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$89F21C04-F7B0-4D6C-9881-1015D17CE175",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "fe821e060345f7f7ac8cd44ee23cff5640551788",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 112584182,
                  "id": "Q112584182"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$5603CBE8-259D-45F6-9C54-3AEA9BC4B56C",
            "rank": "normal"
          }
        ],
        "P6262": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P6262",
              "hash": "994e559d1032f7f3e06cf52af1bd7595de000fca",
              "datavalue": {
                "value": "football:2022_FIFA_World_Cup",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "qualifiers": {
              "P407": [
                {
                  "snaktype": "value",
                  "property": "P407",
                  "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 1860,
                      "id": "Q1860"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ],
              "P1810": [
                {
                  "snaktype": "value",
                  "property": "P1810",
                  "hash": "c827a609ebc52575f1f85722f6ba16794f63361b",
                  "datavalue": {
                    "value": "2022 FIFA World Cup",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ],
              "P9675": [
                {
                  "snaktype": "value",
                  "property": "P9675",
                  "hash": "48dd5b91f6f548d51b17911a566314b2b77ef9d1",
                  "datavalue": {
                    "value": "13048",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ]
            },
            "qualifiers-order": [
              "P407",
              "P1810",
              "P9675"
            ],
            "id": "Q284163$8323665c-43a9-963a-63c3-b139b981a11b",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P6262",
              "hash": "4376c5508a183747e2e4abc72bccd49e2b2c250d",
              "datavalue": {
                "value": "logos:2022_FIFA_World_Cup",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "qualifiers": {
              "P1810": [
                {
                  "snaktype": "value",
                  "property": "P1810",
                  "hash": "c827a609ebc52575f1f85722f6ba16794f63361b",
                  "datavalue": {
                    "value": "2022 FIFA World Cup",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ],
              "P407": [
                {
                  "snaktype": "value",
                  "property": "P407",
                  "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 1860,
                      "id": "Q1860"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ],
              "P9675": [
                {
                  "snaktype": "value",
                  "property": "P9675",
                  "hash": "e5980d8cd9a4bd94f931670b379fa951a566d7a6",
                  "datavalue": {
                    "value": "37349",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ]
            },
            "qualifiers-order": [
              "P1810",
              "P407",
              "P9675"
            ],
            "id": "Q284163$6ED987C3-1740-42DF-BCCE-2CCDB98F8786",
            "rank": "normal",
            "references": [
              {
                "hash": "cdd754097245f83a7bf1223134d4f65d885b465f",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "7faa27bae83f4718745651fd36038fb858fc2919",
                      "datavalue": {
                        "value": "https://logos.fandom.com/wiki/2022_FIFA_World_Cup",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "aa8bc6285ddea9e43a01181e7f7aff41c6388554",
                      "datavalue": {
                        "value": {
                          "text": "2022 FIFA World Cup | Logopedia | Fandom",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1d7fb525b2e332076aec1f593f27ffefa8cbde49",
                      "datavalue": {
                        "value": {
                          "time": "+2022-11-29T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P1476",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P6262",
              "hash": "e56f0f138e7d6dcbf8cba28bc371be884bb5fb17",
              "datavalue": {
                "value": "footballranking:2022_FIFA_World_Cup",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "qualifiers": {
              "P1810": [
                {
                  "snaktype": "value",
                  "property": "P1810",
                  "hash": "c827a609ebc52575f1f85722f6ba16794f63361b",
                  "datavalue": {
                    "value": "2022 FIFA World Cup",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ],
              "P407": [
                {
                  "snaktype": "value",
                  "property": "P407",
                  "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 1860,
                      "id": "Q1860"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ],
              "P9675": [
                {
                  "snaktype": "value",
                  "property": "P9675",
                  "hash": "367760f1130c0e0d986dd9e16148e4c106afa0bf",
                  "datavalue": {
                    "value": "8035",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ]
            },
            "qualifiers-order": [
              "P1810",
              "P407",
              "P9675"
            ],
            "id": "Q284163$2C037A58-276B-4E0F-9204-C3E0510BB967",
            "rank": "normal"
          }
        ],
        "P710": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "c7f6da31d06c890270d7847c3bf8089f61697d50",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111496223,
                  "id": "Q111496223"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "cbaadcd36f0b877dbbda357045e54cd9b6faf67c",
                  "datavalue": {
                    "value": {
                      "amount": "+6",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$0FAD7CB1-92F1-4EFA-98B2-9ACFED6201BC",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "8458da71377b5954f7cbabeaff434493a3fa46c6",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111499762,
                  "id": "Q111499762"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "b9638b3f6764ba46fd03a70fa15e73aae62b4efd",
                  "datavalue": {
                    "value": {
                      "amount": "+23",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$41C02798-9312-4047-96F4-04FB9A8A01F0",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "0249fe98a44b692f31f96d0eec7fd71cbeab4123",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111507044,
                  "id": "Q111507044"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "bf708e250f6f6d50b92c1177ba32dc344f2a7f5f",
                  "datavalue": {
                    "value": {
                      "amount": "+28",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$DA7DDFBE-1DC7-460B-9171-FB1B081BC405",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "1e24874340859328142ba60cb1c61dff648eace5",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111510956,
                  "id": "Q111510956"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "ba2a02dbc6c7be6ccb48d427264a770b105256ed",
                  "datavalue": {
                    "value": {
                      "amount": "+3",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$0421D55C-648A-4E15-A6F3-96010738EADB",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "d963f6b7662b292324fa0c088ca6c084b7e3e47c",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111511872,
                  "id": "Q111511872"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "e55ddd08ce050b5a1f3ba07f119cdf406d6266d2",
                  "datavalue": {
                    "value": {
                      "amount": "+5",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$402C16EB-1C5C-4219-A1F4-B028D1891CED",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "02cbae9fcf098af333c9bca8343d393c23600ed2",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111512848,
                  "id": "Q111512848"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "91730a101901e753c73b4ecdc5438df3e600ac71",
                  "datavalue": {
                    "value": {
                      "amount": "+15",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$45C3B717-C81C-43D4-AE20-31F008363209",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "ac5b9bd1cf08f98169b5d870654a270dc8b25874",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111514511,
                  "id": "Q111514511"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "e77fec69644de80f5fd34480ed66ec7b63283476",
                  "datavalue": {
                    "value": {
                      "amount": "+8",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$1FB2610D-0548-4A96-B9D4-15A99A2E3D8C",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "7afbfc637f4dfbd8119c2e03132411047f965a30",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111523325,
                  "id": "Q111523325"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "1677b669a22f2e92d6211557b0093fe5e605feaf",
                  "datavalue": {
                    "value": {
                      "amount": "+12",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$3A71E4E4-3EF0-4216-BE49-0E29C7A91FA5",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "642bc4cc95b62f6cdc864f3d88eab9ba47fc6bbc",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535583,
                  "id": "Q111535583"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "24218f329bbab6d348a01cf8d0f346a08013e0a9",
                  "datavalue": {
                    "value": {
                      "amount": "+29",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$78DB273C-B438-46B7-9B1E-9F19850EDBD2",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "baf00cbcccb775267d54e5e3342017451a336634",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535574,
                  "id": "Q111535574"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "0d109615c75d62315b23bc832d8f93d79f328a94",
                  "datavalue": {
                    "value": {
                      "amount": "+13",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$EB2EC854-E5A4-44A1-854C-2EB5C2F50C7F",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "322fa7789cc328e6461468dbdfa6ebd8788518b4",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535592,
                  "id": "Q111535592"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "d957faa05dfad4ad246e3d9fbae30fd7129531c8",
                  "datavalue": {
                    "value": {
                      "amount": "+24",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$6C21A9C3-7B92-498F-A6B9-206A0F44A3E0",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "3726eafd5e88d430361bc34736bcb9909a3c5328",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535589,
                  "id": "Q111535589"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "f5578e95ef6d705ac139f622ea8b0d92b5f95c45",
                  "datavalue": {
                    "value": {
                      "amount": "+19",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$D64BACE2-F0EF-4A32-B876-08BBAE46FC46",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "39121ad54bdf0dd3bb5fc43cf02d7a3dffb37713",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535594,
                  "id": "Q111535594"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "5e5880d79c7b10631a47acef228c5140c9b8bca1",
                  "datavalue": {
                    "value": {
                      "amount": "+4",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$520523D2-9A88-4EFD-9C2C-44686E4EB147",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "e8bc0fc33868351a10da68358145bc085fd4ce28",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535598,
                  "id": "Q111535598"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "d496cb7a9e6d070cd321b9fb2412c434618380be",
                  "datavalue": {
                    "value": {
                      "amount": "+10",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$A66C8020-B1D3-489A-BC3D-E2EA3484930B",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "e3f5b0bddd7f6972648af6e85954826e71e4b7ac",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535585,
                  "id": "Q111535585"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "34b21175d1a3705a888886d60b9954c8f42d28a6",
                  "datavalue": {
                    "value": {
                      "amount": "+21",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$ACE2375F-FFF1-4CC1-A788-093C50B59014",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "02203f0bc9dc5344dcd97ac202434d32dab97d6d",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535576,
                  "id": "Q111535576"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "f3dc2c47fac48d094dae3a1420184df68800369b",
                  "datavalue": {
                    "value": {
                      "amount": "+26",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$45154493-28A2-4394-BAE8-5368E8C125C0",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "c185f730f972b03b96eaf1b461235764120a4bf2",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535593,
                  "id": "Q111535593"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "09cad1eaf2d3fc1b6f11a8a74488d25498f7e640",
                  "datavalue": {
                    "value": {
                      "amount": "+9",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$8D8E5323-6726-453B-9AF9-BF030E753FCC",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "78ffa9d6072f7f79f307454def0e1c22c3610db6",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535571,
                  "id": "Q111535571"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "5db49f1b02b8cd18b285ca5552f7e5d95e4eeacb",
                  "datavalue": {
                    "value": {
                      "amount": "+25",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$0827C2F9-B176-4A84-BE97-0006A5595748",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "dd7f4b31c187b1bf864e63f78694a0cd45b7f484",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535579,
                  "id": "Q111535579"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "4a5a42db2c261f555c9e1d1bcefd317149061061",
                  "datavalue": {
                    "value": {
                      "amount": "+16",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$F96E140E-5EFA-4F68-BC43-EFAB198AAE5F",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "ef6eabf2553579d2257c60204193b9e3431f201f",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535588,
                  "id": "Q111535588"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "5e1078ddd7f5c508df15f8d5be5df17cbe240b49",
                  "datavalue": {
                    "value": {
                      "amount": "+7",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$66A74496-EC92-4247-B7E1-CF9EFB7BA7BF",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "9c664d82b577ad6e8ac069563738c6ed869491b5",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535572,
                  "id": "Q111535572"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "3df9f7d5d4cbc791e6579735e13985769a537fb9",
                  "datavalue": {
                    "value": {
                      "amount": "+1",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$BCED5477-509A-41B3-A4E7-DD78AB74CFB7",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "66956acca84cf82823a903431554a95e3633bf3d",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535573,
                  "id": "Q111535573"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "7a6beda32f434c6655d7224249c47e50d3662d8f",
                  "datavalue": {
                    "value": {
                      "amount": "+18",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$69F8F692-F16E-4548-875E-29BB5081067A",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "1505098d75511a97a9965994acd9e26a0d21c458",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535577,
                  "id": "Q111535577"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "4490a33bd0855728c0f45c586221887e601ad5f0",
                  "datavalue": {
                    "value": {
                      "amount": "+20",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$7697CAE3-247E-406F-BBF6-D2113F9CA5EB",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "a52b3b463b2fdc296e4ab17f07e0ba993b69e22c",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535590,
                  "id": "Q111535590"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "6618ac919f7f356a6b55c9572d75a68380741b6b",
                  "datavalue": {
                    "value": {
                      "amount": "+31",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$2AE89D30-9AAB-4FA4-9C2E-6E3118365EE3",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "3c72661191f9d665bd5dc0e5fdb3d87e5c360d40",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535586,
                  "id": "Q111535586"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "d05fb83fdb6a1ce3e399d6692a0926719acd9f2e",
                  "datavalue": {
                    "value": {
                      "amount": "+14",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$A6AF51DD-016F-4EF0-98E5-051C752F3A02",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "4ef696c2dbccd03ddf6367812120f7e9eb1bd80d",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111535595,
                  "id": "Q111535595"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "2510a0221274ca29ef3de747e303666e94b41871",
                  "datavalue": {
                    "value": {
                      "amount": "+22",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$2970E72A-694E-4263-A807-1FD86202001C",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "2986dd3d447df18d7291bfc10e823afcc47a1385",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 86670164,
                  "id": "Q86670164"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "7251e1fe770a5c39f21a3760fba9e046a98fa625",
                  "datavalue": {
                    "value": {
                      "amount": "+32",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$49B13B84-4D1C-484E-9BC6-FA82522E1582",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "416f30abb0130636a4bd702fcf135429ac122ec2",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 112265366,
                  "id": "Q112265366"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "5aba8b1d4d45a91215c51ef44e574a17b524a356",
                  "datavalue": {
                    "value": {
                      "amount": "+30",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$93129BCF-820B-47A8-AFDE-C2C2ADA45439",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "b1111d55f679945608b4cac43e5eacb054910810",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 112572853,
                  "id": "Q112572853"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "8caafa6ef94abf71b9210d7a524a4278a5ea205a",
                  "datavalue": {
                    "value": {
                      "amount": "+11",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$37EB5185-BACB-4DDF-910B-B76479D9AED4",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "bc95ee703428bb279253742b121a6b9d422e7d76",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 112584182,
                  "id": "Q112584182"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "d4c96c87f0e969e34a17324e067fe292b8465f29",
                  "datavalue": {
                    "value": {
                      "amount": "+27",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$C0C60B6A-4531-40F7-88F5-D09AE5A8FCDE",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "16289dfdae823826d13843887dd205916be5d806",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 111488567,
                  "id": "Q111488567"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "9b8d47aeb2bb9aa4980c87c3dffd644defec4452",
                  "datavalue": {
                    "value": {
                      "amount": "+17",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$18fddd52-454b-593b-00c7-7f172da540c4",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P710",
              "hash": "36ccac72481c176b01fe43f1ca7ae401c35f7c61",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 109647861,
                  "id": "Q109647861"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "270f0c96a63b9d8572cb04ebbdf12b98a9dff154",
                  "datavalue": {
                    "value": {
                      "amount": "+2",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$b03fdb5f-4405-672d-9cf4-27bdda07219c",
            "rank": "normal",
            "references": [
              {
                "hash": "be7ec789338f922a5d35c66046163ccb68c6e6e7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "25a6f11fab1a6030f8f2e0219e696618aedc8eaa",
                      "datavalue": {
                        "value": "https://ge.globo.com/rj/copa-do-mundo/noticia/2022/12/19/classificacao-da-copa-do-mundo-2022.ghtml",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          }
        ],
        "P856": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P856",
              "hash": "10ce3c442029db3d7b828c04b60664841612f405",
              "datavalue": {
                "value": "https://www.fifa.com/en/tournaments/mens/worldcup/qatar2022",
                "type": "string"
              },
              "datatype": "url"
            },
            "type": "statement",
            "qualifiers": {
              "P407": [
                {
                  "snaktype": "value",
                  "property": "P407",
                  "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 1860,
                      "id": "Q1860"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P407"
            ],
            "id": "Q284163$2c21d0d6-439b-82c5-6718-c929b8f02ad2",
            "rank": "normal"
          }
        ],
        "P3414": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3414",
              "hash": "225337b0ddfffcc542e070562f2d231f6f219799",
              "datavalue": {
                "value": "1-63499961",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$6b1bce3d-4565-68c1-9c7c-92f6406a4b45",
            "rank": "normal"
          }
        ],
        "P8309": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P8309",
              "hash": "72e0fb73f773311a320b082c1ead4b95d2a2323c",
              "datavalue": {
                "value": "18-140451",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$debef126-4a21-bcf8-dcb0-9b778f5ff5a9",
            "rank": "normal"
          }
        ],
        "P11137": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P11137",
              "hash": "0da3a76f2e138ad0cb9634bffdc633938ba58a1a",
              "datavalue": {
                "value": "2022_fifa_world_cup",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$145F141E-ECF4-422C-A1BB-E4E0E3CEC351",
            "rank": "normal"
          }
        ],
        "P2572": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P2572",
              "hash": "23d788fec2bcd7a24610d22fb49c59f3af5bbb70",
              "datavalue": {
                "value": "worldcup2022",
                "type": "string"
              },
              "datatype": "string"
            },
            "type": "statement",
            "id": "Q284163$22FD01E7-DB9A-4570-8494-0F8E6778BDAC",
            "rank": "normal",
            "references": [
              {
                "hash": "5e2fc16f49e87ae4662f3ccc529a48cd60cec0db",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "790140baa6881daa43a0cf83d80f99ef890325d3",
                      "datavalue": {
                        "value": "https://twitter.com/hashtag/WorldCup2022?src=hashtag_click",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "ac0e5d0b4e11c29c93f0a7403a6fd29123cdde1e",
                      "datavalue": {
                        "value": {
                          "text": "#WorldCup2022 - Twitter Search / Twitter",
                          "language": "en-gb"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "5bfda69b8492ebc012bb7deca4152477ceec4239",
                      "datavalue": {
                        "value": {
                          "time": "+2022-11-11T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P1476",
                  "P813"
                ]
              }
            ]
          }
        ],
        "P6817": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P6817",
              "hash": "6d748860b0dd42ac2d96079a71b5d3bbebb6e5f2",
              "datavalue": {
                "value": "fifa-fotbolls-vm-2022",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$d9a9ca21-43c8-e907-2227-132a5e4682cf",
            "rank": "normal"
          }
        ],
        "P10767": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P10767",
              "hash": "fe2906139e41d03df9b2511db27f6c8bd401708e",
              "datavalue": {
                "value": "1275806388367720450",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$3f7d94b7-4d63-3338-8737-aad47be7b83e",
            "rank": "normal"
          }
        ],
        "P9820": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P9820",
              "hash": "397072463cac3927af62e055b7cc0d416dcee412",
              "datavalue": {
                "value": "ae3d352c-7da5-45e9-82c9-a39a2bae5167",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$2639363e-4bd9-7eaa-4510-f26b96fab9c6",
            "rank": "normal"
          }
        ],
        "P2130": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P2130",
              "hash": "8aee52c3b646955dd42d4def6b076306c7eb7005",
              "datavalue": {
                "value": {
                  "amount": "+220000000000",
                  "unit": "http://www.wikidata.org/entity/Q4917"
                },
                "type": "quantity"
              },
              "datatype": "quantity"
            },
            "type": "statement",
            "qualifiers": {
              "P1480": [
                {
                  "snaktype": "value",
                  "property": "P1480",
                  "hash": "fb0102b01e8875f4e3a3c29632412e89593e3401",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 37113960,
                      "id": "Q37113960"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P1480"
            ],
            "id": "Q284163$1dcedc44-4211-b1ae-4859-af30c2d3058b",
            "rank": "normal"
          }
        ],
        "P155": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P155",
              "hash": "108887613999ac8be2ecf64ab262263519bcfc16",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 170645,
                  "id": "Q170645"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$6C1F8148-0870-4F9D-A2C8-A6B890B7D4ED",
            "rank": "normal"
          }
        ],
        "P156": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P156",
              "hash": "343b720ecfe6b31ddc9e339644bfc435999925e5",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 5020214,
                  "id": "Q5020214"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$02B2DA0A-2583-455D-AB2D-64A3BFB3BE9C",
            "rank": "normal"
          }
        ],
        "P6900": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P6900",
              "hash": "d7148875b253824354ca6adedf223c746c196716",
              "datavalue": {
                "value": "2022 fifaワールドカップ",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$94ed7841-452d-d073-529d-2a349b23abeb",
            "rank": "normal"
          }
        ],
        "P227": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P227",
              "hash": "9d2ab3210c2c71f685afb3f5fc43d276e76faf8e",
              "datavalue": {
                "value": "1098574583",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "qualifiers": {
              "P1810": [
                {
                  "snaktype": "value",
                  "property": "P1810",
                  "hash": "bab9c962860009990c98826ca90b9398d491a4fb",
                  "datavalue": {
                    "value": "FIFA Fußball-Weltmeisterschaft (22. : 2022 : Katar)",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ]
            },
            "qualifiers-order": [
              "P1810"
            ],
            "id": "Q284163$a3c0397e-42e0-5b11-eb7e-ed5a8b1ca6ef",
            "rank": "normal",
            "references": [
              {
                "hash": "d02d25aa9ebae6f7af99d69b25a3cf2869ce49c6",
                "snaks": {
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "08541ba9a5e16f6c42705f2ab0447bcefbf26c4b",
                      "datavalue": {
                        "value": {
                          "time": "+2022-12-14T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P813"
                ]
              }
            ]
          }
        ],
        "P3967": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3967",
              "hash": "1a7f2b9ca3e2973441e604ef3dbd10b858a154c7",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 55620455,
                  "id": "Q55620455"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q284163$170f5601-43a2-fbf1-d4b2-73dff06cfdd0",
            "rank": "normal"
          }
        ],
        "P1350": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1350",
              "hash": "3144896a606b5dea1b111b8e37556938b503e3eb",
              "datavalue": {
                "value": {
                  "amount": "+64",
                  "unit": "1"
                },
                "type": "quantity"
              },
              "datatype": "quantity"
            },
            "type": "statement",
            "id": "Q284163$b6a81494-477b-c1ec-2656-43ea7e77da3d",
            "rank": "normal"
          }
        ],
        "P214": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P214",
              "hash": "fd6dc8cd0ab60a94d757a1de03e3d7b6a04a12a1",
              "datavalue": {
                "value": "29146217719909140636",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$b1a26ed5-4311-a342-5f5f-73a9525deff7",
            "rank": "normal"
          }
        ],
        "P269": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P269",
              "hash": "73ca252d1a9c5c71e6a9b96d1c425b5f084789de",
              "datavalue": {
                "value": "257480439",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$00deb8df-47bd-ff24-4b74-71374bba6a38",
            "rank": "normal"
          }
        ],
        "P1346": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1346",
              "hash": "d92ee08ba765478ec9c461f9c225839d73fe401c",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 79800,
                  "id": "Q79800"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1545": [
                {
                  "snaktype": "value",
                  "property": "P1545",
                  "hash": "0e979f28bf306fefdcd352b4eb8dee5da2153a6d",
                  "datavalue": {
                    "value": "3",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ]
            },
            "qualifiers-order": [
              "P1545"
            ],
            "id": "Q284163$fbd3c248-4fbb-0f70-7d3b-adaf95e80999",
            "rank": "normal"
          }
        ],
        "P1923": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1923",
              "hash": "a8f87ff16c0749953619d5b355463e384b283a18",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 79800,
                  "id": "Q79800"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "3df9f7d5d4cbc791e6579735e13985769a537fb9",
                  "datavalue": {
                    "value": {
                      "amount": "+1",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$7a9b48c2-4174-007b-3edc-b457927989c5",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1923",
              "hash": "679fe366bbfad0df79181223bf2bc76ebdac4103",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 47774,
                  "id": "Q47774"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "270f0c96a63b9d8572cb04ebbdf12b98a9dff154",
                  "datavalue": {
                    "value": {
                      "amount": "+2",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$6a182882-4e31-c027-bc39-93fefb64b2e9",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1923",
              "hash": "62432fbc850c79635f7239805fd5fe1d9bf54264",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 134479,
                  "id": "Q134479"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "ba2a02dbc6c7be6ccb48d427264a770b105256ed",
                  "datavalue": {
                    "value": {
                      "amount": "+3",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$5aa8a64e-4af3-193b-bcaf-9befe0f28d34",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1923",
              "hash": "7ca973a9174d33f805a21d978a43e63d6afdb060",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 207337,
                  "id": "Q207337"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1352": [
                {
                  "snaktype": "value",
                  "property": "P1352",
                  "hash": "5e5880d79c7b10631a47acef228c5140c9b8bca1",
                  "datavalue": {
                    "value": {
                      "amount": "+4",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ]
            },
            "qualifiers-order": [
              "P1352"
            ],
            "id": "Q284163$e0d2bcdf-4fc4-4115-7326-27120468b9c9",
            "rank": "normal"
          }
        ],
        "P3279": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3279",
              "hash": "310a48b32e55730a472826a16033bbe46b2b1784",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 21621995,
                  "id": "Q21621995"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1351": [
                {
                  "snaktype": "value",
                  "property": "P1351",
                  "hash": "d7ee4ce3cf7fbbb45976b34ec2f7a1bd4e6de273",
                  "datavalue": {
                    "value": {
                      "amount": "+8",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ],
              "P54": [
                {
                  "snaktype": "value",
                  "property": "P54",
                  "hash": "3c03c6075208e3c8e8509efb7957cc8d353d5c2f",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 47774,
                      "id": "Q47774"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ],
              "P1013": [
                {
                  "snaktype": "value",
                  "property": "P1013",
                  "hash": "4df2535aaea89e1ca2ff339e724f7191214262c4",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 33246803,
                      "id": "Q33246803"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P1351",
              "P54",
              "P1013"
            ],
            "id": "Q284163$B521F8BC-D83F-4D3B-90F3-B0D930AE7CBF",
            "rank": "normal",
            "references": [
              {
                "hash": "942a0d3dbf67864c4c5f3f2b3d3c72fdd9486dc5",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "b73dfe1c5c60fc203f563e6fc7671c94816d920a",
                      "datavalue": {
                        "value": "https://www.espn.com/soccer/stats/_/league/FIFA.WORLD/season/2022",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7f0dfa43261621a38524db1db96fcb200ea2361d",
                      "datavalue": {
                        "value": {
                          "time": "+2026-07-01T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3279",
              "hash": "473dfc188701e22dd9c0a046233bbcd3eb4ee2f6",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 615,
                  "id": "Q615"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1013": [
                {
                  "snaktype": "value",
                  "property": "P1013",
                  "hash": "b515fc81cafbbc8f4c1017ce8faf5f330b813d65",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 652965,
                      "id": "Q652965"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ],
              "P54": [
                {
                  "snaktype": "value",
                  "property": "P54",
                  "hash": "77a0924293f1ca458fb046fb601f21da255c24e2",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 79800,
                      "id": "Q79800"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P1013",
              "P54"
            ],
            "id": "Q284163$e1af01f1-45f3-1ef5-3985-3a381c09718c",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3279",
              "hash": "8906dd2c84dcac8d9cd21244a4a15d29c867e5eb",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 96105248,
                  "id": "Q96105248"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1013": [
                {
                  "snaktype": "value",
                  "property": "P1013",
                  "hash": "c8185fa3181234454db0518fe268b85c5c1beab9",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 121112960,
                      "id": "Q121112960"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ],
              "P54": [
                {
                  "snaktype": "value",
                  "property": "P54",
                  "hash": "77a0924293f1ca458fb046fb601f21da255c24e2",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 79800,
                      "id": "Q79800"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P1013",
              "P54"
            ],
            "id": "Q284163$4b3cd3eb-4fd1-2c62-f271-7b3d2f544acb",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3279",
              "hash": "6e3c504d7e0e9e0de7f0f2c29a702bf4ff0863ee",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 3275904,
                  "id": "Q3275904"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1013": [
                {
                  "snaktype": "value",
                  "property": "P1013",
                  "hash": "5bcf52cacba956d2d243d589c182634886156e61",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 121111173,
                      "id": "Q121111173"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ],
              "P54": [
                {
                  "snaktype": "value",
                  "property": "P54",
                  "hash": "77a0924293f1ca458fb046fb601f21da255c24e2",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 79800,
                      "id": "Q79800"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P1013",
              "P54"
            ],
            "id": "Q284163$7b080e66-4375-e24e-b0ae-0f4300205077",
            "rank": "normal"
          }
        ],
        "P1351": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1351",
              "hash": "fbfc6fb9a93836af8739b08a313c9cf4fcd95176",
              "datavalue": {
                "value": {
                  "amount": "+172",
                  "unit": "1"
                },
                "type": "quantity"
              },
              "datatype": "quantity"
            },
            "type": "statement",
            "id": "Q284163$cf38706b-4d52-c9db-f9f6-cf5f8170aa71",
            "rank": "normal"
          }
        ],
        "P1110": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1110",
              "hash": "1cd2db2be025025d2d6de0f3d992e91357fd29c0",
              "datavalue": {
                "value": {
                  "amount": "+3404252",
                  "unit": "1"
                },
                "type": "quantity"
              },
              "datatype": "quantity"
            },
            "type": "statement",
            "id": "Q284163$dd489d94-4120-46db-2adc-43cd6399f9f9",
            "rank": "normal"
          }
        ],
        "P8313": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P8313",
              "hash": "8a3469c166fbf8a5951044c8a3d9df594267cc21",
              "datavalue": {
                "value": "VM_i_fodbold_for_mænd_2022",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$b2e29f1e-46ed-9289-6c8d-46f197f237d4",
            "rank": "normal"
          }
        ],
        "P268": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P268",
              "hash": "d8fa30b9f68075e11c363743828007b0e022c2fc",
              "datavalue": {
                "value": "18041539r",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$c97871dd-4103-4e2f-51fa-67dd97f1b995",
            "rank": "normal"
          }
        ],
        "P4173": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P4173",
              "hash": "3e2c6d700796a6a65e54c5eb66af49110efbfe97",
              "datavalue": {
                "value": "108912491941762",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$d1c4a92b-41d9-8f8d-7242-99ce048aaba1",
            "rank": "normal"
          }
        ],
        "P12086": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P12086",
              "hash": "a7233cd51ad513e748ee80c694125a2d5d2d3fcf",
              "datavalue": {
                "value": "Wereldkampioenschap_voetbal_2022",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "qualifiers": {
              "P9675": [
                {
                  "snaktype": "value",
                  "property": "P9675",
                  "hash": "120ed866f9bd244257ac1e84387a92a5eadc0427",
                  "datavalue": {
                    "value": "106927",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ]
            },
            "qualifiers-order": [
              "P9675"
            ],
            "id": "Q284163$7A8663B9-1926-40B8-B816-A7E2DC8B2061",
            "rank": "normal"
          }
        ],
        "P12800": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P12800",
              "hash": "574a5ee345d84214e59bdd104dae0c3514be4045",
              "datavalue": {
                "value": "fr:Coupe_du_monde_de_football_de_2022",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$330F636E-1099-48E2-871C-9D8332BF6017",
            "rank": "normal"
          }
        ],
        "P13230": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P13230",
              "hash": "c2279d25653104c57819fa9c85da79b401ba6e69",
              "datavalue": {
                "value": "e8f35947-3d2c-45be-88ec-e23dcde549d9",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$8627A73A-EB08-47E4-9535-C2432A8C25C9",
            "rank": "normal"
          }
        ],
        "P691": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P691",
              "hash": "3c3775e38fca1d4e2484dcc5ab958f111a4d226c",
              "datavalue": {
                "value": "xx0301246",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$c0e7a022-423c-4fb4-3deb-935ed1eec41a",
            "rank": "normal"
          }
        ],
        "P244": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P244",
              "hash": "5c3bdd8d743b65de02972992f30e3c5a9fa99200",
              "datavalue": {
                "value": "n2020027567",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$4882d4ca-4cfb-fbdf-86be-2c59f17be210",
            "rank": "normal"
          }
        ],
        "P1417": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1417",
              "hash": "44b6c4c71c3a2ea6d9eb346854dedc8ae8f5a1be",
              "datavalue": {
                "value": "sports/2022-FIFA-World-Cup",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "qualifiers": {
              "P1810": [
                {
                  "snaktype": "value",
                  "property": "P1810",
                  "hash": "c827a609ebc52575f1f85722f6ba16794f63361b",
                  "datavalue": {
                    "value": "2022 FIFA World Cup",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ],
              "P2093": [
                {
                  "snaktype": "value",
                  "property": "P2093",
                  "hash": "e44ee9955b3b21b14fca2280e47a24b854e48e1d",
                  "datavalue": {
                    "value": "Zeidan",
                    "type": "string"
                  },
                  "datatype": "string"
                },
                {
                  "snaktype": "value",
                  "property": "P2093",
                  "hash": "3a08cebe646513a8c5153828816454ca930a1cef",
                  "datavalue": {
                    "value": "Adam",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ]
            },
            "qualifiers-order": [
              "P1810",
              "P2093"
            ],
            "id": "Q284163$e13ed0ef-43d0-7ff5-0d38-72f8cf049f77",
            "rank": "normal"
          }
        ],
        "P345": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P345",
              "hash": "cd63438a5a92b78b3565f6d1a63ce731d683788a",
              "datavalue": {
                "value": "tt12729982",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$2439778e-4628-ecc5-a9a5-84d15d3f0d45",
            "rank": "normal"
          }
        ],
        "P3788": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3788",
              "hash": "f023ed943a4b83e88a201cae2c9bfe1cd2c1b72f",
              "datavalue": {
                "value": "000070106",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$c919d39f-4ddf-310f-4625-4c3fe92e9d1c",
            "rank": "normal"
          }
        ],
        "P8189": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P8189",
              "hash": "65affee746996bc5f4798a0141c2a76818871809",
              "datavalue": {
                "value": "987012091165705171",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$c456cc42-4a4e-3943-2b97-57c2a775eb05",
            "rank": "normal"
          }
        ],
        "P1890": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1890",
              "hash": "81767327c084cfbaf6ac9de2484e719ee2238278",
              "datavalue": {
                "value": "000967120",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$51ddf597-47e4-4709-5462-4541f326a53c",
            "rank": "normal"
          }
        ],
        "P9984": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P9984",
              "hash": "505dcdf71f2470ce8571fdad7da58a236b0e0b46",
              "datavalue": {
                "value": "981060937254706706",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$c1635298-435c-5914-9710-cdeccce63428",
            "rank": "normal"
          }
        ],
        "P1048": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1048",
              "hash": "0cbd9043b7b5550d9559607a9c4d2d32225b433e",
              "datavalue": {
                "value": "029192168",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "qualifiers": {
              "P1810": [
                {
                  "snaktype": "value",
                  "property": "P1810",
                  "hash": "415e667e292f3326a1eccddf5b147b9f2ecc16a1",
                  "datavalue": {
                    "value": "World Cup (Soccer) (2022 : Qatar)",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ],
              "P3831": [
                {
                  "snaktype": "value",
                  "property": "P3831",
                  "hash": "7b90719c667373fc49bd51c707e85bbabb7b64ca",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 1128340,
                      "id": "Q1128340"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ],
              "P6477": [
                {
                  "snaktype": "value",
                  "property": "P6477",
                  "hash": "5ea528d065350f804b64227e87114962b99379b8",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 1469824,
                      "id": "Q1469824"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P1810",
              "P3831",
              "P6477"
            ],
            "id": "Q284163$db045f27-4e8b-8a8f-d08b-58f62c87857d",
            "rank": "normal"
          }
        ],
        "P13526": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P13526",
              "hash": "484c8889640cf6e090e58428a39314e700a9776b",
              "datavalue": {
                "value": "qatar-2022-fifa-world-cup",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$62DC2200-5E0F-4FC2-86E9-CE4DB7F4AB65",
            "rank": "normal"
          }
        ],
        "P13484": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P13484",
              "hash": "20490f4335e0ed9381bd3fed4f0c4b3d8abc8477",
              "datavalue": {
                "value": "2022-fifa-world-cup-qatar",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "qualifiers": {
              "P6760": [
                {
                  "snaktype": "value",
                  "property": "P6760",
                  "hash": "59926e3c9554e58c0167b03292466056c92369d8",
                  "datavalue": {
                    "value": "26522",
                    "type": "string"
                  },
                  "datatype": "external-id"
                }
              ],
              "P1810": [
                {
                  "snaktype": "value",
                  "property": "P1810",
                  "hash": "ce957a5246f2d85345fb5c8fba5d8ca12db00ec8",
                  "datavalue": {
                    "value": "2022 FIFA World Cup Qatar",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ],
              "P1552": [
                {
                  "snaktype": "value",
                  "property": "P1552",
                  "hash": "b76b8564371282f717acdb4bdb9d47cecb18fee9",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 116763049,
                      "id": "Q116763049"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ],
              "P585": [
                {
                  "snaktype": "value",
                  "property": "P585",
                  "hash": "8e96fcbf23a30cd998400e0e3c4407f04ae8c1f6",
                  "datavalue": {
                    "value": {
                      "time": "+2025-10-26T00:00:00Z",
                      "timezone": 0,
                      "before": 0,
                      "after": 0,
                      "precision": 11,
                      "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                    },
                    "type": "time"
                  },
                  "datatype": "time"
                }
              ]
            },
            "qualifiers-order": [
              "P6760",
              "P1810",
              "P1552",
              "P585"
            ],
            "id": "Q284163$36f982ea-4cd2-417e-8aaf-b4d095fb6ca0",
            "rank": "normal",
            "references": [
              {
                "hash": "4628f7effc98d4477f7bd3de0f9b9d76b2e52591",
                "snaks": {
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "ca35c6a6ee16c3cd1be9226a23eb2e7ac48f48ad",
                      "datavalue": {
                        "value": {
                          "time": "+2025-10-26T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "5a9ac7edaf80f47d974990f43f7d7f30abbb61e2",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 2071334,
                          "id": "Q2071334"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P813",
                  "P248"
                ]
              }
            ]
          }
        ],
        "P9322": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P9322",
              "hash": "d2164a35064ebdb7785282b7ab0a9235e4f43467",
              "datavalue": {
                "value": "0429125-Mistrovstvi-sveta-ve-fotbale",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$74BB0FB5-B01F-4827-BA1B-DE7C83D3559A",
            "rank": "normal"
          }
        ],
        "P1617": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1617",
              "hash": "1c2bb5e4375ee0c27623188fc5c0c28ce69febc3",
              "datavalue": {
                "value": "bbb28178-8069-4b06-939e-bca0571808f0",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$4c5ec1b3-4c42-a990-a63d-e996fb422ba4",
            "rank": "normal",
            "references": [
              {
                "hash": "8582d8416671f1f2567247201bac753552435ca5",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "ea55dc6ac5c3ab77c77d4ae7979e3276d0d4cd20",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 18336371,
                          "id": "Q18336371"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P248"
                ]
              }
            ]
          }
        ],
        "P14544": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P14544",
              "hash": "521c68a9d2d88e6b5f273afc9caefe1e3e4503b7",
              "datavalue": {
                "value": "1079",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$AB6F64DB-6036-4E99-90F5-0742BEF654B6",
            "rank": "normal"
          }
        ],
        "P13236": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P13236",
              "hash": "2451f2b00d596fb7489ca0c58e2e26cfa74a98fc",
              "datavalue": {
                "value": "2022_fifa_world_cup",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$BEC1FB16-A0DA-4D00-9635-046D4AFF1D6B",
            "rank": "normal"
          }
        ],
        "P13390": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P13390",
              "hash": "844ed17b2aacd0e4649987759d2936380f494ae3",
              "datavalue": {
                "value": "2022_fifa_world_cup",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$04B9A8F4-BAF8-43A9-B3D2-9FE81BA0FAB1",
            "rank": "normal"
          }
        ],
        "P2603": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P2603",
              "hash": "bbd923bddf48affc15e29fb9c8dc40225e9f3a7a",
              "datavalue": {
                "value": "5173517",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$98F683A9-AE73-4452-B6A1-E20BD62E8C1C",
            "rank": "normal",
            "references": [
              {
                "hash": "ddec61635e880437b8b04c8a94797462e36cacfb",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "27489c74a6d9c8bb433f99e8b1e6dbd6305747c7",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 140930981,
                          "id": "Q140930981"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "900be1cb5f397b7f4ae5d9d017c7ee57ef1bebe6",
                      "datavalue": {
                        "value": "https://www.kinopoisk.ru/film/5173517/",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "968ec8a6cfc028d552e8144a700d08137b4833b1",
                      "datavalue": {
                        "value": {
                          "time": "+2026-08-07T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P248",
                  "P854",
                  "P813"
                ]
              }
            ]
          }
        ],
        "P12036": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P12036",
              "hash": "476b0eacdc30eefa3001f5f6426deff8fcef01ea",
              "datavalue": {
                "value": "E0000000189",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q284163$63e0ac2b-46bb-1563-1081-59313f44fae0",
            "rank": "normal"
          }
        ]
      }
    }
  },
  "success": 1
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
