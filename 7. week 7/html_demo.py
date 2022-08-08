import sys


class Tag(object):

    def __init__(self, name, content, **attributes):
        self.name = name
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.content = content
        # self.attributes = list()
        self.att = ''
        if attributes:  # here attributes are handled if a tag has one or more actually the string of attributes are
            # created
            for key in attributes:
                self.att += f'{key}={attributes[key]} '
        self.att.strip()

    def __str__(self):
        if self.att:
            self.start_tag = '<{} {}>'.format(self.name, self.att)  # here the attributes are added to the starter tag
        return '{0.start_tag}{0.content}{0.end_tag}'.format(self)  # *important nice way to write string formatting

    def display(self):
        print(self)

    # def handel_attribute(self):  # we don't need this method because attributes are handled in __init__()
    #     pass


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
    # doc2 = DocType(2)  if uncomment this part of code it does not work after this line
    # doc2.display()

    tagWithContents = Tag('t1', 'this is a tag with content', id="123", Class="class_One")
    tagWithContents.display()







