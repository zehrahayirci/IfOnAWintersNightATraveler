This is a inpirational project from the book ["If On A Winter's Night A Traveler"](https://www.goodreads.com/book/show/374233.If_on_a_Winter_s_Night_a_Traveler) by Italo Calvino. 

Loteria argues that most frequent and the least frequent words in a book may reveal style and content of the book. 
This repo dedicateed for her thesis. 

To run this please run `demo.py` which takes two arguments: title of the text and the number determines how many frequent words to take into consideration. For instance 

```
 python demo.py --text="Pride" --number=20
```
This algorhtm uses wikipedia English word vectors from [fastext](https://fasttext.cc/). Please download `wiki.en.vec`

I also created a most frequent words table from Wikipedia and discarding some useless words in books such as numbers and "Chapter", "section". You can adjust it as your needs. 
[MUSE](https://github.com/facebookresearch/MUSE) is also good tool to start playing with word embeddings with multilingual vectors.


