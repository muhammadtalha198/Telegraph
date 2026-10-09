---
intent: CORPORATE_REGISTRY_LOOKUP
slug: corp-krs-pl
status: approved
captured_at: 2026-10-05T09:33:58Z
request_url: https://api-krs.ms.gov.pl/api/krs/OdpisAktualny/0000028860?rejestr=P&format=json
content_type: application/json
inputs: |
  {}
intent_description: |
  Queries national business registers for incorporation status, registered agent details, and beneficial ownership filings.
answer_requirement: |
  Must return the company's registry record (legal name, status, identifiers) for the company asked.
capture_note: |
  golden-test PASS: KRS (Poland)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response contains the requested company's registry details."
reviewed_at: 2026-10-05T12:12:18Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```text
{
  "odpis": {
    "rodzaj": "Aktualny",
    "naglowekA": {
      "rejestr": "RejP",
      "numerKRS": "0000028860",
      "dataCzasOdpisu": "05.10.2026 11:33:56",
      "stanZDnia": "17.09.2026",
      "dataRejestracjiWKRS": "19.07.2001",
      "numerOstatniegoWpisu": 220,
      "dataOstatniegoWpisu": "17.09.2026",
      "sygnaturaAktSprawyDotyczacejOstatniegoWpisu": "LD.XX NS-REJ.KRS/24604/26/528",
      "oznaczenieSaduDokonujacegoOstatniegoWpisu": "SĄD REJONOWY DLA ŁODZI ŚRÓDMIEŚCIA W ŁODZI, XX WYDZIAŁ GOSPODARCZY KRAJOWEGO REJESTRU SĄDOWEGO",
      "stanPozycji": 1
    },
    "dane": {
      "dzial1": {
        "danePodmiotu": {
          "formaPrawna": "SPÓŁKA AKCYJNA",
          "identyfikatory": {
            "regon": "61018820100000",
            "nip": "7740001454"
          },
          "nazwa": "ORLEN SPÓŁKA AKCYJNA",
          "daneOWczesniejszejRejestracji": {
            "nazwaPoprzedniegoRejestru": "RHB",
            "numerWPoprzednimRejestrze": "780",
            "sadProwadzacyRejestr": "SĄD REJONOWY W PŁOCKU"
          },
          "czyProwadziDzialalnoscZInnymiPodmiotami": false,
          "czyPosiadaStatusOPP": false
        },
        "siedzibaIAdres": {
          "siedziba": {
            "kraj": "POLSKA",
            "wojewodztwo": "MAZOWIECKIE",
            "powiat": "M. PŁOCK",
            "gmina": "M. PŁOCK",
            "miejscowosc": "PŁOCK"
          },
          "adres": {
            "ulica": "CHEMIKÓW",
            "nrDomu": "7",
            "miejscowosc": "PŁOCK",
            "kodPocztowy": "09-411",
            "poczta": "PŁOCK-BIAŁA",
            "kraj": "POLSKA"
          },
          "adresPocztyElektronicznej": "ZARZAD@ORLEN.PL",
          "adresStronyInternetowej": "WWW.ORLEN.PL",
          "adresDoDoreczenElektronicznychWpisanyDoBAE": "AE:PL-59420-30959-DSCHB-14"
        },
        "jednostkiTerenoweOddzialy": [
          {
            "nazwa": "ORLEN SPÓŁKA AKCYJNA - ODDZIAŁ CENTRALNY UPSTREAM POLSKA W WARSZAWIE",
            "siedziba": {
              "kraj": "POLSKA",
              "wojewodztwo": "MAZOWIECKIE",
              "powiat": "WARSZAWA",
              "gmina": "WARSZAWA",
              "miejscowosc": "WARSZAWA"
            },
            "adres": {
              "ulica": "UL. MARCINA KASPRZAKA",
              "nrDomu": "25",
              "miejscowosc": "WARSZAWA",
              "kodPocztowy": "01-224",
              "poczta": "WARSZAWA",
              "kraj": "POLSKA"
            }
          },
          {
            "nazwa": "ORLEN SPÓŁKA AKCYJNA - ODDZIAŁ UPSTREAM POLSKA W SANOKU",
            "siedziba": {
              "kraj": "POLSKA",
              "wojewodztwo": "PODKARPACKIE",
              "powiat": "SANOCKI",
              "gmina": "SANOK",
              "miejscowosc": "SANOK"
            },
            "adres": {
              "ulica": "UL. HENRYKA SIENKIEWICZA",
              "nrDomu": "12",
              "miejscowosc": "SANOK",
              "kodPocztowy": "38-500",
              "poczta": "SANOK",
              "kraj": "POLSKA"
            }
          },
          {
            "nazwa": "ORLEN SPÓŁKA AKCYJNA - ODDZIAŁ UPSTREAM POLSKA W ZIELONEJ GÓRZE",
            "siedziba": {
              "kraj": "POLSKA",
              "wojewodztwo": "LUBUSKIE",
              "powiat": "ZIELONA GÓRA",
              "gmina": "ZIELONA GÓRA",
              "miejscowosc": "ZIELONA GÓRA"
            },
            "adres": {
              "ulica": "UL. BOHATERÓW WESTERPLATTE",
              "nrDomu": "15",
              "miejscowosc": "ZIELONA GÓRA",
              "kodPocztowy": "65-034",
              "poczta": "ZIELONA GÓRA",
              "kraj": "POLSKA"
            }
          },
          {
            "nazwa": "ORLEN SPÓŁKA AKCYJNA - POLSKIE GÓRNICTWO NAFTOWE I GAZOWNICTWO ODDZIAŁ OPERATORSKI W PAKISTANIE",
            "siedziba": {
              "kraj": "PAKISTAN",
              "miejscowosc": "ISLAMABAD"
            },
            "adres": {
              "ulica": "6TH FLOOR, UFONE TOWER BUILDING, JINNAH AVENUE BLUE AREA",
              "miejscowosc": "ISLAMABAD",
              "kodPocztowy": "44000",
              "poczta": "ISLAMABAD",
              "kraj": "PAKISTAN"
            }
          },
          {
            "nazwa": "ORLEN SPÓŁKA AKCYJNA - ODDZIAŁ UPSTREAM POLSKA W ODOLANOWIE",
            "siedziba": {
              "kraj": "POLSKA",
              "wojewodztwo": "WIELKOPOLSKIE",
              "powiat": "OSTROWSKI",
              "gmina": "ODOLANÓW",
              "miejscowosc": "ODOLANÓW"
            },
            "adres": {
              "ulica": "UL. KROTOSZYŃSKA",
              "nrDomu": "148",
              "miejscowosc": "ODOLANÓW",
              "kodPocztowy": "63-430",
              "poczta": "ODOLANÓW",
              "kraj": "POLSKA"
            }
          },
          {
            "nazwa": "ORLEN SPÓŁKA AKCYJNA - ODDZIAŁ LABORATORIUM POMIAROWO-BADAWCZE PGNIG W WARSZAWIE",
            "siedziba": {
              "kraj": "POLSKA",
              "wojewodztwo": "MAZOWIECKIE",
              "powiat": "WARSZAWA",
              "gmina": "WARSZAWA",
              "miejscowosc": "WARSZAWA"
            },
            "adres": {
              "ulica": "UL. MARCINA KASPRZAKA",
              "nrDomu": "25",
              "miejscowosc": "WARSZAWA",
              "kodPocztowy": "01-224",
              "poczta": "WARSZAWA",
              "kraj": "POLSKA"
            }
          },
          {
            "nazwa": "ORLEN SPÓŁKA AKCYJNA - ODDZIAŁ RATOWNICZA STACJA GÓRNICTWA OTWOROWEGO UPSTREAM POLSKA W KRAKOWIE",
            "siedziba": {
              "kraj": "POLSKA",
              "wojewodztwo": "MAŁOPOLSKIE",
              "powiat": "KRAKÓW",
              "gmina": "KRAKÓW",
              "miejscowosc": "KRAKÓW"
            },
            "adres": {
              "ulica": "UL. IGNACEGO ŁUKASIEWICZA",
              "nrDomu": "3",
              "miejscowosc": "KRAKÓW",
              "kodPocztowy": "31-429",
              "poczta": "KRAKÓW",
              "kraj": "POLSKA"
            }
          },
          {
            "nazwa": "ORLEN SPÓŁKA AKCYJNA - ODDZIAŁ OBROTU HURTOWEGO UPSTREAM POLSKA W WARSZAWIE",
            "siedziba": {
              "kraj": "POLSKA",
              "wojewodztwo": "MAZOWIECKIE",
              "powiat": "WARSZAWA",
              "gmina": "WARSZAWA",
              "miejscowosc": "WARSZAWA"
            },
            "adres": {
              "ulica": "UL. MARCINA KASPRZAKA",
              "nrDomu": "25A",
              "miejscowosc": "WARSZAWA",
              "kodPocztowy": "01-224",
              "poczta": "WARSZAWA",
              "kraj": "POLSKA"
            }
          },
          {
            "nazwa": "ORLEN SPÓŁKA AKCYJNA - POLSKIE GÓRNICTWO NAFTOWE I GAZOWNICTWO ODDZIAŁ W RAS AL. KHAIMAH W ZJEDNOCZONYCH EMIRATACH ARABSKICH",
            "siedziba": {
              "kraj": "ZJEDNOCZONE EMIRATY ARABSKIE",
              "miejscowosc": "RAS AL. KHAIMAH"
            },
            "adres": {
              "ulica": "AL. HISN STREET JULFAR OFFICE TOWER",
              "nrDomu": "1711",
              "miejscowosc": "RAS AL. KHAIMAH",
              "poczta": "RAS AL. KHAIMAH",
              "kraj": "ZJEDNOCZONE EMIRATY ARABSKIE"
            }
          }
        ],
        "umowaStatut": {
          "informacjaOZawarciuZmianieUmowyStatutu": [
            {
              "zawarcieZmianaUmowyStatutu": "1) 29.06.1993R. KANCELARIA NOTARIALNA PAWŁA BŁASZCZAKA REP A NR 6377/93\n2) 14.05.2001R. KANCELARIA NOTARIALNA SPÓŁKA CYWILNA DOROTA RYNKIEWICZ-NOTARIUSZ, MAŁGORZATA BRYLEWSKA-IWAŃCZYK-NOTARIUSZ; AKT SPORZĄDZONY PRZED NOTARIUSZEM DOROTĄ RYNKIEWICZ REP A NR 2422/2001 ZMIANA PAR.7 PKT 7 STATUTU\n3) 14.05.2001R. KANCELARIA NOTRIALNA SPÓŁKA CYWILNA DOROTA RYNKIEWICZ-NOTARIUSZ, MAŁGORZATA BRYLEWSKA-IWAŃCZYK-NOTARIUSZ; AKT SPORZĄDZONY PRZED NOTARIUSZEM DOROTĄ RYNKIEWICZ REP A NR 2433/2001 TEKST JEDNOLITY STATUTU SPÓŁKI"
            },
            {
              "zawarcieZmianaUmowyStatutu": "11.07.2001R. SPORZĄDZENIE AKTU NOTARIALNEGO ZAWIERAJĄCEGO UCHWAŁY NADZWYCZAJNEGO WALNEGO ZGROMADZENIA AKCJONARIUSZY Z DN. 06.07.2001R. KANCELARIA NOTARIALNA SPÓŁKA CYWILNA BARBARA MACUGA-NOTARIUSZ HANNA BANUCHA-NOTARIUSZ; AKT SPORZĄDZONY PRZED NOTARIUSZEM HANNĄ BANUCHĄ REP. A NR 5536/2001\nZMIANA W PAR.7 UST.7 PKT 8; DODANIE W PAR.8 UST.11 PKT 13; DODANIE W PAR.8 UST.11 PKT 14; ZMIANA W PAR.9 UST.7 ORAZ TEKST JEDNOLITY STATUTU"
            },
            {
              "zawarcieZmianaUmowyStatutu": "04.07.2002 R. AKT SPORZĄDZIŁ NOTARIUSZ W WARSZAWIE, ELŻBIETA BAREJ-MAGIERA W SWOJEJ KANCELARII PRZY UL. BONIFRATERSKIEJ 6 LOKAL NR 17; REPERTORIUM A NR 3561/2002 - STATUT\nZMIANY NASTĘPUJĄCYCH PARAGRAFÓW: PAR. 3 - ZMIANA TYTUŁU; PAR.3 UST.1; PAR.3 UST.3; PAR.4; PAR.5 UST.1; PAR.5 UST.2; PAR.7 UST.1, PAR.7 UST.2, PAR.7 UST.4; PAR.7 UST.7 PKT 2; PAR.7 UST.7 PKT 4; PAR.7 UST.7 PKT 5; PAR.7 UST.7 PKT 12; PAR.7 UST.8; PAR.7 UST.9; PAR.7 UST.12; PAR.8 UST.6; PAR.8 UST.7; PAR.8 UST.11 PKT 2; PAR.8 UST.11 PKT 6; PAR.8 UST.11 PKT 9; PAR.8 UST.12 PKT 4; PAR.8 UST.12 PKT 5; PAR.8 UST.12 PKT 6; PAR.8 UST.12 PKT 7; PAR.8 UST.13\n04.07.2002 R. AKT NOTARIALNY SPORZĄDZONY PRZEZ NOTARIUSZA W WARSZAWIE, ELŻBIETĘ BAREJ-MAGIERA W KANCELARII NOTARIALNEJ PRZY ULICY BONIFRATERSKIEJ 6 LOKAL 17; REPERTORIUM A 3561/2002; TEKST JEDNOLITY STATUTU."
            },
            {
              "zawarcieZmianaUmowyStatutu": "AKT NOTARIALNY SPORZĄDZONY W DNIU 24.04.2003R. PRZEZ NOTARIUSZA ELŻBIETĘ BAREJ-MAGIERĘ, W KANCELARII NOTARIALNEJ W WARSZAWIE PRZY UL.BONIFRATERSKIEJ 6 LOKAL 17, REPERTORIUM A NR 1851/2003 - ZMIENIONO: PAR.2 UST.2; PAR.3 UST.3; PAR.8 UST.9; PAR.8 UST.12A; PAR.9 UST.2; PAR.9 UST.3 STATUTU SPÓŁKI ORAZ PRZYJĘTO TEKST JEDNOLITY STATUTU"
            },
            {
              "zawarcieZmianaUmowyStatutu": "AKT NOTARIALNY Z DN. 08.04.204R., REP. A NR 4351/2004, NOTARIUSZ MAREK BARTNICKI PROWADZĄCY KANCELARIĘ NOTARIALNĄ MAREK BARTNICKI-NOTARIUSZ, MAGDALENA PRONIEWICZ-NOTARIUSZ, SŁAWOMIR STROJNY-NOTARIUSZ, SPÓŁKA CYWILNA, PRZY ULICY GAŁCZYŃSKIEGO 4, 00-362 WARSZAWA\nNUMERY ZMIENIONYCH PARAGRAFÓW: PAR.2 UST.2, PAR.3 UST.1, PAR.7 UST.7 PKT 8, PAR.8 UST.3, PAR.8 UST.7, PAR.9 UST.5\nNUMER DODANEGO USTĘPU: PAR.7 UST.7A"
            },
            {
              "zawarcieZmianaUmowyStatutu": "AKT NOTARIALNY Z DN. 28 CZERWCA 2004R., REPERTORIUM A NR 8172/2004, NOTARIUSZ MAREK BARTNICKI PROWADZĄCY KANCELARIĘ NOTARIALNĄ MAREK BARTNICKI-NOTARIUSZ, MAGDALENA PRONIEWICZ-NOTARIUSZ, SŁAWOMIR STROJNY-NOTARIUSZ, SPÓŁKA CYWILNA, PRZY UL.GAŁCZYŃSKIEGO 4, 00-362 WARSZAWA\nNUMERY ZMIENIONYCH PARAGRAFÓW: PAR.8 UST.11 PKT 13, PAR.8 UST.11 PKT 14, PAR.9 UST.7 PKT 2, PAR.9 UST.7 PKT 3\nNUMERY DODANYCH POSTANOWIEŃ: PAR.8 UST.3 PKT 3\nNUMERY WYKREŚLONYCH POSTANOWIEŃ: PAR.9 UST.7 PKT 4"
            },
            {
              "zawarcieZmianaUmowyStatutu": "AKT NOTARIALNY SPORZĄDZONY W DNIU 29 CZERWCA 2005 R. PRZEZ KRZYSZTOFA NURKOWSKIEGO Z KANCELARII NOTARIALNEJ KRZYSZTOF NURKOWSKI NOTARIUSZ W WARSZAWIE Z SIEDZIBĄ PRZY ULICY DOMANIEWSKIEJ 41, WARSZAWA, REP.A NR 7066/2005;\nWYKREŚLONO PAR.2 UST.5; W PAR.7 DODANO UST. 9A; W PAR.8 DODANO UST.9A; ZMIENIONO  PAR.8 UST.11 PKT 10; ZMIENIONO PAR.8 UST.11 PKT 11; ZMIENIONO PAR.8 UST.11 PKT 12; W PAR.8 UST.12 DODANO PKT 8; ZMIENIONO PAR.9 UST.1 PKT 1; W PAR.9 DODANO UST.7 A; ZMIENIONO PAR.9 UST.9"
            },
            {
              "zawarcieZmianaUmowyStatutu": "27.06.2006R., REPERTORIUM A 13974/2006, KANCELARIA NOTARIALNA KRZYSZTOF NURKOWSKI NOTARIUSZ W WARSZAWIE, UL.DOMANIEWSKA 41, 02-672 WARSZAWA, ZMIANY STATUTU SPÓŁKI: PAR.2 UST.2 PKT.18, PAR.2 UST.2 PKT.19, PAR.8 UST.5, PAR.8 UST.9A, PAR.8 UST.12 PKT.4 LIT.A,; DODANO: PAR.2 UST.2 PKT.27, PAR.2 UST.2 PKT.28, PAR.2 UST.2 PKT.29, PAR.9A."
            },
            {
              "zawarcieZmianaUmowyStatutu": "PROTOKÓŁ ZWYCZAJNEGO WALNEGO ZGROMADZENIA PKN ORLEN S.A. Z DNIA 15.07.2009R. REPERTORIUM A NR 11147/2009\nKANCELARIA NOTARIALNA MAREK BARTNICKI-NOTARIUSZ, MAGDALENA PRONIEWICZ-NOTARIUSZ, SŁAWOMIR SRTOJNY-NOTARIUSZ, WIKTOR WĄGROWSKI-NOTARIUSZ S.C.\nZMIANY STAT. 1) W PAR.1 STATUTU DODANO UST.4, 2)ZMIANIE ULEGŁ PAR.2 UST.2 STAT., 3) ZMIENIE ULEGŁ PAR.2 UST.4 STAT.,4) ZMIANIE ULEGŁ PAR.4 STAT., 5) ZMIANIE ULEGŁ PAR.7 UST.4 STAT.,6) ZMIANIE ULEGŁ PAR.7 UST.5 STAT.,7) ZMIANIE ULEGŁ PAR.7 UST.6 STAT., 8)ZMIANIE ULEGŁ PAR.7 UST.7 PKT 1 STAT.,9) ZMIANIE ULEGŁ PAR.7 UST.7 PKT 4 STAT.,10) ZMIANIE ULEGŁ PAR.7 UST.7 PKT 11 STAT.,11) ZMIANIE ULEGŁ PAR.7 UST.7 PKT 12 STAT.,12) W TREŚCI PAR.7 UST.7 STAT. DODANO PKT 14,13) ZMIANIE ULEGŁ PAR.7 UST.12 STATUTU,14) DOTYCHCZASOWA TREŚĆ PAR.7 UST.11 STATUTU ZOSTAŁA OZNACZONA JAKO PAR.7 UST.11 PKT 1,15) W TREŚCI PAR.7 UST.11 STATUTU DODANO PKT 2,16) W TRESCI PAR.7 UST.11 STATUTU DODANO PKT.3,17) W TREŚCI PAR.7 UST.11 STATUTU DODANO PKT 4,18) W TRE SCI PAR.7 UST.11 STATUTU DODANO PKT 5,19) W TREŚCI PAR.7 UST. 11 STATUTU DODANO PKT 6,20) W TREŚCI PAR.7 UST. 11 STATUTU DODANO PKT 7, 21) ZMIENIONO TREŚĆ PAR.8 UST.3 PKT 1 STATUTU,22) WYKREŚLONY ZOSTAŁ PAR.8 UST.3 PKT 3 STATUTU,23) ZMIENIONY ZOSTAŁ PAR.9 UST.3 PKT 1 STATUTU,24) ZMIENIONY ZOSTAŁ PAR.8UST.5 STATUTU,25) ZMIENIONY ZOSTAŁ PAR.8 UST.9A STATUTU,26)ZMIENIONY ZOSTAŁ PAR.8 UST.11 PKT 6 STATUTU,27) W TREŚCI PAR.8 UST.11 STATUTU PO PKT 6 DODANY ZOSTAŁ PKT 6A,28) W TREŚCI PAR.8 UST.11 STATUTU DODANY ZOSTAŁ PKT 15,29) W TREŚCI PAR.8 UST.11 STATUTUDODANY ZOSTAŁ PKT 16,30) ZMIENIONY ZOSTAŁ PAR.8 UST.12 PKT 4 STATUTU, 31) ZMIENIONY ZOSTAŁ PAR.8 UST.12 PKT 6 STATUTU,32) ZMIENIONY ZOSTAŁ PAR.8 UST.12 PKT 7 STATUTU,33) WYKREŚLONY ZOSTAŁ PAR.8 UST.13 PKT 1 STATUTU,34) W TREŚCI PAR.9 UST.1 PKT 3 STATUTU ZOSTAŁO WYKREŚLONE ZDANIE DRUGIE,35) ZMIENIONY ZOSTAŁ PAR. 9 UST.3 PKT 3 STATUTU,36) ZMIENIONY ZOSTAŁ PAR.9 UST.4 STATUTU,37) ZMIENIONY ZOSTAŁ PAR.9 UST.10 STATUTU,38) WYKREŚLONY ZOSTAŁ PAR.11"
            },
            {
              "zawarcieZmianaUmowyStatutu": "PROTOKÓŁ ZWYCZAJNEGO WALNEGO ZGROMADZENIA PKN ORLEN S.A. - SPORZĄDZONY DNIA 25.06.2010R., REPERTORIUM A NR 10466/2010 PRZEZ NOTARIUSZA MARKA BARTNICKIEGO, KANCELARIA NOTARIALNA MAREK BARTNICKI, MAGDALENA PRONIEWICZ, SŁAWOMIR STROJNY, WIKTOR WAGRODZKI SPÓŁKA CYWILNA, 00-362 WARSZAWA, UL. GAŁCZŃSKIEGO 4;\nZMIANY STATUTU:\n1) W PAR.2 UST.2 STATUTU DODANO PUNKTY 66 ORAZ 67\n2) ZMIANIE ULEGŁ PAR.8 UST.11 PKT 5 STATUTU."
            },
            {
              "zawarcieZmianaUmowyStatutu": "PROTOKÓŁ SPORZĄDZONY DNIA 29.06.2011R., REPERTORIUM A NR 11382/2011 PRZEZ NOTARIUSZA W WARSZAWIE MARKA BARTNICKIEGO, PROWADZĄCEGO KANCELARIE NOTARIALNĄ PRZY UL. GAŁCZYNSKIEGO NR 4, ZMIANA STATUTU:PAR.1 UST.4, PAR.7 UST.11 PKT 1, PAR.7 UST.11 PKT 6"
            },
            {
              "zawarcieZmianaUmowyStatutu": "30.05.2012R., REPERTORIUM A NR 9142/2012, NOTARIUSZ MAREK BARTNICKI W WARSZAWIE, PAR.9A STATUTU (SKREŚLONO)"
            },
            {
              "zawarcieZmianaUmowyStatutu": "AKT NOTARIALNY Z DNIA 27.06.2013R., REP. A NR 10519/2013, NOTARIUSZ MAREK BARTNICKI, KANCELARIA NOTARIALNA W WARSZAWIE, ZMIENIONO PAR. 8 UST. 11 PKT 5 STATUTU SPÓŁKI"
            },
            {
              "zawarcieZmianaUmowyStatutu": "28.04.2015 R., REP. A NR 5599/2015, NOTARIUSZ MAREK BARTNICKI, KANCELARIA NOTARIALNA W WARSZAWIE.\nZMIANA § 1 UST. 4, § 8 UST. 12 PKT 4 LIT.A,§ 2 USTT. 2, § 2 UST. 2 PKT 1 STATUTU."
            },
            {
              "zawarcieZmianaUmowyStatutu": "02.02.2018 R., REPERTORIUM A NR 1641/2018, NOTARIUSZ MAREK BARTNICKI, KANCLARIA NOTARIALNA W WARSZAWIE - PAR. 2 UST. 2 DODANO PUNKTY OD 71 DO 88 STATUTU"
            },
            {
              "zawarcieZmianaUmowyStatutu": "03.07.2018 R., REP. A NR 2604/2018, NOTARIUSZ ANETA SZKUTNIK, KANCELARIA NOTARIALNA W WARSZAWIE.\nZMIANA § 8 UST. 7 PKT 1, § 9 UST. 6.\nDODANO § 9 UST. 5 PKT 4."
            },
            {
              "zawarcieZmianaUmowyStatutu": "14.06.2019 R., REP. A NR 1620/2019,  NOTARIUSZ MICHAŁ ŁUKASZEWICZ, KANCELARIA NOTARIALNA W WARSZAWIE.\nZMIENIONO: § 8 UST.1, § 8 UST.2, § 8 UST.11, § 8 UST.12, § 8 UST.13, § 9 UST.1, § 10;\nDODANO: W § 8 UST.9 DODANO PKT 5, W § 9 DODANO UST.11, § 11, § 12;"
            },
            {
              "zawarcieZmianaUmowyStatutu": "05.06.2020R. REPERTORIUM A NR 13660/2019, MICHAŁ ŁUKASZEWICZ NOTARIUSZ, KANCELARIA NOTARIALNA W WARSZAWIE ZMIENIONO § 1 UST 4 , § 7 UST. 7 PKT. 6A, ZMIENIONO § 8 UST. 9A, DODANO W § 8 UST. 12 PKT. 6A"
            },
            {
              "zawarcieZmianaUmowyStatutu": "27.05.2021 R. REPERTORIUM A NR 2441/2021, NOTARIUSZ MICHAŁ ŁUKASZEWICZ, KANCELARIA NOTARIALNA W WARSZAWIE - ZMIENIONO § 2 ORAZ § 9 UST. 1 PKT 3 STATUTU."
            },
            {
              "zawarcieZmianaUmowyStatutu": "AKT NOT. Z DNIA 21.07.2022 R., REPERTORIUM A NR 4538/2022, NOTARIUSZ MICHAŁ ŁUKASZEWICZ, KANCELARIA NOTARIALNA W WARSZAWIE - ZMIENIONO § 3 UST. 1, § 8 UST. 1 ORAZ § 9 UST. 1 STATUTU."
            },
            {
              "zawarcieZmianaUmowyStatutu": "AKT NOTARIALNY Z DNIA 28.09.2022 R., REPERTORIUM A NR 6531/2022, NOTARIUSZ MICHAŁ ŁUKASZEWICZ, KANCELARIA NOTARIALNA W WARSZAWIE - ZMIENIONO:  § 3 UST. 1, § 7 UST. 4 PKT 1 I 3, § 7 UST. 9, § 8 UST. 12 PKT 8; DODANO: W § 2 UST. 2 DODANO PKT. 90)-151) ORAZ DODANO UST. 5 I 6,  W § 7 UST. 7 DODANO PKT 15, W § 8 UST. 11 DODANO PKT. 20 I 21, W § 9 UST. 7 DODANO PKT 4 ORAZ DODANO UST. 12, 13 I 14 STATUTU."
            },
            {
              "zawarcieZmianaUmowyStatutu": "22.03.2023 R., REPERTORIUM A NR 1848/2023, NOTARIUSZ MICHAŁ ŁUKASZEWICZ, KANCELARIA NOTARIALNA W WARSZAWIE - ZMIENIONO: § 1 UST. 4, § 7 UST. 7 PKT 14, § 7 UST. 9 PKT 1, § 8 UST. 4, § 8 UST. 6, § 8 UST. 7 PKT 1, § 8 UST. 9 PKT 2, § 8 UST. 9 PKT 3, § 8 UST. 11 PKT 6, § 8 UST. 11 PKT 13, § 8 UST. 12 PKT 5, § 8 UST. 12 PKT 6 LIT. A), § 9 UST. 7 PKT 2 STATUTU; W § 8 UST. 11 DOTYCHCZASOWY PKT 6A OTRZYMAŁ NOWĄ NUMERACJĘ 6B; DODANO: W § 2 W UST. 2 DODANO PUNKTY 152 I 153, W § 7 UST. 7 DODANO PKT 16, W § 8 DODANO UST. 8A, W § 8 UST. 11 DODANO NOWY PKT 6A, W § 9 DODANO UST. 11A."
            },
            {
              "zawarcieZmianaUmowyStatutu": "21.06.2023 R., REPERTORIUM A NR 3683/2023, NOTARIUSZ MICHAŁ ŁUKASZEWICZ, KANCELARIA NOTARIALNA W WARSZAWIE - ZMIENIONO: § 1 UST. 3 ORAZ § 1 UST. 4 STATUTU."
            },
            {
              "zawarcieZmianaUmowyStatutu": "02.12.2024 R., REP. A NR 15642/2024, NOTARIUSZ MAREK BARTNICKI, KANCELARIA NOTARIALNA W WARSZAWIE - ZMIENIONO: § 8 UST. 11 PKT 5 STATUTU."
            },
            {
              "zawarcieZmianaUmowyStatutu": "28 PAŹDZIERNIKA 2025 ROKU; REP. A NR 5806/2025; NOTARIUSZ JANUSZ RUDNICKI; KANCELARIA NOTARIALNA W WARSZAWIE; ZMIENIONO:\n- § 1 UST. 4 STATUTU\n- § 8 UST. 11 PKT 5 STATUTU;\n- § 8 UST. 12 PKT 6 LIT. A) STATUTU;"
            },
            {
              "zawarcieZmianaUmowyStatutu": "09 CZERWCA 2026 ROKU; REP. A NR 2681/2026; NOTARIUSZ JANUSZ RUDNICKI; KANCELARIA NOTARIALNA W WARSZAWIE; ZMIENIONO:\n- § 2 UST. 2 STATUTU"
            }
          ]
        },
        "pozostaleInformacje": {
          "czasNaJakiUtworzonyZostalPodmiot": "NIEOZNACZONY",
          "czyUmowaStatutPrzyznajeUprawnieniaOsobiste": true,
          "czyObligatoriuszeMajaPrawoDoUdzialuWZysku": false
        },
        "sposobPowstaniaPodmiotu": {
          "okolicznosciPowstania": "POŁĄCZENIE",
          "opisSposobuPowstaniaInformacjaOUchwale": "UCHWAŁĄ NR 8/99 ZWYCZAJNEGO WALNEGO ZGROMADZENIA AKCJONARIUSZY \"PETROCHEMII PŁOCK\" SPÓŁKI AKCYJNEJ Z DNIA 19 MAJA 1999R. POŁĄCZONO SPÓŁKĘ MAZOWIECKIE ZAKŁADY RAFINERYJNE I PETROCHEMICZNE \"PETROCHEMIA PŁOCK\" SPÓŁKA AKCYJNA W PŁOCKU (SPÓŁKA PRZEJMUJĄCA) ZE SPÓŁKĄ CENTRALNA PRODUKTÓW NAFTOWYCH \"CPN\" SPÓŁKA AKCYJNA W WARSZAWIE (SPÓŁKA PRZEJĘTA)",
          "nrDataDecyzjiPrezesaUOKiK": "NIE PODLEGA OBOWIĄZKOWI ZGŁOSZENIA DO URZĘDU OCHRONY KONKURENCJI I KONSUMENTÓW.",
          "podmioty": [
            {
              "nazwa": "MAZOWIECKIE ZAKŁADY RAFINERYJNE I PETROCHEMICZNE \"PETROCHEMIA PŁOCK\" SP
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response contains the requested company's registry details._
