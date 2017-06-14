import neovim


@neovim.plugin
class TestPlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.function("TestFunction", sync=True)
    def testfunction(self, args):
        return 3

    @neovim.command("TestCommand", range='', nargs='*')
    def testcommand(self, args, range):
        # self.nvim.current.line = ('Command with args: {}, range: {}'
        #                          .format(args, range))
        self.nvim.current.line = str(self.nvim.current.range)

    @neovim.autocmd('BufEnter', pattern='*.py', eval='expand("<afile>")', sync=True)
    def on_bufenter(self, filename):
        self.nvim.out_write("testplugin is in " + filename + "\n")

# nvim
#['api', 'async_call', 'buffers', 'call', 'channel_id', 'chdir', 'command', 'command_output', 'current', 'err_write', 'error', 'eval', 'feedkeys', 'foreach_rtp', 'from_nvim', 'from_session', 'funcs', 'input', 'list_runtime_paths', 'metadata', 'new_highlight_source', 'next_message', 'options', 'out_write', 'quit', 'replace_termcodes', 'request', 'run_loop', 'session', 'stop_loop', 'strwidth', 'subscribe', 'tabpages', 'types', 'ui_attach', 'ui_detach', 'ui_try_resize', 'unsubscribe', 'vars', 'version', 'vvars', 'windows', 'with_decode']

# nvim.current
#['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_session', 'buffer', 'line', 'range', 'tabpage', 'window']


