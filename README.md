# Mirage Linemode

Customizable linemode plugin for [ranger](https://ranger.github.io/).

![mirage_linemode](https://raw.githubusercontent.com/hankei6km/mirage_linemode/master/images/mirage_linemode.png)
* Display folder icon :file_folder:, file icon :page_facing_up: by using emoji.
* Assign icon to XDG User directory and special directories/files(ie. `setup.cfg` `package.json`  `tests` etc).

mirage\_linemode has been strongly influenced by [ranger\_devicons](https://github.com/alexanderjeurissen/ranger_devicons.git)


## Installation

Install package and initialize.

```
# pip install mirage_linemode
$ mirage_linemode_ctrl init
```


## Usage

Enable plugin.

```
$ mirage_linemode_ctrl enable
```


## Uninstallation

```
$ mirage_linemode_ctrl disable
# pip uninstall mirage_linemode
```

and,

Remove `<xdg config home>/mirage-linemode` directory, if you want to clean up cutomized files.
(In many cases, `<xdg config home>` may be `$HOME/.config`)


## Theme

Mirage Linemode imports `<xdg config home>/mirage-linemode/mirage_linemode_theme.yml` as theme when plugin activated every time.

Further info,
See [README_ja.md](https://github.com/hankei6km/mirage_linemode/blob/master/README_ja.md).


## License

Copyright (c) 2018 hankei6km

Licensed under the MIT License. See LICENSE.txt in the project root.
