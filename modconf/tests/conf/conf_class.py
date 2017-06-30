
class Conf(object):
    @classmethod
    def prepare(cls, *args):
        print('args = {}'.format(args))
        cls.args = args

