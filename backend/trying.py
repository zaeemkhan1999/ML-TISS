# import os

# import pandas as pd
# import joblib
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import OneHotEncoder, StandardScaler
# from sklearn.compose import ColumnTransformer
# from sklearn.metrics import classification_report, accuracy_score
# from catboost import CatBoostClassifier
# from sklearn.ensemble import RandomForestClassifier

# # Load datasets
# df_train = pd.read_csv('UNSW_NB15_training-set (1).csv')
# df_test = pd.read_csv('UNSW_NB15_testing-set (1).csv')

# # Preprocessing
# def preprocess_data(df, transformer=None):
#     features = df.drop(['attack_cat', 'label'], axis=1)
#     if transformer is None:
#         transformer = ColumnTransformer(transformers=[
#             ('cat', OneHotEncoder(handle_unknown='ignore'), ['proto', 'service', 'state']),
#             ('num', StandardScaler(), features.columns.difference(['proto', 'service', 'state']))
#         ], remainder='passthrough')
#         processed_features = transformer.fit_transform(features)
#     else:
#         processed_features = transformer.transform(features)
#     return processed_features, transformer

# X_train_processed, transformer = preprocess_data(df_train)
# y_train = df_train['attack_cat']

# # Models to train and evaluate
# models = {
#     'RandomForest': RandomForestClassifier(n_estimators=100, random_state=42),
#     'CatBoost': CatBoostClassifier(iterations=100, learning_rate=0.1, depth=6, random_state=42, verbose=False)
# }

# def train_and_evaluate(models, X_train, y_train):
#     X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
#     for name, model in models.items():
#         model.fit(X_train, y_train)
#         y_pred = model.predict(X_test)
#         print(f"{name} - Accuracy: {accuracy_score(y_test, y_pred)}")
#         print(classification_report(y_test, y_pred))

# train_and_evaluate(models, X_train_processed, y_train)

# # Prepare testing data
# X_test_processed, _ = preprocess_data(df_test, transformer)
# y_test_pred = models['RandomForest'].predict(X_test_processed).flatten()  # Ensure it's flat

# joblib.dump('RandomForest', 'model/model.pkl')
# joblib.dump(transformer, 'model/transformer.pkl')



# df_test.reset_index(drop=True, inplace=True)  # Reset index to avoid any potential issues
# df_test['Predicted_Attack_Category'] = y_test_pred
# df_test['Threat_Level'] = df_test['Predicted_Attack_Category'].map({
#     'Normal': 0, 'Reconnaissance': 1, 'Shellcode': 2, 'Worms': 3,
#     'Analysis': 4, 'Fuzzers': 5, 'Backdoors': 6, 'Generic': 7,
#     'Exploits': 8, 'DoS': 9
# })

# df_test.to_csv('predicted_threat_levels.csv', index=False)

# # Function to calculate overall threat level
# def calculate_overall_threat(csv_path):
#     df = pd.read_csv(csv_path)
#     total_threat = df['Threat_Level'].sum()
#     overall_threat_level = (total_threat / len(df)) * 10 / 9  # Scale to 1-10
#     return overall_threat_level



# overall_threat_level = calculate_overall_threat('predicted_threat_levels.csv')
# print(f"Overall Threat Level: {overall_threat_level}")
# import os
# import pandas as pd
# import joblib
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import OneHotEncoder, StandardScaler
# from sklearn.compose import ColumnTransformer
# from sklearn.metrics import classification_report, accuracy_score
# from catboost import CatBoostClassifier
# from sklearn.ensemble import RandomForestClassifier
#
# # Load datasets
# df_train = pd.read_csv('UNSW_NB15_training-set (1).csv')
# df_test = pd.read_csv('UNSW_NB15_testing-set (1).csv')
#
# # Preprocessing
# def preprocess_data(df, transformer=None):
#     features = df.drop(['attack_cat', 'label'], axis=1)
#     if transformer is None:
#         transformer = ColumnTransformer(transformers=[
#             ('cat', OneHotEncoder(handle_unknown='ignore'), ['proto', 'service', 'state']),
#             ('num', StandardScaler(), features.columns.difference(['proto', 'service', 'state']))
#         ], remainder='passthrough')
#         processed_features = transformer.fit_transform(features)
#     else:
#         processed_features = transformer.transform(features)
#     return processed_features, transformer
#
# X_train_processed, transformer = preprocess_data(df_train)
# y_train = df_train['attack_cat']
#
# # Models to train and evaluate
# models = {
#     'RandomForest': RandomForestClassifier(n_estimators=100, random_state=42),
#     'CatBoost': CatBoostClassifier(iterations=100, learning_rate=0.1, depth=6, random_state=42, verbose=False)
# }
#
# def train_and_evaluate(models, X_train, y_train):
#     X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
#     for name, model in models.items():
#         model.fit(X_train, y_train)
#         y_pred = model.predict(X_test)
#         print(f"{name} - Accuracy: {accuracy_score(y_test, y_pred)}")
#         print(classification_report(y_test, y_pred))
#
# train_and_evaluate(models, X_train_processed, y_train)
#
# # Prepare testing data
# X_test_processed, _ = preprocess_data(df_test, transformer)
# y_test_pred = models['RandomForest'].predict(X_test_processed).flatten()  # Ensure it's flat
#
# # Save the model and transformer
# joblib.dump(models['RandomForest'], 'model/model.pkl')
# joblib.dump(transformer, 'model/transformer.pkl')
#
# df_test.reset_index(drop=True, inplace=True)  # Reset index to avoid any potential issues
# df_test['Predicted_Attack_Category'] = y_test_pred
# df_test['Threat_Level'] = df_test['Predicted_Attack_Category'].map({
#     'Normal': 0, 'Reconnaissance': 1, 'Shellcode': 2, 'Worms': 3,
#     'Analysis': 4, 'Fuzzers': 5, 'Backdoors': 6, 'Generic': 7,
#     'Exploits': 8, 'DoS': 9
# })
#
# df_test.to_csv('predicted_threat_levels.csv', index=False)
#
# # Function to calculate overall threat level
# def calculate_overall_threat(csv_path):
#     df = pd.read_csv(csv_path)
#     total_threat = df['Threat_Level'].sum()
#     overall_threat_level = (total_threat / len(df)) * 10 / 9  # Scale to 1-10
#     return overall_threat_level
#
# overall_threat_level = calculate_overall_threat('predicted_threat_levels.csv')
# print(f"Overall Threat Level: {overall_threat_level}")

import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report, accuracy_score
from catboost import CatBoostClassifier
from sklearn.ensemble import RandomForestClassifier

# Load datasets
df_train = pd.read_csv('UNSW_NB15_training-set (1).csv')
df_test = pd.read_csv('UNSW_NB15_testing-set (1).csv')

# Preprocessing
def preprocess_data(df, transformer=None):
    features = df.drop(['attack_cat', 'label'], axis=1)
    if transformer is None:
        transformer = ColumnTransformer(transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), ['proto', 'service', 'state']),
            ('num', StandardScaler(), features.columns.difference(['proto', 'service', 'state']))
        ], remainder='passthrough')
        processed_features = transformer.fit_transform(features)
    else:
        processed_features = transformer.transform(features)
    return processed_features, transformer

X_train_processed, transformer = preprocess_data(df_train)
y_train = df_train['attack_cat']

# Models to train and evaluate
models = {
    'RandomForest': RandomForestClassifier(n_estimators=100, random_state=42),
    'CatBoost': CatBoostClassifier(iterations=100, learning_rate=0.1, depth=6, random_state=42, verbose=False)
}

def train_and_evaluate(models, X_train, y_train):
    X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print(f"{name} - Accuracy: {accuracy_score(y_test, y_pred)}")
        print(classification_report(y_test, y_pred))

train_and_evaluate(models, X_train_processed, y_train)

# Prepare testing data
X_test_processed, _ = preprocess_data(df_test, transformer)
y_test_pred = models['RandomForest'].predict(X_test_processed).flatten()  # Ensure it's flat

# Save the model and transformer
joblib.dump(models['RandomForest'], 'model/model.pkl')
joblib.dump(transformer, 'model/transformer.pkl')

df_test.reset_index(drop=True, inplace=True)  # Reset index to avoid any potential issues
df_test['Predicted_Attack_Category'] = y_test_pred
df_test['Threat_Level'] = df_test['Predicted_Attack_Category'].map({
    'Normal': 0, 'Reconnaissance': 1, 'Shellcode': 2, 'Worms': 3,
    'Analysis': 4, 'Fuzzers': 5, 'Backdoors': 6, 'Generic': 7,
    'Exploits': 8, 'DoS': 9
})

df_test.to_csv('predicted_threat_levels.csv', index=False)

# Function to calculate overall threat level
def calculate_overall_threat(csv_path):
    df = pd.read_csv(csv_path)
    total_threat = df['Threat_Level'].sum()
    overall_threat_level = (total_threat / len(df)) * 10 / 9  # Scale to 1-10
    return overall_threat_level

overall_threat_level = calculate_overall_threat('predicted_threat_levels.csv')
print(f"Overall Threat Level: {overall_threat_level}")