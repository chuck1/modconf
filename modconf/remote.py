
import async_patterns

class Request:
    def __init__(self, key, id_, args):
        self.key = key
        self.id_ = id_
        self.args = args
    async def __call__(self, proto):
        cm = proto.config_manager
        c = cm.get(self.id_)(*self.args)
        proto.write(Response(c, self.message_id))

class Response:
    def __init__(self, c, response_to):
        self.c = c
        self.response_to = response_to
    async def __call__(self, proto):
        pass

async def import_class(self, loop, host, port, key, mod_name, cls_name, args):

    conf = modconf.import_class('ws_controller.tests.conf.simple', 'Conf', ('DEVELOP',))

    coro = loop.create_connection(functools.partial(async_patterns.protocol.Protocol, loop), host, port)
    
    _, proto = await coro
    
    resp = await proto.write(modconf.remote.Request(
        key, 
        'import_class', 
        (mod_name, cls_name, args)))
    
    return resp.c

