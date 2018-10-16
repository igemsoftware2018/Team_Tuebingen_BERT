import logging

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("ddG Training Dataset Parser")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def write_ddG_trainings_data(angstrom, data):
    """
    writes the training data to a file for subsequent usage
    :param angstrom:
    :param data:
    :return:
    """
    with open('data/regression_trainings_data/contact_blomap_' + str(angstrom) + 'A.csv', 'w') as f:
        content = ''
        for element in data:
            for x in element:
                for y in x:
                    content += str(y) + ','
            content = content[:-1]
            content += '\n'
        f.write(content)
