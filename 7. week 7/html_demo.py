import sys


class Tag(object):

    def __init__(self, name, content, **attributes):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.content = content
        self.attributes = dict()

    def __str__(self):
        return '{0.start_tag}{0.content}{0.end_tag}'.format(self)  # *important nice way to write string formatting

    def display(self):
        print(self)

    def handel_attribute(self):
        pass


class DocType(Tag):
    def __init__(self, version):
        if version == 1:
            name = '!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" ' \
                   '"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"'
        elif version == 4:
            name = '!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"' \
                   ' "http://www.w3.org/TR/html4/loose.dtd"'
        elif version == 5:
            name = '!DOCTYPE html'
        else:
            print('version is not acceptable')
            sys.exit(-1)
        super().__init__(name=name, content='')
        self.end_tag = ''


class Head(Tag):
    def __init__(self):
        super().__init__(name='head', content='')
        self.head_contents = list()

    def add_content(self, content):
        pass


class Body(Tag):
    pass


if __name__ == '__main__':
    myTag = Tag('myTag', 'simple content')
    print(myTag)  # it gives from __str__()
    myTag.display()

    doc = DocType(5)
    doc.display()
    doc2 = DocType(2)
    doc2.display()








