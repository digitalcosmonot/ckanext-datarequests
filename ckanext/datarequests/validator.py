# -*- coding: utf-8 -*-

# Copyright (c) 2015 CoNWeT Lab., Universidad Politécnica de Madrid

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

import constants
import ckan.plugins.toolkit as tk
import ckanext.datarequests.db as db


def validate_datarequest(context, request_data):

    errors = {}

    # Check name
    if len(request_data['title']) > constants.NAME_MAX_LENGTH:
        errors['Title'] = [tk._('Title must be a maximum of %d characters long') % constants.NAME_MAX_LENGTH]

    if not request_data['title']:
        errors['Title'] = [tk._('Title cannot be empty')]

    # Title is only checked in the database when it's correct
    if 'Title' not in errors:
        if db.DataRequest.datarequest_exists(request_data['title']):
            errors['Title'] = ['That title is already in use']

    # Check description
    if len(request_data['description']) > constants.DESCRIPTION_MAX_LENGTH:
        errors['Description'] = [tk._('Description must be a maximum of %d characters long') % constants.DESCRIPTION_MAX_LENGTH]

    # Check organization
    try:
        tk.get_validator('group_id_exists')(request_data['organization'], context)
    except Exception:
        errors['Organization'] = ['Organization is not valid']

    if len(errors) > 0:
        raise tk.ValidationError(errors)