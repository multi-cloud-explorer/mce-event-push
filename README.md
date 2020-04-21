## Multi Cloud Explorer - Push Changes Event

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/multi-cloud-explorer/mce-event-push.svg)](https://travis-ci.org/multi-cloud-explorer/mce-event-push)
[![Coverage Status](https://coveralls.io/repos/github/multi-cloud-explorer/mce-event-push/badge.svg?branch=master)](https://coveralls.io/github/multi-cloud-explorer/mce-event-push?branch=master)
[![codecov](https://codecov.io/gh/multi-cloud-explorer/mce-event-push/branch/master/graph/badge.svg)](https://codecov.io/gh/multi-cloud-explorer/mce-event-push)
[![Code Health](https://landscape.io/github/multi-cloud-explorer/mce-event-push/master/landscape.svg?style=flat)](https://landscape.io/github/multi-cloud-explorer/mce-event-push/master)
[![Requirements Status](https://requires.io/github/multi-cloud-explorer/mce-event-push/requirements.svg?branch=master)](https://requires.io/github/multi-cloud-explorer/mce-event-push/requirements/?branch=master)

Librairie d'envoi des changements d'inventaire.

Pour chaque **changement** enregistré, un message peut être envoyé vers une ou plusieurs Queues de type SQS ou un WebService.

**En cours...**

[Documentation](https://multi-cloud-explorer.readthedocs.org)

### Backends

- [ ] AWS SQS
- [ ] Azure Queue Storage
- [ ] Webhook
- [ ] GCP ?
- [ ] Redis

### Message - Create Event

Pour un évènement de type **CREATE**, le champs **new_object** contient l'ensemble des données de la ressoure qui a été créée.

```json
{
    "id": 1,
    "created": "2019-01-01T00:00:00Z",
    "action": "create",
    "changes": [],
    "old_object": {},
    "new_object": {
        "id": 1,
        "resource_id": "1",
        "slug": "1",
        "name": "myname",
        "provider": "aws",
        "resource_type": "aws.ec2.instance",
        "company": "my-company",
        "metas": {},
        "locked": false,
        "active": true,
        "tags": [
            {
                "id": 1,
                "name": "1",
                "value": "1",
                "provider": "aws"
            },
            {
                "id": 2,
                "name": "2",
                "value": "2",
                "provider": "aws"
            },
            {
                "id": 3,
                "name": "3",
                "value": "3",
                "provider": "aws"
            }
        ]
    },
    "diff": null,
    "content_type": {
        "app_label": "mce_django_app",
        "model": "resource",
        "name": "resource",
        "id": 1
    }
}
```

### Message - Delete Event

Pour l'évènement **DELETE**, l'objet avant la suppression est stocké dans le champs **old_object**

```json
{
    "id": 1,
    "created": "2019-01-01T00:00:00Z",
    "action": "delete",
    "changes": [],
    "old_object": {
        "id": 1,
        "resource_id": "1",
        "slug": "1",
        "name": "myname",
        "provider": "aws",
        "resource_type": "aws.ec2.instance",
        "company": "my-company",
        "metas": {},
        "locked": false,
        "active": true,
        "tags": [
            {
                "id": 1,
                "name": "1",
                "value": "1",
                "provider": "aws"
            },
            {
                "id": 2,
                "name": "2",
                "value": "2",
                "provider": "aws"
            },
            {
                "id": 3,
                "name": "3",
                "value": "3",
                "provider": "aws"
            }
        ]
    },
    "new_object": {},
    "diff": null,
    "content_type": {
        "app_label": "mce_django_app",
        "model": "resource",
        "name": "resource",
        "id": 1
    }
}
```

### Message - Update Event

Pour l'évènement **UPDATE**, l'objet avant modification se trouve dans "old_object", après modification, dans "new_object".

Le champs "changes" contient la différence au format JSON Patch.

```json
{
    "id": 1,
    "created": "2019-01-01T00:00:00Z",
    "action": "update",
    "changes": [
        {
            "op": "replace",
            "path": "/name",
            "value": "new-myname"
        }
    ],
    "old_object": {
        "id": 1,
        "resource_id": "1",
        "slug": "1",
        "name": "myname",
        "provider": "aws",
        "resource_type": "aws.ec2.instance",
        "company": "my-company",
        "metas": {},
        "locked": false,
        "active": true,
        "tags": [
            {
                "id": 1,
                "name": "1",
                "value": "1",
                "provider": "aws"
            },
            {
                "id": 2,
                "name": "2",
                "value": "2",
                "provider": "aws"
            },
            {
                "id": 3,
                "name": "3",
                "value": "3",
                "provider": "aws"
            }
        ]
    },
    "new_object": {
        "id": 1,
        "resource_id": "1",
        "slug": "1",
        "name": "new-myname",
        "provider": "aws",
        "resource_type": "aws.ec2.instance",
        "company": "my-company",
        "metas": {},
        "locked": false,
        "active": true,
        "tags": [
            {
                "id": 1,
                "name": "1",
                "value": "1",
                "provider": "aws"
            },
            {
                "id": 2,
                "name": "2",
                "value": "2",
                "provider": "aws"
            },
            {
                "id": 3,
                "name": "3",
                "value": "3",
                "provider": "aws"
            }
        ]
    },
    "diff": null,
    "content_type": {
        "app_label": "mce_django_app",
        "model": "resource",
        "name": "resource",
        "id": 1
    }
}
```

