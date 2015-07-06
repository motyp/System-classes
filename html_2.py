__author__ = 'student'
Presentation= 'http://noamelf.github.io/ravtech-python/lec{}#/'
home = "file:///home/student/PycharmProjects/untitled1/mi%20html.html"
with open('mi html.html','w')as index:
    index.write('<ul> \n')
    index.write('''

    <html>
    <head>
        <title>{}</title>
    </head>
    <body>
    <h1><a href={}>{}</a></h1>
    <dl> '''.format("Welcome",home,"my file"))
    l=[]
    for i in range(1,7):
        l.append('<dt>lec {}:</dt>'.format(i)+'<dd><a href='+Presentation.format(i) +'>Presentation</a></dd>')
    index.write(''.join(l))

    index.write('''\n</body>
    </html>
    </ul>''')
#<sup>2</sup>

