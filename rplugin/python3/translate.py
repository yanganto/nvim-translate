from os import path
import tempfile
import pynvim
from googletrans import Translator
from enum import Enum

class DisplayType(Enum):
    STATUS = 0
    POPUP = 1

@pynvim.plugin
class TranslatePlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim
        self.engin = Translator()

        # please use local string such as 'zh-TW', 'ja', default is 'zh-TW'
        self.dest_lang = self.nvim.vars.get('translate_dest_lang', 'zh-TW')

        # the spacer between lines,
        # some plugin will automatically trim the space in the end of line
        # so the spacer set " " as default for english
        # if you are using different language, this may set as ""
        self.v_line_spacer = self.nvim.vars.get('translate_v_line_spacer', " ")

        # NOTE: The config is auto use 'pop' for you
        # setup display options, status, pop
        self.display_option = DisplayType.STATUS if self.nvim.vars.get('translate_display_option') == 'status' else DisplayType.POPUP

        self.wording_transformer = []

        # use 0, 1 to enable or disable the snake style correction, default is 1
        if int(self.nvim.vars.get('translate_correct_snake_style', 1)):
            self.wording_transformer.append(lambda x: x.replace('_', ' '))


    @pynvim.command("Translate", range='', nargs='*')
    def translate(self, args, range):
        """Translate the current line"""
        wait_for_translate = self.v_line_spacer.join(self.nvim.current.buffer[range[0] - 1:range[1]])
        self.post_vim_message('Translating...')

        for f in self.wording_transformer:
            wait_for_translate = f(wait_for_translate)

        self.display(
            self.engin.translate(wait_for_translate, dest=self.dest_lang).text.strip(),
            warning=False)


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

        def paragraph_translate(raw_paragraph):
            input_paragraph = raw_paragraph
            for f in self.wording_transformer:
                input_paragraph = f(input_paragraph)
            return self.engin.translate(input_paragraph, dest=self.dest_lang).text if input_paragraph else ""
        translated_patagraph = list(map(paragraph_translate, wait_for_translate))
        self.nvim.current.buffer[:] = translated_patagraph
        self.post_vim_message('Translation completed')


    def post_vim_message(self, message, warning=True, truncate=False):
        """Display a message on the Vim status line. By default, the message is
        highlighted and logged to Vim command-line history (see :h history).
        Unset the |warning| parameter to disable this behavior. Set the |truncate|
        parameter to avoid hit-enter prompts (see :h hit-enter) when the message is
        longer than the window width."""
        # Calling this function from the non-GUI thread will sometimes crash Vim. At
        # the time of writing, YCM only uses the GUI thread inside Vim (this used to
        # not be the case).
        echo_command = 'echom' if warning else 'echo'

        # Displaying a new message while previous ones are still on the status line
        # might lead to a hit-enter prompt or the message appearing without a
        # newline so we do a redraw first.
        self.nvim.command('redraw')

        if warning:
            self.nvim.command('echohl WarningMsg')

        message = to_unicode(message)

        if truncate:
            message = message.replace('\n', ' ')
            if len(message) > self.nvim_width:
                message = message[:self.nvim_width - 4] + '...'

            self.nvim.command('set noruler noshowcmd')

            self.nvim.command("{0} '{1}'".format(echo_command, escape_for_vim(message)))

        else:
            for line in message.split('\n'):
                self.nvim.command("{0} '{1}'".format(echo_command, escape_for_vim(line)))

            if warning:
                self.nvim.command('echohl None')

    def pop(self, message, warning=True, truncate=False):
        # TODO
        # work on here, warning and truncate is not the requirement, but please some note for me,
        # so I can do this part by my self thanks.
        _id = createWindow(self.nvim, [message], 2);

        # following line is can be removed when pop window is done
        self.post_vim_message("[POPWINDOW]" + message, warning=True, truncate=False)

    def display(self, message, warning=True, truncate=False):
        if self.display_option == DisplayType.POPUP:
            self.pop(message, warning=True, truncate=False)
        else:
            self.post_vim_message(message, warning=True, truncate=False)

def to_unicode(value):
    if not value:
        return str()
    if isinstance(value, str):
        return value
    if isinstance(value, bytes):
        # All incoming text should be utf8
        return str(value, 'utf8')
    return str(value)

def escape_for_vim(text):
    return to_unicode(text.replace("'", "''"))

def createWindow(nvim, textArray, min_height = 1, width=20, closeLastWindow=True):
    """
    Creates a floating window in nvim. The window position is relative to the cursor and is offset by one column.

    Returns:
        The handle (ID) of the window, or 0 on error

    TODO:
        Add functionality to customize background and foreground colors
    """

    # Proper error-raising will be added later
    assert(len(textArray) > 0);

    # Close the last created window
    if(closeLastWindow and bool(nvim.eval("exists('win')"))):
      closeWindow(nvim);

    vimScriptCommand = f"""
    let buf = ''\n let buf = nvim_create_buf(v:false, v:true)
    call nvim_buf_set_lines(buf, 0, -1, v:true, {str(textArray)})
    let opts = {{'relative':'cursor', 'width': {width}, 'height': {max(len(textArray), min_height)}, 'col': 1, 'row': 0, 'anchor': 'NW', 'style': 'minimal'}}
    let win = nvim_open_win(buf, v:true, opts)
    """;
    nvim.command(vimScriptCommand)

    # Return the ID of the window
    return nvim.eval("win");

def closeWindow(nvim, windowID = None):
    """Close a window based on an ID, or close the most recently created window"""

    if(windowID == None):
        windowID = nvim.eval("win")
    nvim.command(f"call nvim_win_close({windowID}, v:false)")
