import dracula.draw

# Load existing settings made via :set
config.load_autoconfig(True)

dracula.draw.blood(c, {
    'spacing': {
        'vertical': 6,
        'horizontal': 8
    }
})

c.statusbar.show = 'in-mode'

#config.bind('xs', 'config-cycle statusbar.show always never')
#config.bind('xt', 'config-cycle tabs.show always never')
#config.bind('po', 'config-cycle bind set content.proxy http://localhost:8080/;; config-unset content.proxy')
config.bind('po', 'set content.proxy http://localhost:8080/')
config.bind('pi', 'config-unset content.proxy')

# default size
c.fonts.web.size.default = 20

#config.source('themes/onedark.py')
