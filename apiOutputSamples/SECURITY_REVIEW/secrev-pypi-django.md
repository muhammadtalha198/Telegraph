---
intent: SECURITY_REVIEW
slug: secrev-pypi-django
status: approved
captured_at: 2026-10-04T18:40:24Z
request_url: https://pypi.org/pypi/django/3.0/json
content_type: application/json
inputs: |
  pypi django 3.0
intent_description: |
  Scans codebase dependencies, API endpoints, and configuration files for common CVEs, secrets leakage, and misconfigurations.
answer_requirement: |
  Must list known security vulnerabilities for the package/version asked.
capture_note: |
  sample approved
reviewer_note: "auto_review: [0.90|heuristic] Lists 41 package vulnerabilities"
reviewed_at: 2026-10-04T18:41:49Z
---

## Raw API output

```json
{
  "info": {
    "author": "Django Software Foundation",
    "author_email": "foundation@djangoproject.com",
    "bugtrack_url": null,
    "classifiers": [
      "Development Status :: 5 - Production/Stable",
      "Environment :: Web Environment",
      "Framework :: Django",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: BSD License",
      "Operating System :: OS Independent",
      "Programming Language :: Python",
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3 :: Only",
      "Programming Language :: Python :: 3.6",
      "Programming Language :: Python :: 3.7",
      "Programming Language :: Python :: 3.8",
      "Topic :: Internet :: WWW/HTTP",
      "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
      "Topic :: Internet :: WWW/HTTP :: WSGI",
      "Topic :: Software Development :: Libraries :: Application Frameworks",
      "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    "description": "======\nDjango\n======\n\nDjango is a high-level Python Web framework that encourages rapid development\nand clean, pragmatic design. Thanks for checking it out.\n\nAll documentation is in the \"``docs``\" directory and online at\nhttps://docs.djangoproject.com/en/stable/. If you're just getting started,\nhere's how we recommend you read the docs:\n\n* First, read ``docs/intro/install.txt`` for instructions on installing Django.\n\n* Next, work through the tutorials in order (``docs/intro/tutorial01.txt``,\n  ``docs/intro/tutorial02.txt``, etc.).\n\n* If you want to set up an actual deployment server, read\n  ``docs/howto/deployment/index.txt`` for instructions.\n\n* You'll probably want to read through the topical guides (in ``docs/topics``)\n  next; from there you can jump to the HOWTOs (in ``docs/howto``) for specific\n  problems, and check out the reference (``docs/ref``) for gory details.\n\n* See ``docs/README`` for instructions on building an HTML version of the docs.\n\nDocs are updated rigorously. If you find any problems in the docs, or think\nthey should be clarified in any way, please take 30 seconds to fill out a\nticket here: https://code.djangoproject.com/newticket\n\nTo get more help:\n\n* Join the ``#django`` channel on irc.freenode.net. Lots of helpful people hang\n  out there. See https://en.wikipedia.org/wiki/Wikipedia:IRC/Tutorial if you're\n  new to IRC.\n\n* Join the django-users mailing list, or read the archives, at\n  https://groups.google.com/group/django-users.\n\nTo contribute to Django:\n\n* Check out https://docs.djangoproject.com/en/dev/internals/contributing/ for\n  information about getting involved.\n\nTo run Django's test suite:\n\n* Follow the instructions in the \"Unit tests\" section of\n  ``docs/internals/contributing/writing-code/unit-tests.txt``, published online at\n  https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/#running-the-unit-tests\n\n\n",
    "description_content_type": "",
    "docs_url": null,
    "download_url": "",
    "downloads": {
      "last_day": -1,
      "last_month": -1,
      "last_week": -1
    },
    "dynamic": null,
    "home_page": "https://www.djangoproject.com/",
    "keywords": "",
    "license": "BSD",
    "license_expression": null,
    "license_files": null,
    "maintainer": "",
    "maintainer_email": "",
    "name": "Django",
    "package_url": "https://pypi.org/project/Django/",
    "platform": "",
    "project_url": "https://pypi.org/project/Django/",
    "project_urls": {
      "Documentation": "https://docs.djangoproject.com/",
      "Funding": "https://www.djangoproject.com/fundraising/",
      "Homepage": "https://www.djangoproject.com/",
      "Source": "https://github.com/django/django",
      "Tracker": "https://code.djangoproject.com/"
    },
    "provides_extra": null,
    "release_url": "https://pypi.org/project/Django/3.0/",
    "requires_dist": [
      "pytz",
      "sqlparse (>=0.2.2)",
      "asgiref (~=3.2)",
      "argon2-cffi (>=16.1.0) ; extra == 'argon2'",
      "bcrypt ; extra == 'bcrypt'"
    ],
    "requires_python": ">=3.6",
    "summary": "A high-level Python Web framework that encourages rapid development and clean, pragmatic design.",
    "version": "3.0",
    "yanked": false,
    "yanked_reason": null
  },
  "last_serial": 40659727,
  "ownership": {
    "organization": "django",
    "roles": []
  },
  "urls": [
    {
      "comment_text": "",
      "core-metadata": {
        "sha256": "05e03577fa029167ba7cd07c56449e54cc0f2d5434e84aaea24d2e4ea024b781"
      },
      "digests": {
        "blake2b_256": "43d60aed0b12c66527748ce5a007da4618a65dfbe1f8fca82eccedf57d60295f",
        "md5": "62020205feeac36093077863fd1fdd38",
        "sha256": "6f857bd4e574442ba35a7172f1397b303167dae964cf18e53db5e85fe248d000"
      },
      "downloads": -1,
      "filename": "Django-3.0-py3-none-any.whl",
      "has_sig": false,
      "md5_digest": "62020205feeac36093077863fd1fdd38",
      "packagetype": "bdist_wheel",
      "python_version": "py3",
      "requires_python": ">=3.6",
      "size": 7427980,
      "upload_time": "2019-12-02T11:13:11",
      "upload_time_iso_8601": "2019-12-02T11:13:11.252980Z",
      "url": "https://files.pythonhosted.org/packages/43/d6/0aed0b12c66527748ce5a007da4618a65dfbe1f8fca82eccedf57d60295f/Django-3.0-py3-none-any.whl",
      "yanked": false,
      "yanked_reason": null
    },
    {
      "comment_text": "",
      "core-metadata": false,
      "digests": {
        "blake2b_256": "f846b3b8c61f867827fff2305db40659495dcd64fb35c399e75c53f23c113871",
        "md5": "bd2aebfa7c1106755544f7f217d2acde",
        "sha256": "d98c9b6e5eed147bc51f47c014ff6826bd1ab50b166956776ee13db5a58804ae"
      },
      "downloads": -1,
      "filename": "Django-3.0.tar.gz",
      "has_sig": false,
      "md5_digest": "bd2aebfa7c1106755544f7f217d2acde",
      "packagetype": "sdist",
      "python_version": "source",
      "requires_python": ">=3.6",
      "size": 8909597,
      "upload_time": "2019-12-02T11:13:17",
      "upload_time_iso_8601": "2019-12-02T11:13:17.709458Z",
      "url": "https://files.pythonhosted.org/packages/f8/46/b3b8c61f867827fff2305db40659495dcd64fb35c399e75c53f23c113871/Django-3.0.tar.gz",
      "yanked": false,
      "yanked_reason": null
    }
  ],
  "vulnerabilities": [
    {
      "aliases": [
        "CVE-2021-3281",
        "GHSA-fvgf-6h6h-3322"
      ],
      "details": "In Django 2.2 before 2.2.18, 3.0 before 3.0.12, and 3.1 before 3.1.6, the django.utils.archive.extract method (used by \"startapp --template\" and \"startproject --template\") allows directory traversal via an archive with absolute paths or relative paths with dot segments.",
      "fixed_in": [
        "2.2.18",
        "3.0.12",
        "3.1.6"
      ],
      "id": "PYSEC-2021-9",
      "link": "https://osv.dev/vulnerability/PYSEC-2021-9",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "CVE-2020-24583",
        "GHSA-m6gj-h9gm-gw44"
      ],
      "details": "An issue was discovered in Django 2.2 before 2.2.16, 3.0 before 3.0.10, and 3.1 before 3.1.1 (when Python 3.7+ is used). FILE_UPLOAD_DIRECTORY_PERMISSIONS mode was not applied to intermediate-level directories created in the process of uploading files. It was also not applied to intermediate-level collected static directories when using the collectstatic management command.",
      "fixed_in": [
        "2.2.16",
        "3.0.10",
        "3.1.1"
      ],
      "id": "PYSEC-2020-33",
      "link": "https://osv.dev/vulnerability/PYSEC-2020-33",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "CVE-2020-13254",
        "GHSA-wpjr-j57x-wxfw"
      ],
      "details": "An issue was discovered in Django 2.2 before 2.2.13 and 3.0 before 3.0.7. In cases where a memcached backend does not perform key validation, passing malformed cache keys could result in a key collision, and potential data leakage.",
      "fixed_in": [
        "2.2.13",
        "3.0.7"
      ],
      "id": "PYSEC-2020-31",
      "link": "https://osv.dev/vulnerability/PYSEC-2020-31",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2020-9402",
        "CVE-2020-9402",
        "GHSA-3gh2-xw74-jmcw",
        "PYSEC-2020-345"
      ],
      "details": "Django 1.11 before 1.11.29, 2.2 before 2.2.11, and 3.0 before 3.0.4 allows SQL Injection if untrusted data is used as a tolerance parameter in GIS functions and aggregates on Oracle. By passing a suitably crafted tolerance to GIS functions and aggregates on Oracle, it was possible to break escaping and inject malicious SQL.",
      "fixed_in": [
        "1.11.29",
        "2.2.11",
        "3.0.4"
      ],
      "id": "PYSEC-2020-36",
      "link": "https://osv.dev/vulnerability/PYSEC-2020-36",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "CVE-2021-33203",
        "GHSA-68w8-qjq3-2gfm"
      ],
      "details": "Django before 2.2.24, 3.x before 3.1.12, and 3.2.x before 3.2.4 has a potential directory traversal via django.contrib.admindocs. Staff members could use the TemplateDetailView view to check the existence of arbitrary files. Additionally, if (and only if) the default admindocs templates have been customized by application developers to also show file contents, then not only the existence but also the file contents would have been exposed. In other words, there is directory traversal outside of the template root directories.",
      "fixed_in": [
        "2.2.24",
        "3.1.12",
        "3.2.4"
      ],
      "id": "PYSEC-2021-98",
      "link": "https://osv.dev/vulnerability/PYSEC-2021-98",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "CVE-2021-28658",
        "GHSA-xgxc-v2qg-chmh"
      ],
      "details": "In Django 2.2 before 2.2.20, 3.0 before 3.0.14, and 3.1 before 3.1.8, MultiPartParser allowed directory traversal via uploaded files with suitably crafted file names. Built-in upload handlers were not affected by this vulnerability.",
      "fixed_in": [
        "2.2.20",
        "3.0.14",
        "3.1.8"
      ],
      "id": "PYSEC-2021-6",
      "link": "https://osv.dev/vulnerability/PYSEC-2021-6",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "CVE-2021-33571",
        "GHSA-p99v-5w3c-jqq9"
      ],
      "details": "In Django 2.2 before 2.2.24, 3.x before 3.1.12, and 3.2 before 3.2.4, URLValidator, validate_ipv4_address, and validate_ipv46_address do not prohibit leading zero characters in octal literals. This may allow a bypass of access control that is based on IP addresses. (validate_ipv4_address and validate_ipv46_address are unaffected with Python 3.9.5+..) .",
      "fixed_in": [
        "2.2.24",
        "3.1.12",
        "3.2.4"
      ],
      "id": "PYSEC-2021-99",
      "link": "https://osv.dev/vulnerability/PYSEC-2021-99",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "CVE-2020-7471",
        "GHSA-hmr4-m2h5-33qx"
      ],
      "details": "Django 1.11 before 1.11.28, 2.2 before 2.2.10, and 3.0 before 3.0.3 allows SQL Injection if untrusted data is used as a StringAgg delimiter (e.g., in Django applications that offer downloads of data as a series of rows with a user-specified column delimiter). By passing a suitably crafted delimiter to a contrib.postgres.aggregates.StringAgg instance, it was possible to break escaping and inject malicious SQL.",
      "fixed_in": [
        "1.11.28",
        "2.2.10",
        "3.0.3"
      ],
      "id": "PYSEC-2020-35",
      "link": "https://osv.dev/vulnerability/PYSEC-2020-35",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "CVE-2020-24584",
        "GHSA-fr28-569j-53c4"
      ],
      "details": "An issue was discovered in Django 2.2 before 2.2.16, 3.0 before 3.0.10, and 3.1 before 3.1.1 (when Python 3.7+ is used). The intermediate-level directories of the filesystem cache had the system's standard umask rather than 0o077.",
      "fixed_in": [
        "2.2.16",
        "3.0.10",
        "3.1.1"
      ],
      "id": "PYSEC-2020-34",
      "link": "https://osv.dev/vulnerability/PYSEC-2020-34",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "CVE-2020-13596",
        "GHSA-2m34-jcjv-45xf"
      ],
      "details": "An issue was discovered in Django 2.2 before 2.2.13 and 3.0 before 3.0.7. Query parameters generated by the Django admin ForeignKeyRawIdWidget were not properly URL encoded, leading to a possibility of an XSS attack.",
      "fixed_in": [
        "2.2.13",
        "3.0.7"
      ],
      "id": "PYSEC-2020-32",
      "link": "https://osv.dev/vulnerability/PYSEC-2020-32",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2020-13254",
        "CVE-2020-13254",
        "PYSEC-2020-31"
      ],
      "details": "An issue was discovered in Django version 2.2 before 2.2.13 and 3.0 before 3.0.7. In cases where a memcached backend does not perform key validation, passing malformed cache keys could result in a key collision, and potential data leakage.",
      "fixed_in": [
        "2.2.13",
        "3.0.7"
      ],
      "id": "GHSA-wpjr-j57x-wxfw",
      "link": "https://osv.dev/vulnerability/GHSA-wpjr-j57x-wxfw",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2021-33203",
        "CVE-2021-33203",
        "PYSEC-2021-98"
      ],
      "details": "Django before 2.2.24, 3.x before 3.1.12, and 3.2.x before 3.2.4 has a potential directory traversal via django.contrib.admindocs. Staff members could use the TemplateDetailView view to check the existence of arbitrary files. Additionally, if (and only if) the default admindocs templates have been customized by application developers to also show file contents, then not only the existence but also the file contents would have been exposed. In other words, there is directory traversal outside of the template root directories.",
      "fixed_in": [
        "2.2.24",
        "3.1.12",
        "3.2.4"
      ],
      "id": "GHSA-68w8-qjq3-2gfm",
      "link": "https://osv.dev/vulnerability/GHSA-68w8-qjq3-2gfm",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2021-28658",
        "CVE-2021-28658",
        "PYSEC-2021-6"
      ],
      "details": "In Django 2.2 before 2.2.20, 3.0 before 3.0.14, and 3.1 before 3.1.8, MultiPartParser allowed directory traversal via uploaded files with suitably crafted file names. Built-in upload handlers were not affected by this vulnerability.",
      "fixed_in": [
        "2.2.20",
        "3.0.14",
        "3.1.8"
      ],
      "id": "GHSA-xgxc-v2qg-chmh",
      "link": "https://osv.dev/vulnerability/GHSA-xgxc-v2qg-chmh",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "CVE-2019-19844",
        "PYSEC-2019-16"
      ],
      "details": "Django before 1.11.27, 2.x before 2.2.9, and 3.x before 3.0.1 allows account takeover. A suitably crafted email address (that is equal to an existing user's email address after case transformation of Unicode characters) would allow an attacker to be sent a password reset token for the matched user account. (One mitigation in the new releases is to send password reset tokens only to the registered user email address.)",
      "fixed_in": [
        "1.11.27",
        "2.2.9",
        "3.0.1"
      ],
      "id": "GHSA-vfq6-hq5r-27r6",
      "link": "https://osv.dev/vulnerability/GHSA-vfq6-hq5r-27r6",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2020-24584",
        "CVE-2020-24584",
        "PYSEC-2020-34"
      ],
      "details": "An issue was discovered in Django 2.2 before 2.2.16, 3.0 before 3.0.10, and 3.1 before 3.1.1 (when Python 3.7+ is used). The intermediate-level directories of the filesystem cache had the system's standard umask rather than 0o077.",
      "fixed_in": [
        "2.2.16",
        "3.0.10",
        "3.1.1"
      ],
      "id": "GHSA-fr28-569j-53c4",
      "link": "https://osv.dev/vulnerability/GHSA-fr28-569j-53c4",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2020-9402",
        "CVE-2020-9402",
        "PYSEC-2020-36"
      ],
      "details": "Django 1.11 before 1.11.29, 2.2 before 2.2.11, and 3.0 before 3.0.4 allows SQL Injection if untrusted data is used as a tolerance parameter in GIS functions and aggregates on Oracle. By passing a suitably crafted tolerance to GIS functions and aggregates on Oracle, it was possible to break escaping and inject malicious SQL.",
      "fixed_in": [
        "1.11.29",
        "2.2.11",
        "3.0.4"
      ],
      "id": "GHSA-3gh2-xw74-jmcw",
      "link": "https://osv.dev/vulnerability/GHSA-3gh2-xw74-jmcw",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2021-44420",
        "CVE-2021-44420",
        "PYSEC-2021-439"
      ],
      "details": "In Django 2.2 before 2.2.25, 3.1 before 3.1.14, and 3.2 before 3.2.10, HTTP requests for URLs with trailing newlines could bypass upstream access control based on URL paths. This issue has low severity, according to the Django security policy.",
      "fixed_in": [
        "2.2.25",
        "3.1.14",
        "3.2.10"
      ],
      "id": "GHSA-v6rh-hp5x-86rv",
      "link": "https://osv.dev/vulnerability/GHSA-v6rh-hp5x-86rv",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2021-31542",
        "CVE-2021-31542",
        "PYSEC-2021-7"
      ],
      "details": "In Django 2.2 before 2.2.21, 3.1 before 3.1.9, and 3.2 before 3.2.1, MultiPartParser, UploadedFile, and FieldFile allowed directory traversal via uploaded files with suitably crafted file names.",
      "fixed_in": [
        "2.2.21",
        "3.1.9",
        "3.2.1"
      ],
      "id": "GHSA-rxjp-mfm9-w4wr",
      "link": "https://osv.dev/vulnerability/GHSA-rxjp-mfm9-w4wr",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2021-3281",
        "CVE-2021-3281",
        "PYSEC-2021-9"
      ],
      "details": "In Django 2.2 before 2.2.18, 3.0 before 3.0.12, and 3.1 before 3.1.6, the django.utils.archive.extract method (used by \"startapp --template\" and \"startproject --template\") allows directory traversal via an archive with absolute paths or relative paths with dot segments.",
      "fixed_in": [
        "2.2.18",
        "3.1.6",
        "3.0.12"
      ],
      "id": "GHSA-fvgf-6h6h-3322",
      "link": "https://osv.dev/vulnerability/GHSA-fvgf-6h6h-3322",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2020-7471",
        "CVE-2020-7471",
        "PYSEC-2020-35"
      ],
      "details": "Django 1.11 before 1.11.28, 2.2 before 2.2.10, and 3.0 before 3.0.3 allows SQL Injection if untrusted data is used as a StringAgg delimiter (e.g., in Django applications that offer downloads of data as a series of rows with a user-specified column delimiter). By passing a suitably crafted delimiter to a contrib.postgres.aggregates.StringAgg instance, it was possible to break escaping and inject malicious SQL.",
      "fixed_in": [
        "1.11.28",
        "2.2.10",
        "3.0.3"
      ],
      "id": "GHSA-hmr4-m2h5-33qx",
      "link": "https://osv.dev/vulnerability/GHSA-hmr4-m2h5-33qx",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2021-35042",
        "CVE-2021-35042",
        "PYSEC-2021-109"
      ],
      "details": "Django 3.1.x before 3.1.13 and 3.2.x before 3.2.5 allows QuerySet.order_by SQL injection if order_by is untrusted input from a client of a web application.",
      "fixed_in": [
        "3.2.5",
        "3.1.13"
      ],
      "id": "GHSA-xpfp-f569-q3p2",
      "link": "https://osv.dev/vulnerability/GHSA-xpfp-f569-q3p2",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2020-24583",
        "CVE-2020-24583",
        "PYSEC-2020-33"
      ],
      "details": "An issue was discovered in Django 2.2 before 2.2.16, 3.0 before 3.0.10, and 3.1 before 3.1.1 (when Python 3.7+ is used). FILE_UPLOAD_DIRECTORY_PERMISSIONS mode was not applied to intermediate-level directories created in the process of uploading files. It was also not applied to intermediate-level collected static directories when using the collectstatic management command.",
      "fixed_in": [
        "2.2.16",
        "3.0.10",
        "3.1.1"
      ],
      "id": "GHSA-m6gj-h9gm-gw44",
      "link": "https://osv.dev/vulnerability/GHSA-m6gj-h9gm-gw44",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2021-33571",
        "CVE-2021-33571",
        "PYSEC-2021-99"
      ],
      "details": "In Django 2.2 before 2.2.24, 3.x before 3.1.12, and 3.2 before 3.2.4, URLValidator, validate_ipv4_address, and validate_ipv46_address do not prohibit leading zero characters in octal literals. This may allow a bypass of access control that is based on IP addresses. (validate_ipv4_address and validate_ipv46_address are unaffected with Python 3.9.5+..) .",
      "fixed_in": [
        "2.2.24",
        "3.1.12",
        "3.2.4"
      ],
      "id": "GHSA-p99v-5w3c-jqq9",
      "link": "https://osv.dev/vulnerability/GHSA-p99v-5w3c-jqq9",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2020-13596",
        "CVE-2020-13596",
        "PYSEC-2020-32"
      ],
      "details": "An issue was discovered in Django version 2.2 before 2.2.13 and 3.0 before 3.0.7. Query parameters generated by the Django admin ForeignKeyRawIdWidget were not properly URL encoded, leading to a possibility of an XSS attack.",
      "fixed_in": [
        "2.2.13",
        "3.0.7"
      ],
      "id": "GHSA-2m34-jcjv-45xf",
      "link": "https://osv.dev/vulnerability/GHSA-2m34-jcjv-45xf",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2022-36359",
        "CVE-2022-36359",
        "PYSEC-2022-245"
      ],
      "details": "An issue was discovered in the HTTP FileResponse class in Django 3.2 before 3.2.15 and 4.0 before 4.0.7. An application is vulnerable to a reflected file download (RFD) attack that sets the Content-Disposition header of a FileResponse when the filename is derived from user-supplied input.",
      "fixed_in": [
        "3.2.15",
        "4.0.7"
      ],
      "id": "GHSA-8x94-hmjh-97hq",
      "link": "https://osv.dev/vulnerability/GHSA-8x94-hmjh-97hq",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2024-45231",
        "CVE-2024-45231",
        "PYSEC-2026-1297"
      ],
      "details": "An issue was discovered in Django v5.1.1, v5.0.9, and v4.2.16. The django.contrib.auth.forms.PasswordResetForm class, when used in a view implementing password reset flows, allows remote attackers to enumerate user e-mail addresses by sending password reset requests and observing the outcome (only when e-mail sending is consistently failing).",
      "fixed_in": [
        "5.1.1",
        "5.0.9",
        "4.2.16"
      ],
      "id": "GHSA-rrqc-c2jx-6jgv",
      "link": "https://osv.dev/vulnerability/GHSA-rrqc-c2jx-6jgv",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2025-48432",
        "CVE-2025-48432",
        "PYSEC-2025-47"
      ],
      "details": "An issue was discovered in Django 5.2 before 5.2.2, 5.1 before 5.1.10, and 4.2 before 4.2.22. Internal HTTP response logging does not escape request.path, which allows remote attackers to potentially manipulate log output via crafted URLs. This may lead to log injection or forgery when logs are viewed in terminals or processed by external systems.",
      "fixed_in": [
        "5.2.2",
        "5.1.10",
        "4.2.22"
      ],
      "id": "GHSA-7xr5-9hcq-chf9",
      "link": "https://osv.dev/vulnerability/GHSA-7xr5-9hcq-chf9",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2025-57833",
        "CVE-2025-57833",
        "PYSEC-2025-105"
      ],
      "details": "An issue was discovered in Django 4.2 before 4.2.24, 5.1 before 5.1.12, and 5.2 before 5.2.6. FilteredRelation is subject to SQL injection in column aliases, using a suitably crafted dictionary, with dictionary expansion, as the **kwargs passed QuerySet.annotate() or QuerySet.alias().",
      "fixed_in": [
        "4.2.24",
        "5.1.12",
        "5.2.6"
      ],
      "id": "GHSA-6w2r-r2m5-xq5w",
      "link": "https://osv.dev/vulnerability/GHSA-6w2r-r2m5-xq5w",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2025-64458",
        "CVE-2025-64458",
        "PYSEC-2025-107"
      ],
      "details": "An issue was discovered in 5.1 before 5.1.14, 4.2 before 4.2.26, and 5.2 before 5.2.8.\nNFKC normalization in Python is slow on Windows. As a consequence, `django.http.HttpResponseRedirect`, `django.http.HttpResponsePermanentRedirect`, and the shortcut `django.shortcuts.redirect`  were subject to a potential  denial-of-service attack via certain inputs with a very large number of Unicode characters.\nEarlier, unsupported Django series (such as 5.0.x, 4.1.x, and 3.2.x) were not evaluated and may also be affected.\nDjango would like to thank Seokchan Yoon for reporting this issue.",
      "fixed_in": [
        "5.2.8",
        "5.1.14",
        "4.2.26"
      ],
      "id": "GHSA-qw25-v68c-qjf3",
      "link": "https://osv.dev/vulnerability/GHSA-qw25-v68c-qjf3",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2025-64459",
        "CVE-2025-64459",
        "PYSEC-2025-108"
      ],
      "details": "An issue was discovered in 5.1 before 5.1.14, 4.2 before 4.2.26, and 5.2 before 5.2.8.\nThe methods `QuerySet.filter()`, `QuerySet.exclude()`, and `QuerySet.get()`, and the class `Q()`, are subject to SQL injection when using a suitably crafted dictionary, with dictionary expansion, as the `_connector` argument.\nEarlier, unsupported Django series (such as 5.0.x, 4.1.x, and 3.2.x) were not evaluated and may also be affected.\nDjango would like to thank cyberstan for reporting this issue.",
      "fixed_in": [
        "5.2.8",
        "5.1.14",
        "4.2.26"
      ],
      "id": "GHSA-frmv-pr5f-9mcr",
      "link": "https://osv.dev/vulnerability/GHSA-frmv-pr5f-9mcr",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "CVE-2024-45231",
        "GHSA-rrqc-c2jx-6jgv"
      ],
      "details": "An issue was discovered in Django v5.1.1, v5.0.9, and v4.2.16. The django.contrib.auth.forms.PasswordResetForm class, when used in a view implementing password reset flows, allows remote attackers to enumerate user e-mail addresses by sending password reset requests and observing the outcome (only when e-mail sending is consistently failing).",
      "fixed_in": [
        "4.2.16",
        "5.0.9",
        "5.1.1"
      ],
      "id": "PYSEC-2026-1297",
      "link": "https://osv.dev/vulnerability/PYSEC-2026-1297",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "CVE-2026-15830"
      ],
      "details": "An issue was discovered in Django 5.2 before 5.2.17 and 6.0 before 6.0.8.\nGeoDjango's `django.contrib.gis.geos.GEOSGeometry` is subject to a potential denial-of-service when parsing deeply nested `GEOMETRYCOLLECTION` objects supplied as well-known text (WKT), well-known binary (WKB), or hex-encoded WKB, which triggers unbounded recursion and a segmentation fault in the underlying GEOS library. Spatial field lookups and the `django.contrib.gis.forms.GeometryField` form field are also affected.\nEarlier, unsupported Django series (such as 5.1.x, 5.0.x, and 4.2.x) were not evaluated and may also be affected.\nDjango would like to thank Andrew MacPherson and kimchunbok_ for reporting this issue.",
      "fixed_in": [
        "5.2.17",
        "6.0.8",
        "6.1.1"
      ],
      "id": "GHSA-q238-5cxm-5c9h",
      "link": "https://osv.dev/vulnerability/GHSA-q238-5cxm-5c9h",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "CVE-2026-15307"
      ],
      "details": "An issue was discovered in Django 5.2 before 5.2.17 and 6.0 before 6.0.8.\nGeoDjango spatial lookups optimistically parse the right-hand-side value as a raster by passing it to the `django.contrib.gis.gdal.GDALRaster` constructor. Any value used in a spatial lookup against a `GeometryField` or `RasterField` reaches this constructor, including untrusted input, for example a spatial-field filter submitted through the Django admin changelist query string by a staff user with view permission. A `dict`, or a `str` holding its JSON representation, is opened in write mode regardless of the constructor's `write=False` default, allowing a file with an attacker-chosen name and contents to be written through a file-backed GDAL driver. Any other `str` is treated as a datasource, allowing an outbound network request through a GDAL virtual filesystem handler. Writing a file to a location later imported by the application can result in remote code execution.\nEarlier, unsupported Django series (such as 5.1.x, 5.0.x, and 4.2.x) were not evaluated and may also be affected.\nDjango would like to thank Bence Nagy, localhost-detect, and kimchunbok_ for reporting this issue.",
      "fixed_in": [
        "5.2.17",
        "6.0.8"
      ],
      "id": "GHSA-wvqv-fj8w-qmhm",
      "link": "https://osv.dev/vulnerability/GHSA-wvqv-fj8w-qmhm",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2026-48587",
        "CVE-2026-48587",
        "PYSEC-2026-198"
      ],
      "details": "An issue was discovered in Django 5.2 before 5.2.15 and 6.0 before 6.0.6.\n`django.utils.cache.has_vary_header()` in Django does not strip leading or trailing whitespace from `Vary` response header values before comparison, which allows remote attackers to read cached responses via requests to URLs whose responses contain whitespace-padded Vary header values.\nEarlier, unsupported Django series (such as 5.0.x, 4.1.x, and 3.2.x) were not evaluated and may also be affected.\nDjango would like to thank Navid Rezazadeh for reporting this issue.",
      "fixed_in": [
        "5.2.15",
        "6.0.6"
      ],
      "id": "GHSA-923m-gv2p-w5qp",
      "link": "https://osv.dev/vulnerability/GHSA-923m-gv2p-w5qp",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2026-6873",
        "CVE-2026-6873",
        "PYSEC-2026-199"
      ],
      "details": "An issue was discovered in Django 6.0 before 6.0.6 and 5.2 before 5.2.15.\n`django.http.HttpRequest.get_signed_cookie` in Django uses a non-injective salt derivation (concatenating the cookie name and salt argument), which allows a remote attacker to use a cookie in a context different from the one where it was signed, via distinct `(name, salt)` pairs that produce the same concatenation.\nEarlier, unsupported Django series (such as 5.0.x, 4.1.x, and 3.2.x) were not evaluated and may also be affected.\nDjango would like to thank Peng Zhou for reporting this issue.",
      "fixed_in": [
        "5.2.15",
        "6.0.6"
      ],
      "id": "GHSA-h7pc-vwp9-298g",
      "link": "https://osv.dev/vulnerability/GHSA-h7pc-vwp9-298g",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2026-8404",
        "CVE-2026-8404",
        "PYSEC-2026-201"
      ],
      "details": "An issue was discovered in Django 5.2 before 5.2.15 and 6.0 before 6.0.6.\n`django.middleware.cache.UpdateCacheMiddleware` in Django does not match `Cache-Control` response directives case-insensitively, which allows remote attackers to read responses that were incorrectly cached because their `Cache-Control` directives used uppercase or mixed-case values.\nEarlier, unsupported Django series (such as 5.0.x, 4.1.x, and 3.2.x) were not evaluated and may also be affected.\nDjango would like to thank Ahmed Badawe for reporting this issue.",
      "fixed_in": [
        "5.2.15",
        "6.0.6"
      ],
      "id": "GHSA-8cjm-8mp7-r2xf",
      "link": "https://osv.dev/vulnerability/GHSA-8cjm-8mp7-r2xf",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2026-48588",
        "CVE-2026-48588",
        "PYSEC-2026-2090"
      ],
      "details": "An issue was discovered in Django 6.0 before 6.0.7 and 5.2 before 5.2.16.\n`UpdateCacheMiddleware` and the `cache_page()` decorator cache responses that vary on cookies when the incoming request carries unrelated cookies, which allows remote attackers to read private data from the shared cache.\nEarlier, unsupported Django series (such as 5.0.x, 4.1.x, and 3.2.x) were not evaluated and may also be affected.\nDjango would like to thank Chris Whyland for reporting this issue.",
      "fixed_in": [
        "5.2.16",
        "6.0.7"
      ],
      "id": "GHSA-3h9f-r86x-qvjx",
      "link": "https://osv.dev/vulnerability/GHSA-3h9f-r86x-qvjx",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2026-53877",
        "CVE-2026-53877",
        "PYSEC-2026-2091"
      ],
      "details": "An issue was discovered in Django 6.0 before 6.0.7 and 5.2 before 5.2.16.\n`django.contrib.gis.gdal.GDALRaster` over-reads its in-memory buffer when constructed from a bytes object, which can disclose adjacent memory or cause service degradation via a potential segmentation fault when the `vsi_buffer` property is accessed.\nEarlier, unsupported Django series (such as 5.0.x, 4.1.x, and 3.2.x) were not evaluated and may also be affected.\nDjango would like to thank Bence Nagy for reporting this issue.",
      "fixed_in": [
        "5.2.16",
        "6.0.7"
      ],
      "id": "GHSA-crhf-3pfg-w68w",
      "link": "https://osv.dev/vulnerability/GHSA-crhf-3pfg-w68w",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2026-53878",
        "CVE-2026-53878",
        "PYSEC-2026-2092"
      ],
      "details": "An issue was discovered in Django 6.0 before 6.0.7 and 5.2 before 5.2.16.\n`DomainNameValidator` does not prohibit newlines in domain names (unless used via a form field, since `CharField` strips newlines). If an application uses values with newlines in an HTTP response, header injection can occur. Django itself is unaffected because `HttpResponse` prohibits newlines in HTTP headers.\nEarlier, unsupported Django series (such as 5.0.x, 4.1.x, and 3.2.x) were not evaluated and may also be affected.\nDjango would like to thank Bence Nagy for reporting this issue.",
      "fixed_in": [
        "5.2.16",
        "6.0.7"
      ],
      "id": "GHSA-8qcx-xf44-272x",
      "link": "https://osv.dev/vulnerability/GHSA-8qcx-xf44-272x",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "BIT-django-2026-15830",
        "CVE-2026-15830",
        "GHSA-q238-5cxm-5c9h"
      ],
      "details": "An issue was discovered in Django 5.2 before 5.2.17 and 6.0 before 6.0.8.\nGeoDjango's `django.contrib.gis.geos.GEOSGeometry` is subject to a potential denial-of-service when parsing deeply nested `GEOMETRYCOLLECTION` objects supplied as well-known text (WKT), well-known binary (WKB), or hex-encoded WKB, which triggers unbounded recursion and a segmentation fault in the underlying GEOS library. Spatial field lookups and the `django.contrib.gis.forms.GeometryField` form field are also affected.\nEarlier, unsupported Django series (such as 5.1.x, 5.0.x, and 4.2.x) were not evaluated and may also be affected.\nDjango would like to thank Andrew MacPherson and kimchunbok_ for reporting this issue.",
      "fixed_in": [
        "5.2.17",
        "6.0.8"
      ],
      "id": "PYSEC-2026-3717",
      "link": "https://osv.dev/vulnerability/PYSEC-2026-3717",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    },
    {
      "aliases": [
        "CVE-2026-15307",
        "GHSA-wvqv-fj8w-qmhm"
      ],
      "details": "An issue was discovered in Django 5.2 before 5.2.17 and 6.0 before 6.0.8.\nGeoDjango spatial lookups optimistically parse the right-hand-side value as a raster by passing it to the `django.contrib.gis.gdal.GDALRaster` constructor. Any value used in a spatial lookup against a `GeometryField` or `RasterField` reaches this constructor, including untrusted input, for example a spatial-field filter submitted through the Django admin changelist query string by a staff user with view permission. A `dict`, or a `str` holding its JSON representation, is opened in write mode regardless of the constructor's `write=False` default, allowing a file with an attacker-chosen name and contents to be written through a file-backed GDAL driver. Any other `str` is treated as a datasource, allowing an outbound network request through a GDAL virtual filesystem handler. Writing a file to a location later imported by the application can result in remote code execution.\nEarlier, unsupported Django series (such as 5.1.x, 5.0.x, and 4.2.x) were not evaluated and may also be affected.\nDjango would like to thank Bence Nagy, localhost-detect, and kimchunbok_ for reporting this issue.",
      "fixed_in": [
        "5.2.17",
        "6.0.8"
      ],
      "id": "PYSEC-2026-4035",
      "link": "https://osv.dev/vulnerability/PYSEC-2026-4035",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    }
  ]
}
```

## Why this matches (or not)

_[0.90|heuristic] Lists 41 package vulnerabilities_
