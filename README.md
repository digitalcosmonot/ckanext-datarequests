

## Installation

Install this extension in your CKAN instance is as easy as install any other CKAN extension.

* Activate your virtual environment
```
. /usr/lib/ckan/default/bin/activate
```
* Install the extension
```
pip install -e 'git+https://github.com/digitalcosmonot/ckanext-datarequests'
```


* Modify your configuration file (generally in `/etc/ckan/default/production.ini`) and add `datarequests` in the `ckan.plugins` property.
```
ckan.plugins = datarequests <OTHER_PLUGINS>
```
* Enable or disable the comments system by setting up the `ckan.datarequests.comments` property in the configuration file (by default, the comments system is enabled).
```
ckan.datarequests.comments = [true|false]
```
* Enable or disable a badge to show the number of data requests in the menu by setting up the `ckan.datarequests.show_datarequests_badge` property in the configuration file (by default, the badge is not shown).
```
ckan.datarequests.show_datarequests_badge = [true|false]
```
* Enable or disable description as a required field on data request forms. False by default
```
ckan.datarequests.description_required = [True|False]
```
* Restart your apache2 reserver
```
sudo service apache2 restart
```
* That's All!

## Translations

Help us to translate this extension so everyone can create data requests. Currently, the extension is translated to English, Spanish, German, French, Somali, Romanian and Brazilian Portuguese. If you want to contribute with your translation, the first step is to clone this repo and move to the `develop` branch. Then, create the locale for your translation by executing:

```
python setup.py init_catalog -l <YOUR_LOCALE>
```

This will generate a file called `i18n/YOUR_LOCALE/LC_MESSAGES/ckanext-datarequests.po`. This file contains all the untranslated strings. You can manually add a translation for it by editing the `msgstr` section:

```
msgid "This is an untranslated string"
msgstr "This is a itranslated string"
```

Once the translation files (`po`) have been updated, compile them by running:

```
python setup.py compile_catalog
```

This will generate the required `mo` file. Once this file has been generated, commit your changes and create a Pull Request (to the `develop` branch).


