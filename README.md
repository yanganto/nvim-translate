# Neovim Translate
- A nvim plugin for translate
- version 0.0.2

## Requirement
- Python
- googletrans (PYPI package)
- neovim (PYPI package)


## Installing
- `pacman -S neovim python-neovim`

## Usage
- `:Translate`
		- translate the current line

## Settings
set translate target language as following in `init.vim`
`set g:translate_dest_lang='ja'`

## Change log
- 0.0.2 - translate destinate language setting
- 0.0.1 - basic function

## Thanks
Thanks [YouCompleteMe](https://github.com/Valloric/YouCompleteMe) contributor and Google Inc.
This plugin use lots of function from YouCompleteMe within GNU licence.
