# The_role_of_discussions_in_collaborative_KGs_PhD_thesis

This repo contains code and data produced for the experiments described in the PhD thesis "The Role of Discussions in Collaborative KGs".

## **Data** 
This folder includes code for gathering and processing the data of this thesis.
* **download_Wikidata_dumps**: This is a script to download Wikidata xml dumps from https://dumps.wikimedia.org/wikidatawiki/ .
* **process_Wikidata_dumps.py**: This is a script to process the xml files and extract pages for item and property talk pages.

## **Use of Discussions** 
This folder includes code and data for the analysis in Chapter 6.
* **data**: This folder includes the sample of discussions used for the thematic analysis.
* **text_statistics.py**: This notebook processes the talk pages to separate threads and posts, and to count the words.
* **statistical_tests.py**: This script includes statistical tests for the thematic analysis results.


## **Collaboration Patterns in Discussions** 
This folder contains code and data for the analysis in Chapter 7.
* **graph_analysis.ipynb**: This notebook consists of the network analysis code.
* **statistics_data.ipynb**: This notebook includes statistical analysis and figures for the editors' features. 


## **Impact of Discussions** 
This folder contains code and data for the analysis in Chapter 8.
* **framework_analysis.ipynb**: This notebook includes the code for the text and graph embeddings, and the neural network model.
* **items_cleaned.csv.zip**: This zip includes the dataset of discussions found in item talk pages.



## **Disagreements in Discussions** 
This folder includes code and data for the analysis in Chpater 9.
* **raw_data** and **radial_trees_connections**: These folders include data for the process of radial trees.
* **radial_trees_process.ipynb**: This notebook consists of the analysis related to radial trees.
* **num_revisios_types_v2.csv** and **num_revision_usercount_editcount.csv**: These files include the data for the section Exploratory Data Analysis.
* **exploratory_data_analysis.ipynb**: This notebook includes the analysis of the section Exploratory Data Analysis.
