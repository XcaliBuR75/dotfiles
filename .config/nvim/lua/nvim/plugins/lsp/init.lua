local Lsp = require('nvim.utils.lsp')

local M = {}

local servers = {
    'bashls',
    'cssls',
    'dockerls',
    'eslint',
    'graphql',
    'html',
    'jsonls',
    'lua_ls',
    'pyright',
    'rust_analyzer',
    'tsserver',
    'volar',
    'clangd',
}

function M.setup()
    Lsp.setup(servers)
end

return M
