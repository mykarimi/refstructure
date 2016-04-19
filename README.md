#Referemce Restructuring Module version 3.0

This package restructs a texts that contains foonotes within the text. This package uses the nltk toolkit to tokenize sentences and replace the footnotes to the end of the document. The script is not generic, it is only applicabel to texts that are of the same format as the example.in.txt that can be found in the unstructured/ folder

- Author: M. Yassine Karimi
- Date: October the , 2016
- Modeling Perspectives in Philosophy
- Computational Lexicology and Terminology Lab
- Vrije Universiteit Amsterdam

##Requirements
- Mac OS X Terminal or Linux OS Terminal installed
- Installed version of Python 3.0 or higher (script was built on 3.4)
- KafNafParser for Python (which can be installed by the following command):

            - pip install KafNafParserPy

- Natural Language Processing Toolkit (which can be installed by the following command)

            - pip install nltk

- XML v1.0 or higher
- Text editor (Sublime Text 2, gedit)


##Setup
Download the complete github repository with the follwing command to a chosen location:

            - git clone https://github.com/mykarimi/refstructure
            
##Quick startup guide
- In order to run the Reference Restructure Module, the user must go to the main folder of the module

            - cd location_of_folder/refsructure
            
- Put the textfiles that you want to proces in the folder

            - refstruct/unstructured

- When in the main folder run the command

            - ./resfstruct.sh
            
- The restructured text files should now be in 

            - /pathtomainfolder/restruct/restructured 
            
