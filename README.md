# `spreadsheet2shortlinks`

CLI tool for syncing Rebrandly shortlinks from a Google Spreadsheet.

This command-line tool takes data from a spreadsheet, and uses it to
create/update shortlinks managed on Rebrandly. (For examples, see "Data
Sources", under _Supported Platforms_ below.)

## Supported Platforms

- Link Shorteners
  - Rebrandly
- Data Sources
  - Google Spreadsheets. [Example.][example-gsheet]
  - GitHub. [Example.][example-github]
  - Raw CSV. [Example.][example-rawcsv]

   [example-gsheet]: https://docs.google.com/spreadsheets/d/12VUXPCpActC77wy6Q8Khyb-iZ_nlNwshO8XswYRj5XE/edit#gid=776462093
   [example-github]: https://github.com/hyphacoop/shortlinks/blob/master/shortlinks.csv
   [example-rawcsv]: https://raw.githubusercontent.com/hyphacoop/shortlinks/master/shortlinks.csv

## Usage

For full usage instructions:

```
# Don't forget to prefix with `pipenv run` if using pipenv!
$ spreadsheet2shortlinks --help
```

## Technologies Used

- Python.
  - Click.

## Installation

```
$ pip install git+https://github.com/hyphacoop/spreadsheet2shortlinks#egg=spreadsheet2shortlinks
```

You may also choose to use pipenv, if you have it installed. It allows
for better isolation of Python projects.

```
# To use `pipenv` and an isolated project environment via `pipenv run`:
$ pipenv install --editable git+https://github.com/hyphacoop/spreadsheet2shortlinks#egg=spreadsheet2shortlinks
$ pipenv run spreadsheet2shortlinks --help

# You can set config via a dot-env file
$ cp sample.env .env
```

## Development

```
$ cd path/to/spreadsheet2shortlinks
$ git submodule update --init
$ pipenv install
```
