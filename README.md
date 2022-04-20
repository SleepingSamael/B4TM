# B4TM


## Cross validation scheme
folds.pickle file

Contains cross validation splits for samples excluding HER2+ samples.
* All splits object, list of splits (10 for now)
  * Split 1, tuple with 2 items 
    * Cross validation list (10 folds as well)
      * Split 1.1, tuple with 2 items
        * Training 1.1 Indices for model training (around 55)
        * Validation 1.1 Indices for model validation and meta parameter update (around 7 samples)
      * Split 1.2
      * Split ...
      * Split 1.10
    * Test 1 sample indices (around 7 samples)
  * Split 2
  * ...
  * Split 10

You can use cross_validation.ipynb code to get same list with training data and labels instead of indices. Takes around 150MB memory.