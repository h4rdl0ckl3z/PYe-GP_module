class e_GP:
    def __new__(self, dept_ids):
        from urllib.request import urlopen
        from urllib.error import URLError, HTTPError
        import xml.etree.ElementTree as ET

        base_url = 'http://process3.gprocurement.go.th/EPROCRssFeedWeb/egpannouncerss.xml'
        anounce_types = ['W0', 'W2', 'B0', 'D0', 'D1', 'D2', 'P0', 'W1', '15']

        list_data = {
            'title': [],
            'link': [],
            'pubDate': [],
            'anounceType': [],
            'egpid': []
        }

        try:
            for anounce_type in anounce_types:
                for dept_id in dept_ids:
                    url = f"{base_url}?deptId={dept_id}&anounceType={anounce_type}"
                    res = urlopen(url)
                    tree = ET.parse(source=res, parser=ET.XMLParser(encoding='cp874')).getroot()
                    for root in tree.findall('./channel/item'):
                        list_data['egpid'].append(dept_id)
                        list_data['anounceType'].append(anounce_type)
                        for rss in root:
                            if rss.tag not in ('description', 'guid'):
                                list_data[rss.tag].append(rss.text)
        except (URLError, HTTPError, ConnectionError, ET.ParseError) as err:
            print(f"Error fetching data: {err}")

        return list_data
