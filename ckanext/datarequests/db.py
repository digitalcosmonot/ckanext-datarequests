# Copyright (c) 2015-2016 CoNWeT Lab., Universidad Politécnica de Madrid

# This file is part of CKAN Data Requests Extension.

# CKAN Data Requests Extension is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# CKAN Data Requests Extension is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with CKAN Data Requests Extension. If not, see <http://www.gnu.org/licenses/>.

import uuid

import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy.sql.expression import or_

from . import constants

DataRequest = None
Comment = None
DataRequestFollower = None


def uuid4():
    return str(uuid.uuid4())


def init_db(model):

    global DataRequest
    global Comment
    global DataRequestFollower

    if DataRequest is None:

        class _DataRequest(model.DomainObject):
            @classmethod
            def get(cls, **kw):
                """Finds all the instances required."""
                query = model.Session.query(cls).autoflush(False)
                return query.filter_by(**kw).all()

            @classmethod
            def datarequest_exists(cls, title):
                """Returns true if there is a Data Request with the same title (case insensitive)"""
                query = model.Session.query(cls).autoflush(False)
                return (
                    query.filter(func.lower(cls.title) == func.lower(title)).first()
                    is not None
                )

            @classmethod
            def get_ordered_by_date(cls, **kw):
                '''Personalized query'''
                query = model.Session.query(cls).autoflush(False)
                return query.filter_by(**kw).order_by(cls.open_time.desc()).all()

            @classmethod
            def get_open_datarequests_number(cls):
                """Returns the number of data requests that are open"""
                return (
                    model.Session.query(func.count(cls.id))
                    .filter_by(closed=False)
                    .scalar()
                )

        DataRequest = _DataRequest

        # FIXME: References to the other tables...
        datarequests_table = sa.Table('datarequests', model.meta.metadata,
            sa.Column('user_id', sa.types.UnicodeText, primary_key=False, default=u''),
            sa.Column('id', sa.types.UnicodeText, primary_key=True, default=uuid4),
            sa.Column('title', sa.types.Unicode(constants.NAME_MAX_LENGTH), primary_key=True, default=u''),
            sa.Column('description', sa.types.Unicode(constants.DESCRIPTION_MAX_LENGTH), primary_key=False, default=u''),
            sa.Column('organization_id', sa.types.UnicodeText, primary_key=False, default=None),
            sa.Column('open_time', sa.types.DateTime, primary_key=False, default=None),
            sa.Column('accepted_dataset_id', sa.types.UnicodeText, primary_key=False, default=None),
            sa.Column('close_time', sa.types.DateTime, primary_key=False, default=None),
            sa.Column('closed', sa.types.Boolean, primary_key=False, default=False),
            sa.Column('extras', model.types.JsonDictType),
            sa.Column('visibility',
                      sa.types.Integer,
                      default=constants.DataRequestState.hidden.value),
            sa.Column('status', sa.types.Unicode(128), primary_key=False, default=u'Open')
        )

        # Create the table only if it does not exist
        datarequests_table.create(checkfirst=True)

        model.meta.mapper(
            DataRequest,
            datarequests_table,
        )

    if Comment is None:

        class _Comment(model.DomainObject):
            @classmethod
            def get(cls, **kw):
                """Finds all the instances required."""
                query = model.Session.query(cls).autoflush(False)
                return query.filter_by(**kw).all()

            @classmethod
            def get_ordered_by_date(cls, datarequest_id, desc=False):
                """Personalized query"""
                query = model.Session.query(cls).autoflush(False)
                order_by_filter = cls.time.desc() if desc else cls.time.asc()
                return (
                    query.filter_by(datarequest_id=datarequest_id)
                    .order_by(order_by_filter)
                    .all()
                )

            @classmethod
            def get_comment_datarequests_number(cls, **kw):
                """
                Returned the number of comments of a data request
                """
                return model.Session.query(func.count(cls.id)).filter_by(**kw).scalar()

        Comment = _Comment

        # FIXME: References to the other tables...
        comments_table = sa.Table(
            "datarequests_comments",
            model.meta.metadata,
            sa.Column("id", sa.types.UnicodeText, primary_key=True, default=uuid4),
            sa.Column("user_id", sa.types.UnicodeText, primary_key=False, default=""),
            sa.Column(
                "datarequest_id", sa.types.UnicodeText, primary_key=True, default=uuid4
            ),
            sa.Column("time", sa.types.DateTime, primary_key=True, default=""),
            sa.Column(
                "comment",
                sa.types.Unicode(constants.COMMENT_MAX_LENGTH),
                primary_key=False,
                default="",
            ),
        )

        # Create the table only if it does not exist
        comments_table.create(checkfirst=True)

        model.meta.mapper(
            Comment,
            comments_table,
        )

    if DataRequestFollower is None:

        class _DataRequestFollower(model.DomainObject):
            @classmethod
            def get(cls, **kw):
                """Finds all the instances required."""
                query = model.Session.query(cls).autoflush(False)
                return query.filter_by(**kw).all()

            @classmethod
            def get_datarequest_followers_number(cls, **kw):
                """
                Returned the number of followers of a data request
                """
                return model.Session.query(func.count(cls.id)).filter_by(**kw).scalar()

        DataRequestFollower = _DataRequestFollower

        # FIXME: References to the other tables...
        followers_table = sa.Table(
            "datarequests_followers",
            model.meta.metadata,
            sa.Column("id", sa.types.UnicodeText, primary_key=True, default=uuid4),
            sa.Column("user_id", sa.types.UnicodeText, primary_key=False, default=""),
            sa.Column(
                "datarequest_id", sa.types.UnicodeText, primary_key=True, default=uuid4
            ),
            sa.Column("time", sa.types.DateTime, primary_key=True, default=""),
        )

        # Create the table only if it does not exist
        followers_table.create(checkfirst=True)

        model.meta.mapper(
            DataRequestFollower,
            followers_table,
        )
