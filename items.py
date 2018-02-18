pkg_dnf = {
    'vim-enhanced': {},
}

actions = {
    'git_deploy_vim': {
        'command': 'git clone --depth=1 git://github.com/amix/vimrc.git ~/.vim_runtime',
        'unless': 'file -E ~/.vim_runtime',
        'needs': ['pkg_dnf:git'],
        'triggers': ['action:install_vim'],
    },
    'install_vim': {
        'command': 'sh /root/.vim_runtime/install_basic_vimrc.sh',
        'triggered': True,
        'needs': ['pkg_dnf:vim-enhanced'],
    },
}
