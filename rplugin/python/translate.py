from os import path
import tempfile
import pynvim
from googletrans import Translator


@pynvim.plugin
class TranslatePlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim
        self.engin = Translator()
        self.dest_lang = self.nvim.vars.get('translate_dest_lang', 'zh-TW')


    @pynvim.command("Translate", range='', nargs='*')
    def translate(self, args, range):
        """Translate the current line"""
        wait_for_translate = self.nvim.current.line
        self.post_vim_message('Translating...')
        self.post_vim_message(self.engin.translate(wait_for_translate, dest=self.dest_lang).text.strip(), warning=False)


    @pynvim.command("TranslateAll", range='', nargs='*')
    def translate_all(self, args, range):
        """Translate the all paragraphs"""
        def to_paragraphs(lines):
            paragraphs = [""]
            for raw_line in lines:
                line = raw_line.strip()
                if line:
                    paragraphs[-1] += line
                else:
                    paragraphs += ["", ""]
            if not paragraphs[-1]:
                paragraphs.pop()
            return paragraphs

        wait_for_translate = to_paragraphs(self.nvim.current.buffer[:])
        self.post_vim_message('Translating...')
        self.nvim.command('vsplit ' + path.join(tempfile.gettempdir(), 'nvim-translate.txt'))
        def paragraph_translate(p):
            return  self.engin.translate(p, dest=self.dest_lang).text if p else ""
        translated_patagraph = list(map(paragraph_translate, wait_for_translate))
        self.nvim.current.buffer[:] = translated_patagraph
        self.post_vim_message('Translation completed')


    # This function was refactor from YouCompleteMe vimsupport.py
    # Calling this function from the non-GUI thread will sometimes crash Vim. At
    # the time of writing, YCM only uses the GUI thread inside Vim (this used to
    # not be the case).
    def post_vim_message(self, message, warning = True, truncate = False ):
      """Display a message on the Vim status line. By default, the message is
      highlighted and logged to Vim command-line history (see :h history).
      Unset the |warning| parameter to disable this behavior. Set the |truncate|
      parameter to avoid hit-enter prompts (see :h hit-enter) when the message is
      longer than the window width."""
      echo_command = 'echom' if warning else 'echo'

      # Displaying a new message while previous ones are still on the status line
      # might lead to a hit-enter prompt or the message appearing without a
      # newline so we do a redraw first.
      self.nvim.command( 'redraw' )

      if warning:
        self.nvim.command( 'echohl WarningMsg' )

      message = to_unicode( message )

      if truncate:
        # self.nvim_width = get_int_value( '&columns' )

        message = message.replace( '\n', ' ' )
        if len( message ) > self.nvim_width:
          message = message[ : self.nvim_width - 4 ] + '...'

        # old_ruler = get_int_value( '&ruler' )
        # old_showcmd = get_int_value( '&showcmd' )
        self.nvim.command( 'set noruler noshowcmd' )

        self.nvim.command( "{0} '{1}'".format( echo_command,
                                         escape_for_vim( message ) ) )

        # SetVariableValue( '&ruler', old_ruler )
        # SetVariableValue( '&showcmd', old_showcmd )
      else:
        for line in message.split( '\n' ):
          self.nvim.command( "{0} '{1}'".format( echo_command,
                                           escape_for_vim( line ) ) )

      if warning:
        self.nvim.command( 'echohl None' )

# This function was refactor from YouCompleteMe utils.py
# Returns a unicode type; either the new python-future str type or the real
# unicode type. The difference shouldn't matter.
def to_unicode( value ):
  if not value:
    return str()
  if isinstance( value, str ):
    return value
  if isinstance( value, bytes ):
    # All incoming text should be utf8
    return str( value, 'utf8' )
  return str( value )


# This function was refactor from YouCompleteMe utils.py
# def get_int_value( variable ):
#   return int( vim.eval( variable ) )


# This function was refactor from YouCompleteMe utils.py
def escape_for_vim( text ):
  return to_unicode( text.replace( "'", "''" ) )
