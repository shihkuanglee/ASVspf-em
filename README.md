This repository aims to provide a library on github that can be used as a github submodule for computing tandem detection cost function (t-DCF) metric and equal error rate (EER) used in [ASVspoof](https://www.asvspoof.org).

The file `eval_metrics_2019.py` is a copy of `eval_metrics.py` from the implementation provide by ASVspoof, it is used in [ASVspoof2019](https://www.asvspoof.org/index2019.html).


### Usage

Add submodule to your repository:
```
git submodule add git@github.com:shihkuanglee/ASVspf-em.git em
```

Then the library is now able to be import:
```
import em.eval_metrics_2019 as em
```


### Licensing

This repository is licensed under the [CC BY-NC-SA 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/), which is same to the licence of the implementation provide by ASVspoof.
