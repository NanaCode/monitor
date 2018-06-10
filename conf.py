PASTE_INI = "api-paste.ini"
DEFAULT_API_LOG = "monitor.log"

from oslo.config import cfg

opts = [
        cfg.StrOpt('monitor_bind_ip',
                    default = '0.0.0.0', secret = True),
        cfg.IntOpt('monitor_bind_port', 
                   default = 8010),
       ]

CONF = cfg.CONF
CONF.register_opts(opts)
config_files = getattr(CONF, 'default_config_files', [])
config_files.append('monitor.conf')

CONF(default_config_files = config_files)
