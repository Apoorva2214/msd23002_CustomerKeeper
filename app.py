import streamlit as st
import joblib
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load scaler and model
scaler = joblib.load('scaler.pkl')  # Load the saved scaler
model = joblib.load('churn_predict_model')  # Load your trained model

# Function to make predictions
def predict_churn(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
    # Geography encoding
    if p9 == 1:
        Geography_Germany, Geography_Spain = 1, 0
    elif p9 == 2:
        Geography_Germany, Geography_Spain = 0, 1
    else:
        Geography_Germany, Geography_Spain = 0, 0  # France is the reference category

    features = np.array([[p1, p2, p3, p4, p5, p6, p7, p8, Geography_Germany, Geography_Spain, p10]])
    scaled_features = scaler.transform(features)
    result = model.predict(scaled_features)
    proba = model.predict_proba(scaled_features)
    return result[0], proba[0]

# Function to generate retention offers
def generate_offers(age, balance, salary, num_products, credit_score, active_member):
    offers = []

    if age < 30:
        offers.append({
            "title": "Youth Advantage Savings Account",
            "description": "A high-interest savings account designed for young customers to achieve financial goals faster."
        })
    elif age >= 30 and age <= 50:
        offers.append({
            "title": "Family Benefit Program",
            "description": "Provides benefits for families, such as joint accounts and insurance for family members."
        })
    else:
        offers.append({
            "title": "Senior Citizen Wellness Program",
            "description": "A program with lower banking fees, priority service, and health-related perks for senior customers."
        })

    if balance < 5000:
        offers.append({
            "title": "Low-Balance Fee Waiver",
            "description": "Waives fees on maintaining a minimum balance, helping customers manage their accounts affordably."
        })
    elif balance >= 5000 and balance < 20000:
        offers.append({
            "title": "Priority Banking",
            "description": "Provides dedicated support and faster service for medium balance accounts, improving the customer experience."
        })
    else:
        offers.append({
            "title": "Platinum Membership",
            "description": "Exclusive banking privileges, including personal advisors and premium support."
        })

    if salary < 40000:
        offers.append({
            "title": "Savings Booster Plan",
            "description": "Automated deposits to encourage savings and build financial security over time."
        })
    else:
        offers.append({
            "title": "Premium Investment Plan",
            "description": "Tailored for high earners, offering personalized investment options and wealth management support."
        })

    if num_products < 2:
        offers.append({
            "title": "Cross-sell Offer",
            "description": "Special discounts on loans and credit cards to encourage use of multiple banking products."
        })
    else:
        offers.append({
            "title": "Reward Program",
            "description": "Loyalty rewards, including cashback and exclusive benefits for long-term customers."
        })

    if credit_score < 600:
        offers.append({
            "title": "Credit Improvement Assistance",
            "description": "Financial counseling and credit score monitoring to help improve credit scores."
        })
    elif credit_score >= 600 and credit_score < 750:
        offers.append({
            "title": "Loyalty Rewards",
            "description": "Special rewards for good credit behavior, offering perks and reduced fees."
        })
    else:
        offers.append({
            "title": "Preferred Customer Program",
            "description": "Lower loan rates and exclusive benefits for customers with excellent credit scores."
        })

    if not active_member:
        offers.append({
            "title": "Special Engagement Package",
            "description": "Increased account activity benefits, such as fee reductions and reward points."
        })

    return offers

# Streamlit app configuration
st.set_page_config(page_title="CustomerKeeper", page_icon=":shield:", layout="wide")
st.title("CustomerKeeper")
st.text("Empowering Retention with Data-Driven Offers")

# Sidebar actions as header and About section as footer
with st.sidebar:
    st.markdown("## Actions")  # Header
    predict_button = st.button("🔍 Predict Churn")
    generate_button = st.button("🎁 Generate Retention Offers")
    st.markdown("---")
    
    # Footer-like About section
    st.markdown("## About")
    st.markdown("""
        CustomerKeeper is a machine learning-powered application designed to predict customer churn and suggest personalized retention offers to retain valuable customers.
    """)
    st.markdown("#### [GitHub Repository](https://github.com/Apoorva2214/Churn-Analysis)")
    st.markdown("---")

# Display customer information form in the main center area in two columns
st.header("Customer Information Form")
col1, col2 = st.columns(2)

with col1:
    p1 = st.number_input('Credit Score', min_value=0, max_value=1000, value=600)
    p2 = st.number_input('Age', min_value=0, max_value=120, value=35)
    p3 = st.number_input('Tenure', min_value=0, max_value=10, value=5)
    p4 = st.number_input('Balance', value=0.0)
    p5 = st.number_input('Number of Products', min_value=1, max_value=4, value=1)

with col2:
    p6 = st.selectbox('Has Credit Card', options=[0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    p7 = st.selectbox('Is Active Member', options=[0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    p8 = st.number_input('Estimated Salary', value=50000.0)
    p9 = st.selectbox('Geography', options=[1, 2, 3], format_func=lambda x: {1: 'Germany', 2: 'Spain', 3: 'France'}.get(x))
    p10 = st.selectbox('Gender', options=[0, 1], format_func=lambda x: 'Male' if x == 1 else 'Female')

# Display results in the main center area based on button clicks
if predict_button:
    result, proba = predict_churn(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
    
    churn_message = "The customer is likely to churn." if result == 1 else "The customer is not likely to churn."
    churn_probability = proba[1]  # Probability of churn (class 1)
    not_churn_probability = proba[0]  # Probability of not churning (class 0)
    
    st.subheader("Churn Prediction Result")
    st.write(churn_message)
    
    # Display probabilities
    st.write(f"Probability of Churn: {churn_probability*100:.2f}%")
    st.write(f"Probability of Not Churn: {not_churn_probability*100:.2f}%")

if generate_button:
    offers = generate_offers(p2, p4, p8, p5, p1, p7)
    st.subheader("Recommended Retention Offers")
    for i, offer in enumerate(offers, start=1):
        st.write(f"**{i}. {offer['title']}**: {offer['description']}")

# Footer for credits
st.markdown("""
    ---
    Powered by machine learning to keep your customers happy and loyal.  
""")
