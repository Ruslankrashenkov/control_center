import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from migrations import metadata


Base = declarative_base()


class Asset(Base):
    __tablename__ = "assets"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    ticker = sa.Column(sa.String, unique=True)
    name = sa.Column(sa.String, unique=True)
    unified_cryptoasset_id = sa.Column(sa.Integer)

    can_deposit = sa.Column(sa.Boolean)
    can_withdraw = sa.Column(sa.Boolean)
    min_withdraw = sa.Column(sa.Numeric)
    max_withdraw = sa.Column(sa.Numeric)

    maker_fee = sa.Column(sa.Numeric)
    taker_fee = sa.Column(sa.Numeric)


class Coin(Base):
    __tablename__ = "coins"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    name = sa.Column(sa.String, unique=True)
    description = sa.Column(sa.String)
    backing_coin = sa.Column(sa.String)
    symbol = sa.Column(sa.String)

    deposit_allowed = sa.Column(sa.Boolean)
    withdrawal_allowed = sa.Column(sa.Boolean)

    memo_support = sa.Column(sa.Boolean)
    memo_version = sa.Column(sa.Integer)

    precision = sa.Column(sa.Integer)

    issuer = sa.Column(sa.String)
    issuer_id = sa.Column(sa.String)

    gateway_wallet = sa.Column(sa.String)
    wallet_type = sa.Column(sa.String)

    min_amount = sa.Column(sa.Integer)
    withdraw_fee = sa.Column(sa.String)
    deposit_fee = sa.Column(sa.Integer)

    # 0 means "irreversible" type of confirmation, 0< means "block" type
    confirmations = sa.Column(sa.Integer)
