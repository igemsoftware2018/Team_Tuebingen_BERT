import csv
import logging

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("ddG Training Dataset Parser")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def parser_dataset():
    """
    parses ddG dataset
    removes header
    :return: whole dataset
    """
    LOG.debug("Parsing ddG training dataset")
    f = open('data/dataset_S2648_edited_tsv.csv', 'r')
    reader = csv.reader(f, delimiter=',')
    content = []
    for row in reader:
        content.append(row)
    content.remove(content[0])

    return content
