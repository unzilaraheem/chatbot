# HYCODE Chatbot (Roman Urdu + English Hybrid)
# Works offline | CLI-based | Type 'bye' or 'allah hafiz' to exit

from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

print("\n🤖 HYCODE Chatbot Ready (Roman Urdu + English)\n")

def hycode_bot_reply(user_input):
    user = user_input.lower().strip()

    # 🌐 Roman Urdu synonyms for easy matching
    if any(w in user for w in ["service", "services", "kam", "work", "ap kya karte", "ap kya krte"]):
        return (
            "HYCODE provides complete business solutions:\n\n"
            "1) Software Development\n"
            "2) Web & App Development\n"
            "3) Digital Marketing\n"
            "4) AI & Automation\n\n"
            "Kis service ke bare me maloomat chahiye?"
        )

    # 💻 Software Solutions
    if any(w in user for w in ["software", "system", "program", "softwer"]):
        return (
            "HYCODE Software Solutions include:\n"
            "- Wholesale POS System\n"
            "- Retail POS System\n"
            "- ERP & Business Management\n"
            "- Restaurant & Distribution Systems\n\n"
            "Kis software ke bare me detail chahiye?"
        )

    # 🧾 Wholesale POS
    if any(w in user for w in ["wholesale pos", "whole pos", "pos system", "pos", "point of sale"]):
        return (
            "Wholesale POS System features:\n"
            "1) Easy Billing & Invoices\n"
            "2) Stock & Supplier Management\n"
            "3) Profit & Expense Tracking\n"
            "4) Multi-User Access\n\n"
            "Perfect for distributors & wholesalers."
        )

    # 🏢 ERP
    if any(w in user for w in ["erp", "erp system", "erp software"]):
        return (
            "ERP System features:\n"
            "1) Sales, HR & Accounts in one place\n"
            "2) Real-time business reports\n"
            "3) Custom modules per industry\n"
            "4) Better workflow & accuracy"
        )

    # 🌐 Web / App
    if any(w in user for w in ["website", "web", "app", "android", "ios", "ecommerce"]):
        return (
            "Web & App Development:\n"
            "- Business & Portfolio Websites\n"
            "- E-Commerce Stores\n"
            "- Android & iOS Apps\n\n"
            "Apko website chahiye ya mobile app?"
        )

    # 🎯 Marketing
    if any(w in user for w in ["marketing", "seo", "ads", "branding", "promotion", "digital"]):
        return (
            "Digital Marketing Services:\n"
            "- Google Ads & SEO\n"
            "- Social Media Management\n"
            "- Brand Identity & Logo Design\n\n"
            "Kis area me marketing chahiye?"
        )

    # 🤖 AI / Automation
    if any(w in user for w in ["ai", "automation", "chatbot", "data", "auto"]):
        return (
            "AI & Automation Tools:\n"
            "- Chatbots\n"
            "- Data Analytics Tools\n"
            "- AI Content Generators\n\n"
            "Kya ap AI based solutions chahte hain?"
        )

    # 📍 Location
    if any(w in user for w in ["karachi", "pakistan", "kahan", "location", "area", "city"]):
        return (
            "We provide our services all across Pakistan — specially Karachi:\n"
            "Clifton, Gulshan, Korangi, North Karachi, Saddar and others.\n\n"
            "Free demo bhi book kar sakte hain : https://hycodeinnovation.com"
        )

    # 🗣 Small Talk
    if any(w in user for w in ["hi", "hello", "salam", "assalamualaikum"]):
        return "Hello! I’m HYCODE Assistant. How can I help you today?"
    if "how are you" in user or "kaise ho" in user:
        return "I’m fine, thank you! Aap kaise hain?"
    if any(w in user for w in ["thank", "shukriya"]):
        return "You're welcome! Always happy to help."
    if any(w in user for w in ["your name", "who are you", "kya naam", "ap kon"]):
        return "I’m HYCODE Assistant — your virtual business guide."
    if any(w in user for w in ["joke", "funny"]):
        return "Sorry, jokes nahi bata sakta — but I can help you grow your business!"

    #  Default: AI model response
    tokens = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    generated = model.generate(
        tokens,
        max_length=120,
        temperature=0.7,
        top_p=0.9,
        pad_token_id=tokenizer.eos_token_id
    )
    reply = tokenizer.decode(generated[:, tokens.shape[-1]:][0], skip_special_tokens=True)
    return reply + "\n\nFor more info visit: https://hycodeinnovation.com"


# ----------------------------
# Chat Loop
# ----------------------------
print("HYCODE Chatbot Online (Roman Urdu Mode). Type 'bye' or 'allah hafiz' to exit.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["bye", "allah hafiz", "khuda hafiz", "goodbye"]:
        print("Bot: Allah Hafiz. Have a great day!")
        break
    print("Bot:", hycode_bot_reply(user_input), "\n")

