from ftplib import FTP_TLS
import settings as cfg

def upload_xml():
    ftps = FTP_TLS(cfg.BING_IP_ADDRESS)
    ftps.connect()
    ftps.login(cfg.BING_FTP_USERNAME, cfg.BING_FTP_PASSWORD)
    ftps.getwelcome()

    # Add upload code here storbinary()
    file = open('bing.txt', 'rb')
    ftps.storbinary('STOR ' + 'bing.txt', file)
    file.close()

    ftps.quit()
