# Neovim Translate
- A neovim plugin for translate
- version 0.0.5

## Requirement
- neovim
- Python
- googletrans (PYPI package)
- pynvim (PYPI package)


## Dependency
- `pip install googletrans pynvim`

## Usage
- `:Translate`
  - translate the current line
- `:'<,'>Translate`
  - V-LINE mode
  - translate the selected lines
  - Ex: `:39,40Translate` will translate the line 39 to line 40
  - or use `shift` + `v` to select the lines than press `:Translate`
- `:TranslateAll`
  - translate all the content in the current window

## Settings
set translate target language as following in `init.vim`
`set g:translate_dest_lang='ja'`

## Change log
- 0.0.5 - support V-Line select mode
- 0.0.4 - update pynvim package
- 0.0.3 - translate full paragraph function
- 0.0.2 - translate destinate language setting
- 0.0.1 - basic function

## Snapshot
![snapshot](https://raw.githubusercontent.com/yanganto/nvim-translate/master/snapshot.png)

## Thanks
Many thanks for [YouCompleteMe](https://github.com/Valloric/YouCompleteMe) contributor and Google Inc.
This plugin use lots of function from YouCompleteMe within GNU licence.
