import neovim
from googletrans import Translator


@neovim.plugin
class TestPlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim
        self.engin = Translator()


    @neovim.command("Translate", range='', nargs='*')
    def translate(self, args, range):
        """Translate the current line"""
        # TODO translate language as config
        #self.nvim.command('echo ' + self.engin.translate(self.nvim.current.line, dest='en').text.strip())
        self.nvim.current.line += self.engin.translate(self.nvim.current.line, dest='zh-TW').text.strip()

