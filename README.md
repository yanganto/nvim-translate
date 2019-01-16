# Neovim Translate
- A nvim plugin for translate
- version 0.0.4

## Requirement
- Python
- googletrans (PYPI package)
- pynvim (PYPI package)


## Installing
- `pacman -S neovim python-neovim`

## Usage
- `:Translate`
		- translate the current line
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

## Thanks
Thanks [YouCompleteMe](https://github.com/Valloric/YouCompleteMe) contributor and Google Inc.
This plugin use lots of function from YouCompleteMe within GNU licence.
