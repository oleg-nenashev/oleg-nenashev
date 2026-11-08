# Contributing to the Site

This is a personal site of Oleg Nenashev,
but any contributions, typo fixes and patches are welcome.
The website engine, tooling and configuration are also open source,
feel free to reuse and contribute.
If you want to work together and build a template on the top of Material for MkDocs,
let me know :)

## Quick Start

For the local development without full rebuild:

```shell
mkdocs serve
```

Full build with PDF generqation:

```shell
GENERATE_PDF=true mkdocs build
```

## Under the Hood

The site is built with [MkDocs](https://www.mkdocs.org/),
[MkDocs Multirepo Plugin](https://github.com/jdoiro3/mkdocs-multirepo-plugin/tree/main),
and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material).
For development, everything is powered by Dev Containers and GitHub Actions.

## Talks

The site contains a Speaking site, which is expected to convert to a separate plugin later.
Forks and contributions are welcome!

### Talk Metadata

Use `presented` for events where a talk was delivered and `cancelled` for cancelled appearances.
Both fields accept a list of events with `event`, `year`, `month`, `url`, `location`, and `note` as applicable.

Set `status` in a talk or workshop's front matter to control its listing:

- `highlighted` displays the item prominently at the top of its section.
- `normal` displays it normally and is the default when `status` is omitted.
- `collapsed` places it behind the section's **More talks** button. Without JavaScript,
  collapsed items remain visible.
- `hidden` excludes it from the listing and tag cloud.

Items in each status are sorted by title. These settings affect the lists only:
the individual pages remain published and may appear in site search.

## Localization

The default language of the website is English.
Some pages are in French.
For that, the [mkdocs-static-i18n](https://github.com/ultrabug/mkdocs-static-i18n) plugin is used on the top of the default Material for MkDocs functionality.

## License

<p xmlns:cc="https://creativecommons.org/ns#" xmlns:dct="https://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/oleg-nenashev/oleg-nenashev">This site</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/oleg-nenashev/">Oleg Nenashev</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p>
