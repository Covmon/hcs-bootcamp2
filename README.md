# hcs-bootcamp2

### Noah Covey
### October 30, 2019

The notebook Bootcamp 2 Assignment.ipynb, when run, creates an API that takes in a student's gender, race, parental education level, wealth (in terms of whether the student has free/reduced or standard lunch), and preparation level, and outputs a prediction for their test score based on a dataset of 1000 students. I used data from Kaggle found at https://www.kaggle.com/spscientist/students-performance-in-exams. I thought this data would be interesting to look at to find out how significant the correlation is between the five variables in the data and performance on test scores.

When running the notebook, a server will be created at http://127.0.0.1:5000/

The URL takes five (5) arguments, all integers:
- gender (0 = female, 1 = male)
- race (0 = group A, 1 = group B, 2 = group C, 3 = group D)
- parental_education (0 = some high school, 1 = high school, 2 = some college, 3 = associate's, 4 = bachelor's, 5 = master's)
- lunch (0 = reduced/free, 1 = standard)
- prep (0 = none, 1 = completed a prep course)

An example URL for a male student of racial group C whose parents have master's degrees, who has standard lunch fees, and who has completed a prep course would be:
http://127.0.0.1:5000/?gender=1&race=2&parental_education=5&lunch=1&prep=1



