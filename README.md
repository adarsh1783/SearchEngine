# SearchEngine
A simple search engine build using gensim LSI model. 

### Runing the Project
```bash
$ python3 main.py -dataset Path_to_dataset -out_folder Path_output_folder/ -segmenter punkt -tokenizer ptb -IRmodel gensim
```
Options 
```bash
$ python3 main.py --help
usage: main.py [-h] [-dataset DATASET] [-out_folder OUT_FOLDER] [-segmenter SEGMENTER] [-tokenizer TOKENIZER] [-custom]
               [-IRmodel IRMODEL]

main.py

optional arguments:
  -h, --help            show this help message and exit
  -dataset DATASET      Path to the dataset folder
  -out_folder OUT_FOLDER
                        Path to output folder
  -segmenter SEGMENTER  Sentence Segmenter Type [naive|punkt]
  -tokenizer TOKENIZER  Tokenizer Type [naive|ptb]
  -custom               Take custom query as input
  -IRmodel IRMODEL      module name for information retrieval [naive|gensim]

```

### Running on Cranfield Dataset
```bash
$ python3 main.py -dataset ../../cranfield/ -out_folder output/ -segmenter punkt -tokenizer ptb -IRmodel gensim
Precision, Recall and F-score @ 1 : 0.7066666666666667, 0.1215685933425052, 0.19895198255542085
MAP, nDCG @ 1 : 0.7066666666666667, 0.7066666666666667
Precision, Recall and F-score @ 2 : 0.6177777777777778, 0.20506008780912888, 0.2897749207457946
MAP, nDCG @ 2 : 0.7577777777777778, 0.7468259398570983
Precision, Recall and F-score @ 3 : 0.5451851851851848, 0.2627050699999531, 0.33028458329864724
MAP, nDCG @ 3 : 0.7674074074074076, 0.7602296975165828
Precision, Recall and F-score @ 4 : 0.49, 0.30427728818529876, 0.34860173082567114
MAP, nDCG @ 4 : 0.7529629629629631, 0.7519621680551742
Precision, Recall and F-score @ 5 : 0.441777777777778, 0.3371924175854856, 0.35443323363776547
MAP, nDCG @ 5 : 0.7404876543209876, 0.7459000164802987
Precision, Recall and F-score @ 6 : 0.41111111111111126, 0.3681053398121334, 0.35967001016513084
MAP, nDCG @ 6 : 0.730754320987654, 0.7450419429521669
Precision, Recall and F-score @ 7 : 0.3873015873015876, 0.3999642735561248, 0.3640203224044782
MAP, nDCG @ 7 : 0.7204326278659609, 0.7432934165162283
Precision, Recall and F-score @ 8 : 0.36333333333333334, 0.42279887315091064, 0.3616483801314161
MAP, nDCG @ 8 : 0.7115759133282944, 0.7441666730869073
Precision, Recall and F-score @ 9 : 0.3412345679012349, 0.44329197881068305, 0.3570214594790494
MAP, nDCG @ 9 : 0.7082508818342151, 0.7450088907196634
Precision, Recall and F-score @ 10 : 0.324, 0.4632086160357823, 0.35341953695771633
MAP, nDCG @ 10 : 0.6931820441756946, 0.7379135441817931
```


## Authors
Adarsh Singh and Sri harsha

##### Link to Project
* https://github.com/adarsh1783/SearchEngine
