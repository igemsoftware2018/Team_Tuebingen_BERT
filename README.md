[![Build Status](https://travis-ci.org/steffenlem/Deimmunization.svg?branch=master)](https://travis-ci.org/steffenlem/Deimmunization)
[![codecov](https://codecov.io/gh/steffenlem/Deimmunization/branch/master/graph/badge.svg)](https://codecov.io/gh/steffenlem/Deimmunization)

# BERT 
BERT is a powerful workflow for the automated deimmunization of proteins. BERT is based on three modular tools: EvoCS, MHCBoost or alternatively NetMHCIIPan and CoReM.
Please refer to our wiki for details: [Software](http://2018.igem.org/Team:Tuebingen/Software).


Quick Setup for users
=====
1. <code>$ git clone https://github.com/steffenlem/Deimmunization</code>
2. <code>$ python setup.py install</code>
3. Installation of NetMHCIIpan (http://www.cbs.dtu.dk/cgi-bin/nph-sw_request?netMHCIIpan) 
4. <code>$ BERT</code>

We are unfortunately not allowed to ship NetMHCIIPan, but for academic users it's free of charge.
If you have any issues with the setup, please don't hesitate to contact us on igem@ifib.uni-tuebingen.de  .

Usage
=====

## The CLI - Command Line Interface

```
$ deimmunization --help
Options:
  -in, --input_msa <arg>          file path to msa.txt  [required]
  -rs, --reference_sequence <arg> titlestring of reference sequence
                                  [required]
  -t, --majority_threshold <val>  value between 0 and 1 to decide the
                                  consensus value  [required]
  -a, --mhc_alleles <arg>         Input the MHC allele in the following form:
                                  MHC-I: e.g. XXX-000 
                                  MHC-II: e.g. DRB1_0101
                                  It is also possible (and recommended) to
                                  choose multiple alleles. The alleles have to
                                  be comma separated. 
                                  e.g.; DRB1_0101,
                                  DRB1_0202, DRB1_0303, ...  [required]
  -mp, --mhc_ii_pan <arg>         path to netMHCIIpan  [required]
  -mt, --number_mutations <val>   the number of mutation which should be
                                  introduced in the sequence  [required]
  -pos, --pos_to_check <val>      the number of positions to check to
                                  introduce a mutation in each iteration
                                  [required]
  -pdb, --pdb_file <arg>          path to pdb file  [required]
  -cha, --pdb_chain <arg>         Chain in the pdb file  [required]
  -w, --weight <val>              Weighting factor between deimmunization and
                                  ddG. A low value favors low immunity and a
                                  high valuefavors a stable protein
                                  [required]
  -frq, --allele_frequency <val>  Frequency of the alleles in the target
                                  population. The frequencies have to be comma
                                  separated  [required]
  --help                          Show this message and exit.

```


Examples
=====
Example command:    
```
BERT -in <MSApath> -rs <ref.seqMSA> -t 0.5 -a DRB1_0301,DRB1_0701,DRB1_1501 -mp <path_netMHCIIPan> -pdb <path.pdb> -pos 2 -mt 2 -cha B -w 10 -frq 0.099,0.109,0.0967    
```
You can use the following MSA, PDB and sequence files shipped with this program:
Example MSA: 'data/Isomerase_90_similarity.clustal_num'    
Example PDB: 'data/2wcv.pdb'    
Example Reference Sequence: '2WCV_Paris'    
  
Performance and Results
=====
BERT has been applied to team iGEM Paris-Bettencourt's FucU isomerase protein. The results are documented on our wiki: [Collaboration](http://2018.igem.org/Team:Tuebingen/Collaborations).

License
=====
Our tool is made available under the [MIT License](http://www.opensource.org/licenses/mit-license.php).

Authors
=====
Team iGEM 2018 Tübingen    
Steffen Lemke    
Lukas Heumos    
Alexander Röhl



