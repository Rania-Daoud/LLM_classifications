# LLM_classifications

This is part of Natural Language Module assessment at BBK university, the assessment aims to read a list of texts, transforms the data for easier processing, extracts useful feature, and finally classification with LLMs

## Part One

### Reading the novels

- This part is to prepare the data for more analysis.
- For this we rely on [Pandas](https://pandas.pydata.org) which is great for data analysis.
- The input to this function is the file path containing the novels to be analysed example `"texts/novels"`.
- The output is Pandas dataframe of ["year","title","author","content"] with year as index sorted in ascending order example:
``` 
                title             author        content 
year 

1811     Sense_and_Sensibility    Austen  \nCHAPTER 1\n\nThe family of Dashwood had long...
1855           North_and_South   Gaskell  'Wooed and married and a'.'\n'Edith!' said Mar...
1858      A_Tale_of_Two_Cities   Dickens  Book the First--Recalled to Life\n\n\n\n\nI. T...
1872                   Erewhon    Butler  SAMUEL BUTLER.\nAugust 7, 1901\n\nCHAPTER I: W...
1877              The_American     James  THE AMERICAN\n\nby Henry James\n\n\n1877\n\n\n...
1890               Dorian_Gray     Wilde  \nThe Picture of Dorian Gray\n\nby\n\nOscar Wi...
1891  Tess_of_the_DUrbervilles     Hardy  Phase the First: The Maiden\n\n\nI\n\n\nOn an ...
1911         The_Secret_Garden   Burnett  THE SECRET GARDEN\n\nBY FRANCES HODGSON BURNET...
1916    Portrait_of_the_Artist     Joyce  Chapter 1\n\nOnce upon a time and a very good ...
1926            The_Black_Moth     Heyer  \nTHE BLACK MOTH\n\nA ROMANCE OF THE XVIII CEN...
1928                   Orlando     Woolf  ORLANDO\n\nA BIOGRAPHY\n\nBY\n\nVIRGINIA WOOLF...
1930            Blood_Meridian  McCarthy  Your ideas are terrifying and your hearts are ...

```
### Adding TTR

- TTR is the type-token ratio, it's the ratio of unique words to the total number of words
- the function `nltk_ttr`: 
  - takes a text.
  - removes punctuation.
  - lowers case of the whole text(ignore case).
  - get the unique number of words.
  - divide the unique number of words by the total number of words.
  - example "This is a sample text, this should be easy to parse" -> 
    - unique words: this, is, a, sample, text, should, be, easy, to, parse. (10)
    - ttr = 8/9 = .89. 
- the function `get_ttrs`
  - takes a pandas dataframe.
  - add a new column "ttr" using the function `nltk_ttr`
  - example:
  ```
                title             author                         text                         token
    year                                                                                             
    1811  Sense_and_Sensibility   Austen  \nCHAPTER 1\n\nThe family of Dashwood had long...  0.052356
    1855        North_and_South  Gaskell  'Wooed and married and a'.'\n'Edith!' said Mar...  0.053415
    1858   A_Tale_of_Two_Cities  Dickens  Book the First--Recalled to Life\n\n\n\n\nI. T...  0.070454
    1872                Erewhon   Butler  SAMUEL BUTLER.\nAugust 7, 1901\n\nCHAPTER I: W...  0.091810
    1877           The_American    James  THE AMERICAN\n\nby Henry James\n\n\n1877\n\n\n...  0.065669

### Adding fk_level reading ease score
- fk_level reading ease score is a measure of how easy to read the text is
- it follows the formula 
<div style="text-align: center; background-color:white; border-radius: 12px">
  <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/bd4916e193d2f96fa3b74ee258aaa6fe242e110e" alt="formula" style="border-radius: 12px; width: 800px; display: inline-block;"/>
</div>

- example:
```
                         title    author                                               text     token      fks
year                                                                                                          
1811     Sense_and_Sensibility    Austen  \nCHAPTER 1\n\nThe family of Dashwood had long...  0.052356 -53.1708
1855           North_and_South   Gaskell  'Wooed and married and a'.'\n'Edith!' said Mar...  0.053415 -16.4633
1858      A_Tale_of_Two_Cities   Dickens  Book the First--Recalled to Life\n\n\n\n\nI. T...  0.070454 -48.2182
1872                   Erewhon    Butler  SAMUEL BUTLER.\nAugust 7, 1901\n\nCHAPTER I: W...  0.091810 -98.2469
1877              The_American     James  THE AMERICAN\n\nby Henry James\n\n\n1877\n\n\n...  0.065669 -24.5451
1890               Dorian_Gray     Wilde  \nThe Picture of Dorian Gray\n\nby\n\nOscar Wi...  0.085033   5.5178
1891  Tess_of_the_DUrbervilles     Hardy  Phase the First: The Maiden\n\n\nI\n\n\nOn an ...  0.077824 -24.7142
1911         The_Secret_Garden   Burnett  THE SECRET GARDEN\n\nBY FRANCES HODGSON BURNET...  0.057881   0.4218
1916    Portrait_of_the_Artist     Joyce  Chapter 1\n\nOnce upon a time and a very good ...  0.103858 -11.4509
1926            The_Black_Moth     Heyer  \nTHE BLACK MOTH\n\nA ROMANCE OF THE XVIII CEN...  0.079646  11.6998
1928                   Orlando     Woolf  ORLANDO\n\nA BIOGRAPHY\n\nBY\n\nVIRGINIA WOOLF...  0.113415 -46.5725
1930            Blood_Meridian  McCarthy  Your ideas are terrifying and your hearts are ...  0.085785  -8.2455
```