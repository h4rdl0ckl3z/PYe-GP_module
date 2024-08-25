class e_GP:
    def __new__(self, dept_ids):
        from urllib.request import urlopen
        from urllib.error import URLError, HTTPError
        import xml.etree.ElementTree as ET

        base_url = 'http://process3.gprocurement.go.th/EPROCRssFeedWeb/egpannouncerss.xml'
        anounce_types = ['W0', 'W2', 'B0', 'D0', 'D1', 'D2', 'P0', 'W1', '15']

        myData = []

        try:
            for anounce_type in anounce_types:
                for dept_id in dept_ids:
                    url = f'{base_url}?deptId={dept_id}&anounceType={anounce_type}'
                    res = urlopen(url)
                    tree = ET.parse(source=res, parser=ET.XMLParser(encoding='cp874')).getroot()
                    list_data = {}
                    for item in tree.findall('./channel/item'):
                        list_data = {rss.tag: rss.text for rss in item if rss.tag not in ('description', 'guid')}
                        list_data['anounceType'] = anounce_type
                        list_data['egpid'] = dept_id
                    myData.append(list_data)
                    list_data.clear()
        except (URLError, HTTPError, ConnectionError, ET.ParseError) as err:
            print(f'Error fetching data for dept_id {dept_id} and anounce_type {anounce_type}: {err}')

        return myData
