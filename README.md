# Neovim Translate
- A neovim plugin for translate
- version 0.0.6

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

```vim
" use local string to setup the target language such as 'zh-TW', 'ja', 
" default is 'zh-TW'
let g:translate_dest_lang='ja'
" the spacer between lines,
" some plugin will automatically trim the space in the end of line
" so the spacer set " " as default for english
" if you are using different language, this may set as ""
let g:translate_v_line_spacer=" "
" use 0, 1 to enable or disable the snake style correction, default is 1
let g:translate_correct_snake_style=1
```

## Change log
- 0.0.6 - Handle snake style wording
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
