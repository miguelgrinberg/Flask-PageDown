# Flask-PageDown Change Log

**Release 0.4.0** - 2021-09-08

- Fix deprecation warnings by using markupsafe.Markup [#27](https://github.com/miguelgrinberg/flask-pagedown/issues/27) ([commit](https://github.com/miguelgrinberg/flask-pagedown/commit/b0bf84f7757f975bef075faab24a6bf11ba02829)) (thanks **Nick Bautista**!)
- Document how to use your own PageDown JavaScript source files [#24](https://github.com/miguelgrinberg/flask-pagedown/issues/24) ([commit](https://github.com/miguelgrinberg/flask-pagedown/commit/f13f81a72d2dfd0f881306ddc18d5d6642c5744d)) (thanks **olumidesan**!)
- Improved project structure ([commit](https://github.com/miguelgrinberg/flask-pagedown/commit/ea12a8551b4e17fc7a8adffb26845abbead82b72))
- Add a change log ([commit](https://github.com/miguelgrinberg/flask-pagedown/commit/a00e7195b1b98008c33cf9c4fafcd5b66026ceb5))
- Added github actions build ([commit](https://github.com/miguelgrinberg/flask-pagedown/commit/4fec2e7f04c4013193a542218d852072b20bf528))

**Release 0.3.0** - 2020-05-02

- Converted strings to markup [#21](https://github.com/miguelgrinberg/flask-pagedown/issues/21) ([commit](https://github.com/miguelgrinberg/flask-pagedown/commit/90139d9b45aa1a74adbf4ce221faabf8f9b2ca4f)) (thanks **Petr Deriabin**!)

**Release 0.2.2** - 2016-09-30

- Updated Form to FlaskForm ([commit](https://github.com/miguelgrinberg/flask-pagedown/commit/fc69896717eea1ebd055c70511a144aee71525f7))
- Updated requirements for example app ([commit](https://github.com/miguelgrinberg/flask-pagedown/commit/5b0f452200cd382aa64c7c5fdadcb7bfcfa29d73))

**Release 0.2.1** - 2015-05-11

- Support custom CSS classes in field render call ([commit](https://github.com/miguelgrinberg/flask-pagedown/commit/3ee04376a20a7e430190d016a41695c464970201))

**Release 0.2.0** - 2015-05-11

- Change Flask plugins to new recommended import syntax ([commit](https://github.com/miguelgrinberg/flask-pagedown/commit/c70899a0cc3c23d69cb280177e8dc98cd88fc5b7))
- Render preview separately from input area ([commit](https://github.com/miguelgrinberg/flask-pagedown/commit/69a243900a49baca336040cf0ed73094f7d9f66d))
- pep8 fixes ([commit](https://github.com/miguelgrinberg/flask-pagedown/commit/5b04c2de0e6ad697c0399cd40a59f3709fd33944))

**Release 0.1.5** - 2014-05-26

- Fix support for SSL for proxied sites, or otherwise uncertain situations My particular situation is deployed through ElasticBeanstalk, proxying HTTPS to HTTP on the actual endpoints. This makes flask think that it is only running with http, not https ([commit](https://github.com/miguelgrinberg/flask-pagedown/commit/04df5c189d6d1760c692d1985faf558058e56eb2)) (thanks **Frank Tackitt**!)

**Release 0.1.4** - 2014-02-13

- Use of secure URLs when request is secure [#3](https://github.com/miguelgrinberg/flask-pagedown/issues/3) ([commit](https://github.com/miguelgrinberg/flask-pagedown/commit/50ba142994e47d584f5bdf083e0c47f4a9209aa4))

**Release 0.1.3** - 2014-01-07

- Add check if the document is already ready, and if so skip the onload handlers. Fixes live loading of markdown forms ([commit](https://github.com/miguelgrinberg/flask-pagedown/commit/868a4c51028e580fd265d428a9d8f2afe3f4aa7c)) (thanks **Frank Tackitt**!)

**Release 0.1.2** - 2013-11-11

- Minor updates ([commit](https://github.com/miguelgrinberg/flask-pagedown/commit/be1a3e4f25f552178e36d7f383783ff192685832))

**Release 0.1.1** - 2013-11-05

- Fixed setup.py and minor corrections to example app ([commit](https://github.com/miguelgrinberg/flask-pagedown/commit/b50acac4b14f1a882f7de0d47702a175dabde9dc))

**Release 0.1** - 2013-11-04

- Initial version ([commit](https://github.com/miguelgrinberg/flask-pagedown/commit/d8a30b86354b264c4427424d444140bc9f568116))
