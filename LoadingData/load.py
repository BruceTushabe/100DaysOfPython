
# Load sckit-learn's datasets

from sklearn import datasets

# Load digits dataset

digits = datasets.load_digits()

# Create features matrix

features = digits.data

# Create target vector

target = digits.target

# View first observation

features[0]




