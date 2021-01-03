This is a inpirational project from the book ["If On A Winter's Night A Traveler"](https://www.goodreads.com/book/show/374233.If_on_a_Winter_s_Night_a_Traveler) by Italo Calvino. I explain it better in this [blogpost](http://blog.zehrah.net/if-on-a-winters-night)

Loteria argues that most frequent and the least frequent words in a book may reveal style and content of the book. 
This repo dedicateed for her thesis. 

To run this please run `demo.py` which takes two arguments: title of the text and the number determines how many frequent words to take into consideration. For instance 

```
 python demo.py --text="Pride" --number=20
```
This algorhtm uses wikipedia English word vectors from [fastext](https://fasttext.cc/). Please download `wiki.en.vec`

I also created a most frequent words table from Wikipedia and discarding some useless words in books such as numbers and "Chapter", "section". You can adjust it as your needs. 
[MUSE](https://github.com/facebookresearch/MUSE) is also good tool to start playing with word embeddings with multilingual vectors.

Results:
| Book                          | Variance of the most common   words |   | Variance of the least common   words |
|-------------------------------|-------------------------------------|---|--------------------------------------|
| Adventures of Sherlock Holmes |        0.028085537                  |   |        0.03516535                    |
| 80 Days Around the World      |        0.030894253                  |   |        0.040569678                   |
| Pride and Prejudice           |        0.03324658                   |   |        0.040003102                   |
| The Call of the Wild          |        0.033583995                  |   |        0.0330922                     |
| Th Last Leaf                  |        0.034217913                  |   |        0.02933074                    |
| Tell Tale Heart               |        0.036268003                  |   |        0.03617519                    |
| White Fang                    |        0.036824886                  |   |        0.022111746                   |
| MagnaCarta                    |        0.039580483                  |   |        0.039130308                   |
| Communist Manifesto           |        0.0404633                    |   |        0.033829868                   |
| Canterville's Ghost           | 0.041121338                         |   |        0.035551053                   |

