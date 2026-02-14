import joblib
from keras.models import load_model
import numpy as np
from sklearn.decomposition import PCA

le_gender = joblib.load('app/models/le_gender (1).pkl')
le_married = joblib.load('app/models/le_married (1).pkl')
le_education = joblib.load('app/models/le_education (1).pkl')
le_self_employed = joblib.load('app/models/le_self_employed (1).pkl')
le_property_area = joblib.load('app/models/le_property_area (1).pkl')

pca_transformer = joblib.load('app/models/pca (2).pkl')

Load_model = load_model('app/models/model.keras')

print(pca_transformer.n_features_in_)   # number of input features PCA expects
print(pca_transformer.components_)      # PCA components (weights)
print(pca_transformer.explained_variance_) 