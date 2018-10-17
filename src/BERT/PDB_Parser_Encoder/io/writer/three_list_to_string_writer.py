import logging

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Util: Three Lists into Single String")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)

def three_list_to_string(three_list):
    """
    Util: concatenates three lists into a single string
    :param three_list:
    :return:
    """
    content = ''
    for element in three_list:
        for x in element:
            for y in x:
                content += str(y) + ','
        content = content[:-1]
        content += '\n'
    return content
