---
intent: LIQUIDITY_DEPTH_VERIFY
slug: liq-independentreserve-book
status: rejected
captured_at: 2026-10-08T04:42:03Z
request_url: https://api.independentreserve.com/Public/GetOrderBook?primaryCurrencyCode=xbt&secondaryCurrencyCode=usd
content_type: application/json
inputs: |
  {"upbit": "USDT-BTC", "poloniex": "BTC_USDT", "lbank": "btc_usdt", "bingx": "BTC-USDT", "whitebit": "BTC_USDT", "deribit": "BTC_USDC", "ir": "xbt", "hl": "BTC", "dydx": "BTC-USD", "binance": "BTCUSDT"}
intent_description: |
  Measures bid-ask order book depth, cumulative slippage bands, and market maker liquidity across decentralized pools.
answer_requirement: |
  Must return the live bid/ask order book (depth levels) for the pair asked.
capture_note: |
  (none)
reviewer_note: "auto_review: [0.80|heuristic] no bid/ask depth or pool liquidity structure found"
reviewed_at: 2026-10-08T04:56:30Z
review_source: auto_review
review_mode: heuristic
llm_used: false
review_confidence: 0.800
---

## Raw API output

```json
{
  "BuyOrders": [
    {
      "OrderType": "LimitBid",
      "Price": 82500,
      "Volume": 1.55129715
    },
    {
      "OrderType": "LimitBid",
      "Price": 82417.92,
      "Volume": 0.36488533
    },
    {
      "OrderType": "LimitBid",
      "Price": 82355.09,
      "Volume": 0.03376133
    },
    {
      "OrderType": "LimitBid",
      "Price": 82338.27,
      "Volume": 0.01334
    },
    {
      "OrderType": "LimitBid",
      "Price": 82101.93,
      "Volume": 0.1924
    },
    {
      "OrderType": "LimitBid",
      "Price": 82069.41,
      "Volume": 0.162006
    },
    {
      "OrderType": "LimitBid",
      "Price": 82069.4,
      "Volume": 1.19036246
    },
    {
      "OrderType": "LimitBid",
      "Price": 82026.69,
      "Volume": 0.0421
    },
    {
      "OrderType": "LimitBid",
      "Price": 82026.62,
      "Volume": 0.02100094
    },
    {
      "OrderType": "LimitBid",
      "Price": 82011.92,
      "Volume": 0.26877335
    },
    {
      "OrderType": "LimitBid",
      "Price": 82011.91,
      "Volume": 0.00011128
    },
    {
      "OrderType": "LimitBid",
      "Price": 82000,
      "Volume": 0.00364033
    },
    {
      "OrderType": "LimitBid",
      "Price": 81985.49,
      "Volume": 0.1085668
    },
    {
      "OrderType": "LimitBid",
      "Price": 81977.13,
      "Volume": 0.00083883
    },
    {
      "OrderType": "LimitBid",
      "Price": 81944.91,
      "Volume": 0.06
    },
    {
      "OrderType": "LimitBid",
      "Price": 81936.25,
      "Volume": 0.00011138
    },
    {
      "OrderType": "LimitBid",
      "Price": 81907.9,
      "Volume": 0.00203176
    },
    {
      "OrderType": "LimitBid",
      "Price": 81872.76,
      "Volume": 0.00010348
    },
    {
      "OrderType": "LimitBid",
      "Price": 81867.64,
      "Volume": 0.044625
    },
    {
      "OrderType": "LimitBid",
      "Price": 81860.59,
      "Volume": 0.00011148
    },
    {
      "OrderType": "LimitBid",
      "Price": 81853.5,
      "Volume": 0.00025254
    },
    {
      "OrderType": "LimitBid",
      "Price": 81829.73,
      "Volume": 0.219
    },
    {
      "OrderType": "LimitBid",
      "Price": 81829.72,
      "Volume": 0.175452
    },
    {
      "OrderType": "LimitBid",
      "Price": 81807.58,
      "Volume": 0.00842287
    },
    {
      "OrderType": "LimitBid",
      "Price": 81804.63,
      "Volume": 0.00010356
    },
    {
      "OrderType": "LimitBid",
      "Price": 81803.23,
      "Volume": 0.01684663
    },
    {
      "OrderType": "LimitBid",
      "Price": 81798.84,
      "Volume": 0.00315891
    },
    {
      "OrderType": "LimitBid",
      "Price": 81784.93,
      "Volume": 0.00011159
    },
    {
      "OrderType": "LimitBid",
      "Price": 81784.25,
      "Volume": 0.00674021
    },
    {
      "OrderType": "LimitBid",
      "Price": 81763.76,
      "Volume": 0.00037832
    },
    {
      "OrderType": "LimitBid",
      "Price": 81754.69,
      "Volume": 0.01364899
    },
    {
      "OrderType": "LimitBid",
      "Price": 81715.01,
      "Volume": 0.0421
    },
    {
      "OrderType": "LimitBid",
      "Price": 81715,
      "Volume": 1.12898735
    },
    {
      "OrderType": "LimitBid",
      "Price": 81691.41,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitBid",
      "Price": 81683.72,
      "Volume": 0.00189348
    },
    {
      "OrderType": "LimitBid",
      "Price": 81671.44,
      "Volume": 0.00011174
    },
    {
      "OrderType": "LimitBid",
      "Price": 81606,
      "Volume": 0.01495692
    },
    {
      "OrderType": "LimitBid",
      "Price": 81584.91,
      "Volume": 0.00010385
    },
    {
      "OrderType": "LimitBid",
      "Price": 81518.95,
      "Volume": 0.04743273
    },
    {
      "OrderType": "LimitBid",
      "Price": 81477.75,
      "Volume": 0.00010397
    },
    {
      "OrderType": "LimitBid",
      "Price": 81447.69,
      "Volume": 0.0020527
    },
    {
      "OrderType": "LimitBid",
      "Price": 81438,
      "Volume": 0.00253832
    },
    {
      "OrderType": "LimitBid",
      "Price": 81406.83,
      "Volume": 0.1036881
    },
    {
      "OrderType": "LimitBid",
      "Price": 81403.37,
      "Volume": 0.05925286
    },
    {
      "OrderType": "LimitBid",
      "Price": 81396.93,
      "Volume": 0.09500767
    },
    {
      "OrderType": "LimitBid",
      "Price": 81318.9,
      "Volume": 0.04754942
    },
    {
      "OrderType": "LimitBid",
      "Price": 81302.35,
      "Volume": 0.01695042
    },
    {
      "OrderType": "LimitBid",
      "Price": 81299.5,
      "Volume": 0.00254265
    },
    {
      "OrderType": "LimitBid",
      "Price": 81296.04,
      "Volume": 0.00010422
    },
    {
      "OrderType": "LimitBid",
      "Price": 81271.8,
      "Volume": 0.04239199
    },
    {
      "OrderType": "LimitBid",
      "Price": 81240,
      "Volume": 0.01696343
    },
    {
      "OrderType": "LimitBid",
      "Price": 81230.25,
      "Volume": 0.16972226
    },
    {
      "OrderType": "LimitBid",
      "Price": 81161,
      "Volume": 0.00254699
    },
    {
      "OrderType": "LimitBid",
      "Price": 81149.55,
      "Volume": 0.00010439
    },
    {
      "OrderType": "LimitBid",
      "Price": 81149,
      "Volume": 0.09529794
    },
    {
      "OrderType": "LimitBid",
      "Price": 81091.75,
      "Volume": 0.043
    },
    {
      "OrderType": "LimitBid",
      "Price": 81043.19,
      "Volume": 0.01700462
    },
    {
      "OrderType": "LimitBid",
      "Price": 81023.19,
      "Volume": 0.00042522
    },
    {
      "OrderType": "LimitBid",
      "Price": 81022.5,
      "Volume": 0.1564826
    },
    {
      "OrderType": "LimitBid",
      "Price": 81006.14,
      "Volume": 0.00010459
    },
    {
      "OrderType": "LimitBid",
      "Price": 81000,
      "Volume": 0.06068423
    },
    {
      "OrderType": "LimitBid",
      "Price": 80900.3,
      "Volume": 0.0955909
    },
    {
      "OrderType": "LimitBid",
      "Price": 80884,
      "Volume": 0.01107475
    },
    {
      "OrderType": "LimitBid",
      "Price": 80883.5,
      "Volume": 0.00340764
    },
    {
      "OrderType": "LimitBid",
      "Price": 80843.53,
      "Volume": 0.00027446
    },
    {
      "OrderType": "LimitBid",
      "Price": 80828.8,
      "Volume": 0.00287026
    },
    {
      "OrderType": "LimitBid",
      "Price": 80820.01,
      "Volume": 0.00010482
    },
    {
      "OrderType": "LimitBid",
      "Price": 80745.5,
      "Volume": 0.00256009
    },
    {
      "OrderType": "LimitBid",
      "Price": 80735.8,
      "Volume": 0.00103565
    },
    {
      "OrderType": "LimitBid",
      "Price": 80715.2,
      "Volume": 0.00010497
    },
    {
      "OrderType": "LimitBid",
      "Price": 80652.37,
      "Volume": 0.09588475
    },
    {
      "OrderType": "LimitBid",
      "Price": 80641.62,
      "Volume": 0.28566561
    },
    {
      "OrderType": "LimitBid",
      "Price": 80622.23,
      "Volume": 0.00042733
    },
    {
      "OrderType": "LimitBid",
      "Price": 80494.12,
      "Volume": 0.50910493
    },
    {
      "OrderType": "LimitBid",
      "Price": 80489.13,
      "Volume": 0.00010525
    },
    {
      "OrderType": "LimitBid",
      "Price": 80488.8,
      "Volume": 0.22258279
    },
    {
      "OrderType": "LimitBid",
      "Price": 80468.5,
      "Volume": 0.00256891
    },
    {
      "OrderType": "LimitBid",
      "Price": 80427.59,
      "Volume": 0.01713478
    },
    {
      "OrderType": "LimitBid",
      "Price": 80423.2,
      "Volume": 0.00010535
    },
    {
      "OrderType": "LimitBid",
      "Price": 80412.4,
      "Volume": 0.0018
    },
    {
      "OrderType": "LimitBid",
      "Price": 80404.44,
      "Volume": 0.09618041
    },
    {
      "OrderType": "LimitBid",
      "Price": 80400.99,
      "Volume": 0.00321383
    },
    {
      "OrderType": "LimitBid",
      "Price": 80399.25,
      "Volume": 0.0425
    },
    {
      "OrderType": "LimitBid",
      "Price": 80374.32,
      "Volume": 0.04286535
    },
    {
      "OrderType": "LimitBid",
      "Price": 80330.69,
      "Volume": 0.00042888
    },
    {
      "OrderType": "LimitBid",
      "Price": 80330,
      "Volume": 0.21435003
    },
    {
      "OrderType": "LimitBid",
      "Price": 80271.92,
      "Volume": 0.00289017
    },
    {
      "OrderType": "LimitBid",
      "Price": 80260.75,
      "Volume": 0.00257556
    },
    {
      "OrderType": "LimitBid",
      "Price": 80191.5,
      "Volume": 0.02362969
    },
    {
      "OrderType": "LimitBid",
      "Price": 80176.92,
      "Volume": 0.00429708
    },
    {
      "OrderType": "LimitBid",
      "Price": 80156.88,
      "Volume": 0.00010569
    },
    {
      "OrderType": "LimitBid",
      "Price": 80155.74,
      "Volume": 0.09647884
    },
    {
      "OrderType": "LimitBid",
      "Price": 80138.37,
      "Volume": 0.00482498
    },
    {
      "OrderType": "LimitBid",
      "Price": 80130.14,
      "Volume": 0.00010573
    },
    {
      "OrderType": "LimitBid",
      "Price": 80122.25,
      "Volume": 0.11742874
    },
    {
      "OrderType": "LimitBid",
      "Price": 80067.61,
      "Volume": 0.1721182
    },
    {
      "OrderType": "LimitBid",
      "Price": 80063.25,
      "Volume": 0.09660951
    },
    {
      "OrderType": "LimitBid",
      "Price": 80053,
      "Volume": 0.00258224
    },
    {
      "OrderType": "LimitBid",
      "Price": 80051.6,
      "Volume": 0.00579626
    },
    {
      "OrderType": "LimitBid",
      "Price": 79986.4,
      "Volume": 0.04307323
    },
    {
      "OrderType": "LimitBid",
      "Price": 79984.44,
      "Volume": 0.12922297
    },
    {
      "OrderType": "LimitBid",
      "Price": 79907.81,
      "Volume": 0.09677818
    },
    {
      "OrderType": "LimitBid",
      "Price": 79900.87,
      "Volume": 0.01724773
    },
    {
      "OrderType": "LimitBid",
      "Price": 79900.82,
      "Volume": 0.09680591
    },
    {
      "OrderType": "LimitBid",
      "Price": 79845.25,
      "Volume": 0.045
    },
    {
      "OrderType": "LimitBid",
      "Price": 79836.01,
      "Volume": 0.00010612
    },
    {
      "OrderType": "LimitBid",
      "Price": 79823.25,
      "Volume": 0.00010613
    },
    {
      "OrderType": "LimitBid",
      "Price": 79776,
      "Volume": 0.00259121
    },
    {
      "OrderType": "LimitBid",
      "Price": 79749.26,
      "Volume": 0.09698988
    },
    {
      "OrderType": "LimitBid",
      "Price": 79746.63,
      "Volume": 0.0148124
    },
    {
      "OrderType": "LimitBid",
      "Price": 79717.13,
      "Volume": 0.00518624
    },
    {
      "OrderType": "LimitBid",
      "Price": 79706.75,
      "Volume": 0.00086448
    },
    {
      "OrderType": "LimitBid",
      "Price": 79676.28,
      "Volume": 0.00012972
    },
    {
      "OrderType": "LimitBid",
      "Price": 79659.89,
      "Volume": 0.09707938
    },
    {
      "OrderType": "LimitBid",
      "Price": 79640.96,
      "Volume": 0.0008652
    },
    {
      "OrderType": "LimitBid",
      "Price": 79638.19,
      "Volume": 0.00043261
    },
    {
      "OrderType": "LimitBid",
      "Price": 79638.14,
      "Volume": 0.0002163
    },
    {
      "OrderType": "LimitBid",
      "Price": 79637.5,
      "Volume": 0.20809272
    },
    {
      "OrderType": "LimitBid",
      "Price": 79564.4,
      "Volume": 0.00970087
    },
    {
      "OrderType": "LimitBid",
      "Price": 79559.94,
      "Volume": 0.04070621
    },
    {
      "OrderType": "LimitBid",
      "Price": 79547.98,
      "Volume": 0.0972353
    },
    {
      "OrderType": "LimitBid",
      "Price": 79540.79,
      "Volume": 0.00010652
    },
    {
      "OrderType": "LimitBid",
      "Price": 79499,
      "Volume": 0.00260023
    },
    {
      "OrderType": "LimitBid",
      "Price": 79489.66,
      "Volume": 0.00043342
    },
    {
      "OrderType": "LimitBid",
      "Price": 79488.22,
      "Volume": 0.00010658
    },
    {
      "OrderType": "LimitBid",
      "Price": 79460.92,
      "Volume": 0.00097322
    },
    {
      "OrderType": "LimitBid",
      "Price": 79447.71,
      "Volume": 0.00486693
    },
    {
      "OrderType": "LimitBid",
      "Price": 79411.18,
      "Volume": 0.09738342
    },
    {
      "OrderType": "LimitBid",
      "Price": 79388.4,
      "Volume": 0.00433976
    },
    {
      "OrderType": "LimitBid",
      "Price": 79360.5,
      "Volume": 0.00260477
    },
    {
      "OrderType": "LimitBid",
      "Price": 79277.4,
      "Volume": 0.04345845
    },
    {
      "OrderType": "LimitBid",
      "Price": 79275.95,
      "Volume": 0.09756896
    },
    {
      "OrderType": "LimitBid",
      "Price": 79274.4,
      "Volume": 0.0039996
    },
    {
      "OrderType": "LimitBid",
      "Price": 79244.46,
      "Volume": 0.00010691
    },
    {
      "OrderType": "LimitBid",
      "Price": 79222,
      "Volume": 0.00260933
    },
    {
      "OrderType": "LimitBid",
      "Price": 79163.26,
      "Volume": 0.09768841
    },
    {
      "OrderType": "LimitBid",
      "Price": 79158.75,
      "Volume": 0.00435235
    },
    {
      "OrderType": "LimitBid",
      "Price": 79151.77,
      "Volume": 0.00010703
    },
    {
      "OrderType": "LimitBid",
      "Price": 79151.66,
      "Volume": 0.02176374
    },
    {
      "OrderType": "LimitBid",
      "Price": 79120.51,
      "Volume": 0.09776064
    },
    {
      "OrderType": "LimitBid",
      "Price": 79083.5,
      "Volume": 0.0026139
    },
    {
      "OrderType": "LimitBid",
      "Price": 79014.25,
      "Volume": 0.045
    },
    {
      "OrderType": "LimitBid",
      "Price": 78996.6,
      "Volume": 0.09791398
    },
    {
      "OrderType": "LimitBid",
      "Price": 78947.03,
      "Volume": 0.00010732
    },
    {
      "OrderType": "LimitBid",
      "Price": 78945.69,
      "Volume": 0.00043641
    },
    {
      "OrderType": "LimitBid",
      "Price": 78945,
      "Volume": 0.0488784
    },
    {
      "OrderType": "LimitBid",
      "Price": 78915.33,
      "Volume": 0.09799531
    },
    {
      "OrderType": "LimitBid",
      "Price": 78885.8,
      "Volume": 0.049016
    },
    {
      "OrderType": "LimitBid",
      "Price": 78813.88,
      "Volume": 0.00010749
    },
    {
      "OrderType": "LimitBid",
      "Price": 78808.85,
      "Volume": 0.09816678
    },
    {
      "OrderType": "LimitBid",
      "Price": 78806.5,
      "Volume": 0.00262308
    },
    {
      "OrderType": "LimitBid",
      "Price": 78668,
      "Volume": 0.16843986
    },
    {
      "OrderType": "LimitBid",
      "Price": 78667.4,
      "Volume": 0.09830415
    },
    {
      "OrderType": "LimitBid",
      "Price": 78656.66,
      "Volume": 0.03066099
    },
    {
      "OrderType": "LimitBid",
      "Price": 78648.47,
      "Volume": 0.00010772
    },
    {
      "OrderType": "LimitBid",
      "Price": 78632.99,
      "Volume": 0.00175258
    },
    {
      "OrderType": "LimitBid",
      "Price": 78629.03,
      "Volume": 0.00438168
    },
    {
      "OrderType": "LimitBid",
      "Price": 78618.14,
      "Volume": 0.01314686
    },
    {
      "OrderType": "LimitBid",
      "Price": 78599.44,
      "Volume": 0.00043833
    },
    {
      "OrderType": "LimitBid",
      "Price": 78598.75,
      "Volume": 0.07005658
    },
    {
      "OrderType": "LimitBid",
      "Price": 78585.24,
      "Volume": 0.02952207
    },
    {
      "OrderType": "LimitBid",
      "Price": 78544.63,
      "Volume": 0.00877277
    },
    {
      "OrderType": "LimitBid",
      "Price": 78529.5,
      "Volume": 0.00263234
    },
    {
      "OrderType": "LimitBid",
      "Price": 78497.2,
      "Volume": 0.00270922
    },
    {
      "OrderType": "LimitBid",
      "Price": 78485.87,
      "Volume": 0.00702347
    },
    {
      "OrderType": "LimitBid",
      "Price": 78474.55,
      "Volume": 0.00010795
    },
    {
      "OrderType": "LimitBid",
      "Price": 78418.7,
      "Volume": 0.09861593
    },
    {
      "OrderType": "LimitBid",
      "Price": 78391,
      "Volume": 0.00263699
    },
    {
      "OrderType": "LimitBid",
      "Price": 78379.92,
      "Volume": 0.01507069
    },
    {
      "OrderType": "LimitBid",
      "Price": 78348.77,
      "Volume": 0.00010814
    },
    {
      "OrderType": "LimitBid",
      "Price": 78255.96,
      "Volume": 0.00044025
    },
    {
      "OrderType": "LimitBid",
      "Price": 78252.5,
      "Volume": 0.11352221
    },
    {
      "OrderType": "LimitBid",
      "Price": 78186.01,
      "Volume": 0.0044065
    },
    {
      "OrderType": "LimitBid",
      "Price": 78170.77,
      "Volume": 0.0989287
    },
    {
      "OrderType": "LimitBid",
      "Price": 78133.73,
      "Volume": 0.00010842
    },
    {
      "OrderType": "LimitBid",
      "Price": 78114,
      "Volume": 0.00352845
    },
    {
      "OrderType": "LimitBid",
      "Price": 78050.48,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitBid",
      "Price": 78047.92,
      "Volume": 0.00010855
    },
    {
      "OrderType": "LimitBid",
      "Price": 78044.75,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitBid",
      "Price": 77998.85,
      "Volume": 0.03600125
    },
    {
      "OrderType": "LimitBid",
      "Price": 77975.5,
      "Volume": 0.00353472
    },
    {
      "OrderType": "LimitBid",
      "Price": 77926.73,
      "Volume": 0.09923851
    },
    {
      "OrderType": "LimitBid",
      "Price": 77906.25,
      "Volume": 0.26049859
    },
    {
      "OrderType": "LimitBid",
      "Price": 77837,
      "Volume": 0.00354101
    },
    {
      "OrderType": "LimitBid",
      "Price": 77802.37,
      "Volume": 0.04428237
    },
    {
      "OrderType": "LimitBid",
      "Price": 77791.42,
      "Volume": 0.0001089
    },
    {
      "OrderType": "LimitBid",
      "Price": 77745.91,
      "Volume": 0.00010897
    },
    {
      "OrderType": "LimitBid",
      "Price": 77720,
      "Volume": 0.01268655
    },
    {
      "OrderType": "LimitBid",
      "Price": 77698.5,
      "Volume": 0.04878454
    },
    {
      "OrderType": "LimitBid",
      "Price": 77673.36,
      "Volume": 0.09956222
    },
    {
      "OrderType": "LimitBid",
      "Price": 77634.79,
      "Volume": 0.39256573
    },
    {
      "OrderType": "LimitBid",
      "Price": 77560.69,
      "Volume": 0.0004442
    },
    {
      "OrderType": "LimitBid",
      "Price": 77560,
      "Volume": 1.03185714
    },
    {
      "OrderType": "LimitBid",
      "Price": 77555.15,
      "Volume": 0.00039981
    },
    {
      "OrderType": "LimitBid",
      "Price": 77526.15,
      "Volume": 0.000399
    },
    {
      "OrderType": "LimitBid",
      "Price": 77447.6,
      "Volume": 0.00010938
    },
    {
      "OrderType": "LimitBid",
      "Price": 77442.72,
      "Volume": 0.0001094
    },
    {
      "OrderType": "LimitBid",
      "Price": 77426.21,
      "Volume": 0.09988003
    },
    {
      "OrderType": "LimitBid",
      "Price": 77421.5,
      "Volume": 0.07120034
    },
    {
      "OrderType": "LimitBid",
      "Price": 77375.01,
      "Volume": 0.00178107
    },
    {
      "OrderType": "LimitBid",
      "Price": 77283,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitBid",
      "Price": 77178.29,
      "Volume": 0.10020088
    },
    {
      "OrderType": "LimitBid",
      "Price": 77138.34,
      "Volume": 0.00010983
    },
    {
      "OrderType": "LimitBid",
      "Price": 77113.39,
      "Volume": 0.00088913
    },
    {
      "OrderType": "LimitBid",
      "Price": 77102.25,
      "Volume": 0.00010987
    },
    {
      "OrderType": "LimitBid",
      "Price": 76942.8,
      "Volume": 0.20678676
    },
    {
      "OrderType": "LimitBid",
      "Price": 76929.58,
      "Volume": 0.10052482
    },
    {
      "OrderType": "LimitBid",
      "Price": 76867.5,
      "Volume": 0.11
    },
    {
      "OrderType": "LimitBid",
      "Price": 76681.66,
      "Volume": 0.10084984
    },
    {
      "OrderType": "LimitBid",
      "Price": 76638.76,
      "Volume": 0.0002
    },
    {
      "OrderType": "LimitBid",
      "Price": 76566.35,
      "Volume": 0.01799888
    },
    {
      "OrderType": "LimitBid",
      "Price": 76521.25,
      "Volume": 0.0180095
    },
    {
      "OrderType": "LimitBid",
      "Price": 76433.73,
      "Volume": 0.10117696
    },
    {
      "OrderType": "LimitBid",
      "Price": 76185.8,
      "Volume": 0.10150622
    },
    {
      "OrderType": "LimitBid",
      "Price": 76178.46,
      "Volume": 0.00090452
    },
    {
      "OrderType": "LimitBid",
      "Price": 76175.69,
      "Volume": 0.00045227
    },
    {
      "OrderType": "LimitBid",
      "Price": 76175,
      "Volume": 3.23953527
    },
    {
      "OrderType": "LimitBid",
      "Price": 76165.6,
      "Volume": 0.23454157
    },
    {
      "OrderType": "LimitBid",
      "Price": 75936.32,
      "Volume": 0.1018397
    },
    {
      "OrderType": "LimitBid",
      "Price": 75907.38,
      "Volume": 0.00181551
    },
    {
      "OrderType": "LimitBid",
      "Price": 75787.2,
      "Volume": 0.06104609
    },
    {
      "OrderType": "LimitBid",
      "Price": 75689.17,
      "Volume": 0.10217224
    },
    {
      "OrderType": "LimitBid",
      "Price": 75482.5,
      "Volume": 0.08162671
    },
    {
      "OrderType": "LimitBid",
      "Price": 75472.8,
      "Volume": 1.3
    },
    {
      "OrderType": "LimitBid",
      "Price": 75441.24,
      "Volume": 0.10250802
    },
    {
      "OrderType": "LimitBid",
      "Price": 75397.04,
      "Volume": 9.139e-05
    },
    {
      "OrderType": "LimitBid",
      "Price": 75389.17,
      "Volume": 0.00926727
    },
    {
      "OrderType": "LimitBid",
      "Price": 75388.4,
      "Volume": 0.0055
    },
    {
      "OrderType": "LimitBid",
      "Price": 75192.54,
      "Volume": 0.10284707
    },
    {
      "OrderType": "LimitBid",
      "Price": 75170.87,
      "Volume": 0.06416558
    },
    {
      "OrderType": "LimitBid",
      "Price": 75136.94,
      "Volume": 0.00917065
    },
    {
      "OrderType": "LimitBid",
      "Price": 75136.25,
      "Volume": 0.10087809
    },
    {
      "OrderType": "LimitBid",
      "Price": 75135.55,
      "Volume": 0.00917082
    },
    {
      "OrderType": "LimitBid",
      "Price": 75018.52,
      "Volume": 0.01837025
    },
    {
      "OrderType": "LimitBid",
      "Price": 75000,
      "Volume": 0.00663349
    },
    {
      "OrderType": "LimitBid",
      "Price": 74944.61,
      "Volume": 0.1031873
    },
    {
      "OrderType": "LimitBid",
      "Price": 74870.23,
      "Volume": 0.01032898
    },
    {
      "OrderType": "LimitBid",
      "Price": 74829.38,
      "Volume": 0.0322292
    },
    {
      "OrderType": "LimitBid",
      "Price": 74790,
      "Volume": 1.23137751
    },
    {
      "OrderType": "LimitBid",
      "Price": 74449.94,
      "Volume": 0.03116187
    },
    {
      "OrderType": "LimitBid",
      "Price": 74278.45,
      "Volume": 0.09279286
    },
    {
      "OrderType": "LimitBid",
      "Price": 74236,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitBid",
      "Price": 74195.83,
      "Volume": 0.09379844
    },
    {
      "OrderType": "LimitBid",
      "Price": 74136.28,
      "Volume": 0.00037177
    },
    {
      "OrderType": "LimitBid",
      "Price": 74098.19,
      "Volume": 0.00046496
    },
    {
      "OrderType": "LimitBid",
      "Price": 74097.5,
      "Volume": 0.20411958
    },
    {
      "OrderType": "LimitBid",
      "Price": 73895.28,
      "Volume": 9.418e-05
    },
    {
      "OrderType": "LimitBid",
      "Price": 73834,
      "Volume": 0.01571091
    },
    {
      "OrderType": "LimitBid",
      "Price": 73817.73,
      "Volume": 0.00933454
    },
    {
      "OrderType": "LimitBid",
      "Price": 73792.8,
      "Volume": 0.01600751
    },
    {
      "OrderType": "LimitBid",
      "Price": 73780,
      "Volume": 0.0008
    },
    {
      "OrderType": "LimitBid",
      "Price": 73773.41,
      "Volume": 0.18172495
    },
    {
      "OrderType": "LimitBid",
      "Price": 73751.25,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitBid",
      "Price": 73550,
      "Volume": 1.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 73405,
      "Volume": 0.02971698
    },
    {
      "OrderType": "LimitBid",
      "Price": 73331.19,
      "Volume": 0.0527498
    },
    {
      "OrderType": "LimitBid",
      "Price": 73205.84,
      "Volume": 0.0374558
    },
    {
      "OrderType": "LimitBid",
      "Price": 73134.52,
      "Volume": 0.0073957
    },
    {
      "OrderType": "LimitBid",
      "Price": 73058.75,
      "Volume": 0.78582757
    },
    {
      "OrderType": "LimitBid",
      "Price": 73056.8,
      "Volume": 0.01058537
    },
    {
      "OrderType": "LimitBid",
      "Price": 73000,
      "Volume": 0.0035
    },
    {
      "OrderType": "LimitBid",
      "Price": 72989.5,
      "Volume": 0.00236011
    },
    {
      "OrderType": "LimitBid",
      "Price": 72851,
      "Volume": 0.0023646
    },
    {
      "OrderType": "LimitBid",
      "Price": 72828.14,
      "Volume": 0.00189227
    },
    {
      "OrderType": "LimitBid",
      "Price": 72810.13,
      "Volume": 0.00033123
    },
    {
      "OrderType": "LimitBid",
      "Price": 72796.61,
      "Volume": 0.01419821
    },
    {
      "OrderType": "LimitBid",
      "Price": 72715.96,
      "Volume": 0.00094759
    },
    {
      "OrderType": "LimitBid",
      "Price": 72712.5,
      "Volume": 0.31461261
    },
    {
      "OrderType": "LimitBid",
      "Price": 72574,
      "Volume": 0.00237362
    },
    {
      "OrderType": "LimitBid",
      "Price": 72495.16,
      "Volume": 0.00094097
    },
    {
      "OrderType": "LimitBid",
      "Price": 72475,
      "Volume": 0.001
    },
    {
      "OrderType": "LimitBid",
      "Price": 72435.5,
      "Volume": 0.00237816
    },
    {
      "OrderType": "LimitBid",
      "Price": 72433.42,
      "Volume": 0.27762874
    },
    {
      "OrderType": "LimitBid",
      "Price": 72380,
      "Volume": 0.0008
    },
    {
      "OrderType": "LimitBid",
      "Price": 72297,
      "Volume": 0.00238272
    },
    {
      "OrderType": "LimitBid",
      "Price": 72279.6,
      "Volume": 0.43042853
    },
    {
      "OrderType": "LimitBid",
      "Price": 72158.5,
      "Volume": 0.00238729
    },
    {
      "OrderType": "LimitBid",
      "Price": 72020,
      "Volume": 1.57296314
    },
    {
      "OrderType": "LimitBid",
      "Price": 72000,
      "Volume": 0.00019454
    },
    {
      "OrderType": "LimitBid",
      "Price": 71982.6,
      "Volume": 0.0003829
    },
    {
      "OrderType": "LimitBid",
      "Price": 71960.52,
      "Volume": 0.0191509
    },
    {
      "OrderType": "LimitBid",
      "Price": 71942.44,
      "Volume": 0.00239446
    },
    {
      "OrderType": "LimitBid",
      "Price": 71896,
      "Volume": 0.02509959
    },
    {
      "OrderType": "LimitBid",
      "Price": 71891,
      "Volume": 0.01
    },
    {
      "OrderType": "LimitBid",
      "Price": 71881.5,
      "Volume": 0.00287579
    },
    {
      "OrderType": "LimitBid",
      "Price": 71798.4,
      "Volume": 0.01645217
    },
    {
      "OrderType": "LimitBid",
      "Price": 71753.76,
      "Volume": 1.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 71743,
      "Volume": 0.00336157
    },
    {
      "OrderType": "LimitBid",
      "Price": 71711.83,
      "Volume": 0.00024021
    },
    {
      "OrderType": "LimitBid",
      "Price": 71645.21,
      "Volume": 0.01442639
    },
    {
      "OrderType": "LimitBid",
      "Price": 71604.5,
      "Volume": 0.00336807
    },
    {
      "OrderType": "LimitBid",
      "Price": 71600,
      "Volume": 0.0008
    },
    {
      "OrderType": "LimitBid",
      "Price": 71466,
      "Volume": 0.00337459
    },
    {
      "OrderType": "LimitBid",
      "Price": 71327.5,
      "Volume": 0.00495097
    },
    {
      "OrderType": "LimitBid",
      "Price": 71208.32,
      "Volume": 0.00019353
    },
    {
      "OrderType": "LimitBid",
      "Price": 71189,
      "Volume": 0.00338773
    },
    {
      "OrderType": "LimitBid",
      "Price": 71120.11,
      "Volume": 0.02978165
    },
    {
      "OrderType": "LimitBid",
      "Price": 71113.8,
      "Volume": 0.00250115
    },
    {
      "OrderType": "LimitBid",
      "Price": 71050.5,
      "Volume": 0.00387923
    },
    {
      "OrderType": "LimitBid",
      "Price": 71042.28,
      "Volume": 0.00544276
    },
    {
      "OrderType": "LimitBid",
      "Price": 70989.56,
      "Volume": 0.01358899
    },
    {
      "OrderType": "LimitBid",
      "Price": 70981.25,
      "Volume": 0.1164907
    },
    {
      "OrderType": "LimitBid",
      "Price": 70919.5,
      "Volume": 0.00545219
    },
    {
      "OrderType": "LimitBid",
      "Price": 70912,
      "Volume": 0.00388681
    },
    {
      "OrderType": "LimitBid",
      "Price": 70878.06,
      "Volume": 0.37829484
    },
    {
      "OrderType": "LimitBid",
      "Price": 70773.5,
      "Volume": 0.00389442
    },
    {
      "OrderType": "LimitBid",
      "Price": 70732.63,
      "Volume": 0.00048708
    },
    {
      "OrderType": "LimitBid",
      "Price": 70635,
      "Volume": 0.11998827
    },
    {
      "OrderType": "LimitBid",
      "Price": 70557.44,
      "Volume": 0.00122113
    },
    {
      "OrderType": "LimitBid",
      "Price": 70437.9,
      "Volume": 0.00043915
    },
    {
      "OrderType": "LimitBid",
      "Price": 70404.39,
      "Volume": 0.00094602
    },
    {
      "OrderType": "LimitBid",
      "Price": 70391.01,
      "Volume": 0.16485936
    },
    {
      "OrderType": "LimitBid",
      "Price": 70375.46,
      "Volume": 0.05495432
    },
    {
      "OrderType": "LimitBid",
      "Price": 70358,
      "Volume": 0.00293806
    },
    {
      "OrderType": "LimitBid",
      "Price": 70313.83,
      "Volume": 0.03299492
    },
    {
      "OrderType": "LimitBid",
      "Price": 70288.75,
      "Volume": 0.0318604
    },
    {
      "OrderType": "LimitBid",
      "Price": 70258.88,
      "Volume": 0.00990173
    },
    {
      "OrderType": "LimitBid",
      "Price": 70219.5,
      "Volume": 0.00244775
    },
    {
      "OrderType": "LimitBid",
      "Price": 70156.14,
      "Volume": 0.00269036
    },
    {
      "OrderType": "LimitBid",
      "Price": 70093.46,
      "Volume": 0.47816166
    },
    {
      "OrderType": "LimitBid",
      "Price": 70081,
      "Volume": 0.00294967
    },
    {
      "OrderType": "LimitBid",
      "Price": 69990.76,
      "Volume": 0.0002
    },
    {
      "OrderType": "LimitBid",
      "Price": 69950.81,
      "Volume": 0.29659496
    },
    {
      "OrderType": "LimitBid",
      "Price": 69948,
      "Volume": 0.03110529
    },
    {
      "OrderType": "LimitBid",
      "Price": 69942.5,
      "Volume": 0.05640361
    },
    {
      "OrderType": "LimitBid",
      "Price": 69804,
      "Volume": 0.00296138
    },
    {
      "OrderType": "LimitBid",
      "Price": 69734.75,
      "Volume": 0.24702702
    },
    {
      "OrderType": "LimitBid",
      "Price": 69722.97,
      "Volume": 0.57684294
    },
    {
      "OrderType": "LimitBid",
      "Price": 69596.25,
      "Volume": 0.00990074
    },
    {
      "OrderType": "LimitBid",
      "Price": 69589.32,
      "Volume": 0.00019803
    },
    {
      "OrderType": "LimitBid",
      "Price": 69527,
      "Volume": 0.00297318
    },
    {
      "OrderType": "LimitBid",
      "Price": 69430.74,
      "Volume": 0.001
    },
    {
      "OrderType": "LimitBid",
      "Price": 69388.65,
      "Volume": 0.00993036
    },
    {
      "OrderType": "LimitBid",
      "Price": 69327.91,
      "Volume": 0.09939066
    },
    {
      "OrderType": "LimitBid",
      "Price": 69319.25,
      "Volume": 0.01988061
    },
    {
      "OrderType": "LimitBid",
      "Price": 69253.46,
      "Volume": 0.00099497
    },
    {
      "OrderType": "LimitBid",
      "Price": 69250,
      "Volume": 3.70318035
    },
    {
      "OrderType": "LimitBid",
      "Price": 69215.37,
      "Volume": 0.00143494
    },
    {
      "OrderType": "LimitBid",
      "Price": 69180.75,
      "Volume": 0.00198218
    },
    {
      "OrderType": "LimitBid",
      "Price": 69172.44,
      "Volume": 0.00249035
    },
    {
      "OrderType": "LimitBid",
      "Price": 69084.43,
      "Volume": 0.01119403
    },
    {
      "OrderType": "LimitBid",
      "Price": 68973,
      "Volume": 0.00299706
    },
    {
      "OrderType": "LimitBid",
      "Price": 68888,
      "Volume": 0.00722204
    },
    {
      "OrderType": "LimitBid",
      "Price": 68876.51,
      "Volume": 0.5
    },
    {
      "OrderType": "LimitBid",
      "Price": 68790.18,
      "Volume": 0.00162371
    },
    {
      "OrderType": "LimitBid",
      "Price": 68765.25,
      "Volume": 0.00300611
    },
    {
      "OrderType": "LimitBid",
      "Price": 68730.62,
      "Volume": 0.00050127
    },
    {
      "OrderType": "LimitBid",
      "Price": 68702.92,
      "Volume": 0.07293208
    },
    {
      "OrderType": "LimitBid",
      "Price": 68655.13,
      "Volume": 0.00050182
    },
    {
      "OrderType": "LimitBid",
      "Price": 68611.14,
      "Volume": 0.00050214
    },
    {
      "OrderType": "LimitBid",
      "Price": 68558.19,
      "Volume": 0.00100506
    },
    {
      "OrderType": "LimitBid",
      "Price": 68557.5,
      "Volume": 0.05326899
    },
    {
      "OrderType": "LimitBid",
      "Price": 68526.19,
      "Volume": 0.00305622
    },
    {
      "OrderType": "LimitBid",
      "Price": 68456.39,
      "Volume": 0.00101
    },
    {
      "OrderType": "LimitBid",
      "Price": 68419,
      "Volume": 0.00302133
    },
    {
      "OrderType": "LimitBid",
      "Price": 68280.5,
      "Volume": 0.00302745
    },
    {
      "OrderType": "LimitBid",
      "Price": 68279.28,
      "Volume": 0.0566527
    },
    {
      "OrderType": "LimitBid",
      "Price": 68211.25,
      "Volume": 0.03030532
    },
    {
      "OrderType": "LimitBid",
      "Price": 68142,
      "Volume": 0.00303361
    },
    {
      "OrderType": "LimitBid",
      "Price": 68003.5,
      "Volume": 0.00303979
    },
    {
      "OrderType": "LimitBid",
      "Price": 67869.84,
      "Volume": 0.00101525
    },
    {
      "OrderType": "LimitBid",
      "Price": 67865,
      "Volume": 0.26918344
    },
    {
      "OrderType": "LimitBid",
      "Price": 67821.37,
      "Volume": 0.00507992
    },
    {
      "OrderType": "LimitBid",
      "Price": 67787.44,
      "Volume": 1.1
    },
    {
      "OrderType": "LimitBid",
      "Price": 67726.5,
      "Volume": 0.00406963
    },
    {
      "OrderType": "LimitBid",
      "Price": 67657.25,
      "Volume": 0.00407379
    },
    {
      "OrderType": "LimitBid",
      "Price": 67482.74,
      "Volume": 0.00104
    },
    {
      "OrderType": "LimitBid",
      "Price": 67403.1,
      "Volume": 0.00916198
    },
    {
      "OrderType": "LimitBid",
      "Price": 67329.04,
      "Volume": 0.01023413
    },
    {
      "OrderType": "LimitBid",
      "Price": 67227.8,
      "Volume": 0.06901906
    },
    {
      "OrderType": "LimitBid",
      "Price": 67217.5,
      "Volume": 0.00082008
    },
    {
      "OrderType": "LimitBid",
      "Price": 67176.65,
      "Volume": 0.00102573
    },
    {
      "OrderType": "LimitBid",
      "Price": 67172.5,
      "Volume": 0.41256827
    },
    {
      "OrderType": "LimitBid",
      "Price": 67074.69,
      "Volume": 0.02882358
    },
    {
      "OrderType": "LimitBid",
      "Price": 67019.59,
      "Volume": 0.00051406
    },
    {
      "OrderType": "LimitBid",
      "Price": 66900,
      "Volume": 0.002
    },
    {
      "OrderType": "LimitBid",
      "Price": 66757,
      "Volume": 0.12
    },
    {
      "OrderType": "LimitBid",
      "Price": 66549.94,
      "Volume": 0.1155
    },
    {
      "OrderType": "LimitBid",
      "Price": 66509.08,
      "Volume": 0.00104
    },
    {
      "OrderType": "LimitBid",
      "Price": 66480,
      "Volume": 0.05182421
    },
    {
      "OrderType": "LimitBid",
      "Price": 66272.25,
      "Volume": 0.00051986
    },
    {
      "OrderType": "LimitBid",
      "Price": 66265.32,
      "Volume": 0.07278894
    },
    {
      "OrderType": "LimitBid",
      "Price": 66259.5,
      "Volume": 0.00583564
    },
    {
      "OrderType": "LimitBid",
      "Price": 66164.25,
      "Volume": 5.207e-05
    },
    {
      "OrderType": "LimitBid",
      "Price": 66126.82,
      "Volume": 0.00156302
    },
    {
      "OrderType": "LimitBid",
      "Price": 66064.5,
      "Volume": 1.03257299
    },
    {
      "OrderType": "LimitBid",
      "Price": 66062,
      "Volume": 0.25418275
    },
    {
      "OrderType": "LimitBid",
      "Price": 65924.22,
      "Volume": 0.2
    },
    {
      "OrderType": "LimitBid",
      "Price": 65788.19,
      "Volume": 0.05139366
    },
    {
      "OrderType": "LimitBid",
      "Price": 65787.5,
      "Volume": 1.39586972
    },
    {
      "OrderType": "LimitBid",
      "Price": 65095,
      "Volume": 0.10908642
    },
    {
      "OrderType": "LimitBid",
      "Price": 64748.75,
      "Volume": 0.075
    },
    {
      "OrderType": "LimitBid",
      "Price": 64507.6,
      "Volume": 0.01798237
    },
    {
      "OrderType": "LimitBid",
      "Price": 64471.75,
      "Volume": 0.0497152
    },
    {
      "OrderType": "LimitBid",
      "Price": 64402.5,
      "Volume": 0.03209757
    },
    {
      "OrderType": "LimitBid",
      "Price": 64141.58,
      "Volume": 0.00537135
    },
    {
      "OrderType": "LimitBid",
      "Price": 63796.93,
      "Volume": 0.03240224
    },
    {
      "OrderType": "LimitBid",
      "Price": 63710,
      "Volume": 0.14429978
    },
    {
      "OrderType": "LimitBid",
      "Price": 63370.67,
      "Volume": 0.0054367
    },
    {
      "OrderType": "LimitBid",
      "Price": 63156.69,
      "Volume": 0.1225
    },
    {
      "OrderType": "LimitBid",
      "Price": 63029.26,
      "Volume": 0.26669213
    },
    {
      "OrderType": "LimitBid",
      "Price": 63017.5,
      "Volume": 0.80012572
    },
    {
      "OrderType": "LimitBid",
      "Price": 63012.82,
      "Volume": 0.00109351
    },
    {
      "OrderType": "LimitBid",
      "Price": 62993.25,
      "Volume": 0.00164078
    },
    {
      "OrderType": "LimitBid",
      "Price": 62948.79,
      "Volume": 0.00262777
    },
    {
      "OrderType": "LimitBid",
      "Price": 62876.08,
      "Volume": 0.01705229
    },
    {
      "OrderType": "LimitBid",
      "Price": 62736.62,
      "Volume": 0.3
    },
    {
      "OrderType": "LimitBid",
      "Price": 62718.75,
      "Volume": 0.00051387
    },
    {
      "OrderType": "LimitBid",
      "Price": 62715.36,
      "Volume": 0.0010987
    },
    {
      "OrderType": "LimitBid",
      "Price": 62394.56,
      "Volume": 0.06626105
    },
    {
      "OrderType": "LimitBid",
      "Price": 62359.62,
      "Volume": 0.5
    },
    {
      "OrderType": "LimitBid",
      "Price": 62325,
      "Volume": 0.57756171
    },
    {
      "OrderType": "LimitBid",
      "Price": 62318.07,
      "Volume": 0.1105706
    },
    {
      "OrderType": "LimitBid",
      "Price": 62182.21,
      "Volume": 0.01243656
    },
    {
      "OrderType": "LimitBid",
      "Price": 62176,
      "Volume": 0.08084576
    },
    {
      "OrderType": "LimitBid",
      "Price": 62175.22,
      "Volume": 0.03731389
    },
    {
      "OrderType": "LimitBid",
      "Price": 62141.48,
      "Volume": 0.22176962
    },
    {
      "OrderType": "LimitBid",
      "Price": 62027.01,
      "Volume": 0.0004
    },
    {
      "OrderType": "LimitBid",
      "Price": 62017.05,
      "Volume": 0.0016666
    },
    {
      "OrderType": "LimitBid",
      "Price": 61810.71,
      "Volume": 0.00125113
    },
    {
      "OrderType": "LimitBid",
      "Price": 61611.75,
      "Volume": 0.03765515
    },
    {
      "OrderType": "LimitBid",
      "Price": 61494,
      "Volume": 0.00280164
    },
    {
      "OrderType": "LimitBid",
      "Price": 61438.35,
      "Volume": 0.02223432
    },
    {
      "OrderType": "LimitBid",
      "Price": 61398.8,
      "Volume": 0.08845001
    },
    {
      "OrderType": "LimitBid",
      "Price": 61355.5,
      "Volume": 0.00673831
    },
    {
      "OrderType": "LimitBid",
      "Price": 61341.03,
      "Volume": 0.15159822
    },
    {
      "OrderType": "LimitBid",
      "Price": 61286.25,
      "Volume": 0.78702532
    },
    {
      "OrderType": "LimitBid",
      "Price": 61245.79,
      "Volume": 0.00225012
    },
    {
      "OrderType": "LimitBid",
      "Price": 61217,
      "Volume": 0.00675356
    },
    {
      "OrderType": "LimitBid",
      "Price": 61157.1,
      "Volume": 0.002529
    },
    {
      "OrderType": "LimitBid",
      "Price": 61113.12,
      "Volume": 0.05637534
    },
    {
      "OrderType": "LimitBid",
      "Price": 61106.6,
      "Volume": 0.00011276
    },
    {
      "OrderType": "LimitBid",
      "Price": 61078.5,
      "Volume": 0.00676887
    },
    {
      "OrderType": "LimitBid",
      "Price": 61025.59,
      "Volume": 0.01129124
    },
    {
      "OrderType": "LimitBid",
      "Price": 60940,
      "Volume": 0.49800619
    },
    {
      "OrderType": "LimitBid",
      "Price": 60912.98,
      "Volume": 0.00282802
    },
    {
      "OrderType": "LimitBid",
      "Price": 60801.5,
      "Volume": 0.00736635
    },
    {
      "OrderType": "LimitBid",
      "Price": 60758.83,
      "Volume": 5.642e-05
    },
    {
      "OrderType": "LimitBid",
      "Price": 60737.27,
      "Volume": 0.00178699
    },
    {
      "OrderType": "LimitBid",
      "Price": 60732.25,
      "Volume": 0.01134577
    },
    {
      "OrderType": "LimitBid",
      "Price": 60700.39,
      "Volume": 0.00567586
    },
    {
      "OrderType": "LimitBid",
      "Price": 60663,
      "Volume": 0.00738317
    },
    {
      "OrderType": "LimitBid",
      "Price": 60621.6,
      "Volume": 0.02551344
    },
    {
      "OrderType": "LimitBid",
      "Price": 60593.75,
      "Volume": 0.30929281
    },
    {
      "OrderType": "LimitBid",
      "Price": 60574.48,
      "Volume": 0.00113753
    },
    {
      "OrderType": "LimitBid",
      "Price": 60524.5,
      "Volume": 0.0079693
    },
    {
      "OrderType": "LimitBid",
      "Price": 60421.46,
      "Volume": 0.00148367
    },
    {
      "OrderType": "LimitBid",
      "Price": 60420.62,
      "Volume": 0.00114042
    },
    {
      "OrderType": "LimitBid",
      "Price": 60386,
      "Volume": 0.00912866
    },
    {
      "OrderType": "LimitBid",
      "Price": 60247.5,
      "Volume": 0.48451213
    },
    {
      "OrderType": "LimitBid",
      "Price": 60233,
      "Volume": 0.0025
    },
    {
      "OrderType": "LimitBid",
      "Price": 60109,
      "Volume": 0.00859756
    },
    {
      "OrderType": "LimitBid",
      "Price": 60081.3,
      "Volume": 0.0107215
    },
    {
      "OrderType": "LimitBid",
      "Price": 59970.5,
      "Volume": 0.01148989
    },
    {
      "OrderType": "LimitBid",
      "Price": 59948.34,
      "Volume": 0.0011931
    },
    {
      "OrderType": "LimitBid",
      "Price": 59832,
      "Volume": 0.01151649
    },
    {
      "OrderType": "LimitBid",
      "Price": 59693.5,
      "Volume": 0.01154321
    },
    {
      "OrderType": "LimitBid",
      "Price": 59652.5,
      "Volume": 9.299e-05
    },
    {
      "OrderType": "LimitBid",
      "Price": 59555,
      "Volume": 0.5816504
    },
    {
      "OrderType": "LimitBid",
      "Price": 59501.26,
      "Volume": 0.01456121
    },
    {
      "OrderType": "LimitBid",
      "Price": 59416.5,
      "Volume": 0.01159702
    },
    {
      "OrderType": "LimitBid",
      "Price": 59409.57,
      "Volume": 0.00231967
    },
    {
      "OrderType": "LimitBid",
      "Price": 59278,
      "Volume": 0.01743618
    },
    {
      "OrderType": "LimitBid",
      "Price": 59243.37,
      "Volume": 0.04332983
    },
    {
      "OrderType": "LimitBid",
      "Price": 59217.06,
      "Volume": 0.05818042
    },
    {
      "OrderType": "LimitBid",
      "Price": 59208.75,
      "Volume": 0.89680252
    },
    {
      "OrderType": "LimitBid",
      "Price": 59124.95,
      "Volume": 0.00329755
    },
    {
      "OrderType": "LimitBid",
      "Price": 59104.87,
      "Volume": 0.01748725
    },
    {
      "OrderType": "LimitBid",
      "Price": 59067.2,
      "Volume": 0.02618485
    },
    {
      "OrderType": "LimitBid",
      "Price": 58935.21,
      "Volume": 0.09353385
    },
    {
      "OrderType": "LimitBid",
      "Price": 58872.19,
      "Volume": 0.00233609
    },
    {
      "OrderType": "LimitBid",
      "Price": 58863.88,
      "Volume": 0.11705899
    },
    {
      "OrderType": "LimitBid",
      "Price": 58862.5,
      "Volume": 0.8212054
    },
    {
      "OrderType": "LimitBid",
      "Price": 58793.25,
      "Volume": 0.01757994
    },
    {
      "OrderType": "LimitBid",
      "Price": 58724,
      "Volume": 0.04693513
    },
    {
      "OrderType": "LimitBid",
      "Price": 58516.25,
      "Volume": 0.00011775
    },
    {
      "OrderType": "LimitBid",
      "Price": 58483.76,
      "Volume": 0.58945106
    },
    {
      "OrderType": "LimitBid",
      "Price": 58481.62,
      "Volume": 0.02356482
    },
    {
      "OrderType": "LimitBid",
      "Price": 58467.9,
      "Volume": 0.00058925
    },
    {
      "OrderType": "LimitBid",
      "Price": 58350.2,
      "Volume": 0.00236179
    },
    {
      "OrderType": "LimitBid",
      "Price": 58308.5,
      "Volume": 0.02363479
    },
    {
      "OrderType": "LimitBid",
      "Price": 58290,
      "Volume": 0.0403997
    },
    {
      "OrderType": "LimitBid",
      "Price": 58184.54,
      "Volume": 0.00035527
    },
    {
      "OrderType": "LimitBid",
      "Price": 58173.42,
      "Volume": 0.00664679
    },
    {
      "OrderType": "LimitBid",
      "Price": 58170,
      "Volume": 0.09754172
    },
    {
      "OrderType": "LimitBid",
      "Price": 58169.3,
      "Volume": 0.0004
    },
    {
      "OrderType": "LimitBid",
      "Price": 58100.75,
      "Volume": 0.00118596
    },
    {
      "OrderType": "LimitBid",
      "Price": 57989.84,
      "Volume": 0.11882334
    },
    {
      "OrderType": "LimitBid",
      "Price": 57950.47,
      "Volume": 0.0027
    },
    {
      "OrderType": "LimitBid",
      "Price": 57940.98,
      "Volume": 0.00400407
    },
    {
      "OrderType": "LimitBid",
      "Price": 57823.75,
      "Volume": 0.01203562
    },
    {
      "OrderType": "LimitBid",
      "Price": 57814.35,
      "Volume": 0.00401284
    },
    {
      "OrderType": "LimitBid",
      "Price": 57777.04,
      "Volume": 0.00100385
    },
    {
      "OrderType": "LimitBid",
      "Price": 57772.49,
      "Volume": 0.00357811
    },
    {
      "OrderType": "LimitBid",
      "Price": 57688.07,
      "Volume": 0.00048079
    },
    {
      "OrderType": "LimitBid",
      "Price": 57654.08,
      "Volume": 0.00035854
    },
    {
      "OrderType": "LimitBid",
      "Price": 57590.52,
      "Volume": 0.00134281
    },
    {
      "OrderType": "LimitBid",
      "Price": 57581.37,
      "Volume": 0.03
    },
    {
      "OrderType": "LimitBid",
      "Price": 57556.15,
      "Volume": 0.00239437
    },
    {
      "OrderType": "LimitBid",
      "Price": 57518.84,
      "Volume": 0.00119203
    },
    {
      "OrderType": "LimitBid",
      "Price": 57512.8,
      "Volume": 0.01815246
    },
    {
      "OrderType": "LimitBid",
      "Price": 57478.19,
      "Volume": 0.08
    },
    {
      "OrderType": "LimitBid",
      "Price": 57477.5,
      "Volume": 0.01592609
    },
    {
      "OrderType": "LimitBid",
      "Price": 57425.75,
      "Volume": 0.00538666
    },
    {
      "OrderType": "LimitBid",
      "Price": 57399.94,
      "Volume": 0.00010659
    },
    {
      "OrderType": "LimitBid",
      "Price": 57372.58,
      "Volume": 0.00404374
    },
    {
      "OrderType": "LimitBid",
      "Price": 57301.4,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitBid",
      "Price": 57300,
      "Volume": 0.00348
    },
    {
      "OrderType": "LimitBid",
      "Price": 57223.6,
      "Volume": 0.02408288
    },
    {
      "OrderType": "LimitBid",
      "Price": 57200.5,
      "Volume": 0.0120463
    },
    {
      "OrderType": "LimitBid",
      "Price": 57165.87,
      "Volume": 0.0602
    },
    {
      "OrderType": "LimitBid",
      "Price": 57139.56,
      "Volume": 0.30147883
    },
    {
      "OrderType": "LimitBid",
      "Price": 57131.25,
      "Volume": 0.48259289
    },
    {
      "OrderType": "LimitBid",
      "Price": 57079.01,
      "Volume": 0.00120719
    },
    {
      "OrderType": "LimitBid",
      "Price": 57070.86,
      "Volume": 0.01509208
    },
    {
      "OrderType": "LimitBid",
      "Price": 57037.15,
      "Volume": 0.00542336
    },
    {
      "OrderType": "LimitBid",
      "Price": 56958.12,
      "Volume": 0.004
    },
    {
      "OrderType": "LimitBid",
      "Price": 56933.78,
      "Volume": 0.33956726
    },
    {
      "OrderType": "LimitBid",
      "Price": 56929.53,
      "Volume": 0.00013584
    },
    {
      "OrderType": "LimitBid",
      "Price": 56888.87,
      "Volume": 0.03
    },
    {
      "OrderType": "LimitBid",
      "Price": 56798.85,
      "Volume": 0.00680764
    },
    {
      "OrderType": "LimitBid",
      "Price": 56791.92,
      "Volume": 0.00121329
    },
    {
      "OrderType": "LimitBid",
      "Price": 56788.46,
      "Volume": 0.01
    },
    {
      "OrderType": "LimitBid",
      "Price": 56788.39,
      "Volume": 0.06808902
    },
    {
      "OrderType": "LimitBid",
      "Price": 56785,
      "Volume": 0.10641733
    },
    {
      "OrderType": "LimitBid",
      "Price": 56737.93,
      "Volume": 0.03
    },
    {
      "OrderType": "LimitBid",
      "Price": 56735.6,
      "Volume": 0.03066856
    },
    {
      "OrderType": "LimitBid",
      "Price": 56715.75,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitBid",
      "Price": 56651.55,
      "Volume": 0.07297819
    },
    {
      "OrderType": "LimitBid",
      "Price": 56584.17,
      "Volume": 0.12176298
    },
    {
      "OrderType": "LimitBid",
      "Price": 56563.42,
      "Volume": 0.01218198
    },
    {
      "OrderType": "LimitBid",
      "Price": 56540.07,
      "Volume": 0.00049056
    },
    {
      "OrderType": "LimitBid",
      "Price": 56493.11,
      "Volume": 0.00684449
    },
    {
      "OrderType": "LimitBid",
      "Price": 56448.81,
      "Volume": 0.01331723
    },
    {
      "OrderType": "LimitBid",
      "Price": 56439.44,
      "Volume": 0.00122087
    },
    {
      "OrderType": "LimitBid",
      "Price": 56438.75,
      "Volume": 0.10012208
    },
    {
      "OrderType": "LimitBid",
      "Price": 56347,
      "Volume": 0.00686224
    },
    {
      "OrderType": "LimitBid",
      "Price": 56299.55,
      "Volume": 0.01270095
    },
    {
      "OrderType": "LimitBid",
      "Price": 56231,
      "Volume": 0.03
    },
    {
      "OrderType": "LimitBid",
      "Price": 56095.96,
      "Volume": 0.01
    },
    {
      "OrderType": "LimitBid",
      "Price": 56093.19,
      "Volume": 0.00122841
    },
    {
      "OrderType": "LimitBid",
      "Price": 56092.5,
      "Volume": 0.21078049
    },
    {
      "OrderType": "LimitBid",
      "Price": 55959.17,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitBid",
      "Price": 55850.12,
      "Volume": 0.0055519
    },
    {
      "OrderType": "LimitBid",
      "Price": 55750,
      "Volume": 0.005
    },
    {
      "OrderType": "LimitBid",
      "Price": 55746.25,
      "Volume": 0.01384381
    },
    {
      "OrderType": "LimitBid",
      "Price": 55715.91,
      "Volume": 0.00693996
    },
    {
      "OrderType": "LimitBid",
      "Price": 55677,
      "Volume": 0.00346526
    },
    {
      "OrderType": "LimitBid",
      "Price": 55675.42,
      "Volume": 0.01389004
    },
    {
      "OrderType": "LimitBid",
      "Price": 55644.54,
      "Volume": 0.01945634
    },
    {
      "OrderType": "LimitBid",
      "Price": 55573.12,
      "Volume": 0.03
    },
    {
      "OrderType": "LimitBid",
      "Price": 55570.66,
      "Volume": 0.07620519
    },
    {
      "OrderType": "LimitBid",
      "Price": 55563.21,
      "Volume": 0.01240127
    },
    {
      "OrderType": "LimitBid",
      "Price": 55538.5,
      "Volume": 0.00248135
    },
    {
      "OrderType": "LimitBid",
      "Price": 55486.14,
      "Volume": 0.00062092
    },
    {
      "OrderType": "LimitBid",
      "Price": 55485.17,
      "Volume": 0.01751163
    },
    {
      "OrderType": "LimitBid",
      "Price": 55472.71,
      "Volume": 0.04993446
    },
    {
      "OrderType": "LimitBid",
      "Price": 55469.25,
      "Volume": 0.03850906
    },
    {
      "OrderType": "LimitBid",
      "Price": 55465.78,
      "Volume": 0.00310576
    },
    {
      "OrderType": "LimitBid",
      "Price": 55400,
      "Volume": 1.40599017
    },
    {
      "OrderType": "LimitBid",
      "Price": 55393.07,
      "Volume": 0.08
    },
    {
      "OrderType": "LimitBid",
      "Price": 55239.54,
      "Volume": 0.00699981
    },
    {
      "OrderType": "LimitBid",
      "Price": 55232.96,
      "Volume": 0.05021696
    },
    {
      "OrderType": "LimitBid",
      "Price": 55192.25,
      "Volume": 0.03745388
    },
    {
      "OrderType": "LimitBid",
      "Price": 55181.97,
      "Volume": 0.03
    },
    {
      "OrderType": "LimitBid",
      "Price": 55181.2,
      "Volume": 0.05607147
    },
    {
      "OrderType": "LimitBid",
      "Price": 55111.11,
      "Volume": 0.06210881
    },
    {
      "OrderType": "LimitBid",
      "Price": 55062.06,
      "Volume": 0.31285368
    },
    {
      "OrderType": "LimitBid",
      "Price": 55053.75,
      "Volume": 0.06445748
    },
    {
      "OrderType": "LimitBid",
      "Price": 54938.71,
      "Volume": 0.00703814
    },
    {
      "OrderType": "LimitBid",
      "Price": 54915.25,
      "Volume": 0.00125476
    },
    {
      "OrderType": "LimitBid",
      "Price": 54880.62,
      "Volume": 0.03
    },
    {
      "OrderType": "LimitBid",
      "Price": 54813.45,
      "Volume": 0.01187182
    },
    {
      "OrderType": "LimitBid",
      "Price": 54713.73,
      "Volume": 0.00125938
    },
    {
      "OrderType": "LimitBid",
      "Price": 54707.5,
      "Volume": 0.06423577
    },
    {
      "OrderType": "LimitBid",
      "Price": 54630.54,
      "Volume": 0.00553921
    },
    {
      "OrderType": "LimitBid",
      "Price": 54559.24,
      "Volume": 0.00378884
    },
    {
      "OrderType": "LimitBid",
      "Price": 54404,
      "Volume": 0.18190972
    },
    {
      "OrderType": "LimitBid",
      "Price": 54400,
      "Volume": 0.00367
    },
    {
      "OrderType": "LimitBid",
      "Price": 54361.25,
      "Volume": 0.06496192
    },
    {
      "OrderType": "LimitBid",
      "Price": 54269.16,
      "Volume": 0.00507879
    },
    {
      "OrderType": "LimitBid",
      "Price": 54222.75,
      "Volume": 0.03
    },
    {
      "OrderType": "LimitBid",
      "Price": 54222.43,
      "Volume": 0.07844231
    },
    {
      "OrderType": "LimitBid",
      "Price": 54161.51,
      "Volume": 0.00713914
    },
    {
      "OrderType": "LimitBid",
      "Price": 54153.5,
      "Volume": 0.00127241
    },
    {
      "OrderType": "LimitBid",
      "Price": 54116.93,
      "Volume": 0.0127327
    },
    {
      "OrderType": "LimitBid",
      "Price": 54015,
      "Volume": 0.05213508
    },
    {
      "OrderType": "LimitBid",
      "Price": 53963.75,
      "Volume": 0.01276884
    },
    {
      "OrderType": "LimitBid",
      "Price": 53860.57,
      "Volume": 0.0005
    },
    {
      "OrderType": "LimitBid",
      "Price": 53751.85,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitBid",
      "Price": 53668.75,
      "Volume": 0.00052242
    },
    {
      "OrderType": "LimitBid",
      "Price": 53646.07,
      "Volume": 0.00256889
    },
    {
      "OrderType": "LimitBid",
      "Price": 53626.8,
      "Volume": 0.0006
    },
    {
      "OrderType": "LimitBid",
      "Price": 53564.87,
      "Volume": 0.03
    },
    {
      "OrderType": "LimitBid",
      "Price": 53538.45,
      "Volume": 0.01444444
    },
    {
      "OrderType": "LimitBid",
      "Price": 53531.1,
      "Volume": 0.1287
    },
    {
      "OrderType": "LimitBid",
      "Price": 53426.37,
      "Volume": 0.00580377
    },
    {
      "OrderType": "LimitBid",
      "Price": 53393.64,
      "Volume": 0.00579344
    },
    {
      "OrderType": "LimitBid",
      "Price": 53391.75,
      "Volume": 0.01290564
    },
    {
      "OrderType": "LimitBid",
      "Price": 53322.5,
      "Volume": 0.09124218
    },
    {
      "OrderType": "LimitBid",
      "Price": 53287.87,
      "Volume": 0.41395027
    },
    {
      "OrderType": "LimitBid",
      "Price": 53189.54,
      "Volume": 0.64773518
    },
    {
      "OrderType": "LimitBid",
      "Price": 52990.77,
      "Volume": 0.5
    },
    {
      "OrderType": "LimitBid",
      "Price": 52984.56,
      "Volume": 0.26009642
    },
    {
      "OrderType": "LimitBid",
      "Price": 52920.85,
      "Volume": 0.00325511
    },
    {
      "OrderType": "LimitBid",
      "Price": 52888,
      "Volume": 0.0094069
    },
    {
      "OrderType": "LimitBid",
      "Price": 52872.37,
      "Volume": 0.03
    },
    {
      "OrderType": "LimitBid",
      "Price": 52849.6,
      "Volume": 0.06218903
    },
    {
      "OrderType": "LimitBid",
      "Price": 52764.1,
      "Volume": 0.0366411
    },
    {
      "OrderType": "LimitBid",
      "Price": 52702.71,
      "Volume": 0.11
    },
    {
      "OrderType": "LimitBid",
      "Price": 52630,
      "Volume": 0.46155279
    },
    {
      "OrderType": "LimitBid",
      "Price": 52586.37,
      "Volume": 0.069
    },
    {
      "OrderType": "LimitBid",
      "Price": 52491.5,
      "Volume": 0.02494125
    },
    {
      "OrderType": "LimitBid",
      "Price": 52462.2,
      "Volume": 0.32835769
    },
    {
      "OrderType": "LimitBid",
      "Price": 52461,
      "Volume": 0.03890178
    },
    {
      "OrderType": "LimitBid",
      "Price": 52321.18,
      "Volume": 0.00230469
    },
    {
      "OrderType": "LimitBid",
      "Price": 52283.75,
      "Volume": 0.46589568
    },
    {
      "OrderType": "LimitBid",
      "Price": 52214.5,
      "Volume": 0.03
    },
    {
      "OrderType": "LimitBid",
      "Price": 52183.26,
      "Volume": 0.13204514
    },
    {
      "OrderType": "LimitBid",
      "Price": 52166.75,
      "Volume": 0.0252013
    },
    {
      "OrderType": "LimitBid",
      "Price": 52145.94,
      "Volume": 0.01321396
    },
    {
      "OrderType": "LimitBid",
      "Price": 52076,
      "Volume": 0.03969514
    },
    {
      "OrderType": "LimitBid",
      "Price": 51985.97,
      "Volume": 0.1065672
    },
    {
      "OrderType": "LimitBid",
      "Price": 51938.88,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitBid",
      "Price": 51938.19,
      "Volume": 0.00132668
    },
    {
      "OrderType": "LimitBid",
      "Price": 51937.5,
      "Volume": 0.1563548
    },
    {
      "OrderType": "LimitBid",
      "Price": 51799,
      "Volume": 0.15
    },
    {
      "OrderType": "LimitBid",
      "Price": 51722.13,
      "Volume": 0.00026644
    },
    {
      "OrderType": "LimitBid",
      "Price": 51700,
      "Volume": 0.00386
    },
    {
      "OrderType": "LimitBid",
      "Price": 51683.8,
      "Volume": 0.04488834
    },
    {
      "OrderType": "LimitBid",
      "Price": 51660.5,
      "Volume": 0.085
    },
    {
      "OrderType": "LimitBid",
      "Price": 51563.33,
      "Volume": 0.15
    },
    {
      "OrderType": "LimitBid",
      "Price": 51524.47,
      "Volume": 0.15009048
    },
    {
      "OrderType": "LimitBid",
      "Price": 51467.29,
      "Volume": 0.01472702
    },
    {
      "OrderType": "LimitBid",
      "Price": 51411.78,
      "Volume": 0.0152
    },
    {
      "OrderType": "LimitBid",
      "Price": 51383.5,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitBid",
      "Price": 51321.86,
      "Volume": 0.01315762
    },
    {
      "OrderType": "LimitBid",
      "Price": 51300.4,
      "Volume": 0.16
    },
    {
      "OrderType": "LimitBid",
      "Price": 51245,
      "Volume": 0.0287909
    },
    {
      "OrderType": "LimitBid",
      "Price": 51141.12,
      "Volume": 0.08533389
    },
    {
      "OrderType": "LimitBid",
      "Price": 51111.11,
      "Volume": 0.4
    },
    {
      "OrderType": "LimitBid",
      "Price": 50984.32,
      "Volume": 0.00455041
    },
    {
      "OrderType": "LimitBid",
      "Price": 50933.8,
      "Volume": 0.30366212
    },
    {
      "OrderType": "LimitBid",
      "Price": 50906.6,
      "Volume": 0.0075956
    },
    {
      "OrderType": "LimitBid",
      "Price": 50691,
      "Volume": 0.05437294
    },
    {
      "OrderType": "LimitBid",
      "Price": 50605.13,
      "Volume": 0.08368267
    },
    {
      "OrderType": "LimitBid",
      "Price": 50556.86,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitBid",
      "Price": 50552.5,
      "Volume": 0.00136304
    },
    {
      "OrderType": "LimitBid",
      "Price": 50518.77,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitBid",
      "Price": 50518,
      "Volume": 0.13011862
    },
    {
      "OrderType": "LimitBid",
      "Price": 50323.7,
      "Volume": 0.38417948
    },
    {
      "OrderType": "LimitBid",
      "Price": 50233.95,
      "Volume": 0.16
    },
    {
      "OrderType": "LimitBid",
      "Price": 50213.86,
      "Volume": 0.13652226
    },
    {
      "OrderType": "LimitBid",
      "Price": 50168.26,
      "Volume": 0.00770739
    },
    {
      "OrderType": "LimitBid",
      "Price": 50113.13,
      "Volume": 0.7958
    },
    {
      "OrderType": "LimitBid",
      "Price": 50112.12,
      "Volume": 0.06830454
    },
    {
      "OrderType": "LimitBid",
      "Price": 50067.75,
      "Volume": 0.00550497
    },
    {
      "OrderType": "LimitBid",
      "Price": 49963.87,
      "Volume": 0.068
    },
    {
      "OrderType": "LimitBid",
      "Price": 49950.64,
      "Volume": 0.46446816
    },
    {
      "OrderType": "LimitBid",
      "Price": 49929.25,
      "Volume": 0.13800622
    },
    {
      "OrderType": "LimitBid",
      "Price": 49860,
      "Volume": 0.8249752
    },
    {
      "OrderType": "LimitBid",
      "Price": 49790.75,
      "Volume": 0.15
    },
    {
      "OrderType": "LimitBid",
      "Price": 49782.44,
      "Volume": 0.07612726
    },
    {
      "OrderType": "LimitBid",
      "Price": 49740.8,
      "Volume": 0.001
    },
    {
      "OrderType": "LimitBid",
      "Price": 49514.44,
      "Volume": 0.00139162
    },
    {
      "OrderType": "LimitBid",
      "Price": 49467.97,
      "Volume": 0.00255349
    },
    {
      "OrderType": "LimitBid",
      "Price": 49305.3,
      "Volume": 0.48913426
    },
    {
      "OrderType": "LimitBid",
      "Price": 49170.96,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitBid",
      "Price": 49167.5,
      "Volume": 0.77568089
    },
    {
      "OrderType": "LimitBid",
      "Price": 49123.87,
      "Volume": 0.09730447
    },
    {
      "OrderType": "LimitBid",
      "Price": 49100,
      "Volume": 0.0041
    },
    {
      "OrderType": "LimitBid",
      "Price": 49090.55,
      "Volume": 1.05757666
    },
    {
      "OrderType": "LimitBid",
      "Price": 49090.54,
      "Volume": 0.92037868
    },
    {
      "OrderType": "LimitBid",
      "Price": 49006.58,
      "Volume": 0.00281209
    },
    {
      "OrderType": "LimitBid",
      "Price": 48963.6,
      "Volume": 0.49500835
    },
    {
      "OrderType": "LimitBid",
      "Price": 48822.1,
      "Volume": 0.211
    },
    {
      "OrderType": "LimitBid",
      "Price": 48790.55,
      "Volume": 0.03530677
    },
    {
      "OrderType": "LimitBid",
      "Price": 48752.35,
      "Volume": 0.01413377
    },
    {
      "OrderType": "LimitBid",
      "Price": 48688.97,
      "Volume": 0.0301781
    },
    {
      "OrderType": "LimitBid",
      "Price": 48509.62,
      "Volume": 0.00142044
    },
    {
      "OrderType": "LimitBid",
      "Price": 48488.85,
      "Volume": 0.26134304
    },
    {
      "OrderType": "LimitBid",
      "Price": 48483.31,
      "Volume": 0.0213183
    },
    {
      "OrderType": "LimitBid",
      "Price": 48475,
      "Volume": 1.72725791
    },
    {
      "OrderType": "LimitBid",
      "Price": 47955.62,
      "Volume": 0.6
    },
    {
      "OrderType": "LimitBid",
      "Price": 47782.5,
      "Volume": 0.12587799
    },
    {
      "OrderType": "LimitBid",
      "Price": 47704.94,
      "Volume": 0.20680333
    },
    {
      "OrderType": "LimitBid",
      "Price": 47700,
      "Volume": 0.00389132
    },
    {
      "OrderType": "LimitBid",
      "Price": 47436.25,
      "Volume": 0.22
    },
    {
      "OrderType": "LimitBid",
      "Price": 47112.12,
      "Volume": 0.42
    },
    {
      "OrderType": "LimitBid",
      "Price": 47090,
      "Volume": 0.01463271
    },
    {
      "OrderType": "LimitBid",
      "Price": 46882.25,
      "Volume": 0.01469756
    },
    {
      "OrderType": "LimitBid",
      "Price": 46743.75,
      "Volume": 0.00884481
    },
    {
      "OrderType": "LimitBid",
      "Price": 46702.37,
      "Volume": 0.04139689
    },
    {
      "OrderType": "LimitBid",
      "Price": 46632,
      "Volume": 0.1050645
    },
    {
      "OrderType": "LimitBid",
      "Price": 46397.5,
      "Volume": 0.14851118
    },
    {
      "OrderType": "LimitBid",
      "Price": 46321.12,
      "Volume": 0.33390096
    },
    {
      "OrderType": "LimitBid",
      "Price": 45912.75,
      "Volume": 0.22520838
    },
    {
      "OrderType": "LimitBid",
      "Price": 45854.8,
      "Volume": 0.02529724
    },
    {
      "OrderType": "LimitBid",
      "Price": 45787.4,
      "Volume": 0.52671502
    },
    {
      "OrderType": "LimitBid",
      "Price": 45705,
      "Volume": 0.50580554
    },
    {
      "OrderType": "LimitBid",
      "Price": 45467.07,
      "Volume": 0.09313933
    },
    {
      "OrderType": "LimitBid",
      "Price": 45199.47,
      "Volume": 0.24
    },
    {
      "OrderType": "LimitBid",
      "Price": 45114.14,
      "Volume": 0.884
    },
    {
      "OrderType": "LimitBid",
      "Price": 45113.13,
      "Volume": 0.07587337
    },
    {
      "OrderType": "LimitBid",
      "Price": 45019.42,
      "Volume": 0.00153057
    },
    {
      "OrderType": "LimitBid",
      "Price": 45012.5,
      "Volume": 1.19746265
    },
    {
      "OrderType": "LimitBid",
      "Price": 44766.72,
      "Volume": 0.02
    },
    {
      "OrderType": "LimitBid",
      "Price": 44320,
      "Volume": 0.706217
    },
    {
      "OrderType": "LimitBid",
      "Price": 44191.49,
      "Volume": 0.00077576
    },
    {
      "OrderType": "LimitBid",
      "Price": 43884,
      "Volume": 0.00453479
    },
    {
      "OrderType": "LimitBid",
      "Price": 43858.1,
      "Volume": 0.3142
    },
    {
      "OrderType": "LimitBid",
      "Price": 43663.51,
      "Volume": 0.10600034
    },
    {
      "OrderType": "LimitBid",
      "Price": 43627.5,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitBid",
      "Price": 42380.3,
      "Volume": 0.56905947
    },
    {
      "OrderType": "LimitBid",
      "Price": 42311.75,
      "Volume": 0.03
    },
    {
      "OrderType": "LimitBid",
      "Price": 42242.5,
      "Volume": 0.5
    },
    {
      "OrderType": "LimitBid",
      "Price": 42167.71,
      "Volume": 0.16422519
    },
    {
      "OrderType": "LimitBid",
      "Price": 41924.69,
      "Volume": 0.01643553
    },
    {
      "OrderType": "LimitBid",
      "Price": 41812.5,
      "Volume": 0.002
    },
    {
      "OrderType": "LimitBid",
      "Price": 41733.4,
      "Volume": 0.0240895
    },
    {
      "OrderType": "LimitBid",
      "Price": 41619.25,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitBid",
      "Price": 41550,
      "Volume": 1.16705288
    },
    {
      "OrderType": "LimitBid",
      "Price": 41278.11,
      "Volume": 4.085e-05
    },
    {
      "OrderType": "LimitBid",
      "Price": 41113.13,
      "Volume": 0.5
    },
    {
      "OrderType": "LimitBid",
      "Price": 40511.25,
      "Volume": 0.000426
    },
    {
      "OrderType": "LimitBid",
      "Price": 40507.66,
      "Volume": 0.00596
    },
    {
      "OrderType": "LimitBid",
      "Price": 40495.33,
      "Volume": 0.10457434
    },
    {
      "OrderType": "LimitBid",
      "Price": 40373,
      "Volume": 0.00492915
    },
    {
      "OrderType": "LimitBid",
      "Price": 40165,
      "Volume": 0.00043
    },
    {
      "OrderType": "LimitBid",
      "Price": 40115.11,
      "Volume": 1.01
    },
    {
      "OrderType": "LimitBid",
      "Price": 40114.14,
      "Volume": 0.08532865
    },
    {
      "OrderType": "LimitBid",
      "Price": 39818.75,
      "Volume": 0.0004329
    },
    {
      "OrderType": "LimitBid",
      "Price": 39637.2,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitBid",
      "Price": 39611,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitBid",
      "Price": 39472.5,
      "Volume": 1.60923956
    },
    {
      "OrderType": "LimitBid",
      "Price": 39126.25,
      "Volume": 0.01
    },
    {
      "OrderType": "LimitBid",
      "Price": 39024.44,
      "Volume": 0.01421484
    },
    {
      "OrderType": "LimitBid",
      "Price": 38861.02,
      "Volume": 0.62059394
    },
    {
      "OrderType": "LimitBid",
      "Price": 38860,
      "Volume": 0.09455222
    },
    {
      "OrderType": "LimitBid",
      "Price": 38780,
      "Volume": 0.1423826
    },
    {
      "OrderType": "LimitBid",
      "Price": 38642.35,
      "Volume": 0.30756653
    },
    {
      "OrderType": "LimitBid",
      "Price": 38511.11,
      "Volume": 1.05
    },
    {
      "OrderType": "LimitBid",
      "Price": 38226,
      "Volume": 0.000451
    },
    {
      "OrderType": "LimitBid",
      "Price": 38192.22,
      "Volume": 0.48272837
    },
    {
      "OrderType": "LimitBid",
      "Price": 38087.5,
      "Volume": 0.1914568
    },
    {
      "OrderType": "LimitBid",
      "Price": 37834.73,
      "Volume": 0.01821222
    },
    {
      "OrderType": "LimitBid",
      "Price": 37741.25,
      "Volume": 0.0004567
    },
    {
      "OrderType": "LimitBid",
      "Price": 37600,
      "Volume": 0.7
    },
    {
      "OrderType": "LimitBid",
      "Price": 37395,
      "Volume": 0.7972
    },
    {
      "OrderType": "LimitBid",
      "Price": 36910.25,
      "Volume": 0.000467
    },
    {
      "OrderType": "LimitBid",
      "Price": 36702.5,
      "Volume": 0.09702691
    },
    {
      "OrderType": "LimitBid",
      "Price": 36356.25,
      "Volume": 1.000474
    },
    {
      "OrderType": "LimitBid",
      "Price": 36273.22,
      "Volume": 9.49e-06
    },
    {
      "OrderType": "LimitBid",
      "Price": 36211.11,
      "Volume": 0.09462888
    },
    {
      "OrderType": "LimitBid",
      "Price": 35970.73,
      "Volume": 0.25
    },
    {
      "OrderType": "LimitBid",
      "Price": 35911.11,
      "Volume": 0.80888546
    },
    {
      "OrderType": "LimitBid",
      "Price": 35512.12,
      "Volume": 1.13
    },
    {
      "OrderType": "LimitBid",
      "Price": 35399.21,
      "Volume": 0.6812839
    },
    {
      "OrderType": "LimitBid",
      "Price": 35366.6,
      "Volume": 0.11980427
    },
    {
      "OrderType": "LimitBid",
      "Price": 34974,
      "Volume": 0.03316749
    },
    {
      "OrderType": "LimitBid",
      "Price": 34777.84,
      "Volume": 0.0289075
    },
    {
      "OrderType": "LimitBid",
      "Price": 34625,
      "Volume": 0.77676893
    },
    {
      "OrderType": "LimitBid",
      "Price": 34278.75,
      "Volume": 0.02060401
    },
    {
      "OrderType": "LimitBid",
      "Price": 33240,
      "Volume": 0.002073
    },
    {
      "OrderType": "LimitBid",
      "Price": 32893.75,
      "Volume": 0.0005236
    },
    {
      "OrderType": "LimitBid",
      "Price": 31935.33,
      "Volume": 0.75517977
    },
    {
      "OrderType": "LimitBid",
      "Price": 31902.78,
      "Volume": 0.03748117
    },
    {
      "OrderType": "LimitBid",
      "Price": 31479.29,
      "Volume": 0.5
    },
    {
      "OrderType": "LimitBid",
      "Price": 31382.57,
      "Volume": 2.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 31162.5,
      "Volume": 0.17892852
    },
    {
      "OrderType": "LimitBid",
      "Price": 31088,
      "Volume": 0.02487562
    },
    {
      "OrderType": "LimitBid",
      "Price": 30816.25,
      "Volume": 0.000559
    },
    {
      "OrderType": "LimitBid",
      "Price": 30000,
      "Volume": 0.00013029
    },
    {
      "OrderType": "LimitBid",
      "Price": 29925.69,
      "Volume": 0.34545156
    },
    {
      "OrderType": "LimitBid",
      "Price": 29085,
      "Volume": 1.17033878
    },
    {
      "OrderType": "LimitBid",
      "Price": 28471.44,
      "Volume": 0.84705624
    },
    {
      "OrderType": "LimitBid",
      "Price": 27700,
      "Volume": 0.3336
    },
    {
      "OrderType": "LimitBid",
      "Price": 26661.25,
      "Volume": 0.000646
    },
    {
      "OrderType": "LimitBid",
      "Price": 26261.69,
      "Volume": 0.02623801
    },
    {
      "OrderType": "LimitBid",
      "Price": 26038,
      "Volume": 0.01339106
    },
    {
      "OrderType": "LimitBid",
      "Price": 25968.75,
      "Volume": 0.0053
    },
    {
      "OrderType": "LimitBid",
      "Price": 25026.61,
      "Volume": 0.03090043
    },
    {
      "OrderType": "LimitBid",
      "Price": 25006.86,
      "Volume": 0.96441169
    },
    {
      "OrderType": "LimitBid",
      "Price": 24376,
      "Volume": 0.000707
    },
    {
      "OrderType": "LimitBid",
      "Price": 24237.5,
      "Volume": 0.62208756
    },
    {
      "OrderType": "LimitBid",
      "Price": 24168.25,
      "Volume": 0.000713
    },
    {
      "OrderType": "LimitBid",
      "Price": 23991.66,
      "Volume": 1.00542076
    },
    {
      "OrderType": "LimitBid",
      "Price": 23683.5,
      "Volume": 0.000728
    },
    {
      "OrderType": "LimitBid",
      "Price": 21661.4,
      "Volume": 1.00202313
    },
    {
      "OrderType": "LimitBid",
      "Price": 21467.5,
      "Volume": 0.003
    },
    {
      "OrderType": "LimitBid",
      "Price": 20775,
      "Volume": 0.10075
    },
    {
      "OrderType": "LimitBid",
      "Price": 20428.75,
      "Volume": 0.003373
    },
    {
      "OrderType": "LimitBid",
      "Price": 19528.5,
      "Volume": 0.001764
    },
    {
      "OrderType": "LimitBid",
      "Price": 19182.25,
      "Volume": 0.001796
    },
    {
      "OrderType": "LimitBid",
      "Price": 18836,
      "Volume": 0.001829
    },
    {
      "OrderType": "LimitBid",
      "Price": 18489.75,
      "Volume": 0.001863
    },
    {
      "OrderType": "LimitBid",
      "Price": 18084.63,
      "Volume": 0.00762071
    },
    {
      "OrderType": "LimitBid",
      "Price": 17875.6,
      "Volume": 0.002
    },
    {
      "OrderType": "LimitBid",
      "Price": 17658.75,
      "Volume": 0.005
    },
    {
      "OrderType": "LimitBid",
      "Price": 17312.5,
      "Volume": 0.33
    },
    {
      "OrderType": "LimitBid",
      "Price": 17104.75,
      "Volume": 0.01611422
    },
    {
      "OrderType": "LimitBid",
      "Price": 16966.25,
      "Volume": 0.01
    },
    {
      "OrderType": "LimitBid",
      "Price": 16620,
      "Volume": 0.005
    },
    {
      "OrderType": "LimitBid",
      "Price": 16481.5,
      "Volume": 0.001045
    },
    {
      "OrderType": "LimitBid",
      "Price": 16066,
      "Volume": 0.001072
    },
    {
      "OrderType": "LimitBid",
      "Price": 15927.5,
      "Volume": 0.004327
    },
    {
      "OrderType": "LimitBid",
      "Price": 15581.25,
      "Volume": 0.00221166
    },
    {
      "OrderType": "LimitBid",
      "Price": 15544,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitBid",
      "Price": 14639.45,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitBid",
      "Price": 14542.5,
      "Volume": 0.005
    },
    {
      "OrderType": "LimitBid",
      "Price": 14257.19,
      "Volume": 0.001
    },
    {
      "OrderType": "LimitBid",
      "Price": 13973.18,
      "Volume": 0.005
    },
    {
      "OrderType": "LimitBid",
      "Price": 13850,
      "Volume": 0.0781841
    },
    {
      "OrderType": "LimitBid",
      "Price": 13157.5,
      "Volume": 0.002618
    },
    {
      "OrderType": "LimitBid",
      "Price": 12824.57,
      "Volume": 0.04576099
    },
    {
      "OrderType": "LimitBid",
      "Price": 12725.38,
      "Volume": 0.0054
    },
    {
      "OrderType": "LimitBid",
      "Price": 12700.45,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitBid",
      "Price": 12465,
      "Volume": 0.002764
    },
    {
      "OrderType": "LimitBid",
      "Price": 12388.76,
      "Volume": 0.05825393
    },
    {
      "OrderType": "LimitBid",
      "Price": 12283.39,
      "Volume": 0.01
    },
    {
      "OrderType": "LimitBid",
      "Price": 12118.75,
      "Volume": 0.025686
    },
    {
      "OrderType": "LimitBid",
      "Price": 11902.69,
      "Volume": 0.003
    },
    {
      "OrderType": "LimitBid",
      "Price": 11841.75,
      "Volume": 0.09
    },
    {
      "OrderType": "LimitBid",
      "Price": 11772.5,
      "Volume": 0.30585279
    },
    {
      "OrderType": "LimitBid",
      "Price": 11564.75,
      "Volume": 0.00595869
    },
    {
      "OrderType": "LimitBid",
      "Price": 10761.45,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitBid",
      "Price": 10387.5,
      "Volume": 0.4525
    },
    {
      "OrderType": "LimitBid",
      "Price": 10041.25,
      "Volume": 0.001
    },
    {
      "OrderType": "LimitBid",
      "Price": 9720.14,
      "Volume": 0.01417787
    },
    {
      "OrderType": "LimitBid",
      "Price": 9695,
      "Volume": 0.001
    },
    {
      "OrderType": "LimitBid",
      "Price": 9575.89,
      "Volume": 0.005
    },
    {
      "OrderType": "LimitBid",
      "Price": 9477.5,
      "Volume": 0.066
    },
    {
      "OrderType": "LimitBid",
      "Price": 9409.69,
      "Volume": 0.000736
    },
    {
      "OrderType": "LimitBid",
      "Price": 9168.02,
      "Volume": 0.01504
    },
    {
      "OrderType": "LimitBid",
      "Price": 9074.96,
      "Volume": 0.01517748
    },
    {
      "OrderType": "LimitBid",
      "Price": 9002.5,
      "Volume": 0.001
    },
    {
      "OrderType": "LimitBid",
      "Price": 8656.25,
      "Volume": 0.05275
    },
    {
      "OrderType": "LimitBid",
      "Price": 8511.96,
      "Volume": 0.0199995
    },
    {
      "OrderType": "LimitBid",
      "Price": 8310,
      "Volume": 0.06058673
    },
    {
      "OrderType": "LimitBid",
      "Price": 8209.58,
      "Volume": 0.8980824
    },
    {
      "OrderType": "LimitBid",
      "Price": 7852.95,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitBid",
      "Price": 7617.5,
      "Volume": 0.01
    },
    {
      "OrderType": "LimitBid",
      "Price": 6970.7,
      "Volume": 0.0004
    },
    {
      "OrderType": "LimitBid",
      "Price": 6925.69,
      "Volume": 0.0014
    },
    {
      "OrderType": "LimitBid",
      "Price": 6925,
      "Volume": 0.11458629
    },
    {
      "OrderType": "LimitBid",
      "Price": 6924.3,
      "Volume": 0.03
    },
    {
      "OrderType": "LimitBid",
      "Price": 6918.42,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitBid",
      "Price": 6882.33,
      "Volume": 0.00042616
    },
    {
      "OrderType": "LimitBid",
      "Price": 6705.47,
      "Volume": 0.00685
    },
    {
      "OrderType": "LimitBid",
      "Price": 6674.31,
      "Volume": 0.01365
    },
    {
      "OrderType": "LimitBid",
      "Price": 6441.23,
      "Volume": 0.15
    },
    {
      "OrderType": "LimitBid",
      "Price": 6194.38,
      "Volume": 0.11
    },
    {
      "OrderType": "LimitBid",
      "Price": 6154.94,
      "Volume": 0.01
    },
    {
      "OrderType": "LimitBid",
      "Price": 5886.25,
      "Volume": 0.0055
    },
    {
      "OrderType": "LimitBid",
      "Price": 5616.17,
      "Volume": 0.001234
    },
    {
      "OrderType": "LimitBid",
      "Price": 5539.99,
      "Volume": 1.00018756
    },
    {
      "OrderType": "LimitBid",
      "Price": 5531.69,
      "Volume": 0.001253
    },
    {
      "OrderType": "LimitBid",
      "Price": 5193.75,
      "Volume": 0.0075
    },
    {
      "OrderType": "LimitBid",
      "Price": 4944.45,
      "Volume": 0.2
    },
    {
      "OrderType": "LimitBid",
      "Price": 4846.8,
      "Volume": 0.00143
    },
    {
      "OrderType": "LimitBid",
      "Price": 4826.72,
      "Volume": 1.18872223
    },
    {
      "OrderType": "LimitBid",
      "Price": 4785.17,
      "Volume": 0.001448
    },
    {
      "OrderType": "LimitBid",
      "Price": 4155,
      "Volume": 0.99500015
    },
    {
      "OrderType": "LimitBid",
      "Price": 4064.94,
      "Volume": 0.00028354
    },
    {
      "OrderType": "LimitBid",
      "Price": 3463.19,
      "Volume": 0.008877
    },
    {
      "OrderType": "LimitBid",
      "Price": 3462.5,
      "Volume": 0.36
    },
    {
      "OrderType": "LimitBid",
      "Price": 3378.09,
      "Volume": 0.66
    },
    {
      "OrderType": "LimitBid",
      "Price": 3116.25,
      "Volume": 0.02
    },
    {
      "OrderType": "LimitBid",
      "Price": 2930.71,
      "Volume": 0.001
    },
    {
      "OrderType": "LimitBid",
      "Price": 2770,
      "Volume": 0.025
    },
    {
      "OrderType": "LimitBid",
      "Price": 2700.75,
      "Volume": 0.0125
    },
    {
      "OrderType": "LimitBid",
      "Price": 2693.82,
      "Volume": 1.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 2547.77,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitBid",
      "Price": 2423.75,
      "Volume": 0.03
    },
    {
      "OrderType": "LimitBid",
      "Price": 2077.5,
      "Volume": 0.09
    },
    {
      "OrderType": "LimitBid",
      "Price": 2008.25,
      "Volume": 0.03
    },
    {
      "OrderType": "LimitBid",
      "Price": 1873.9,
      "Volume": 0.073584
    },
    {
      "OrderType": "LimitBid",
      "Price": 1467.68,
      "Volume": 0.04862689
    },
    {
      "OrderType": "LimitBid",
      "Price": 1385,
      "Volume": 0.1822
    },
    {
      "OrderType": "LimitBid",
      "Price": 1281.12,
      "Volume": 1.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 1073.37,
      "Volume": 0.01
    },
    {
      "OrderType": "LimitBid",
      "Price": 706.35,
      "Volume": 0.097
    },
    {
      "OrderType": "LimitBid",
      "Price": 693.19,
      "Volume": 4.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 692.5,
      "Volume": 15.01868199
    },
    {
      "OrderType": "LimitBid",
      "Price": 648.87,
      "Volume": 1.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 623.25,
      "Volume": 0.01
    },
    {
      "OrderType": "LimitBid",
      "Price": 472.06,
      "Volume": 0.99500528
    },
    {
      "OrderType": "LimitBid",
      "Price": 446.28,
      "Volume": 0.99500983
    },
    {
      "OrderType": "LimitBid",
      "Price": 418.27,
      "Volume": 0.0415
    },
    {
      "OrderType": "LimitBid",
      "Price": 346.94,
      "Volume": 0.2
    },
    {
      "OrderType": "LimitBid",
      "Price": 346.25,
      "Volume": 3.01502675
    },
    {
      "OrderType": "LimitBid",
      "Price": 342.78,
      "Volume": 0.0096136
    },
    {
      "OrderType": "LimitBid",
      "Price": 237.52,
      "Volume": 0.99722107
    },
    {
      "OrderType": "LimitBid",
      "Price": 207.75,
      "Volume": 0.004
    },
    {
      "OrderType": "LimitBid",
      "Price": 173.12,
      "Volume": 1.995
    },
    {
      "OrderType": "LimitBid",
      "Price": 169.66,
      "Volume": 0.78
    },
    {
      "OrderType": "LimitBid",
      "Price": 166.2,
      "Volume": 1.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 138.5,
      "Volume": 0.01540526
    },
    {
      "OrderType": "LimitBid",
      "Price": 136.42,
      "Volume": 0.00253098
    },
    {
      "OrderType": "LimitBid",
      "Price": 131.57,
      "Volume": 1.01976056
    },
    {
      "OrderType": "LimitBid",
      "Price": 105.95,
      "Volume": 0.0021
    },
    {
      "OrderType": "LimitBid",
      "Price": 103.87,
      "Volume": 3.05015151
    },
    {
      "OrderType": "LimitBid",
      "Price": 85.17,
      "Volume": 0.01
    },
    {
      "OrderType": "LimitBid",
      "Price": 81.71,
      "Volume": 0.84324142
    },
    {
      "OrderType": "LimitBid",
      "Price": 80.33,
      "Volume": 0.00765
    },
    {
      "OrderType": "LimitBid",
      "Price": 76.17,
      "Volume": 0.45771144
    },
    {
      "OrderType": "LimitBid",
      "Price": 69.25,
      "Volume": 15.328613
    },
    {
      "OrderType": "LimitBid",
      "Price": 68.55,
      "Volume": 1.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 67.86,
      "Volume": 0.0015
    },
    {
      "OrderType": "LimitBid",
      "Price": 55.4,
      "Volume": 0.027
    },
    {
      "OrderType": "LimitBid",
      "Price": 41.55,
      "Volume": 0.009
    },
    {
      "OrderType": "LimitBid",
      "Price": 36.67,
      "Volume": 0.99507239
    },
    {
      "OrderType": "LimitBid",
      "Price": 35.73,
      "Volume": 0.001255
    },
    {
      "OrderType": "LimitBid",
      "Price": 34.62,
      "Volume": 22.1002782
    },
    {
      "OrderType": "LimitBid",
      "Price": 33.93,
      "Volume": 21.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 32.54,
      "Volume": 2.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 27.7,
      "Volume": 0.64537503
    },
    {
      "OrderType": "LimitBid",
      "Price": 27,
      "Volume": 0.00178842
    },
    {
      "OrderType": "LimitBid",
      "Price": 24.23,
      "Volume": 50.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 15.92,
      "Volume": 0.04
    },
    {
      "OrderType": "LimitBid",
      "Price": 15.54,
      "Volume": 5.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 15.38,
      "Volume": 15.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 13.85,
      "Volume": 8.50822902
    },
    {
      "OrderType": "LimitBid",
      "Price": 13.38,
      "Volume": 1.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 13.16,
      "Volume": 0.001
    },
    {
      "OrderType": "LimitBid",
      "Price": 11.08,
      "Volume": 1.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 10.38,
      "Volume": 0.45966673
    },
    {
      "OrderType": "LimitBid",
      "Price": 10.03,
      "Volume": 1.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 7.77,
      "Volume": 2.99004975
    },
    {
      "OrderType": "LimitBid",
      "Price": 7.61,
      "Volume": 4.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 6.99,
      "Volume": 5.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 6.92,
      "Volume": 48.0255663
    },
    {
      "OrderType": "LimitBid",
      "Price": 6.91,
      "Volume": 0.0011
    },
    {
      "OrderType": "LimitBid",
      "Price": 6.77,
      "Volume": 0.993
    },
    {
      "OrderType": "LimitBid",
      "Price": 6.23,
      "Volume": 0.001
    },
    {
      "OrderType": "LimitBid",
      "Price": 5.88,
      "Volume": 1.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 5.54,
      "Volume": 1.02527263
    },
    {
      "OrderType": "LimitBid",
      "Price": 4.46,
      "Volume": 1.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 3.88,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitBid",
      "Price": 3.73,
      "Volume": 10.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 3.46,
      "Volume": 3.99004975
    },
    {
      "OrderType": "LimitBid",
      "Price": 3.11,
      "Volume": 2.5
    },
    {
      "OrderType": "LimitBid",
      "Price": 3.08,
      "Volume": 1.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 2.77,
      "Volume": 10.99502487
    },
    {
      "OrderType": "LimitBid",
      "Price": 2.42,
      "Volume": 10.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 2.07,
      "Volume": 5.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 1.86,
      "Volume": 0.01
    },
    {
      "OrderType": "LimitBid",
      "Price": 1.78,
      "Volume": 3.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 1.77,
      "Volume": 6.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 1.73,
      "Volume": 4.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 1.59,
      "Volume": 2.3
    },
    {
      "OrderType": "LimitBid",
      "Price": 1.55,
      "Volume": 4.97512437
    },
    {
      "OrderType": "LimitBid",
      "Price": 1.45,
      "Volume": 6.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 1.38,
      "Volume": 30.9805005
    },
    {
      "OrderType": "LimitBid",
      "Price": 1.25,
      "Volume": 800.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 1.24,
      "Volume": 90.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 1.03,
      "Volume": 7.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 1,
      "Volume": 0.001
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.98,
      "Volume": 0.99511334
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.89,
      "Volume": 10.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.88,
      "Volume": 5.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.87,
      "Volume": 2.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.86,
      "Volume": 5.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.85,
      "Volume": 100.00092806
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.83,
      "Volume": 91.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.77,
      "Volume": 126.7164179
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.69,
      "Volume": 822.084851
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.68,
      "Volume": 0.99502487
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.62,
      "Volume": 14.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.61,
      "Volume": 7.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.6,
      "Volume": 11.30710085
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.55,
      "Volume": 20.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.54,
      "Volume": 22.75672917
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.53,
      "Volume": 10.00706356
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.51,
      "Volume": 14.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.5,
      "Volume": 1016.35353803
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.48,
      "Volume": 3.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.47,
      "Volume": 14.42065037
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.44,
      "Volume": 2.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.42,
      "Volume": 26.31401076
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.41,
      "Volume": 11.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.38,
      "Volume": 10.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.37,
      "Volume": 18.42638658
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.34,
      "Volume": 245.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.33,
      "Volume": 30.7296849
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.31,
      "Volume": 10.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.29,
      "Volume": 33.69106846
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.27,
      "Volume": 10.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.25,
      "Volume": 26.8925642
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.24,
      "Volume": 16.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.23,
      "Volume": 15.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.22,
      "Volume": 30.15226895
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.2,
      "Volume": 70.3112026
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.19,
      "Volume": 20.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.18,
      "Volume": 398.85861081
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.17,
      "Volume": 59.09102278
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.16,
      "Volume": 17.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.15,
      "Volume": 128.01350758
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.14,
      "Volume": 30.0
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.13,
      "Volume": 116.75134378
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.12,
      "Volume": 94.27915975
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.11,
      "Volume": 88.52506301
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.1,
      "Volume": 3154.1732054
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.09,
      "Volume": 275.99194503
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.08,
      "Volume": 102.91873963
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.07,
      "Volume": 608.03265346
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.06,
      "Volume": 914.75422884
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.05,
      "Volume": 185.46763034
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.04,
      "Volume": 775.82136934
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.03,
      "Volume": 1006.96763085
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.02,
      "Volume": 4162.75953563
    },
    {
      "OrderType": "LimitBid",
      "Price": 0.01,
      "Volume": 36093.59904129
    }
  ],
  "SellOrders": [
    {
      "OrderType": "LimitOffer",
      "Price": 82589.28,
      "Volume": 0.13601681
    },
    {
      "OrderType": "LimitOffer",
      "Price": 82751.01,
      "Volume": 0.01334
    },
    {
      "OrderType": "LimitOffer",
      "Price": 82979.66,
      "Volume": 0.108569
    },
    {
      "OrderType": "LimitOffer",
      "Price": 83017.47,
      "Volume": 0.12357535
    },
    {
      "OrderType": "LimitOffer",
      "Price": 83081.83,
      "Volume": 0.0164371
    },
    {
      "OrderType": "LimitOffer",
      "Price": 83082.43,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 83084.45,
      "Volume": 0.32257354
    },
    {
      "OrderType": "LimitOffer",
      "Price": 83153.92,
      "Volume": 0.214
    },
    {
      "OrderType": "LimitOffer",
      "Price": 83153.95,
      "Volume": 0.1754556
    },
    {
      "OrderType": "LimitOffer",
      "Price": 83331.43,
      "Volume": 0.0421
    },
    {
      "OrderType": "LimitOffer",
      "Price": 83347.56,
      "Volume": 0.0421
    },
    {
      "OrderType": "LimitOffer",
      "Price": 83357.59,
      "Volume": 0.17467841
    },
    {
      "OrderType": "LimitOffer",
      "Price": 83369.6,
      "Volume": 0.02
    },
    {
      "OrderType": "LimitOffer",
      "Price": 83577.75,
      "Volume": 0.0421
    },
    {
      "OrderType": "LimitOffer",
      "Price": 83642.81,
      "Volume": 0.1403
    },
    {
      "OrderType": "LimitOffer",
      "Price": 84103.95,
      "Volume": 0.0499
    },
    {
      "OrderType": "LimitOffer",
      "Price": 84778.96,
      "Volume": 3.28374859
    },
    {
      "OrderType": "LimitOffer",
      "Price": 84991.51,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85011.65,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85023.69,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85028.23,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85031.25,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85069.65,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85261.64,
      "Volume": 0.19753187
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85268.61,
      "Volume": 0.21813223
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85553.97,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85554.85,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85555.63,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85589.1,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85600.9,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85604.62,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85609.77,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85748,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85856.1,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85856.43,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85856.45,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85856.56,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85856.57,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85857.42,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85882.27,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85937.32,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85941.07,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85943.72,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85949.44,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85949.78,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85959.32,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85960.57,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85961.32,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85982.53,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85989.97,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85991.9,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 85999.3,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86000.35,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86006.31,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86016.39,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86017.91,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86018.08,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86019.44,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86023.04,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86024.36,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86028.7,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86032.46,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86033.59,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86039.25,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86045.03,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86054.72,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86057.91,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86058.71,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86061.94,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86069.02,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86069.51,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86076.7,
      "Volume": 0.00849881
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86089.82,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86127.2,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86127.26,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86387.81,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86710.76,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86737.55,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86837.2,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86877.45,
      "Volume": 0.00460532
    },
    {
      "OrderType": "LimitOffer",
      "Price": 86908.35,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 87082.06,
      "Volume": 0.00043245
    },
    {
      "OrderType": "LimitOffer",
      "Price": 87112.55,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 87112.62,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 87148.06,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 87225.72,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 87256.4,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 87263.01,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 87264.68,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 87265.83,
      "Volume": 0.0001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 87297.15,
      "Volume": 0.01
    },
    {
      "OrderType": "LimitOffer",
      "Price": 87338.09,
      "Volume": 0.0009413
    },
    {
      "OrderType": "LimitOffer",
      "Price": 87437.05,
      "Volume": 0.003
    },
    {
      "OrderType": "LimitOffer",
      "Price": 87576.95,
      "Volume": 0.025
    },
    {
      "OrderType": "LimitOffer",
      "Price": 87786.8,
      "Volume": 0.082665
    },
    {
      "OrderType": "LimitOffer",
      "Price": 87926.7,
      "Volume": 0.01
    },
    {
      "OrderType": "LimitOffer",
      "Price": 88136.55,
      "Volume": 0.00167652
    },
    {
      "OrderType": "LimitOffer",
      "Price": 88375.77,
      "Volume": 0.08072569
    },
    {
      "OrderType": "LimitOffer",
      "Price": 88478.63,
      "Volume": 0.01437251
    },
    {
      "OrderType": "LimitOffer",
      "Price": 89158.34,
      "Volume": 0.02853365
    },
    {
      "OrderType": "LimitOffer",
      "Price": 89496,
      "Volume": 0.11781118
    },
    {
      "OrderType": "LimitOffer",
      "Price": 89690.13,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 90025.19,
      "Volume": 0.001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 90047.11,
      "Volume": 0.00011223
    },
    {
      "OrderType": "LimitOffer",
      "Price": 90105.32,
      "Volume": 0.0005
    },
    {
      "OrderType": "LimitOffer",
      "Price": 90225.24,
      "Volume": 0.00230974
    },
    {
      "OrderType": "LimitOffer",
      "Price": 90281.05,
      "Volume": 0.15174787
    },
    {
      "OrderType": "LimitOffer",
      "Price": 90310.89,
      "Volume": 0.66969785
    },
    {
      "OrderType": "LimitOffer",
      "Price": 90533.17,
      "Volume": 0.00569092
    },
    {
      "OrderType": "LimitOffer",
      "Price": 90739.37,
      "Volume": 0.025
    },
    {
      "OrderType": "LimitOffer",
      "Price": 90748.06,
      "Volume": 0.054
    },
    {
      "OrderType": "LimitOffer",
      "Price": 90825.25,
      "Volume": 0.00264752
    },
    {
      "OrderType": "LimitOffer",
      "Price": 90933.13,
      "Volume": 0.001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 90934.53,
      "Volume": 1.12174898
    },
    {
      "OrderType": "LimitOffer",
      "Price": 91214.33,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 91219.37,
      "Volume": 9.576e-05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 91223.12,
      "Volume": 0.00122
    },
    {
      "OrderType": "LimitOffer",
      "Price": 91284.28,
      "Volume": 0.45
    },
    {
      "OrderType": "LimitOffer",
      "Price": 91513.21,
      "Volume": 0.0005
    },
    {
      "OrderType": "LimitOffer",
      "Price": 91644.71,
      "Volume": 0.01245783
    },
    {
      "OrderType": "LimitOffer",
      "Price": 91681.51,
      "Volume": 0.01086445
    },
    {
      "OrderType": "LimitOffer",
      "Price": 92133.33,
      "Volume": 1.0
    },
    {
      "OrderType": "LimitOffer",
      "Price": 92333.52,
      "Volume": 0.02944703
    },
    {
      "OrderType": "LimitOffer",
      "Price": 92636.21,
      "Volume": 0.21292906
    },
    {
      "OrderType": "LimitOffer",
      "Price": 92921.11,
      "Volume": 0.0005
    },
    {
      "OrderType": "LimitOffer",
      "Price": 92964.68,
      "Volume": 0.00501663
    },
    {
      "OrderType": "LimitOffer",
      "Price": 93033.02,
      "Volume": 0.20056675
    },
    {
      "OrderType": "LimitOffer",
      "Price": 93322.72,
      "Volume": 0.00518124
    },
    {
      "OrderType": "LimitOffer",
      "Price": 93590.89,
      "Volume": 0.054
    },
    {
      "OrderType": "LimitOffer",
      "Price": 93732.52,
      "Volume": 0.01194148
    },
    {
      "OrderType": "LimitOffer",
      "Price": 94047.42,
      "Volume": 0.24088696
    },
    {
      "OrderType": "LimitOffer",
      "Price": 94206.32,
      "Volume": 0.0540637
    },
    {
      "OrderType": "LimitOffer",
      "Price": 94329,
      "Volume": 0.0005
    },
    {
      "OrderType": "LimitOffer",
      "Price": 94432.01,
      "Volume": 0.99598735
    },
    {
      "OrderType": "LimitOffer",
      "Price": 94716.6,
      "Volume": 0.00563395
    },
    {
      "OrderType": "LimitOffer",
      "Price": 94828.97,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 95131.51,
      "Volume": 0.00055425
    },
    {
      "OrderType": "LimitOffer",
      "Price": 95139.75,
      "Volume": 0.08559526
    },
    {
      "OrderType": "LimitOffer",
      "Price": 95831.01,
      "Volume": 0.05232972
    },
    {
      "OrderType": "LimitOffer",
      "Price": 96530.5,
      "Volume": 0.00036414
    },
    {
      "OrderType": "LimitOffer",
      "Price": 96537.92,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 96993.09,
      "Volume": 9.664e-05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 97546.17,
      "Volume": 0.01
    },
    {
      "OrderType": "LimitOffer",
      "Price": 97705.66,
      "Volume": 0.6
    },
    {
      "OrderType": "LimitOffer",
      "Price": 97851.77,
      "Volume": 0.00092288
    },
    {
      "OrderType": "LimitOffer",
      "Price": 97877.22,
      "Volume": 0.00018705
    },
    {
      "OrderType": "LimitOffer",
      "Price": 97929.5,
      "Volume": 2.39990526
    },
    {
      "OrderType": "LimitOffer",
      "Price": 98131.58,
      "Volume": 0.25
    },
    {
      "OrderType": "LimitOffer",
      "Price": 98273.35,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 98549.25,
      "Volume": 0.02
    },
    {
      "OrderType": "LimitOffer",
      "Price": 98628.99,
      "Volume": 0.33731008
    },
    {
      "OrderType": "LimitOffer",
      "Price": 98711.93,
      "Volume": 0.00799294
    },
    {
      "OrderType": "LimitOffer",
      "Price": 99328.49,
      "Volume": 0.2
    },
    {
      "OrderType": "LimitOffer",
      "Price": 99335.48,
      "Volume": 0.025
    },
    {
      "OrderType": "LimitOffer",
      "Price": 99483.78,
      "Volume": 0.02
    },
    {
      "OrderType": "LimitOffer",
      "Price": 99897.79,
      "Volume": 0.00064195
    },
    {
      "OrderType": "LimitOffer",
      "Price": 100000,
      "Volume": 0.6
    },
    {
      "OrderType": "LimitOffer",
      "Price": 100304.61,
      "Volume": 1.04e-05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 100323.68,
      "Volume": 0.0562229
    },
    {
      "OrderType": "LimitOffer",
      "Price": 101038.06,
      "Volume": 0.02
    },
    {
      "OrderType": "LimitOffer",
      "Price": 101327.63,
      "Volume": 0.00010303
    },
    {
      "OrderType": "LimitOffer",
      "Price": 101426.98,
      "Volume": 0.85138625
    },
    {
      "OrderType": "LimitOffer",
      "Price": 101562.26,
      "Volume": 0.00848039
    },
    {
      "OrderType": "LimitOffer",
      "Price": 101776.73,
      "Volume": 0.021
    },
    {
      "OrderType": "LimitOffer",
      "Price": 102056.84,
      "Volume": 0.15
    },
    {
      "OrderType": "LimitOffer",
      "Price": 102825.97,
      "Volume": 0.16
    },
    {
      "OrderType": "LimitOffer",
      "Price": 102930.89,
      "Volume": 0.04
    },
    {
      "OrderType": "LimitOffer",
      "Price": 103184.23,
      "Volume": 1.0384458
    },
    {
      "OrderType": "LimitOffer",
      "Price": 103524.77,
      "Volume": 0.00742166
    },
    {
      "OrderType": "LimitOffer",
      "Price": 103525.47,
      "Volume": 0.2181754
    },
    {
      "OrderType": "LimitOffer",
      "Price": 104015.11,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 104224.26,
      "Volume": 0.0005
    },
    {
      "OrderType": "LimitOffer",
      "Price": 104411.03,
      "Volume": 0.0007
    },
    {
      "OrderType": "LimitOffer",
      "Price": 104574.71,
      "Volume": 0.02
    },
    {
      "OrderType": "LimitOffer",
      "Price": 104924.46,
      "Volume": 0.06137008
    },
    {
      "OrderType": "LimitOffer",
      "Price": 105169.28,
      "Volume": 0.025
    },
    {
      "OrderType": "LimitOffer",
      "Price": 105354.34,
      "Volume": 1.453e-05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 105576.74,
      "Volume": 0.00713874
    },
    {
      "OrderType": "LimitOffer",
      "Price": 105623.96,
      "Volume": 0.00199674
    },
    {
      "OrderType": "LimitOffer",
      "Price": 106163.41,
      "Volume": 0.00728425
    },
    {
      "OrderType": "LimitOffer",
      "Price": 106197.84,
      "Volume": 0.01131388
    },
    {
      "OrderType": "LimitOffer",
      "Price": 106945.22,
      "Volume": 0.00084517
    },
    {
      "OrderType": "LimitOffer",
      "Price": 107722.44,
      "Volume": 0.01465803
    },
    {
      "OrderType": "LimitOffer",
      "Price": 107944.74,
      "Volume": 0.009
    },
    {
      "OrderType": "LimitOffer",
      "Price": 108337.26,
      "Volume": 0.00766658
    },
    {
      "OrderType": "LimitOffer",
      "Price": 109544.63,
      "Volume": 0.00027956
    },
    {
      "OrderType": "LimitOffer",
      "Price": 109635.57,
      "Volume": 6.983e-05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 109639.12,
      "Volume": 0.03047158
    },
    {
      "OrderType": "LimitOffer",
      "Price": 109820.93,
      "Volume": 0.00192044
    },
    {
      "OrderType": "LimitOffer",
      "Price": 109907.37,
      "Volume": 0.03987725
    },
    {
      "OrderType": "LimitOffer",
      "Price": 109960.83,
      "Volume": 0.032
    },
    {
      "OrderType": "LimitOffer",
      "Price": 109964.31,
      "Volume": 0.0053
    },
    {
      "OrderType": "LimitOffer",
      "Price": 110172.01,
      "Volume": 9.385e-05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 110299.9,
      "Volume": 0.05165179
    },
    {
      "OrderType": "LimitOffer",
      "Price": 110692.42,
      "Volume": 0.05274962
    },
    {
      "OrderType": "LimitOffer",
      "Price": 110806.09,
      "Volume": 0.00150753
    },
    {
      "OrderType": "LimitOffer",
      "Price": 111142.2,
      "Volume": 0.00115524
    },
    {
      "OrderType": "LimitOffer",
      "Price": 111668.16,
      "Volume": 0.0037411
    },
    {
      "OrderType": "LimitOffer",
      "Price": 111919.42,
      "Volume": 0.37791277
    },
    {
      "OrderType": "LimitOffer",
      "Price": 112436.42,
      "Volume": 0.00011357
    },
    {
      "OrderType": "LimitOffer",
      "Price": 113278.94,
      "Volume": 0.00368656
    },
    {
      "OrderType": "LimitOffer",
      "Price": 113527.2,
      "Volume": 0.00277797
    },
    {
      "OrderType": "LimitOffer",
      "Price": 114017.91,
      "Volume": 0.00246632
    },
    {
      "OrderType": "LimitOffer",
      "Price": 114225.16,
      "Volume": 0.01312874
    },
    {
      "OrderType": "LimitOffer",
      "Price": 115349.75,
      "Volume": 0.00175067
    },
    {
      "OrderType": "LimitOffer",
      "Price": 115416.9,
      "Volume": 0.00274098
    },
    {
      "OrderType": "LimitOffer",
      "Price": 115795.26,
      "Volume": 0.07272662
    },
    {
      "OrderType": "LimitOffer",
      "Price": 116174.46,
      "Volume": 0.03630806
    },
    {
      "OrderType": "LimitOffer",
      "Price": 116582.27,
      "Volume": 0.01
    },
    {
      "OrderType": "LimitOffer",
      "Price": 116738.25,
      "Volume": 0.0006
    },
    {
      "OrderType": "LimitOffer",
      "Price": 116815.9,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 116875.88,
      "Volume": 0.00675074
    },
    {
      "OrderType": "LimitOffer",
      "Price": 117515.39,
      "Volume": 0.00156013
    },
    {
      "OrderType": "LimitOffer",
      "Price": 117757.89,
      "Volume": 0.69127254
    },
    {
      "OrderType": "LimitOffer",
      "Price": 117963.07,
      "Volume": 0.15
    },
    {
      "OrderType": "LimitOffer",
      "Price": 118137.16,
      "Volume": 0.00067221
    },
    {
      "OrderType": "LimitOffer",
      "Price": 118144.94,
      "Volume": 0.03
    },
    {
      "OrderType": "LimitOffer",
      "Price": 118214.89,
      "Volume": 0.25014868
    },
    {
      "OrderType": "LimitOffer",
      "Price": 118263.23,
      "Volume": 5.182e-05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 118914.39,
      "Volume": 0.25171961
    },
    {
      "OrderType": "LimitOffer",
      "Price": 118976.75,
      "Volume": 0.0008775
    },
    {
      "OrderType": "LimitOffer",
      "Price": 119074.57,
      "Volume": 0.06216801
    },
    {
      "OrderType": "LimitOffer",
      "Price": 119328,
      "Volume": 0.07
    },
    {
      "OrderType": "LimitOffer",
      "Price": 119493.67,
      "Volume": 0.1508899
    },
    {
      "OrderType": "LimitOffer",
      "Price": 120000,
      "Volume": 0.5
    },
    {
      "OrderType": "LimitOffer",
      "Price": 120648.82,
      "Volume": 0.15089439
    },
    {
      "OrderType": "LimitOffer",
      "Price": 121000,
      "Volume": 0.0616
    },
    {
      "OrderType": "LimitOffer",
      "Price": 121079.02,
      "Volume": 0.15542641
    },
    {
      "OrderType": "LimitOffer",
      "Price": 121133.18,
      "Volume": 0.00023692
    },
    {
      "OrderType": "LimitOffer",
      "Price": 121336.3,
      "Volume": 0.00068835
    },
    {
      "OrderType": "LimitOffer",
      "Price": 121683.16,
      "Volume": 0.15355091
    },
    {
      "OrderType": "LimitOffer",
      "Price": 121691.31,
      "Volume": 0.00199336
    },
    {
      "OrderType": "LimitOffer",
      "Price": 121712.37,
      "Volume": 0.00014441
    },
    {
      "OrderType": "LimitOffer",
      "Price": 122411.87,
      "Volume": 0.48769125
    },
    {
      "OrderType": "LimitOffer",
      "Price": 122468.21,
      "Volume": 0.0697008
    },
    {
      "OrderType": "LimitOffer",
      "Price": 122597.6,
      "Volume": 0.00363071
    },
    {
      "OrderType": "LimitOffer",
      "Price": 122756.48,
      "Volume": 0.00037213
    },
    {
      "OrderType": "LimitOffer",
      "Price": 123503.46,
      "Volume": 0.00036248
    },
    {
      "OrderType": "LimitOffer",
      "Price": 123634.01,
      "Volume": 0.00117486
    },
    {
      "OrderType": "LimitOffer",
      "Price": 123810.86,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 124370.46,
      "Volume": 0.02826775
    },
    {
      "OrderType": "LimitOffer",
      "Price": 124517.18,
      "Volume": 0.01000599
    },
    {
      "OrderType": "LimitOffer",
      "Price": 125131.51,
      "Volume": 0.01264091
    },
    {
      "OrderType": "LimitOffer",
      "Price": 125209.85,
      "Volume": 0.0038541
    },
    {
      "OrderType": "LimitOffer",
      "Price": 125370.72,
      "Volume": 0.05982523
    },
    {
      "OrderType": "LimitOffer",
      "Price": 125451.41,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 125598.07,
      "Volume": 0.03344103
    },
    {
      "OrderType": "LimitOffer",
      "Price": 125608.42,
      "Volume": 2.01233038
    },
    {
      "OrderType": "LimitOffer",
      "Price": 125909.35,
      "Volume": 0.33386274
    },
    {
      "OrderType": "LimitOffer",
      "Price": 125951.69,
      "Volume": 0.05011431
    },
    {
      "OrderType": "LimitOffer",
      "Price": 126112.13,
      "Volume": 0.061
    },
    {
      "OrderType": "LimitOffer",
      "Price": 126152.75,
      "Volume": 0.00857207
    },
    {
      "OrderType": "LimitOffer",
      "Price": 126531.12,
      "Volume": 0.00062761
    },
    {
      "OrderType": "LimitOffer",
      "Price": 126608.85,
      "Volume": 0.00014407
    },
    {
      "OrderType": "LimitOffer",
      "Price": 126886.76,
      "Volume": 0.15589498
    },
    {
      "OrderType": "LimitOffer",
      "Price": 127308.34,
      "Volume": 0.00015
    },
    {
      "OrderType": "LimitOffer",
      "Price": 127308.55,
      "Volume": 0.02395907
    },
    {
      "OrderType": "LimitOffer",
      "Price": 127675.87,
      "Volume": 0.00129529
    },
    {
      "OrderType": "LimitOffer",
      "Price": 127993.13,
      "Volume": 0.03062371
    },
    {
      "OrderType": "LimitOffer",
      "Price": 128626.75,
      "Volume": 0.00029761
    },
    {
      "OrderType": "LimitOffer",
      "Price": 128707.34,
      "Volume": 0.10015
    },
    {
      "OrderType": "LimitOffer",
      "Price": 128815.06,
      "Volume": 0.2
    },
    {
      "OrderType": "LimitOffer",
      "Price": 129406.83,
      "Volume": 0.02636118
    },
    {
      "OrderType": "LimitOffer",
      "Price": 129526.39,
      "Volume": 5.182e-05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 129533.68,
      "Volume": 1.53863574
    },
    {
      "OrderType": "LimitOffer",
      "Price": 129864.57,
      "Volume": 0.00090226
    },
    {
      "OrderType": "LimitOffer",
      "Price": 130000,
      "Volume": 0.22662977
    },
    {
      "OrderType": "LimitOffer",
      "Price": 130106.33,
      "Volume": 0.16372557
    },
    {
      "OrderType": "LimitOffer",
      "Price": 130318.74,
      "Volume": 0.01
    },
    {
      "OrderType": "LimitOffer",
      "Price": 130652.71,
      "Volume": 0.25326
    },
    {
      "OrderType": "LimitOffer",
      "Price": 130805.82,
      "Volume": 0.03006122
    },
    {
      "OrderType": "LimitOffer",
      "Price": 130944.33,
      "Volume": 0.05397575
    },
    {
      "OrderType": "LimitOffer",
      "Price": 130980.7,
      "Volume": 0.00026837
    },
    {
      "OrderType": "LimitOffer",
      "Price": 131029.74,
      "Volume": 0.0119834
    },
    {
      "OrderType": "LimitOffer",
      "Price": 131155.57,
      "Volume": 2.681e-05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 131505.32,
      "Volume": 0.1612498
    },
    {
      "OrderType": "LimitOffer",
      "Price": 131513.26,
      "Volume": 0.00189879
    },
    {
      "OrderType": "LimitOffer",
      "Price": 131810.34,
      "Volume": 0.06093245
    },
    {
      "OrderType": "LimitOffer",
      "Price": 132126.47,
      "Volume": 0.02007889
    },
    {
      "OrderType": "LimitOffer",
      "Price": 132127.09,
      "Volume": 0.00239891
    },
    {
      "OrderType": "LimitOffer",
      "Price": 132204.82,
      "Volume": 0.52393814
    },
    {
      "OrderType": "LimitOffer",
      "Price": 132379.69,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 132673.89,
      "Volume": 0.00011894
    },
    {
      "OrderType": "LimitOffer",
      "Price": 132825.97,
      "Volume": 0.01338379
    },
    {
      "OrderType": "LimitOffer",
      "Price": 132834.36,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 132842.88,
      "Volume": 0.02114036
    },
    {
      "OrderType": "LimitOffer",
      "Price": 132903.61,
      "Volume": 0.08
    },
    {
      "OrderType": "LimitOffer",
      "Price": 132904.31,
      "Volume": 0.53827698
    },
    {
      "OrderType": "LimitOffer",
      "Price": 133063.2,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 133217.69,
      "Volume": 0.2
    },
    {
      "OrderType": "LimitOffer",
      "Price": 133254.06,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 133334.47,
      "Volume": 0.02106123
    },
    {
      "OrderType": "LimitOffer",
      "Price": 133451.1,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 133458.95,
      "Volume": 0.27130344
    },
    {
      "OrderType": "LimitOffer",
      "Price": 133533.86,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 133646.14,
      "Volume": 0.00532948
    },
    {
      "OrderType": "LimitOffer",
      "Price": 133693.8,
      "Volume": 0.01
    },
    {
      "OrderType": "LimitOffer",
      "Price": 133715.82,
      "Volume": 0.003
    },
    {
      "OrderType": "LimitOffer",
      "Price": 133763.97,
      "Volume": 0.03615451
    },
    {
      "OrderType": "LimitOffer",
      "Price": 133820.28,
      "Volume": 0.02098362
    },
    {
      "OrderType": "LimitOffer",
      "Price": 133957.96,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 134233.36,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 134300.46,
      "Volume": 0.02090748
    },
    {
      "OrderType": "LimitOffer",
      "Price": 134303.31,
      "Volume": 0.45
    },
    {
      "OrderType": "LimitOffer",
      "Price": 134406.83,
      "Volume": 0.12545449
    },
    {
      "OrderType": "LimitOffer",
      "Price": 134750.73,
      "Volume": 0.00417371
    },
    {
      "OrderType": "LimitOffer",
      "Price": 134775.14,
      "Volume": 0.02083276
    },
    {
      "OrderType": "LimitOffer",
      "Price": 134932.85,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 134962.23,
      "Volume": 0.02
    },
    {
      "OrderType": "LimitOffer",
      "Price": 135046.17,
      "Volume": 0.0014
    },
    {
      "OrderType": "LimitOffer",
      "Price": 135228.65,
      "Volume": 0.11
    },
    {
      "OrderType": "LimitOffer",
      "Price": 135244.44,
      "Volume": 0.02075942
    },
    {
      "OrderType": "LimitOffer",
      "Price": 135352.55,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 135359.55,
      "Volume": 1.0
    },
    {
      "OrderType": "LimitOffer",
      "Price": 135382.16,
      "Volume": 0.00122153
    },
    {
      "OrderType": "LimitOffer",
      "Price": 135623.96,
      "Volume": 0.04
    },
    {
      "OrderType": "LimitOffer",
      "Price": 135632.35,
      "Volume": 0.25
    },
    {
      "OrderType": "LimitOffer",
      "Price": 135667.32,
      "Volume": 0.06
    },
    {
      "OrderType": "LimitOffer",
      "Price": 135702.3,
      "Volume": 0.25537522
    },
    {
      "OrderType": "LimitOffer",
      "Price": 135708.5,
      "Volume": 0.02068742
    },
    {
      "OrderType": "LimitOffer",
      "Price": 135814.31,
      "Volume": 0.003
    },
    {
      "OrderType": "LimitOffer",
      "Price": 135982.1,
      "Volume": 0.005
    },
    {
      "OrderType": "LimitOffer",
      "Price": 136156.24,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 136167.44,
      "Volume": 0.02061671
    },
    {
      "OrderType": "LimitOffer",
      "Price": 136331.85,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 136401.8,
      "Volume": 0.88691011
    },
    {
      "OrderType": "LimitOffer",
      "Price": 136621.37,
      "Volume": 0.02054725
    },
    {
      "OrderType": "LimitOffer",
      "Price": 136751.54,
      "Volume": 1.0
    },
    {
      "OrderType": "LimitOffer",
      "Price": 136847.45,
      "Volume": 0.184
    },
    {
      "OrderType": "LimitOffer",
      "Price": 137031.34,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 137066.32,
      "Volume": 2.81784936
    },
    {
      "OrderType": "LimitOffer",
      "Price": 137070.4,
      "Volume": 0.02047901
    },
    {
      "OrderType": "LimitOffer",
      "Price": 137101.29,
      "Volume": 0.25
    },
    {
      "OrderType": "LimitOffer",
      "Price": 137514.65,
      "Volume": 0.02041195
    },
    {
      "OrderType": "LimitOffer",
      "Price": 137723.06,
      "Volume": 0.00065812
    },
    {
      "OrderType": "LimitOffer",
      "Price": 137800.79,
      "Volume": 0.25
    },
    {
      "OrderType": "LimitOffer",
      "Price": 137954.22,
      "Volume": 0.02034603
    },
    {
      "OrderType": "LimitOffer",
      "Price": 137973.76,
      "Volume": 0.15
    },
    {
      "OrderType": "LimitOffer",
      "Price": 138150.54,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 138351.82,
      "Volume": 0.15092311
    },
    {
      "OrderType": "LimitOffer",
      "Price": 138389.21,
      "Volume": 0.02028123
    },
    {
      "OrderType": "LimitOffer",
      "Price": 138443.97,
      "Volume": 7.541e-05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 138500.28,
      "Volume": 0.33840887
    },
    {
      "OrderType": "LimitOffer",
      "Price": 138570.23,
      "Volume": 0.02
    },
    {
      "OrderType": "LimitOffer",
      "Price": 138620.03,
      "Volume": 0.003
    },
    {
      "OrderType": "LimitOffer",
      "Price": 138819.72,
      "Volume": 0.0202175
    },
    {
      "OrderType": "LimitOffer",
      "Price": 139121.44,
      "Volume": 0.07914576
    },
    {
      "OrderType": "LimitOffer",
      "Price": 139199.78,
      "Volume": 0.36430002
    },
    {
      "OrderType": "LimitOffer",
      "Price": 139231.75,
      "Volume": 5.498e-05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 139245.85,
      "Volume": 0.02015483
    },
    {
      "OrderType": "LimitOffer",
      "Price": 139497.07,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 139549.53,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 139667.68,
      "Volume": 0.02009317
    },
    {
      "OrderType": "LimitOffer",
      "Price": 139739.37,
      "Volume": 0.00565
    },
    {
      "OrderType": "LimitOffer",
      "Price": 139794.35,
      "Volume": 0.25
    },
    {
      "OrderType": "LimitOffer",
      "Price": 139820.93,
      "Volume": 0.002
    },
    {
      "OrderType": "LimitOffer",
      "Price": 139898.58,
      "Volume": 0.43030157
    },
    {
      "OrderType": "LimitOffer",
      "Price": 139899.28,
      "Volume": 2.38949405
    },
    {
      "OrderType": "LimitOffer",
      "Price": 140000,
      "Volume": 0.07751455
    },
    {
      "OrderType": "LimitOffer",
      "Price": 140014.52,
      "Volume": 5.965e-05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 140085.32,
      "Volume": 0.02003251
    },
    {
      "OrderType": "LimitOffer",
      "Price": 140131.89,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 140396.62,
      "Volume": 0.008
    },
    {
      "OrderType": "LimitOffer",
      "Price": 140498.82,
      "Volume": 0.01997281
    },
    {
      "OrderType": "LimitOffer",
      "Price": 140551.17,
      "Volume": 0.0046685
    },
    {
      "OrderType": "LimitOffer",
      "Price": 140598.77,
      "Volume": 0.25
    },
    {
      "OrderType": "LimitOffer",
      "Price": 140612.76,
      "Volume": 0.0005
    },
    {
      "OrderType": "LimitOffer",
      "Price": 140789.55,
      "Volume": 1.0045
    },
    {
      "OrderType": "LimitOffer",
      "Price": 140908.31,
      "Volume": 0.01991404
    },
    {
      "OrderType": "LimitOffer",
      "Price": 140948.52,
      "Volume": 1.0
    },
    {
      "OrderType": "LimitOffer",
      "Price": 140962.42,
      "Volume": 0.0011
    },
    {
      "OrderType": "LimitOffer",
      "Price": 140999.54,
      "Volume": 0.00149578
    },
    {
      "OrderType": "LimitOffer",
      "Price": 141309.47,
      "Volume": 0.18752032
    },
    {
      "OrderType": "LimitOffer",
      "Price": 141313.83,
      "Volume": 0.01985619
    },
    {
      "OrderType": "LimitOffer",
      "Price": 141648.02,
      "Volume": 1.0
    },
    {
      "OrderType": "LimitOffer",
      "Price": 141715.48,
      "Volume": 0.01979923
    },
    {
      "OrderType": "LimitOffer",
      "Price": 141857.87,
      "Volume": 0.0306717
    },
    {
      "OrderType": "LimitOffer",
      "Price": 141962.79,
      "Volume": 1.0
    },
    {
      "OrderType": "LimitOffer",
      "Price": 141997.77,
      "Volume": 0.3
    },
    {
      "OrderType": "LimitOffer",
      "Price": 142113.34,
      "Volume": 0.01974313
    },
    {
      "OrderType": "LimitOffer",
      "Price": 142182.29,
      "Volume": 0.00049445
    },
    {
      "OrderType": "LimitOffer",
      "Price": 142267.38,
      "Volume": 1.472e-05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 142507.48,
      "Volume": 0.01968788
    },
    {
      "OrderType": "LimitOffer",
      "Price": 142596.07,
      "Volume": 0.04557565
    },
    {
      "OrderType": "LimitOffer",
      "Price": 142627.31,
      "Volume": 0.00988777
    },
    {
      "OrderType": "LimitOffer",
      "Price": 142697.26,
      "Volume": 0.25
    },
    {
      "OrderType": "LimitOffer",
      "Price": 142897.96,
      "Volume": 0.01963344
    },
    {
      "OrderType": "LimitOffer",
      "Price": 142965,
      "Volume": 0.005
    },
    {
      "OrderType": "LimitOffer",
      "Price": 143046.31,
      "Volume": 0.00029488
    },
    {
      "OrderType": "LimitOffer",
      "Price": 143047.01,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 143048.56,
      "Volume": 0.01
    },
    {
      "OrderType": "LimitOffer",
      "Price": 143186.91,
      "Volume": 0.002
    },
    {
      "OrderType": "LimitOffer",
      "Price": 143284.87,
      "Volume": 0.01957981
    },
    {
      "OrderType": "LimitOffer",
      "Price": 143326.81,
      "Volume": 1.0
    },
    {
      "OrderType": "LimitOffer",
      "Price": 143396.75,
      "Volume": 0.31492841
    },
    {
      "OrderType": "LimitOffer",
      "Price": 143664.63,
      "Volume": 0.00226568
    },
    {
      "OrderType": "LimitOffer",
      "Price": 143668.25,
      "Volume": 0.01952695
    },
    {
      "OrderType": "LimitOffer",
      "Price": 143746.51,
      "Volume": 1.0
    },
    {
      "OrderType": "LimitOffer",
      "Price": 143960,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 144048.19,
      "Volume": 0.01947486
    },
    {
      "OrderType": "LimitOffer",
      "Price": 144096.26,
      "Volume": 0.25
    },
    {
      "OrderType": "LimitOffer",
      "Price": 144323.14,
      "Volume": 0.00057871
    },
    {
      "OrderType": "LimitOffer",
      "Price": 144424.75,
      "Volume": 0.01942351
    },
    {
      "OrderType": "LimitOffer",
      "Price": 144795.75,
      "Volume": 0.25
    },
    {
      "OrderType": "LimitOffer",
      "Price": 144797.99,
      "Volume": 0.01937288
    },
    {
      "OrderType": "LimitOffer",
      "Price": 145167.96,
      "Volume": 0.01932296
    },
    {
      "OrderType": "LimitOffer",
      "Price": 145226.87,
      "Volume": 0.00035944
    },
    {
      "OrderType": "LimitOffer",
      "Price": 145495.25,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 145530.22,
      "Volume": 0.09231747
    },
    {
      "OrderType": "LimitOffer",
      "Price": 145534.73,
      "Volume": 0.01927372
    },
    {
      "OrderType": "LimitOffer",
      "Price": 145736.57,
      "Volume": 1.0
    },
    {
      "OrderType": "LimitOffer",
      "Price": 145875.07,
      "Volume": 0.00240964
    },
    {
      "OrderType": "LimitOffer",
      "Price": 145898.36,
      "Volume": 0.01922516
    },
    {
      "OrderType": "LimitOffer",
      "Price": 146116.4,
      "Volume": 0.015
    },
    {
      "OrderType": "LimitOffer",
      "Price": 146194.74,
      "Volume": 0.25288524
    },
    {
      "OrderType": "LimitOffer",
      "Price": 146243.67,
      "Volume": 0.01737074
    },
    {
      "OrderType": "LimitOffer",
      "Price": 146258.9,
      "Volume": 0.01917726
    },
    {
      "OrderType": "LimitOffer",
      "Price": 146544.49,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 146591.36,
      "Volume": 0.0578
    },
    {
      "OrderType": "LimitOffer",
      "Price": 146616.4,
      "Volume": 0.01913
    },
    {
      "OrderType": "LimitOffer",
      "Price": 146893.54,
      "Volume": 0.00028716
    },
    {
      "OrderType": "LimitOffer",
      "Price": 146894.24,
      "Volume": 0.41607703
    },
    {
      "OrderType": "LimitOffer",
      "Price": 146970.93,
      "Volume": 0.01908336
    },
    {
      "OrderType": "LimitOffer",
      "Price": 147049.53,
      "Volume": 0.0125
    },
    {
      "OrderType": "LimitOffer",
      "Price": 147091.49,
      "Volume": 0.01419557
    },
    {
      "OrderType": "LimitOffer",
      "Price": 147322.51,
      "Volume": 0.01903734
    },
    {
      "OrderType": "LimitOffer",
      "Price": 147589.89,
      "Volume": 0.03
    },
    {
      "OrderType": "LimitOffer",
      "Price": 147593.74,
      "Volume": 0.25
    },
    {
      "OrderType": "LimitOffer",
      "Price": 148280.74,
      "Volume": 0.04
    },
    {
      "OrderType": "LimitOffer",
      "Price": 148293.23,
      "Volume": 0.3
    },
    {
      "OrderType": "LimitOffer",
      "Price": 148573.03,
      "Volume": 0.03325439
    },
    {
      "OrderType": "LimitOffer",
      "Price": 148992.73,
      "Volume": 0.25
    },
    {
      "OrderType": "LimitOffer",
      "Price": 149160,
      "Volume": 0.11672953
    },
    {
      "OrderType": "LimitOffer",
      "Price": 149215.27,
      "Volume": 0.0006273
    },
    {
      "OrderType": "LimitOffer",
      "Price": 149359.62,
      "Volume": 0.005
    },
    {
      "OrderType": "LimitOffer",
      "Price": 149412.43,
      "Volume": 0.002
    },
    {
      "OrderType": "LimitOffer",
      "Price": 149693.83,
      "Volume": 0.2
    },
    {
      "OrderType": "LimitOffer",
      "Price": 150041.28,
      "Volume": 0.00032799
    },
    {
      "OrderType": "LimitOffer",
      "Price": 150391.72,
      "Volume": 0.31944797
    },
    {
      "OrderType": "LimitOffer",
      "Price": 150605.07,
      "Volume": 0.0033
    },
    {
      "OrderType": "LimitOffer",
      "Price": 151091.22,
      "Volume": 0.25
    },
    {
      "OrderType": "LimitOffer",
      "Price": 151644.69,
      "Volume": 0.59438888
    },
    {
      "OrderType": "LimitOffer",
      "Price": 151790.72,
      "Volume": 0.35
    },
    {
      "OrderType": "LimitOffer",
      "Price": 151862.55,
      "Volume": 0.00054998
    },
    {
      "OrderType": "LimitOffer",
      "Price": 152070.51,
      "Volume": 0.03
    },
    {
      "OrderType": "LimitOffer",
      "Price": 152490.21,
      "Volume": 0.25
    },
    {
      "OrderType": "LimitOffer",
      "Price": 153111.36,
      "Volume": 0.015
    },
    {
      "OrderType": "LimitOffer",
      "Price": 153189.71,
      "Volume": 0.25
    },
    {
      "OrderType": "LimitOffer",
      "Price": 153767.84,
      "Volume": 2.009e-05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 153784.28,
      "Volume": 0.25
    },
    {
      "OrderType": "LimitOffer",
      "Price": 153887.81,
      "Volume": 0.00031979
    },
    {
      "OrderType": "LimitOffer",
      "Price": 153889.2,
      "Volume": 0.16
    },
    {
      "OrderType": "LimitOffer",
      "Price": 153889.55,
      "Volume": 0.00501253
    },
    {
      "OrderType": "LimitOffer",
      "Price": 154247.73,
      "Volume": 0.2
    },
    {
      "OrderType": "LimitOffer",
      "Price": 155637.95,
      "Volume": 0.002
    },
    {
      "OrderType": "LimitOffer",
      "Price": 155959.53,
      "Volume": 8.033e-05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 157010.52,
      "Volume": 2.1954578
    },
    {
      "OrderType": "LimitOffer",
      "Price": 157036.24,
      "Volume": 0.00031338
    },
    {
      "OrderType": "LimitOffer",
      "Price": 157036.94,
      "Volume": 0.2
    },
    {
      "OrderType": "LimitOffer",
      "Price": 157386.69,
      "Volume": 0.0781111
    },
    {
      "OrderType": "LimitOffer",
      "Price": 159485.18,
      "Volume": 0.10374871
    },
    {
      "OrderType": "LimitOffer",
      "Price": 160353.95,
      "Volume": 0.04464538
    },
    {
      "OrderType": "LimitOffer",
      "Price": 160881.37,
      "Volume": 0.00032774
    },
    {
      "OrderType": "LimitOffer",
      "Price": 160884.17,
      "Volume": 0.11039608
    },
    {
      "OrderType": "LimitOffer",
      "Price": 162066.32,
      "Volume": 0.03
    },
    {
      "OrderType": "LimitOffer",
      "Price": 162283.16,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 163397.14,
      "Volume": 5.138e-05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 163787.08,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 163992.73,
      "Volume": 0.035
    },
    {
      "OrderType": "LimitOffer",
      "Price": 164381.65,
      "Volume": 0.11932406
    },
    {
      "OrderType": "LimitOffer",
      "Price": 165288.9,
      "Volume": 0.054
    },
    {
      "OrderType": "LimitOffer",
      "Price": 166826.78,
      "Volume": 0.02267265
    },
    {
      "OrderType": "LimitOffer",
      "Price": 167022.58,
      "Volume": 0.00050324
    },
    {
      "OrderType": "LimitOffer",
      "Price": 167102.69,
      "Volume": 0.00843589
    },
    {
      "OrderType": "LimitOffer",
      "Price": 167179.64,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 167879.13,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 169186.49,
      "Volume": 0.03
    },
    {
      "OrderType": "LimitOffer",
      "Price": 169757.06,
      "Volume": 0.00082826
    },
    {
      "OrderType": "LimitOffer",
      "Price": 171376.61,
      "Volume": 0.12
    },
    {
      "OrderType": "LimitOffer",
      "Price": 172076.11,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 173475.1,
      "Volume": 0.02142544
    },
    {
      "OrderType": "LimitOffer",
      "Price": 174096.87,
      "Volume": 0.00186318
    },
    {
      "OrderType": "LimitOffer",
      "Price": 174101.51,
      "Volume": 0.000673
    },
    {
      "OrderType": "LimitOffer",
      "Price": 174174.6,
      "Volume": 0.00470318
    },
    {
      "OrderType": "LimitOffer",
      "Price": 174489.37,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 174524.35,
      "Volume": 0.08056314
    },
    {
      "OrderType": "LimitOffer",
      "Price": 174856.61,
      "Volume": 0.03
    },
    {
      "OrderType": "LimitOffer",
      "Price": 174874.1,
      "Volume": 0.87007966
    },
    {
      "OrderType": "LimitOffer",
      "Price": 175618.28,
      "Volume": 0.00016431
    },
    {
      "OrderType": "LimitOffer",
      "Price": 175752.87,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 176768.71,
      "Volume": 0.00042778
    },
    {
      "OrderType": "LimitOffer",
      "Price": 177982.66,
      "Volume": 0.035
    },
    {
      "OrderType": "LimitOffer",
      "Price": 180000,
      "Volume": 0.0212
    },
    {
      "OrderType": "LimitOffer",
      "Price": 181131.09,
      "Volume": 0.00028819
    },
    {
      "OrderType": "LimitOffer",
      "Price": 181822.89,
      "Volume": 0.00634
    },
    {
      "OrderType": "LimitOffer",
      "Price": 183368.08,
      "Volume": 2.277e-05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 184342.79,
      "Volume": 2.831e-05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 185214.05,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 185901.97,
      "Volume": 0.00421199
    },
    {
      "OrderType": "LimitOffer",
      "Price": 186661.66,
      "Volume": 0.00201392
    },
    {
      "OrderType": "LimitOffer",
      "Price": 188487.99,
      "Volume": 0.01216907
    },
    {
      "OrderType": "LimitOffer",
      "Price": 188816.46,
      "Volume": 0.03
    },
    {
      "OrderType": "LimitOffer",
      "Price": 189563.52,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 191473.79,
      "Volume": 2.0
    },
    {
      "OrderType": "LimitOffer",
      "Price": 192361.5,
      "Volume": 0.07579608
    },
    {
      "OrderType": "LimitOffer",
      "Price": 193061,
      "Volume": 0.14775239
    },
    {
      "OrderType": "LimitOffer",
      "Price": 194339.12,
      "Volume": 0.05239678
    },
    {
      "OrderType": "LimitOffer",
      "Price": 195893.96,
      "Volume": 0.0003589
    },
    {
      "OrderType": "LimitOffer",
      "Price": 196263.15,
      "Volume": 0.5067311
    },
    {
      "OrderType": "LimitOffer",
      "Price": 196593.46,
      "Volume": 0.000359
    },
    {
      "OrderType": "LimitOffer",
      "Price": 197261.48,
      "Volume": 0.000359
    },
    {
      "OrderType": "LimitOffer",
      "Price": 197960.97,
      "Volume": 0.000358
    },
    {
      "OrderType": "LimitOffer",
      "Price": 198691.95,
      "Volume": 0.000356
    },
    {
      "OrderType": "LimitOffer",
      "Price": 199391.44,
      "Volume": 0.00035259
    },
    {
      "OrderType": "LimitOffer",
      "Price": 200000,
      "Volume": 0.03329358
    },
    {
      "OrderType": "LimitOffer",
      "Price": 200062.26,
      "Volume": 0.0003515
    },
    {
      "OrderType": "LimitOffer",
      "Price": 200790.44,
      "Volume": 0.000352
    },
    {
      "OrderType": "LimitOffer",
      "Price": 202189.43,
      "Volume": 0.00035
    },
    {
      "OrderType": "LimitOffer",
      "Price": 202853.95,
      "Volume": 0.5
    },
    {
      "OrderType": "LimitOffer",
      "Price": 203204.4,
      "Volume": 0.000349
    },
    {
      "OrderType": "LimitOffer",
      "Price": 204252.94,
      "Volume": 0.000346
    },
    {
      "OrderType": "LimitOffer",
      "Price": 204275.07,
      "Volume": 0.01509235
    },
    {
      "OrderType": "LimitOffer",
      "Price": 204987.41,
      "Volume": 0.000346
    },
    {
      "OrderType": "LimitOffer",
      "Price": 205662.43,
      "Volume": 0.000344
    },
    {
      "OrderType": "LimitOffer",
      "Price": 206354.93,
      "Volume": 0.000343
    },
    {
      "OrderType": "LimitOffer",
      "Price": 207061.42,
      "Volume": 0.00034
    },
    {
      "OrderType": "LimitOffer",
      "Price": 207751.12,
      "Volume": 0.00034
    },
    {
      "OrderType": "LimitOffer",
      "Price": 208473.7,
      "Volume": 0.00034
    },
    {
      "OrderType": "LimitOffer",
      "Price": 209079.47,
      "Volume": 0.03418959
    },
    {
      "OrderType": "LimitOffer",
      "Price": 209151.52,
      "Volume": 0.0003368
    },
    {
      "OrderType": "LimitOffer",
      "Price": 209848.91,
      "Volume": 0.66859761
    },
    {
      "OrderType": "LimitOffer",
      "Price": 209918.86,
      "Volume": 0.000335
    },
    {
      "OrderType": "LimitOffer",
      "Price": 210548.41,
      "Volume": 0.000335
    },
    {
      "OrderType": "LimitOffer",
      "Price": 211247.91,
      "Volume": 0.0003329
    },
    {
      "OrderType": "LimitOffer",
      "Price": 211947.4,
      "Volume": 0.000332
    },
    {
      "OrderType": "LimitOffer",
      "Price": 211964.21,
      "Volume": 0.05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 212646.9,
      "Volume": 0.000331
    },
    {
      "OrderType": "LimitOffer",
      "Price": 213347.1,
      "Volume": 0.00033
    },
    {
      "OrderType": "LimitOffer",
      "Price": 214045.89,
      "Volume": 0.0003289
    },
    {
      "OrderType": "LimitOffer",
      "Price": 214745.39,
      "Volume": 0.00033
    },
    {
      "OrderType": "LimitOffer",
      "Price": 215095.14,
      "Volume": 0.001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 215444.88,
      "Volume": 0.000327
    },
    {
      "OrderType": "LimitOffer",
      "Price": 216144.38,
      "Volume": 0.0003259
    },
    {
      "OrderType": "LimitOffer",
      "Price": 216843.88,
      "Volume": 0.000325
    },
    {
      "OrderType": "LimitOffer",
      "Price": 223838.84,
      "Volume": 0.000315
    },
    {
      "OrderType": "LimitOffer",
      "Price": 227336.32,
      "Volume": 0.02
    },
    {
      "OrderType": "LimitOffer",
      "Price": 229434.81,
      "Volume": 0.02916931
    },
    {
      "OrderType": "LimitOffer",
      "Price": 234331.29,
      "Volume": 1.0
    },
    {
      "OrderType": "LimitOffer",
      "Price": 237051.54,
      "Volume": 0.00151133
    },
    {
      "OrderType": "LimitOffer",
      "Price": 240937.33,
      "Volume": 0.035
    },
    {
      "OrderType": "LimitOffer",
      "Price": 244823.73,
      "Volume": 7.0
    },
    {
      "OrderType": "LimitOffer",
      "Price": 251185.58,
      "Volume": 2.835e-05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 262311.14,
      "Volume": 0.5
    },
    {
      "OrderType": "LimitOffer",
      "Price": 265808.62,
      "Volume": 0.5
    },
    {
      "OrderType": "LimitOffer",
      "Price": 268256.86,
      "Volume": 0.01039608
    },
    {
      "OrderType": "LimitOffer",
      "Price": 269306.1,
      "Volume": 1.0921961
    },
    {
      "OrderType": "LimitOffer",
      "Price": 272803.59,
      "Volume": 0.5
    },
    {
      "OrderType": "LimitOffer",
      "Price": 279796.58,
      "Volume": 0.00491017
    },
    {
      "OrderType": "LimitOffer",
      "Price": 279798.55,
      "Volume": 1.10366677
    },
    {
      "OrderType": "LimitOffer",
      "Price": 280498.05,
      "Volume": 0.5
    },
    {
      "OrderType": "LimitOffer",
      "Price": 314073.87,
      "Volume": 0.25
    },
    {
      "OrderType": "LimitOffer",
      "Price": 314773.37,
      "Volume": 0.40522689
    },
    {
      "OrderType": "LimitOffer",
      "Price": 331772.89,
      "Volume": 0.00237813
    },
    {
      "OrderType": "LimitOffer",
      "Price": 339255.74,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 349049.39,
      "Volume": 0.00017485
    },
    {
      "OrderType": "LimitOffer",
      "Price": 349748.19,
      "Volume": 1.21158629
    },
    {
      "OrderType": "LimitOffer",
      "Price": 367235.6,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 370733.08,
      "Volume": 0.001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 398712.93,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 419697.82,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 454672.64,
      "Volume": 0.01
    },
    {
      "OrderType": "LimitOffer",
      "Price": 475657.53,
      "Volume": 0.5
    },
    {
      "OrderType": "LimitOffer",
      "Price": 481000,
      "Volume": 1.517
    },
    {
      "OrderType": "LimitOffer",
      "Price": 489647.46,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 524622.28,
      "Volume": 0.10335638
    },
    {
      "OrderType": "LimitOffer",
      "Price": 529238.95,
      "Volume": 8.32e-06
    },
    {
      "OrderType": "LimitOffer",
      "Price": 544052.73,
      "Volume": 1.20062014
    },
    {
      "OrderType": "LimitOffer",
      "Price": 559597.1,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 562595.04,
      "Volume": 0.02
    },
    {
      "OrderType": "LimitOffer",
      "Price": 605064.36,
      "Volume": 0.02904697
    },
    {
      "OrderType": "LimitOffer",
      "Price": 621773.93,
      "Volume": 1e-05
    },
    {
      "OrderType": "LimitOffer",
      "Price": 629546.73,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 699495.67,
      "Volume": 0.02
    },
    {
      "OrderType": "LimitOffer",
      "Price": 699496.37,
      "Volume": 1.20072015
    },
    {
      "OrderType": "LimitOffer",
      "Price": 727476.22,
      "Volume": 0.01947322
    },
    {
      "OrderType": "LimitOffer",
      "Price": 785052.6,
      "Volume": 0.0144
    },
    {
      "OrderType": "LimitOffer",
      "Price": 786933.41,
      "Volume": 0.00494991
    },
    {
      "OrderType": "LimitOffer",
      "Price": 839395.64,
      "Volume": 0.00973661
    },
    {
      "OrderType": "LimitOffer",
      "Price": 918438.73,
      "Volume": 0.2
    },
    {
      "OrderType": "LimitOffer",
      "Price": 1049244.55,
      "Volume": 0.005
    },
    {
      "OrderType": "LimitOffer",
      "Price": 1126316.39,
      "Volume": 0.1
    },
    {
      "OrderType": "LimitOffer",
      "Price": 1224118.64,
      "Volume": 0.00127084
    },
    {
      "OrderType": "LimitOffer",
      "Price": 1398992.03,
      "Volume": 0.01
    },
    {
      "OrderType": "LimitOffer",
      "Price": 1398992.73,
      "Volume": 0.00730246
    },
    {
      "OrderType": "LimitOffer",
      "Price": 1741731.96,
      "Volume": 0.001
    },
    {
      "OrderType": "LimitOffer",
      "Price": 2098489.09,
      "Volume": 0.00150619
    },
    {
      "OrderType": "LimitOffer",
      "Price": 3497481.82,
      "Volume": 0.49820887
    },
    {
      "OrderType": "LimitOffer",
      "Price": 4196978.18,
      "Volume": 0.00796531
    },
    {
      "OrderType": "LimitOffer",
      "Price": 6044905.01,
      "Volume": 0.00166138
    },
    {
      "OrderType": "LimitOffer",
      "Price": 6994963.63,
      "Volume": 0.01396
    }
  ],
  "PrimaryCurrencyCode": "Xbt",
  "SecondaryCurrencyCode": "Usd",
  "CreatedTimestampUtc": "2026-10-08T04:42:01.3134401Z"
}
```

## Why this matches (or not)

_[0.80|heuristic] no bid/ask depth or pool liquidity structure found_
