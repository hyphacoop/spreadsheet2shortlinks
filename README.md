# `spreadsheet2shortlinks`

This command-line tool takes data from a GDrive spreadsheet
([sample][sample_shortlink_sheet]), and uses it to create/update
shortlinks managed on Rebrandly.

   [sample_shortlink_sheet]: https://docs.google.com/spreadsheets/d/12VUXPCpActC77wy6Q8Khyb-iZ_nlNwshO8XswYRj5XE/edit#gid=776462093

## Supported Platforms

- Link Shorteners
  - Rebrandly
- Data Sources
  - Google Spreadsheets

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
$ pipenv install
git+https://github.com/civictechto/anki-meetup-memorizer#egg=anki-meetup-memorizer
$ pipenv run anki-meetup-memorizer --help

# You can set config via a dot-env file
$ cp sample.env .env
```

## Development

```
$ cd path/to/spreadsheet2shortlinks
$ git submodule update --init
$ pipenv install
```
