# 💬 HYCODE Interactive Chatbot (Smart, Simple & Offline)

# 🧩 Step 1: Install and import required libraries (sirf pehli dafa chalao)
!pip install transformers torch sentencepiece -q

from transformers import AutoModelForCausalLM, AutoTokenizer

# 🧠 Step 2: Load Free AI Model (DialoGPT)
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

print("✅ HYCODE Smart Chatbot Ready! Type 'exit' to stop.\n")

# 🗣️ Step 3: Define main reply function
def hycode_bot_reply(user_input):
    user = user_input.lower()

    # 👋 Greetings
    if user in ["hi", "hello", "hey"]:
        return "Hello! I’m HYCODE Assistant 👋 I can help you with POS, ERP systems, or business solutions!"
    elif user in ["assalamualaikum", "salam"]:
        return "Wa Alaikum Assalam! How can I assist you today?"

    # 📍 Location Queries
    if any(phrase in user for phrase in [
        "where you provide", "where do you provide", "location", "karachi", "pakistan",
        "available in", "which city", "area", "cities"
    ]):
        return (
            "📍 We provide our services all across Pakistan — especially in Karachi:\n"
            "Clifton, Gulshan, Korangi, North Karachi, Saddar, and many more!\n\n"
            "💬 You can also book a *Free Demo* today 👉 https://hycodeinnovation.com"
        )

    # 💼 Services Queries
    elif any(phrase in user for phrase in [
        "services", "what do you do", "kya karte", "kam", "work", "your service", "ap kya karte", "ap kya krte"
    ]):
        return (
            "HYCODE provides complete business solutions:\n\n"
            "💻 Software Development\n"
            "🌐 Web & App Development\n"
            "🎯 Digital Marketing\n"
            "🤖 AI & Automation\n\n"
            "Which one would you like to explore?"
        )

    # 🌐 Web / App Development
    elif any(word in user for word in ["web", "app", "website", "android", "ios"]):
        return (
            "🌐 Web & App Development Services:\n"
            "• Business & Portfolio Sites\n"
            "• E-Commerce Stores\n"
            "• Android & iOS Apps\n\n"
            "Would you like website or mobile app details?"
        )

    # 🎯 Digital Marketing
    elif any(word in user for word in ["marketing", "seo", "ads", "branding"]):
        return (
            "🎯 Digital Marketing Services:\n"
            "• SEO & Google Ads\n"
            "• Social Media Marketing\n"
            "• Brand Identity & Logo Design\n\n"
            "Would you like details about a specific area?"
        )

    # 🤖 AI / Automation
    elif any(word in user for word in ["ai", "automation", "chatbot", "data", "analytics"]):
        return (
            "🤖 HYCODE AI & Automation:\n"
            "• Chatbots\n"
            "• Data Analytics Tools\n"
            "• AI Content Generators\n\n"
            "Would you like to know how these tools work?"
        )

    # 🧾 Wholesale POS
    elif "wholesale pos" in user:
        return (
            "🧾 Wholesale POS System:\n"
            "1️⃣ Billing & Invoices\n"
            "2️⃣ Stock & Supplier Management\n"
            "3️⃣ Profit & Expense Tracking\n"
            "4️⃣ Multi-User Access\n"
            "Perfect for distributors and wholesalers!"
        )

    # 🛍️ Retail POS
    elif "retail pos" in user:
        return (
            "🛍️ Retail POS System:\n"
            "1️⃣ Barcode Billing\n"
            "2️⃣ Sales & Receipts Management\n"
            "3️⃣ Real-Time Stock Updates\n"
            "4️⃣ Discount & Report Features"
        )

    # 🏢 ERP Systems
    elif "erp" in user:
        return (
            "🏢 Enterprise ERP System:\n"
            "1️⃣ Sales, HR & Accounts in one place\n"
            "2️⃣ Real-Time Business Reports\n"
            "3️⃣ Custom Modules per industry\n"
            "4️⃣ Increases productivity & accuracy"
        )

    # 🍽️ Restaurant System
    elif "restaurant" in user:
        return (
            "🍽️ Restaurant Management:\n"
            "1️⃣ Table & Order Handling\n"
            "2️⃣ Kitchen Display (KOT)\n"
            "3️⃣ Billing & Staff Management\n"
            "4️⃣ Menu Tracking & Reports"
        )

    # 🧵 Textile ERP
    elif "textile" in user or "garment" in user:
        return (
            "🧵 Textile & Garment ERP:\n"
            "1️⃣ Track Production & Stitching\n"
            "2️⃣ Raw Material Management\n"
            "3️⃣ Order Status Monitoring\n"
            "4️⃣ Delivery & Cost Reports"
        )

    # 🗨️ General Small Talks
    elif "how are you" in user:
        return "I’m doing great! 😊 How about you?"
    elif "your name" in user or "who are you" in user:
        return "I’m HYCODE Assistant 🤖 — your virtual guide for business solutions."
    elif "thank" in user:
        return "You're welcome! 😊 Glad to help."
    elif "bye" in user or "goodbye" in user:
        return "Goodbye 👋 Visit https://hycodeinnovation.com anytime!"
    elif "joke" in user:
        return "😅 Sorry, I can’t tell jokes — but I can help you grow your business!"

    # 🤖 Default AI Reply (fallback with DialoGPT)
    else:
        input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
        reply_ids = model.generate(
            input_ids,                          # user input tokens
            max_length=120,                     # max reply length
            temperature=0.7,                    # creativity level
            top_p=0.9,                          # natural response control
            pad_token_id=tokenizer.eos_token_id, # padding token
            do_sample=True,                     # random reply variation
            num_return_sequences=1              # only 1 reply
        )
        bot_reply = tokenizer.decode(reply_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
        return bot_reply + "\n\nVisit 👉 https://hycodeinnovation.com for more info."

# 💬 Step 4: Chat Loop
print("🤖 HYCODE Chatbot Online!\n")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "allah hafiz", "khuda hafiz", "goodbye", "exit"]:
        print("Bot: Goodbye! 👋 Have a great day.")
        break
    print("Bot:", hycode_bot_reply(user_input), "\n")
