---
intent: URL_CONTENT_EXTRACTION
slug: extract-jina-reader
status: pending_review
captured_at: 2026-10-05T09:34:50Z
request_url: https://r.jina.ai/https://example.com
content_type: application/json
inputs: |
  {"url": "https://example.com", "urle": "https%3A%2F%2Fexample.com"}
intent_description: |
  Scrapes target web pages, cleans boilerplate DOM nodes, and extracts clean markdown article content.
answer_requirement: |
  Must return the cleaned main content of the target web page.
capture_note: |
  golden-test PASS: Jina Reader
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```text
Title: Example Domain

URL Source: https://example.com/

Published Time: Fri, 02 Oct 2026 16:11:02 GMT

Markdown Content:
This domain is for use in documentation examples without needing permission. This is not a service; avoid relying on it for testing and monitoring purposes.

هذا النطاق مُخصص للاستخدام في أمثلة التوثيق دون الحاجة إلى إذن. هذه ليست خدمة، يُرجى تجنب الاعتماد عليها لأغراض الاختبار والمراقبة.

该域名仅用于文档示例，无需获得许可。这并非一项服务，请勿将其用于测试和监控目的。

L’usage de ce domaine est réservé à des exemples de documentation, sans autorisation préalable. Il ne s’agit pas d’un service ; son utilisation à des fins de test ou de surveillance est à éviter.

Данный домен предназначен для использования в примерах документации без необходимости получения предварительного разрешения. Это не сервис; не рекомендуется его использование для тестирования и мониторинга.

Este dominio está destinado al uso en ejemplos de documentación sin necesidad de permiso. Esto no es un servicio; evitar utilizarlo para realizar pruebas o monitoreos.

[Learn more](https://iana.org/help/example-domains)
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
