import peewee
from playhouse.sqlite_ext import SqliteExtDatabase, JSONField

db = SqliteExtDatabase('bakery_bot.db', pragmas=(
    ('cache_size', -1024 * 64),
    ('journal_mode', 'wal'),
    ('foreign_keys', 1)))


class BaseTable(peewee.Model):
    class Meta:
        database = db


class Client(BaseTable):
    user_id = peewee.CharField(unique=True)
    scenario_name = peewee.CharField()
    step_name = peewee.CharField()
    context = JSONField()


class ShoppingProgress(BaseTable):
    phone_number = peewee.CharField()
    cart_sum = peewee.IntegerField(default=0)
    confirmed = peewee.BooleanField(default=False)
    order = JSONField()
