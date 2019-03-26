import xml.etree.ElementTree as ET
import csv
import html
import re

def convert_xml():
    urlRegex = re.compile('\?utm[^.]*#googlebase')

    tree = ET.parse('edited.xml')
    root = tree.getroot()

    product_data = open('bing.txt', 'w', newline='')
    csvwriter = csv.writer(product_data, delimiter='\t')

    header = []
    gtin_missing_array = []

    count = 0
    mpn_missing = 0
    gtin_missing = 0
    label_0_missing = 0
    label_1_missing = 0
    label_2_missing = 0
    label_3_missing = 0

    for item in root.findall('item'):
        data = []
        
        # this gets the initial header row
        if count == 0:
            header.append(item.find('id').tag)
            header.append(item.find('title').tag)
            header.append(item.find('description').tag)
            header.append(item.find('google_product_category').tag)
            header.append(item.find('product_type').tag)
            header.append(item.find('link').tag)
            header.append(item.find('image_link').tag)
            header.append(item.find('condition').tag)
            header.append(item.find('availability').tag)
            header.append(item.find('price').tag)
            header.append(item.find('brand').tag)
            header.append(item.find('mpn').tag)
            header.append(item.find('gtin').tag)
            header.append(item.find('custom_label_0').tag)
            header.append(item.find('custom_label_1').tag)
            header.append(item.find('custom_label_2').tag)
            header.append(item.find('custom_label_3').tag)
            csvwriter.writerow(header)

        data.append(item.find('id').text)
        data.append(item.find('title').text)
        data.append(html.escape(item.find('description').text))
        data.append(item.find('google_product_category').text)
        data.append(item.find('product_type').text)
        data.append(re.sub(urlRegex, '', item.find('link').text))
        data.append(item.find('image_link').text)
        data.append(item.find('condition').text)
        data.append(item.find('availability').text)
        data.append(item.find('price').text)
        data.append(item.find('brand').text)
        if item.find('mpn') != None:
            data.append(item.find('mpn').text)
        else:
            mpn_missing += 1
            data.append('\t')
        if item.find('gtin') != None:
            data.append(item.find('gtin').text)
        else:
            gtin_missing += 1
            gtin_missing_array.append(item.find('title').text)
            data.append('\t')
        if item.find('custom_label_0') != None:
            data.append(item.find('custom_label_0').text)
        else:
            label_0_missing += 1
            data.append('\t')
        if item.find('custom_label_1') != None:
            data.append(item.find('custom_label_1').text)
        else:
            label_1_missing += 1
            data.append('\t')
        if item.find('custom_label_2') != None:
            data.append(item.find('custom_label_2').text)
        else:
            label_2_missing += 1
            data.append('\t')
        if item.find('custom_label_3') != None:
            data.append(item.find('custom_label_3').text)
        else:
            label_3_missing += 1
            data.append('\t')
        count += 1
        csvwriter.writerow(data)

    product_data.close()

    print('Converted: ' + str(count) + ' rows')
    print('MPN Missing: ' + str(mpn_missing))
    print('GTIN Missing: ' + str(gtin_missing))
    print('Label 0 Missing: ' + str(label_0_missing))
    print('Label 1 Missing: ' + str(label_1_missing))
    print('Label 2 Missing: ' + str(label_2_missing))
    print('Label 3 Missing: ' + str(label_3_missing))
    print('\nMissing GTIN from these Listings:\n')
    for i in gtin_missing_array:
        print(i)
