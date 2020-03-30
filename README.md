# Neovim Translate
- A neovim plugin for translate
- version 0.0.7

## Requirement
- neovim
- Python
- googletrans (PYPI package)
- pynvim (PYPI package)
- `develop` branch is for the OS using python3 as default
- `master` branch is for the OS using python2 as default


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
- `:TranslateByte`
  - Like the `Translate` command, and translate a array of numbers into String
  - It's a good tool for Rust code debuging
- If you update the script, please use `:UpdateRemotePlugins` to update the new commands

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
- 0.0.7 - Translate byte array into UTF-8 string
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
