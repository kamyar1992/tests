import sys
# static methods: also call class methods,these methods does not instance(self), they should use by class name
# because of reducing one search

class Tag(object):

    def __init__(self, n, c, **attributes):
        self.name = n
        self.start_tag = '<{}>\n'.format(n)
        self.end_tag = '</{}>\n'.format(n)
        self.content = c
        self._temp1 = 0
        self._sample1 = ''
        self._sample2 = ''
        # python mangling rule
        self.__temp2 = 0
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
        super().__init__(n=name, c='')
        self.end_tag = ''
    # setter and getter: there are two ways for implementing this methods
    # way1:

    def sample1_setter(self, val):
        self._sample1 = val

    def sample2_getter(self):
        return self._sample1

    sample1Variable = property(sample2_getter, sample1_setter)  # methods should be added respectively without ()

class Head(Tag):
    def __init__(self):
        super().__init__(n='head', c='\n')
        self.head_contents = list()

    def add_content(self, n, c='', single=False, **att):  # this make head content tags. these tags are located inside
        new_tage = Tag(n=n, c=c, **att)                   # head tag
        if single:
            new_tage.end_tag = ''
            new_tage.content = ''
        self.head_contents.append('\t'+str(new_tage))

    def __str__(self):
        for item in self.head_contents:
            self.content += item + '\n'
        return super().__str__()

    def display(self):
        for item in self.head_contents:
            self.content += item + '\n'


class Body(Tag):
    def __init__(self):
        super().__init__(n='body', c='\n')

        self.body_contents = list()

    @staticmethod  # static method
    def define_child(n, c, single=False, child=None, **att):
        new_tag = Tag(n, c, **att)
        if single:  # single is ture
            new_tag.content = ''
            new_tag.end_tag = ''
        if child:  # if it has child
            for item in child:
                new_tag.content += '\t' + item + '\n'
        return str(new_tag)

    def add_content(self, n, c='', single=False, child=None, **att):  # this make head content tags
        new_tage = Tag(n=n, c=c, **att)
        if single:
            new_tage.end_tag = ''
            new_tage.content = ''
        if child:
            for item in child:
                new_tage.content += '\t' + item + '\n'
        self.body_contents.append(str(new_tage))

    def __str__(self):
        for item in self.body_contents:
            self.content += item + '\n'
        return super().__str__()

    def display(self):
        for item in self.body_contents:
            self.content += item + '\n'
        super().display()


class Html(object):
    def __init__(self, doc, head, body):  # aggregation: html object will be created by 3 objects
        self.doc = doc
        self.head = head
        self.body = body

    def add_content(self, n, c, single=False, child=None, section='body', **att):
        if section.lower() == 'head':
            if child:
                raise NotImplementedError('head does not have a child tag')
            else:
                self.head.add_content(n=n, c=c, single=single, **att)  # delegation
                # print(str(self.head))
        elif section.lower() == 'body':
            self.body.add_content(n=n, c=c, single=single, child=child, **att)  # delegation
        else:
            raise NotImplementedError('selected section is not supported')

    def define_child(self, n, c, single=False, child=None, **att):
        return self.body.define_child(n=n, c=c, single=single, child=child, **att)

    def display(self):
        new_tag = Tag('Html', '')
        new_tag.content = str(self.doc)
        new_tag.content += str(self.head)
        new_tag.content += str(self.body)
        new_tag.display()

    def write_in_file(self, file='html-index.html'):
        new_tag = Tag('Html', '')
        new_tag.content = str(self.doc)
        new_tag.content += str(self.head)
        new_tag.content += str(self.body)
        with open(file, 'a+') as h_file:  # a+: a means append at the end of the file and + means read/write/create
            print(new_tag, file=h_file)



if __name__ == '__main__':
    # myTag = Tag('myTag', 'simple content')
    # print(myTag)  # it gives from __str__()
    # myTag.display()
    #
    # doc = DocType(5)
    # doc.display()
    # doc2 = DocType(2)  if uncomment this part of code it does not work after this line
    # doc2.display()
    doc = DocType(version=5)  # aggregation: the existence of the doc and other two objects do not dependent on html
    head = Head()             # objects
    body = Body()
    html = Html(doc, head, body)  # the existence of html object rely on 3 objects
    # and 3 objects dependent on html object
    html.add_content('meta', '', single=True, section='head', charset="utf-8")
    html.add_content('meta', '', single=True, section='head', name="viewport", content="width=device-width, initial-scale=1")
    html.add_content('meta', '', single=True, section='head', name="generator", content="Hugo 0.101.0")
    html.add_content('title', 'Bootstrap · The most popular HTML, CSS, and JS library in the world.')

    a1 = html.define_child('a', 'Skip to main content', Class='d-inline-flex p-2 m-1', href='#content')
    div1 = html.define_child('div', '', child=(a1,),  id='container')
    html.add_content('div', '', child=(div1,), Class="container-xl")
    html.display()
    html.write_in_file()
    # tagWithContents = Tag('t1', 'this is a tag with content', id="123", Class="class_One")
    # tagWithContents.display()

    # headTage = Head()
    # headTage.add_content('meta', '', single=True, charset="utf-8")
    # headTage.add_content('meta', '', single=True, name="viewport", content="width=device-width, initial-scale=1")
    # headTage.add_content('meta', '', single=True, name="generator", content="Hugo 0.101.0")
    # headTage.add_content('title', 'Bootstrap · The most popular HTML, CSS, and JS library in the world.')
    # <meta charset = "utf-8" >
    # <meta name = "viewport" content = "width=device-width, initial-scale=1" >
    # < meta name = "generator" content = "Hugo 0.101.0" >
    # <title>Bootstrap · The most popular HTML, CSS, and JS library in the world.</title>
    # headTage.display()

    # htmlBody = Body()
    # child must be made from the inner one
    # a1 = htmlBody.define_child('a', 'Skip to main content', Class='d-inline-flex p-2 m-1', href='#content')
    # div1 = htmlBody.define_child('div', '', child=(a1,),  id='container')
    # the outer child must be added as a content:
    # htmlBody.add_content('div', '', child=(div1,), Class="container-xl")
    # htmlBody.display()



    # body

        # <div class ="container-xl">
        #     <div id='container'>
        #         <a class ="d-inline-flex p-2 m-1" href="#content" > Skip to main content < / a >
        #     </div>
        # </div>






