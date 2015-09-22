from decimal import Decimal


class DecimalEncoder:
    @staticmethod
    def encode(obj):
        if isinstance(obj, Decimal):
            return '%.2f' % obj
        return obj