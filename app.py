import streamlit as st
import pandas as pd
from PIL import Image
import io
from datetime import date
from fpdf import FPDF
import time
import re

st.set_page_config(page_title="AI Freelancer Assistant Pro - Day 5", layout="wide", page_icon="🚀")

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'AI Freelancer Assistant Pro', 0, 1, 'C')
        self.ln(10)

st.markdown("""
<style>
  .stButton>button { border-radius: 10px; background: linear-gradient(90deg, #4F46E5, #7C3AED); color: white; font-weight: bold; }
  .stTabs [data-baseweb="tab-list"] { gap: 24px; }
  .stMetric { background-color: #F3F4F6; padding: 10px; border-radius: 8px; }
</style>
""", unsafe_allow_html=True)

# Session State = Database + Output Storage
if 'gig_descriptions' not in st.session_state: st.session_state.gig_descriptions = []
if 'pricing_history' not in st.session_state: st.session_state.pricing_history = []
if 'client_replies' not in st.session_state: st.session_state.client_replies = []
if 'invoices' not in st.session_state: st.session_state.invoices = []
if 'contracts' not in st.session_state: st.session_state.contracts = []
if 'ai_credits' not in st.session_state: st.session_state.ai_credits = 300
if 'user_profile' not in st.session_state: st.session_state.user_profile = {"name": "Warda", "email": "warda@email.com", "pic": None}
if 'app_settings' not in st.session_state: st.session_state.app_settings = {"theme": "Light", "language": "English", "notifications": True}
if 'last_gig_output' not in st.session_state: st.session_state.last_gig_output = None
if 'last_reply_output' not in st.session_state: st.session_state.last_reply_output = None

def generate_gig_description(inputs):
    time.sleep(1)
    desc = f"""**I will {inputs['service']} for you | {inputs['experience']} Level Expert**

✅ Skills: {inputs['skills']}
✅ {inputs['revisions']} Revisions
✅ Delivery in {inputs['delivery']} days
**Features:** {inputs['features']}"""
    keywords = f"{inputs['service']}, {inputs['skills']}, freelance {inputs['service'].lower()}"
    return desc, keywords

def generate_reply(msg, tone):
    time.sleep(1)
    templates = {
        "Professional": f"Dear Client,\n\nThank you for '{msg}'. Let's schedule a call.\n\nBest Regards,\nWarda",
        "Friendly": f"Hey! Thanks for '{msg}'. Sounds fun!\n\nCheers,\nWarda",
        "Apologetic": f"Dear Client,\n\nI apologize for delay on '{msg}'.\n\nRegards,\nWarda"
    }
    return templates.get(tone)

def create_pdf(content, title):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in content.split('\n'):
        pdf.multi_cell(0, 10, line.encode('latin-1', 'replace').decode('latin-1')) # $ emoji fix
    file_name = f"{title}.pdf"
    pdf.output(file_name)
    return file_name

st.title("🚀 AI Freelancer Assistant Pro - Day 5 Final")

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["📊 Dashboard", "📝 Gig Generator", "💰 Pricing", "💬 Client Reply", "🧾 Invoice", "📑 Contract", "📜 History & Profile"])

with tab1:
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Gigs", len(st.session_state.gig_descriptions))
    c2.metric("Quotes", len(st.session_state.pricing_history))
    c3.metric("Invoices", len(st.session_state.invoices))
    c4.metric("AI Credits", st.session_state.ai_credits)

with tab2:
    st.subheader("AI Gig Description Generator")
    with st.form("gig_form"):
        c1, c2, c3 = st.columns(3)
        service = c1.selectbox("Service", ["AI Bot Development", "Web Scraping", "Data Analysis", "Streamlit App"])
        experience = c2.selectbox("Experience", ["Beginner", "Intermediate", "Expert"])
        delivery = c3.slider("Delivery Days", 1, 30, 5)
        skills = st.text_input("Skills", "Python, Streamlit, AI")
        features = st.text_area("Features", "Fast delivery, Custom solution")
        revisions = st.selectbox("Revisions", ["1", "3", "Unlimited"])
        submitted = st.form_submit_button("✨ Generate Gig")

    if submitted:
        if st.session_state.ai_credits >= 15:
            inputs = {"service":service, "skills":skills, "experience":experience, "delivery":delivery, "features":features, "revisions":revisions}
            desc, keywords = generate_gig_description(inputs)
            st.session_state.gig_descriptions.append({"Service": service, "Date": str(date.today())})
            st.session_state.ai_credits -= 15
            st.session_state.last_gig_output = {"desc": desc, "keywords": keywords}
            st.rerun()
        else:
            st.error("Not enough AI Credits")

    if st.session_state.last_gig_output:
        st.success("Gig Generated!")
        st.text_area("Description", st.session_state.last_gig_output["desc"], height=150, key="gig_out")
        st.text_input("SEO Keywords", st.session_state.last_gig_output["keywords"])
        st.download_button("📥 Download.txt", st.session_state.last_gig_output["desc"], "gig.txt")

with tab3:
    st.subheader("Smart Pricing Calculator")
    rate = st.number_input("Hourly Rate $", 5, 200, 25)
    hours = st.number_input("Hours", 1, 500, 20)
    complexity = st.selectbox("Complexity", ["Simple", "Medium", "Complex"])
    urgency = st.selectbox("Urgency", ["Normal", "Urgent +25%", "Super Urgent +50%"])
    tax = st.slider("Tax %", 0, 30, 10)
    if st.button("💵 Calculate Price"):
        base = rate * hours
        comp_mult = {"Simple": 1.0, "Medium": 1.3, "Complex": 1.7}[complexity]
        urg_mult = {"Normal": 1.0, "Urgent +25%": 1.25, "Super Urgent +50%": 1.5}[urgency]
        subtotal = base * comp_mult * urg_mult
        tax_amount = subtotal * (tax/100)
        total = subtotal + tax_amount
        st.session_state.pricing_history.append({"Total": total, "Date": str(date.today())})
        c1, c2, c3 = st.columns(3)
        c1.metric("Base", f"${base:.2f}")
        c2.metric("Tax", f"${tax_amount:.2f}")
        c3.metric("Total", f"${total:.2f}")

with tab4:
    st.subheader("AI Client Reply Generator")
    client_msg = st.text_area("Client Message", "Send project update please")
    tone = st.selectbox("Tone", ["Professional", "Friendly", "Apologetic"])
    if st.button("✨ Generate Reply"):
        if st.session_state.ai_credits >= 5:
            reply = generate_reply(client_msg, tone)
            st.session_state.client_replies.append({"Msg": client_msg[:30], "Tone": tone, "Date": str(date.today())})
            st.session_state.ai_credits -= 5
            st.session_state.last_reply_output = reply
            st.rerun()
        else:
            st.error("Not enough AI Credits")
    
    if st.session_state.last_reply_output:
        st.text_area("AI Reply", st.session_state.last_reply_output, height=150, key="reply_out")
        st.download_button("📋 Copy.txt", st.session_state.last_reply_output, "reply.txt")

with tab5:
    st.subheader("Invoice Generator")
    client_name = st.text_input("Client Name", "ABC Company")
    client_email = st.text_input("Email", "abc@email.com")
    project = st.text_input("Project", "Website Development")
    amount = st.number_input("Amount $", 50, 10000, 500)
    tax = st.slider("Tax %", 0, 25, 10, key="tax_inv")
    due_date = st.date_input("Due Date", date.today())
    if st.button("🧾 Generate Invoice PDF"):
        total = amount + (amount * tax / 100)
        st.session_state.invoices.append({"Client": client_name, "Total": total, "Date": str(date.today())})
        content = f"INVOICE\nTo: {client_name} - {client_email}\nProject: {project}\nTotal: ${total}\nDue: {due_date}"
        pdf_file = create_pdf(content, f"Invoice_{re.sub(r'[^A-Za-z0-9]+', '_', client_name)}")
        st.download_button("📥 Download PDF", open(pdf_file, "rb"), pdf_file)

with tab6:
    st.subheader("Contract Generator")
    freelancer_name = st.text_input("Your Name", "Warda")
    client_name_c = st.text_input("Client Name", "XYZ Client")
    scope = st.text_area("Scope", "Develop Streamlit app")
    timeline = st.text_input("Timeline", "14 days")
    payment = st.text_input("Payment", "50% upfront")
    if st.button("📑 Generate Contract PDF"):
        contract_text = f"CONTRACT\nBetween: {freelancer_name} and {client_name_c}\nScope: {scope}"
        pdf_file = create_pdf(contract_text, f"Contract_{re.sub(r'[^A-Za-z0-9]+', '_', client_name_c)}")
        st.session_state.contracts.append({"Client": client_name_c, "Date": str(date.today())})
        st.download_button("📥 Export PDF", open(pdf_file, "rb"), pdf_file)

# === TAB 7 FIXED: PURA HISTORY + PROFILE + SETTINGS ===
with tab7:
    st.subheader("📜 Document History")
    
    with st.expander("Gig History", expanded=True):
        if st.session_state.gig_descriptions: 
            st.dataframe(pd.DataFrame(st.session_state.gig_descriptions), use_container_width=True)
        else: 
            st.info("No gigs generated yet.")

    with st.expander("Pricing Quotes History"):
        if st.session_state.pricing_history: 
            st.dataframe(pd.DataFrame(st.session_state.pricing_history), use_container_width=True)
        else: 
            st.info("No quotes generated yet.")

    with st.expander("Invoice History"):
        if st.session_state.invoices: 
            st.dataframe(pd.DataFrame(st.session_state.invoices), use_container_width=True)
        else: 
            st.info("No invoices generated yet.")

    with st.expander("Contract History"):
        if st.session_state.contracts: 
            st.dataframe(pd.DataFrame(st.session_state.contracts), use_container_width=True)
        else: 
            st.info("No contracts generated yet.")

    with st.expander("Client Replies History"):
        if st.session_state.client_replies: 
            st.dataframe(pd.DataFrame(st.session_state.client_replies), use_container_width=True)
        else: 
            st.info("No replies saved yet.")

    st.divider()
    st.subheader("👤 User Profile")
    c1, c2 = st.columns([1, 2])
    with c1:
        uploaded_file = st.file_uploader("Upload Picture", type=['png', 'jpg'])
        if uploaded_file:
            st.session_state.user_profile["pic"] = uploaded_file
            st.image(uploaded_file, width=150)
        elif st.session_state.user_profile["pic"]:
            st.image(st.session_state.user_profile["pic"], width=150)
        else:
            st.image("https://via.placeholder.com/150", caption="No Image")

    with c2:
        st.text_input("Name", value=st.session_state.user_profile["name"], key="name_edit")
        st.text_input("Email", value=st.session_state.user_profile["email"], key="email_edit")
        st.text_input("Password", type="password", placeholder="Enter new password")

        if st.button("Save Profile"):
            st.session_state.user_profile["name"] = st.session_state.name_edit
            st.session_state.user_profile["email"] = st.session_state.email_edit
            st.success("Profile Updated Successfully!")

    st.divider()
    st.subheader("⚙️ Application Settings")
    theme = st.selectbox("Theme", ["Light", "Dark", "Blue"], index=["Light", "Dark", "Blue"].index(st.session_state.app_settings["theme"]))
    api_key = st.text_input("API Key", type="password", placeholder="Enter your OpenAI Key")
    notify = st.toggle("Notifications", value=st.session_state.app_settings["notifications"])
    lang = st.selectbox("Language", ["English", "Urdu", "Arabic"], index=["English", "Urdu", "Arabic"].index(st.session_state.app_settings["language"]))
    if st.button("Save Settings"):
        st.session_state.app_settings = {"theme": theme, "language": lang, "notifications": notify}
        st.success("Settings Saved!")
