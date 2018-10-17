import logging
import warnings

from Bio.PDB import PDBParser
from Bio.PDB.PDBExceptions import PDBConstructionWarning

from src.BERT.PDB_Parser_Encoder.io.parser.ddG_trainings_dataset_parser import parser_dataset
from src.BERT.PDB_Parser_Encoder.io.parser.parse_pdb import get_contact_info
from src.BERT.PDB_Parser_Encoder.io.writer.ddG_trainings_data_writer import write_ddG_trainings_data
from src.BERT.PDB_Parser_Encoder.model.encoding import blopmap_encode_one_letter


console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("ddG Regression Test Data Writer")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)

def write_test_data_for_ddg_regression():
    """
    Writes the test data for subseq
    """
    warnings.simplefilter('ignore', PDBConstructionWarning)
    ddG_dataset = parser_dataset()
    angstroms = [7]  # 6, 8, 10, 12]
    for a in angstroms:
        test_data = []
        for entry in ddG_dataset:
            path = 'data/pdb_files/' + entry[0] + '.pdb'
            structure = PDBParser().get_structure('X', path)
            """
            model = structure[0]
            dssp = DSSP(model, path)
            for residue in list(dssp.keys()):
                if (x[1], (' ', x[3], ' ')) == residue:
                    print(dssp[residue])
            """
            # Compute contact information for residue x
            element = get_contact_info(structure, path, entry[1], a, int(entry[3]))
            element[1].extend(blopmap_encode_one_letter(entry[4]))
            element[len(element)-1].append(float(entry[7]))
            test_data.append(element)
        write_ddG_trainings_data(a, test_data)
