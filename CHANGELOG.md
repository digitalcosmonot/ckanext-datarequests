# Changelog

## v2.0.0 (UNRELEASED)

* New: Python 3 compatibility
* New: CKAN 2.9 compatibility
* New: Migrated from Pylons to Flask
* New: Migrated from `fanstatic` to `assets`
* New: Applied `isort` and `black` code formatting

* NOTE: Backwards incompatible with Python<3.6 and CKAN<2.10

## v1.2.0 (UNRELEASED)

* New: French translations (thanks to @bobeal)
* New: Romanian translations (thanks to @costibleotu)
* New: Option to force users to introduce a request description (thanks to @MarkCalvert)
* Fix: Documentation fixes (thanks to @nykc)
* Fix: Datarequests creation and closing times displayed incorrectly (thanks to @iamarnavgarg)

## v1.1.0

* New: Compatibility with CKAN 2.8.0
* New: Somali translation (thanks to @SimuliChina)

## v1.0.0

* New: Option to follow data requests.
* New: Email notifications:
  * An email will be sent to organization staff when a data request is created in a organization.
  * An email will be sent to followers, people that commented, datarequest creator and organization staff when a comment in a datarequest is created.
  * An email will be sent to followers, people that commented, datarequest creator and organization staff when a data request is closed.
* New: Major API changes:
  * `datarequest_create` :arrow_right: `create_datarequest`
  * `datarequest_show` :arrow_right: `show_datarequest`
  * `datarequest_update` :arrow_right: `update_datarequest`
  * `datarequest_index` :arrow_right: `list_datarequests`
  * `datarequest_delete` :arrow_right: `delete_datarequest`
  * `datarequest_close` :arrow_right: `close_datarequest`
  * `datarequest_comment` :arrow_right: `comment_datarequest`
  * `datarequest_comment_show` :arrow_right: `show_datarequest_comment`
  * `datarequest_comment_list` :arrow_right: `list_datarequest_comments`
  * `datarequest_comment_update` :arrow_right: `update_datarequest_comment`
  * `datarequest_comment_delete` :arrow_right: `delete_datarequest_comment`

## v0.4.1

* New: Brazilian Portuguese translation (thanks to @allysonbarros)

## v0.4.0

* New: Move CI to Travis
* New: Compatibility with CKAN 2.7 (controller adapted by @owl17)

## v0.3.3

* New: German Translation (thanks to @kvlahrosch)
