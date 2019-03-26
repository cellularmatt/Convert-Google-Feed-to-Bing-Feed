import wget
import os
import settings as cfg

def get_xml():
    url = cfg.GOOGLE_FILE

    filename = wget.filename_from_url(url)

    for file in os.listdir(os.getcwd()):
        if file == filename:
            print('File, ' + file + ', already exists!')
            os.remove(file)
            print('File, ' + file + ', has been removed')

    xml = wget.download(url)

    print('File, ' + filename + ', has been downloaded')
