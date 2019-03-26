# This script reads the xml file
# Remove the unnecessary information
# Edit and remove certain text from the tag
import re

def edit_xml():
    xmlRegex = re.compile('^<\?.*')
    rssRegex = re.compile('^<rss.*')
    xmlnsRegex = re.compile('^xmlns.*')
    atomRegex = re.compile('^<atom.*>')
    gRegex = re.compile('g:')
    endRegex = re.compile('<\/rss>')


    xml = open('google_base.xml_products_cpc.xml', 'r')

    f = open('edited.xml', 'w')

    for line in xml:
        if bool(xmlRegex.match(line)):
            print('skipped ' + line)
            continue
        elif bool(rssRegex.match(line)):
            print('skipped ' + line)
            continue
        elif bool(xmlnsRegex.match(line)):
            print('skipped ' + line)
            continue
        elif bool(atomRegex.match(line)):
            print('skipped ' + line)
            continue
        elif line == '</channel></rss>':
            f.write('</channel>')
        else:
            f.write(re.sub(gRegex, '', line))


    f.close()
