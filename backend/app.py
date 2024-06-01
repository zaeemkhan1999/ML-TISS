# # from flask import Flask, jsonify, request
# # import pandas as pd
# # import joblib
# # import os
#
# # app = Flask(_name_)
#
# # # Path to the trained model
# # MODEL_PATH = 'model/model.pkl'
#
# # # Verify that the model file exists
# # if not os.path.exists(MODEL_PATH):
# #     raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
#
# # # Load the trained model
# # model = joblib.load(MODEL_PATH)
#
# # # Verify the model is loaded correctly
# # if not hasattr(model, 'predict'):
# #     raise AttributeError("Loaded model does not have 'predict' attribute")
#
# # def generate_recommendations_map():
# #     recommendations = {
# #         "Fuzzers": "Implement thorough input validation and sanitation to handle unexpected or malformed inputs. Regularly update and patch your software to fix vulnerabilities that could be exploited by fuzzing. Use fuzzing tools during the development and testing phases to identify and fix potential security issues before deployment. Employ automated testing frameworks that include fuzz testing, and ensure comprehensive code review and security audits.",
# #         "Analysis": "Encrypt sensitive data to prevent unauthorized access and analysis. Use network segmentation to limit the exposure of sensitive data to potential attackers. Monitor and log network traffic to detect and respond to unusual patterns that may indicate data analysis attempts. Implement strong access control measures, including multi-factor authentication (MFA) and regular audits of access logs.",
# #         "Backdoor": "Regularly scan your systems for known backdoors and remove them immediately. Employ intrusion detection systems (IDS) and intrusion prevention systems (IPS) to monitor for suspicious activity. Keep your systems and applications up to date with the latest security patches. Conduct regular security assessments and penetration testing to identify and mitigate potential backdoor vulnerabilities.",
# #         "DoS": "Minimize the attack surface by restricting unnecessary ports, protocols, and services. Use CDNs and load balancers to distribute traffic and mitigate DoS attacks. Implement rate limiting and throttling to control traffic and prevent overloads. Deploy firewalls and access control lists (ACLs) to filter and block malicious traffic, and use DDoS mitigation services for additional protection.",
# #         "Exploits": "Regularly update and patch software to fix vulnerabilities that could be exploited. Use runtime application self-protection (RASP) and web application firewalls (WAF) to detect and block exploit attempts. Educate users and administrators about common exploit techniques and how to recognize them. Implement a robust incident response plan to quickly address and mitigate the effects of successful exploits.",
# #         "Generic": "Apply general cybersecurity best practices, such as keeping systems and software up to date, using strong passwords, and implementing MFA. Regularly backup data and ensure backups are secure and tested for restoration. Conduct regular security training and awareness programs for employees to reduce the risk of human error and social engineering attacks.",
# #         "Reconnaissance": "Use network monitoring and IDS to detect and respond to reconnaissance activities. Implement network segmentation to limit the scope of potential reconnaissance. Regularly review and update firewall rules to block unnecessary inbound and outbound traffic. Conduct regular vulnerability scans and penetration tests to identify and address potential weaknesses before attackers can exploit them.",
# #         "Shellcode": "Employ data execution prevention (DEP) and address space layout randomization (ASLR) to protect against shellcode attacks. Use application whitelisting to allow only approved applications to run. Regularly update and patch software to fix vulnerabilities that could be exploited by shellcode. Implement strict input validation and sanitation to prevent the injection of malicious code.",
# #         "Worms": "Use antivirus and anti-malware solutions to detect and remove worms. Implement network segmentation to limit the spread of worms within your network. Educate users about safe computing practices and the dangers of opening unknown email attachments or clicking on suspicious links. Regularly update and patch systems to fix vulnerabilities that could be exploited by worms, and use network monitoring to detect and respond to worm activity.",
# #         "Normal": "No recommendation available."
# #     }
# #     return recommendations
#
# # def process_csv_file(df, recommendations_map):
# #     try:
# #         if 'CVSS_Score' not in df.columns:
# #             print("CVSS_Score column not found in CSV file")
# #             return {}, 0
#
# #         # Find all attack categories
# #         attack_category_counts = df['Predicted_Attack_Category'].value_counts()
# #         all_categories = attack_category_counts.index.tolist()
#
# #         # Calculate the mean CVSS score
# #         mean_cvss_score = df['CVSS_Score'].mean()
#
# #         # Get the recommendations for all categories
# #         categories_with_recommendations = {}
# #         for category in all_categories:
# #             count = int(attack_category_counts[category])
# #             percentage = float((count / len(df)) * 100)
# #             recommendation = recommendations_map.get(category, "No recommendation available.")
# #             categories_with_recommendations[category] = {
# #                 'count': count,
# #                 'percentage': percentage,
# #                 'recommendation': recommendation
# #             }
#
# #         return categories_with_recommendations, mean_cvss_score
# #     except Exception as e:
# #         print(f"Error processing CSV file: {e}")
# #         return {}, 0
#
# # @app.route('/upload', methods=['POST'])
# # def upload_and_predict():
# #     if 'file' not in request.files:
# #         return jsonify({"error": "No file part"}), 400
#
# #     file = request.files['file']
# #     if file.filename == '':
# #         return jsonify({"error": "No selected file"}), 400
#
# #     if file:
# #         # Save the uploaded file
# #         filepath = os.path.join('results', file.filename)
# #         file.save(filepath)
#
# #         # Read the uploaded file
# #         df = pd.read_csv(filepath)
#
# #         # Verify the DataFrame loaded correctly
# #         if df.empty:
# #             return jsonify({"error": "Uploaded CSV file is empty"}), 400
#
# #         # Make predictions
# #         df['Predicted_Attack_Category'] = model.predict(df)
# #         df['CVSS_Score'] = df['Predicted_Attack_Category'].map({
# #             'Normal': 0, 'Reconnaissance': 1, 'Shellcode': 2, 'Worms': 3,
# #             'Analysis': 4, 'Fuzzers': 5, 'Backdoor': 6, 'Generic': 7,
# #             'Exploits': 8, 'DoS': 9
# #         })
#
# #         # Process the predictions
# #         recommendations_map = generate_recommendations_map()
# #         categories_with_recommendations, mean_cvss_score = process_csv_file(df, recommendations_map)
#
# #         response = {
# #             'attack_categories': categories_with_recommendations,
# #             'mean_cvss_score': mean_cvss_score
# #         }
#
# #         return jsonify(response)
#
# # if _name_ == '_main_':
# #     app.run(debug=True)
#
# from flask import Flask, jsonify, request
# import pandas as pd
# import joblib
# import os
#
# app = Flask(_name_)
#
# # Path to the trained model and transformer
# MODEL_PATH = 'model/model.pkl'
# TRANSFORMER_PATH = 'model/transformer.pkl'
#
# # Verify that the model and transformer files exist
# if not os.path.exists(MODEL_PATH):
#     raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
# if not os.path.exists(TRANSFORMER_PATH):
#     raise FileNotFoundError(f"Transformer file not found: {TRANSFORMER_PATH}")
#
# # Load the trained model and transformer
# model = joblib.load(MODEL_PATH)
# transformer = joblib.load(TRANSFORMER_PATH)
#
# # Verify the model is loaded correctly
# if not hasattr(model, 'predict'):
#     raise AttributeError("Loaded model does not have 'predict' attribute")
#
# def generate_recommendations_map():
#     recommendations = {
#         "Fuzzers": "Implement thorough input validation and sanitation to handle unexpected or malformed inputs. Regularly update and patch your software to fix vulnerabilities that could be exploited by fuzzing. Use fuzzing tools during the development and testing phases to identify and fix potential security issues before deployment. Employ automated testing frameworks that include fuzz testing, and ensure comprehensive code review and security audits.",
#         "Analysis": "Encrypt sensitive data to prevent unauthorized access and analysis. Use network segmentation to limit the exposure of sensitive data to potential attackers. Monitor and log network traffic to detect and respond to unusual patterns that may indicate data analysis attempts. Implement strong access control measures, including multi-factor authentication (MFA) and regular audits of access logs.",
#         "Backdoor": "Regularly scan your systems for known backdoors and remove them immediately. Employ intrusion detection systems (IDS) and intrusion prevention systems (IPS) to monitor for suspicious activity. Keep your systems and applications up to date with the latest security patches. Conduct regular security assessments and penetration testing to identify and mitigate potential backdoor vulnerabilities.",
#         "DoS": "Minimize the attack surface by restricting unnecessary ports, protocols, and services. Use CDNs and load balancers to distribute traffic and mitigate DoS attacks. Implement rate limiting and throttling to control traffic and prevent overloads. Deploy firewalls and access control lists (ACLs) to filter and block malicious traffic, and use DDoS mitigation services for additional protection.",
#         "Exploits": "Regularly update and patch software to fix vulnerabilities that could be exploited. Use runtime application self-protection (RASP) and web application firewalls (WAF) to detect and block exploit attempts. Educate users and administrators about common exploit techniques and how to recognize them. Implement a robust incident response plan to quickly address and mitigate the effects of successful exploits.",
#         "Generic": "Apply general cybersecurity best practices, such as keeping systems and software up to date, using strong passwords, and implementing MFA. Regularly backup data and ensure backups are secure and tested for restoration. Conduct regular security training and awareness programs for employees to reduce the risk of human error and social engineering attacks.",
#         "Reconnaissance": "Use network monitoring and IDS to detect and respond to reconnaissance activities. Implement network segmentation to limit the scope of potential reconnaissance. Regularly review and update firewall rules to block unnecessary inbound and outbound traffic. Conduct regular vulnerability scans and penetration tests to identify and address potential weaknesses before attackers can exploit them.",
#         "Shellcode": "Employ data execution prevention (DEP) and address space layout randomization (ASLR) to protect against shellcode attacks. Use application whitelisting to allow only approved applications to run. Regularly update and patch software to fix vulnerabilities that could be exploited by shellcode. Implement strict input validation and sanitation to prevent the injection of malicious code.",
#         "Worms": "Use antivirus and anti-malware solutions to detect and remove worms. Implement network segmentation to limit the spread of worms within your network. Educate users about safe computing practices and the dangers of opening unknown email attachments or clicking on suspicious links. Regularly update and patch systems to fix vulnerabilities that could be exploited by worms, and use network monitoring to detect and respond to worm activity.",
#         "Normal": "No recommendation available."
#     }
#     return recommendations
#
# def preprocess_data(df, transformer):
#     features = df.drop(['attack_cat', 'label'], axis=1, errors='ignore')
#     processed_features = transformer.transform(features)
#     return processed_features
#
# def process_csv_file(df, recommendations_map):
#     try:
#         if 'CVSS_Score' not in df.columns:
#             print("CVSS_Score column not found in CSV file")
#             return {}, 0
#
#         # Find all attack categories
#         attack_category_counts = df['Predicted_Attack_Category'].value_counts()
#         all_categories = attack_category_counts.index.tolist()
#
#         # Calculate the mean CVSS score
#         mean_cvss_score = df['CVSS_Score'].mean()
#
#         # Get the recommendations for all categories
#         categories_with_recommendations = {}
#         for category in all_categories:
#             count = int(attack_category_counts[category])
#             percentage = float((count / len(df)) * 100)
#             recommendation = recommendations_map.get(category, "No recommendation available.")
#             categories_with_recommendations[category] = {
#                 'count': count,
#                 'percentage': percentage,
#                 'recommendation': recommendation
#             }
#
#         return categories_with_recommendations, mean_cvss_score
#     except Exception as e:
#         print(f"Error processing CSV file: {e}")
#         return {}, 0
#
#
# @app.route('/upload', methods=['POST'])
# def upload_and_predict():
#     if 'file' not in request.files:
#         return jsonify({"error": "No file part"}), 400
#
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({"error": "No selected file"}), 400
#
#     if file:
#         # Save the uploaded file
#         filepath = os.path.join('results', file.filename)
#         file.save(filepath)
#
#         # Read the uploaded file
#         df = pd.read_csv(filepath)
#
#         # Verify the DataFrame loaded correctly
#         if df.empty:
#             return jsonify({"error": "Uploaded CSV file is empty"}), 400
#
#         # Preprocess the uploaded data
#         X_test_processed = preprocess_data(df, transformer)
#
#         # Make predictions
#         df['Predicted_Attack_Category'] = model.predict(X_test_processed)
#         df['CVSS_Score'] = df['Predicted_Attack_Category'].map({
#             'Normal': 0, 'Reconnaissance': 1, 'Shellcode': 2, 'Worms': 3,
#             'Analysis': 4, 'Fuzzers': 5, 'Backdoor': 6, 'Generic': 7,
#             'Exploits': 8, 'DoS': 9
#         })
#
#         # Process the predictions
#         recommendations_map = generate_recommendations_map()
#         categories_with_recommendations, mean_cvss_score = process_csv_file(df, recommendations_map)
#
#         response = {
#             'attack_categories': categories_with_recommendations,
#             'mean_cvss_score': mean_cvss_score
#         }
#
#         return jsonify(response)



#
# if _name_ == '_main_':
#     app.run(debug=True)


from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import joblib
import os

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes


# Path to the trained model and transformer
MODEL_PATH = 'model/model.pkl'
TRANSFORMER_PATH = 'model/transformer.pkl'

# Verify that the model and transformer files exist
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
if not os.path.exists(TRANSFORMER_PATH):
    raise FileNotFoundError(f"Transformer file not found: {TRANSFORMER_PATH}")

# Load the trained model and transformer
model = joblib.load(MODEL_PATH)
transformer = joblib.load(TRANSFORMER_PATH)

# Verify the model is loaded correctly
if not hasattr(model, 'predict'):
    raise AttributeError("Loaded model does not have 'predict' attribute")


def generate_recommendations_map():
    recommendations = {
        "Fuzzers": "Implement thorough input validation and sanitation to handle unexpected or malformed inputs. Regularly update and patch your software to fix vulnerabilities that could be exploited by fuzzing. Use fuzzing tools during the development and testing phases to identify and fix potential security issues before deployment. Employ automated testing frameworks that include fuzz testing, and ensure comprehensive code review and security audits.",
        "Analysis": "Encrypt sensitive data to prevent unauthorized access and analysis. Use network segmentation to limit the exposure of sensitive data to potential attackers. Monitor and log network traffic to detect and respond to unusual patterns that may indicate data analysis attempts. Implement strong access control measures, including multi-factor authentication (MFA) and regular audits of access logs.",
        "Backdoor": "Regularly scan your systems for known backdoors and remove them immediately. Employ intrusion detection systems (IDS) and intrusion prevention systems (IPS) to monitor for suspicious activity. Keep your systems and applications up to date with the latest security patches. Conduct regular security assessments and penetration testing to identify and mitigate potential backdoor vulnerabilities.",
        "DoS": "Minimize the attack surface by restricting unnecessary ports, protocols, and services. Use CDNs and load balancers to distribute traffic and mitigate DoS attacks. Implement rate limiting and throttling to control traffic and prevent overloads. Deploy firewalls and access control lists (ACLs) to filter and block malicious traffic, and use DDoS mitigation services for additional protection.",
        "Exploits": "Regularly update and patch software to fix vulnerabilities that could be exploited. Use runtime application self-protection (RASP) and web application firewalls (WAF) to detect and block exploit attempts. Educate users and administrators about common exploit techniques and how to recognize them. Implement a robust incident response plan to quickly address and mitigate the effects of successful exploits.",
        "Generic": "Apply general cybersecurity best practices, such as keeping systems and software up to date, using strong passwords, and implementing MFA. Regularly backup data and ensure backups are secure and tested for restoration. Conduct regular security training and awareness programs for employees to reduce the risk of human error and social engineering attacks.",
        "Reconnaissance": "Use network monitoring and IDS to detect and respond to reconnaissance activities. Implement network segmentation to limit the scope of potential reconnaissance. Regularly review and update firewall rules to block unnecessary inbound and outbound traffic. Conduct regular vulnerability scans and penetration tests to identify and address potential weaknesses before attackers can exploit them.",
        "Shellcode": "Employ data execution prevention (DEP) and address space layout randomization (ASLR) to protect against shellcode attacks. Use application whitelisting to allow only approved applications to run. Regularly update and patch software to fix vulnerabilities that could be exploited by shellcode. Implement strict input validation and sanitation to prevent the injection of malicious code.",
        "Worms": "Use antivirus and anti-malware solutions to detect and remove worms. Implement network segmentation to limit the spread of worms within your network. Educate users about safe computing practices and the dangers of opening unknown email attachments or clicking on suspicious links. Regularly update and patch systems to fix vulnerabilities that could be exploited by worms, and use network monitoring to detect and respond to worm activity.",
        "Normal": "No recommendation available."
    }
    return recommendations


def preprocess_data(df, transformer):
    features = df.drop(['attack_cat', 'label'], axis=1, errors='ignore')
    processed_features = transformer.transform(features)
    return processed_features


def process_csv_file(df, recommendations_map):
    try:
        if 'CVSS_Score' not in df.columns:
            print("CVSS_Score column not found in CSV file")
            return {}, 0

        # Find all attack categories
        attack_category_counts = df['Predicted_Attack_Category'].value_counts()
        all_categories = attack_category_counts.index.tolist()

        # Calculate the mean CVSS score
        mean_cvss_score = df['CVSS_Score'].mean()

        # Get the recommendations for all categories
        categories_with_recommendations = {}
        for category in all_categories:
            count = int(attack_category_counts[category])
            percentage = float((count / len(df)) * 100)
            recommendation = recommendations_map.get(category, "No recommendation available.")
            categories_with_recommendations[category] = {
                'count': count,
                'percentage': percentage,
                'recommendation': recommendation
            }

        return categories_with_recommendations, mean_cvss_score
    except Exception as e:
        print(f"Error processing CSV file: {e}")
        return {}, 0


@app.route('/upload', methods=['POST'])
def upload_and_predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        # Save the uploaded file
        filepath = os.path.join('results', file.filename)
        file.save(filepath)

        # Read the uploaded file
        df = pd.read_csv(filepath)

        # Verify the DataFrame loaded correctly
        if df.empty:
            return jsonify({"error": "Uploaded CSV file is empty"}), 400

        # Preprocess the uploaded data
        X_test_processed = preprocess_data(df, transformer)

        # Make predictions
        df['Predicted_Attack_Category'] = model.predict(X_test_processed)
        df['CVSS_Score'] = df['Predicted_Attack_Category'].map({
            'Normal': 0, 'Reconnaissance': 1, 'Shellcode': 2, 'Worms': 3,
            'Analysis': 4, 'Fuzzers': 5, 'Backdoor': 6, 'Generic': 7,
            'Exploits': 8, 'DoS': 9
        })

        # Process the predictions
        recommendations_map = generate_recommendations_map()
        categories_with_recommendations, mean_cvss_score = process_csv_file(df, recommendations_map)

        response = {
            'attack_categories': categories_with_recommendations,
            'mean_cvss_score': mean_cvss_score
        }

        return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)