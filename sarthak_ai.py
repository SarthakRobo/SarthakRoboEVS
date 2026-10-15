import os, asyncio, base64, uuid, re, urllib.request, urllib.parse
from flask import request, jsonify
import edge_tts
from google import genai
from google.genai import types

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "AQ.Ab8RN6LJ64xyPk5qf" + "LbRSMfkQaPnyufDChamuGl1kc7p0gJSgg")
ai_client = genai.Client(api_key=GEMINI_API_KEY)

SARTHAK_DETAILS = ""
if os.path.exists("sarthak_details.txt"):
    with open("sarthak_details.txt", "r", encoding="utf-8") as f:
        SARTHAK_DETAILS = f.read()

AUDIO_CACHE = {}
REPLY_CACHE = {}

LANG_RULES = {
    "hi-IN": "जवाब केवल शुद्ध हिंदी (देवनागरी) में दो। शुरुआत में 'जी', 'हाँ जी', 'अरे' बिल्कुल मत लगाओ, सीधे उत्तर दो।",
    "gu-IN": "જવાબ ફક્ત શુદ્ધ ગુજરાતી લિપિમાં જ આપો. શરૂઆતમાં વધારાના શબ્દો ન મૂકો, સીધો જ જવાબ આપો. ('મેંનૂ', 'મલા' નહીં પણ 'મને', 'મારું' વાપરો).",
    "en-IN": "Reply strictly in natural Indian English. Give a direct answer without filler words."
}

# Instant 0.1s answers for common questions
FAST_QA = [
    (["आपका नाम", "तुम्हारा नाम", "तेरा नाम", "what is your name", "your name", "તારું નામ", "તમારું નામ", "तारु नाम", "तमारु नाम"], {
        "hi-IN": "मेरा नाम सार्थक पटेल है, और घर में सब मुझे प्यार से गोटू बुलाते हैं।",
        "gu-IN": "મારું નામ સાર્થક પટેલ છે, અને ઘરમાં બધા મને પ્રેમથી ગોટુ બોલાવે છે.",
        "en-IN": "My name is Sarthak Patel, and my nickname is Gotu."
    }),
    (["किसने बनाया", "कोणे बनाव्यो", "who made you", "who created you", "કિસને બનાયા", "કોણે બનાવ્યો"], {
        "hi-IN": "मैं सार्थक पटेल हूँ, और इस रोबोट प्रोजेक्ट को मैंने खुद अपने पापा जिगर पटेल के मार्गदर्शन में बनाया है।",
        "gu-IN": "હું સાર્થક પટેલ છું, અને આ રોબોટ પ્રોજેક્ટ મેં પોતે મારા પપ્પા જિગર પટેલના માર્ગદર્શનથી બનાવ્યો છે.",
        "en-IN": "I am Sarthak Patel, and I built this robot project myself under the guidance of my father Jigar Patel."
    }),
    (["पापा का नाम", "पिताजी का नाम", "father name", "પપ્પાનું નામ", "पप्पा नु नाम"], {
        "hi-IN": "मेरे पापा का नाम जिगर पटेल है।",
        "gu-IN": "મારા પપ્પાનું નામ જિગર પટેલ છે.",
        "en-IN": "My father's name is Jigar Patel."
    }),
    (["मम्मी का नाम", "माताजी का नाम", "mother name", "મમ્મીનું નામ", "मम्मी नू नाम", "तारी मम्मी"], {
        "hi-IN": "मेरी मम्मी का नाम भावना पटेल है।",
        "gu-IN": "મારી મમ્મીનું નામ ભાવના પટેલ છે.",
        "en-IN": "My mother's name is Bhavna Patel."
    }),
    (["दादा का नाम", "दादाजी का नाम", "grandfather name", "દાદાનું નામ"], {
        "hi-IN": "मेरे दादाजी का नाम जयंतीभाई पटेल है।",
        "gu-IN": "મારા દાદાનું નામ જયંતીભાઈ પટેલ છે.",
        "en-IN": "My grandfather's name is Jayantibhai Patel."
    }),
    (["दादी का नाम", "दादीजी का नाम", "grandmother name", "દાદીનું નામ"], {
        "hi-IN": "मेरी दादीजी का नाम कोकिलाबेन पटेल है।",
        "gu-IN": "મારી દાદીનું નામ કોકિલાબેન પટેલ છે.",
        "en-IN": "My grandmother's name is Kokilaben Patel."
    }),
    (["चाचा का नाम", "चाची का नाम", "काका", "काकी", "uncle name", "કાકાનું નામ"], {
        "hi-IN": "मेरे चाचा का नाम अमित पटेल और चाची का नाम नेहा पटेल है।",
        "gu-IN": "મારા કાકાનું નામ અમિત પટેલ અને કાકીનું નામ નેહા પટેલ છે.",
        "en-IN": "My uncle's name is Amit Patel and my aunt's name is Neha Patel."
    }),
    (["स्कूल का नाम", "कया स्कूल", "school name", "સ્કૂલનું નામ", "શાળાનું નામ"], {
        "hi-IN": "मैं एसवीएम इंटरनेशनल स्कूल, रसम में कक्षा 4 में पढ़ता हूँ।",
        "gu-IN": "હું એસવીએમ ઇન્ટરનેશનल સ્કૂલ, રસમમાં ધોરણ 4 માં ભણું છું.",
        "en-IN": "I study in Class 4th at SVM International School, Rasam."
    }),
    (["प्रिंसिपल", "principal", "પ્રિન્સિપાલ", "आचार्य"], {
        "hi-IN": "मेरे स्कूल के प्रिंसिपल साथ सर हैं।",
        "gu-IN": "મારી સ્કૂલના પ્રિન્સિપાલ સાથ સર છે.",
        "en-IN": "Our school principal is Saath Sir."
    }),
    (["ट्रस्टी", "trustee", "ટ્રસ્ટી"], {
        "hi-IN": "हमारे स्कूल के ट्रस्टी महेशभाई पटेल और व्रज सर हैं।",
        "gu-IN": "અમારી સ્કૂલના ટ્રસ્ટી મહેશભાઈ પટેલ અને વ્રજ સર છે.",
        "en-IN": "Our school trustees are Maheshbhai Patel and Vraj Sir."
    }),
    (["क्लास टीचर", "class teacher", "ક્લાસ ટીચર"], {
        "hi-IN": "मेरी क्लास टीचर प्रियंका मैम हैं, और वे हमें हिंदी भी पढ़ाती हैं।",
        "gu-IN": "મારા ક્લાસ ટીચર પ્રિયંકા મેડમ છે.",
        "en-IN": "My class teacher is Priyanka Ma'am."
    })
]

def check_fast_qa(user_text, lang_code):
    low = user_text.lower().strip()
    for keys, ans_map in FAST_QA:
        for k in keys:
            if k in low:
                # If user asked in Gujarati words, return Gujarati
                if any(ch in user_text for ch in "તમણછશળ") or "तारु" in low or "तमारु" in low or "मम्मी नू" in low:
                    return ans_map["gu-IN"]
                return ans_map.get(lang_code, ans_map["hi-IN"])
    return None

def clean_ai_text(text):
    text = re.sub(r"[*#_`~]", "", text or "").strip()
    text = re.sub(r"[\u0600-\u06FF]+", "", text)
    text = re.sub(r"\s*\([^)]{1,35}\)", "", text)
    # Strip 'जी', 'हाँ जी', 'नहीं जी', 'अरे यार' from start so answer is direct
    text = re.sub(r"^(हाँ जी|नहीं जी|जी हाँ|जी नहीं|अरे यार|नहीं यार|हाँ यार|अरे!|अरे|जी)[,!\s]*", "", text)
    text = text.replace("नहीं यार", "नहीं").replace("हाँ यार", "हाँ").replace("अरे यार", "").replace(" यार,", ",").replace(" यार ", " ")
    text = text.replace("हाँ जी,", "हाँ,").replace("नहीं जी,", "नहीं,").replace(" जी,", ",")
    text = text.replace("बिना मैडम", "बिनल मैम").replace("बीना मैडम", "बिनल मैम")
    text = text.replace("सांथ सर", "साथ सर").replace("सांथ", "साथ").replace("સાંથ સર", "સાથ સર")
    text = text.replace("મેંનૂ", "મને").replace("મલા પ્યાર થી", "મને પ્રેમથી").replace("મલા", "મને")
    return text.strip()

def detect_best_voice(text, requested_lang):
    gu = len(re.findall(r'[\u0A80-\u0AFF]', text))
    hi = len(re.findall(r'[\u0900-\u097F]', text))
    if requested_lang == "gu-IN" or (gu > hi and gu > 0):
        return "gu-IN-DhwaniNeural", "gu"
    if requested_lang == "en-IN" and hi == 0 and gu == 0:
        return "en-IN-PrabhatNeural", "en"
    return "hi-IN-MadhurNeural", "hi"

def generate_voice_b64(text, lang_code):
    key = f"{lang_code}:{text}"
    if key in AUDIO_CACHE:
        return AUDIO_CACHE[key]
    voice, tl = detect_best_voice(text, lang_code)
    # Fast Google TTS first for ultra-low latency (<0.4s), fallback to edge-tts if >180 chars
    if len(text) <= 180:
        try:
            url = "https://translate.googleapis.com/translate_tts?ie=UTF-8&client=tw-ob&tl=" + tl + "&q=" + urllib.parse.quote(text)
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=3) as r:
                data = r.read()
                if data:
                    b64 = base64.b64encode(data).decode("utf-8")
                    AUDIO_CACHE[key] = b64
                    return b64
        except Exception:
            pass

    tmp = f"temp_{uuid.uuid4().hex}.mp3"
    try:
        asyncio.run(edge_tts.Communicate(text, voice, rate="+12%").save(tmp))
        with open(tmp, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode("utf-8")
        if len(AUDIO_CACHE) < 150:
            AUDIO_CACHE[key] = b64
        return b64
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)

def get_ai_reply(user_text, lang_code, history):
    user_text = user_text.replace("बिना मैडम", "बिनल मैम").replace("सांथ सर", "साथ सर")
    cache_k = f"{lang_code}:{user_text.lower()}"
    if not history and cache_k in REPLY_CACHE:
        return REPLY_CACHE[cache_k]

    fast_ans = check_fast_qa(user_text, lang_code)
    if fast_ans and len(user_text.split()) <= 7:
        return fast_ans

    hist = ""
    if history:
        hist = "पिछली बात:\n" + "\n".join([f"{'Q' if h.get('role')=='user' else 'A'}: {h.get('text','')}" for h in history[-3:]]) + "\n"

    prompt = (
        "तुम 10 साल के छात्र 'सार्थक पटेल' (गोटू) हो।\n"
        "नियम:\n"
        "1. सीधे मुद्दे का जवाब दो। शुरुआत में 'जी', 'हाँ जी', 'नहीं जी', 'अरे', 'यार' कभी मत लगाओ।\n"
        "2. मम्मी के निमोनिया या स्कूल में पिटाई जैसी झूठी बात का सीधा खंडन करो कि ऐसा कभी नहीं हुआ।\n"
        "3. मेरा जन्म 10 नवंबर 2016 (गुरुवार) को कलोल में हुआ। 8 नवंबर 2016 की नोटबंदी मेरे जन्म से 2 दिन पहले हुई थी।\n"
        "4. जवाब अधिकतम 1 छोटी लाइन (12-15 शब्द) में बिना ब्रैकेट के दो।\n"
        "5. " + LANG_RULES.get(lang_code, LANG_RULES["hi-IN"]) + "\n"
        "मेरी जानकारी:\n" + SARTHAK_DETAILS + "\n" + hist +
        "सवाल: " + user_text + "\nसीधा जवाब:"
    )
    res = ai_client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=prompt,
        config=types.GenerateContentConfig(max_output_tokens=60, temperature=0.3)
    )
    ans = clean_ai_text(res.text)
    if len(REPLY_CACHE) < 200:
        REPLY_CACHE[cache_k] = ans
    return ans

def register_ai_routes(app):
    @app.route('/ask_text', methods=['POST'])
    def ask_text_only():
        try:
            d = request.get_json(force=True)
            txt = d.get("text", "").strip()
            if not txt:
                return jsonify({"error": "Empty"}), 400
            return jsonify({"text": get_ai_reply(txt, d.get("lang", "hi-IN"), d.get("history", []))})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/tts', methods=['POST'])
    def tts_only():
        try:
            d = request.get_json(force=True)
            txt = d.get("text", "").strip()
            if not txt:
                return jsonify({"error": "Empty"}), 400
            return jsonify({"audio": generate_voice_b64(txt, d.get("lang", "hi-IN"))})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/ask', methods=['POST'])
    def ask_sarthak():
        try:
            d = request.get_json(force=True)
            txt = d.get("text", "").strip()
            lang = d.get("lang", "hi-IN")
            if not txt:
                return jsonify({"error": "Empty"}), 400
            reply = get_ai_reply(txt, lang, d.get("history", []))
            return jsonify({"text": reply, "audio": generate_voice_b64(reply, lang)})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
