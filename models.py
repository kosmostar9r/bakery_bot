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
    category = peewee.CharField()
    goods = JSONField()
    phone_number = peewee.CharField()
    confirmed = peewee.BooleanField(default=False)
    # todo передавать в goods json файл со списком покупок по категориям типа круассаны : [шок, шок, класс],
    # todo эклер : [ваниль, шоколад, карамель, карамель]
