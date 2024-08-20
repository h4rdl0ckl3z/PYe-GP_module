class e_GP:
    def __new__(self, deptId_):
        from urllib.request import urlopen
        from urllib.error import URLError, HTTPError
        import xml.etree.ElementTree as ET

        url = 'http://process3.gprocurement.go.th/EPROCRssFeedWeb/egpannouncerss.xml'
        parameter_deptId = '?deptId='
        parameter_anounceType = '&anounceType='

        anounceType_ = ['W0', 'W2', 'B0', 'D0', 'D1', 'D2', 'P0', 'W1', '15']

        list_data = {
            'title': [],
            'link': [],
            'pubDate': [],
            'anounceType': [],
            'egpid': []
        }

        for anounceType in anounceType_:
            for deptId in deptId_:
                url_str = url + parameter_deptId + deptId + parameter_anounceType + anounceType
                try:
                    res = urlopen(url_str)
                    try:
                        tree = ET.parse(source=res, parser=ET.XMLParser(encoding='cp874')).getroot()
                        for root in tree.findall('./channel/item'):
                            if root.tag == 'item':
                                list_data['egpid'].append(deptId)
                                list_data['anounceType'].append(anounceType)
                                for rss in root:
                                    if rss.tag == 'description' or rss.tag == 'guid':
                                        pass
                                    else:
                                        list_data[rss.tag].append(rss.text)
                            else:
                                print('No ITEMS')
                    except ET.ParseError as err:
                        print(err)
                except (URLError, HTTPError, ConnectionError) as err:
                    print(err)
        return list_data
