from typing import List, Dict

from django.db.models import QuerySet
from polaris.integrations import RailsIntegration
from polaris.models import Asset, Transaction


class MyRailsInt(RailsIntegration):
    def poll_pending_deposits(self, pending_deposits: QuerySet, *args: List, **kwargs: Dict):
        print("poll_pending_deposits")
        return list(pending_deposits)

    def execute_outgoing_transaction(
        self, transaction: Transaction, *args: List, **kwargs: Dict
    ):
        print("execute_outgoing_transaction")
        transaction.status = Transaction.STATUS.completed
        transaction.save()
        return transaction


def return_toml_contents(request, *args, **kwargs):
    asset = Asset.objects.first()
    return {
        "DOCUMENTATION": {
            "ORG_NAME": "Anchor Inc.",
            "ORG_URL": "...",
            "ORG_LOGO": "...",
            "ORG_DESCRIPTION": "...",
            "ORG_OFFICIAL_EMAIL": "...",
            "ORG_SUPPORT_EMAIL": "..."
        },
        'CURRENCIES': [
            {
                'code': asset.code,
                'issuer': asset.issuer,
                'status': 'test',
                'desc': "sdfsdf",
                'display_decimals': 2,
            }
        ]

    }
