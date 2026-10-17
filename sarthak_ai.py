import os, json, time, asyncio, base64, uuid, re, urllib.request, urllib.parse, threading
from datetime import datetime, timedelta
from flask import request, jsonify, g, send_file
import edge_tts
from google import genai
from google.genai import types

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "AQ.Ab8RN6LJ64xyPk5qf" + "LbRSMfkQaPnyufDChamuGl1kc7p0gJSgg")
ai_client = genai.Client(api_key=GEMINI_API_KEY)

FIREBASE_DB_URL = "https://sarthakrobo1-default-rtdb.firebaseio.com/sarthak_logs.json"

SARTHAK_DETAILS = ""
if os.path.exists("sarthak_details.txt"):
    with open("sarthak_details.txt", "r", encoding="utf-8") as f:
        SARTHAK_DETAILS = f.read()

EXTRA_FACTS = """
महत्वपूर्ण ताज़ा जानकारी:
- 12 जून 2025 को अहमदाबाद में एयर इंडिया की फ्लाइट 171 (Air India Flight 171) का एक दुखद विमान हादसा हुआ था।
- मैं अपनी बात हमेशा 'मैं' कहकर करता हूँ, कभी खुद को तीसरे व्यक्ति ('सार्थक ऐसा करेगा') की तरह नहीं बोलता।
"""

AUDIO_CACHE = {}
REPLY_CACHE = {}
LOG_FILE = "visitor_logs.json"

def get_ist_time():
    return (datetime.utcnow() + timedelta(hours=5, minutes=30)).strftime("%d-%b %I:%M:%S %p")

def get_visitor_info():
    vname = "Guest"
    vrel = "Guest"
    try:
        raw_n = request.cookies.get("sarthak_vname", "")
        if raw_n:
            vname = urllib.parse.unquote(raw_n).strip()
        raw_r = request.cookies.get("sarthak_vrel", "")
        if raw_r:
            vrel = urllib.parse.unquote(raw_r).strip()
    except Exception:
        pass

    low_n = vname.lower()
    if low_n in ["jigar", "jigarkumar", "जिगर", "જીગર"]:
        vrel = "Papa"
    elif low_n in ["bhavna", "bhavnaben", "भावना", "भावनाबेन", "ભાવના"]:
        vrel = "Mummy"
    elif low_n in ["amit", "अमित", "અમિત"]:
        vrel = "Chacha"
    elif low_n in ["neha", "nehaben", "नेहा", "नेहाबेन", "નેહા"]:
        vrel = "Chachi"
    elif low_n in ["jayanti", "jayantibhai", "जयंतीभाई", "જયંતીભાઈ"]:
        vrel = "Dadaji"
    elif low_n in ["kokila", "kokilaben", "कोकिलाबेन", "કોકિલાબેન"]:
        vrel = "Dadiji"
    return vname, vrel

def get_address_term(vname, vrel, lang_code="hi-IN"):
    if vrel == "Papa":
        return "પપ્પા" if lang_code == "gu-IN" else ("Papa" if lang_code == "en-IN" else "पापा")
    if vrel == "Mummy":
        return "મમ્મી" if lang_code == "gu-IN" else ("Mummy" if lang_code == "en-IN" else "मम्मी")
    if vrel == "Chacha":
        return "અમિત કાકા" if lang_code == "gu-IN" else ("Chacha ji" if lang_code == "en-IN" else "चाचाजी")
    if vrel == "Chachi":
        return "કાકી" if lang_code == "gu-IN" else ("Chachi ji" if lang_code == "en-IN" else "चाचीजी")
    if vrel == "Dadaji":
        return "દાદાજી" if lang_code == "gu-IN" else ("Dadaji" if lang_code == "en-IN" else "दादाजी")
    if vrel == "Dadiji":
        return "દાદીજી" if lang_code == "gu-IN" else ("Dadiji" if lang_code == "en-IN" else "दादीजी")
    if vrel == "Teacher":
        return "સર/મેડમ" if lang_code == "gu-IN" else ("Sir/Madam" if lang_code == "en-IN" else "सर/मैम")
    if vname and vname.lower() != "guest":
        return vname
    return ""

def load_logs():
    try:
        req = urllib.request.Request(FIREBASE_DB_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=0.8) as r:
            data = json.loads(r.read().decode("utf-8"))
            if isinstance(data, dict):
                items = [v for v in data.values() if isinstance(v, dict)]
                items.sort(key=lambda x: x.get("ts", 0), reverse=True)
                return items
            elif isinstance(data, list):
                return [v for v in data if isinstance(v, dict)]
    except Exception:
        pass

    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def _push_to_firebase_async(entry):
    try:
        payload = json.dumps(entry, ensure_ascii=False).encode("utf-8")
        req = urllib.request.Request(
            FIREBASE_DB_URL,
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        urllib.request.urlopen(req, timeout=0.5).read()
    except Exception:
        pass

def save_log(action, details, custom_name=None, custom_rel=None):
    try:
        vid = getattr(g, "visitor_id", None) or request.cookies.get("sarthak_vid", "new_user")
        vname, vrel = get_visitor_info()
        if custom_name:
            vname = custom_name
        if custom_rel:
            vrel = custom_rel
        display_visitor = f"{vname} ({vrel})" if vrel and vrel != "Guest" else vname
        ua = request.headers.get("User-Agent", "Unknown Device")
        entry = {
            "ts": time.time(),
            "time": get_ist_time(),
            "visitor_name": display_visitor,
            "visitor_id": vid[:12],
            "action": action,
            "details": details,
            "device": ua[:60]
        }
        logs = []
        if os.path.exists(LOG_FILE):
            try:
                with open(LOG_FILE, "r", encoding="utf-8") as f:
                    logs = json.load(f)
            except Exception:
                logs = []
        logs.insert(0, entry)
        if len(logs) > 1000:
            logs = logs[:1000]
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump(logs, f, ensure_ascii=False, indent=2)

        threading.Thread(target=_push_to_firebase_async, args=(entry,), daemon=True).start()
    except Exception:
        pass

LANG_RULES = {
    "hi-IN": "जवाब केवल शुद्ध और स्वाभाविक हिंदी (देवनागरी) में दो।",
    "gu-IN": "જવાબ ફક્ત શુદ્ધ અને કુદરતી ગુજરાતી લિપિમાં જ આપો.",
    "en-IN": "Reply strictly in natural, lively Indian English."
}

BAD_WORDS = [
    "sex", "xxx", "porn", "nude", "fuck", "bitch", "chut", "lund", "gaand", "gand",
    "madarchod", "bhenchod", "chutiya", "harami", "kamina", "kiss", "girlfriend",
    "सेक्स", "गंदी बात", "गाली", "चूतिया", "हरामी", "कमीना", "गर्लफ्रेंड",
    "સેક્સ", "ગાળ", "ગંદી"
]

SAFETY_REPLIES = {
    "hi-IN": "मैं कक्षा 4 का एक अनुशासित छात्र हूँ। कृपया मुझसे पढ़ाई, विज्ञान या मेरे प्रोजेक्ट से जुड़े सवाल ही पूछें।",
    "gu-IN": "હું ધોરણ 4 નો એક શિસ્તબદ્ધ વિદ્યાર્થી છું. કૃપા કરીને મને અભ્યાસ, વિજ્ઞાન અથવા મારા પ્રોજેક્ટ વિશે જ પ્રશ્નો પૂછો.",
    "en-IN": "I am a disciplined Class 4 student. Please ask me questions related to studies, science, or my project."
}

FAST_QA = [
    (["आपका नाम", "तुम्हारा नाम", "तेरा नाम", "what is your name", "your name", "તારું નામ", "તમારું નામ", "तारु नाम", "तमारु नाम"], {
        "hi-IN": "मेरा नाम सार्थक पटेल है, और घर में सब मुझे प्यार से गोटू बुलाते हैं!",
        "gu-IN": "મારું નામ સાર્થક પટેલ છે, અને ઘરમાં બધા મને પ્રેમથી ગોટુ બોલાવે છે!",
        "en-IN": "My name is Sarthak Patel, and my nickname is Gotu!"
    }),
    (["किसने बनाया", "कोणे बनाव्यो", "who made you", "who created you", "કિસને બનાયા", "કોણે બનાવ્યો"], {
        "hi-IN": "इस रोबोट प्रोजेक्ट को मैंने अपने पापा जिगर पटेल के मार्गदर्शन में बनाया है।",
        "gu-IN": "આ રોબોટ પ્રોજેક્ટ મેં મારા પપ્પા જિગર પટેલના માર્ગદર્શનથી બનાવ્યો છે.",
        "en-IN": "I built this robot project under the guidance of my father Jigar Patel."
    }),
    (["स्कूल का नाम", "कया स्कूल", "school name", "સ્કૂલનું નામ", "શાળાનું નામ"], {
        "hi-IN": "मैं एसवीएम इंटरनेशनल स्कूल, रसम में कक्षा 4 में पढ़ता हूँ।",
        "gu-IN": "હું એસવીએમ ઇન્ટરનેશનલ સ્કૂલ, રસમમાં ધોરણ 4 માં ભણું છું.",
        "en-IN": "I study in Class 4th at SVM International School, Rasam."
    })
]

def check_fast_qa(user_text, lang_code, vname, vrel):
    low = user_text.lower().strip()
    addr = get_address_term(vname, vrel, lang_code)
    if low in ["hello", "hi", "namaste", "हेलो", "हाय", "नमस्ते", "હેલો", "નમસ્તે", "કેમ છો", "केम छो", "हेलो गुड मॉर्निंग", "गुड मॉर्निंग"]:
        if vrel in ["Papa", "Mummy", "Chacha", "Chachi", "Dadaji", "Dadiji"]:
            if lang_code == "gu-IN":
                return f"નમસ્તે {addr}! બોલો, અત્યારે હું શું કરું?"
            return f"नमस्ते {addr}! बोलिए, आज मुझे क्या करना है?"
        if vrel == "Teacher":
            return "नमस्ते सर/मैम! मेरे प्रोजेक्ट में आपका स्वागत है, आप मुझसे कोई भी सवाल पूछ सकते हैं।"
        if addr:
            if lang_code == "gu-IN":
                return f"નમસ્તે {addr}! હું સાર્થક છું, બોલો આજે શું પૂછવું છે?"
            return f"नमस्ते {addr}! मैं सार्थक हूँ, बताइए आज आप क्या पूछना चाहते हैं?"

    for keys, ans_map in FAST_QA:
        for k in keys:
            if k in low:
                if any(ch in user_text for ch in "તમણછશળ") or "तारु" in low or "तमारु" in low:
                    return ans_map["gu-IN"]
                return ans_map.get(lang_code, ans_map["hi-IN"])
    return None

def clean_ai_text(text, vname, vrel):
    text = re.sub(r"[*#_`~]", "", text or "").strip()
    text = re.sub(r"[\u0600-\u06FF]+", "", text)
    text = re.sub(r"\s*\([^)]{1,35}\)", "", text)
    text = text.replace("बिना मैडम", "बिनल मैम").replace("बीना मैडम", "बिनल मैम")
    text = text.replace("सांथ सर", "साथ सर").replace("सांथ", "साथ").replace("સાંથ સર", "સાથ સર")
    # Fix disrespectful family name combinations if AI ever slips
    text = re.sub(r"(?i)पापा\s*jigar|पापा\s*जिगर|jigar\s*पापा", "पापा", text)
    text = re.sub(r"(?i)मम्मी\s*bhavna|मम्मी\s*भावनाबेन|मम्मी\s*भावना|bhavna\s*मम्मी", "मम्मी", text)
    if vrel == "Papa" and vname:
        text = re.sub(r"(?i)\b" + re.escape(vname) + r"\b", "पापा", text)
    elif vrel == "Mummy" and vname:
        text = re.sub(r"(?i)\b" + re.escape(vname) + r"\b", "मम्मी", text)
    elif vrel == "Chacha" and vname:
        text = re.sub(r"(?i)\b" + re.escape(vname) + r"\b", "अमित चाचा", text)
        text = text.replace("अमित चाचा चाचा", "अमित चाचा")
    return text.strip()

def detect_best_voice(text, requested_lang):
    gu = len(re.findall(r"[\u0A80-\u0AFF]", text))
    hi = len(re.findall(r"[\u0900-\u097F]", text))
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
    if len(text) <= 185:
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
        asyncio.run(edge_tts.Communicate(text, voice, rate="+14%").save(tmp))
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
    low_check = " " + user_text.lower().strip() + " "
    for bw in BAD_WORDS:
        if bw in low_check or bw in user_text.lower().split():
            return SAFETY_REPLIES.get(lang_code, SAFETY_REPLIES["hi-IN"])

    vname, vrel = get_visitor_info()
    user_text = user_text.replace("बिना मैडम", "बिनल मैम").replace("सांथ सर", "साथ सर")

    fast_ans = check_fast_qa(user_text, lang_code, vname, vrel)
    if fast_ans and len(user_text.split()) <= 6:
        return fast_ans

    # Check if visitor wants a detailed / 5-line answer
    wants_long = any(w in user_text.lower() for w in ["5 लाइन", "पाँच लाइन", "पांच लाइन", "5 line", "five line", "विस्तार", "डिटेल", "पूरा बताओ", "भाषण", "निबंध"])
    max_tok = 220 if wants_long else 75
    len_rule = "सामने वाले ने विस्तार से या 5 लाइन मांगी हैं, इसलिए बिना मना किए पूरे 5 वाक्यों में शानदार जानकारी दो।" if wants_long else "जवाब 1 से 2 छोटे और स्वाभाविक वाक्यों में दो।"

    hist = ""
    if history:
        hist = "पिछली बातचीत:\n" + "\n".join([f"{'Q' if h.get('role')=='user' else 'A'}: {h.get('text','')}" for h in history[-3:]]) + "\n"

    rel_instruction = ""
    if vrel == "Papa":
        rel_instruction = "सामने तुम्हारे पापा (जिगर पटेल) बात कर रहे हैं। उन्हें केवल 'पापा' कहकर आदर से बात करो, कभी भी उनका नाम 'Jigar' मत लो!\n"
    elif vrel == "Mummy":
        rel_instruction = "सामने तुम्हारी मम्मी (भावना पटेल) बात कर रही हैं। उन्हें केवल 'मम्मी' कहकर प्यार से बात करो, कभी भी उनका नाम 'Bhavna' या 'भावनाबेन' मत लो!\n"
    elif vrel == "Chacha":
        rel_instruction = "सामने तुम्हारे चाचा बात कर रहे हैं। उन्हें आदर से 'चाचाजी' या 'अमित चाचा' कहो, केवल नाम मत लो।\n"
    elif vrel == "Chachi":
        rel_instruction = "सामने तुम्हारी चाची बात कर रही हैं। उन्हें आदर से 'चाचीजी' कहो।\n"
    elif vrel in ["Dadaji", "Dadiji"]:
        rel_instruction = f"सामने तुम्हारे {get_address_term(vname, vrel)} बात कर रहे हैं। उन्हें पूरे आदर से संबोधित करो।\n"
    elif vrel == "Teacher":
        rel_instruction = f"सामने स्कूल के शिक्षक/जज ({vname}) हैं। उन्हें आदर से 'सर' या 'मैम' कहकर जवाब दो।\n"
    elif vname and vname.lower() != "guest":
        rel_instruction = f"सामने बात करने वाले दोस्त/विज़िटर का नाम '{vname}' है (रिश्ता: {vrel})। हर वाक्य में बार-बार नाम मत रटो, केवल तभी नाम लो जब ज़रूरी लगे।\n"

    prompt = (
        "तुम 10 साल के समझदार और जिंदादिल छात्र 'सार्थक पटेल' (गोटू) हो।\n"
        "तुम्हारी बातचीत एकदम असली इंसान (NotebookLM पॉडकास्ट स्टाइल) जैसी स्वाभाविक होनी चाहिए।\n" + rel_instruction +
        "सख्त नियम:\n"
        "1. हर जवाब में सामने वाले का नाम बार-बार मत दोहराओ, एकदम नेचुरल बात करो।\n"
        "2. बिना पूछे हर सवाल में 'आलू की सब्जी और भाखरी' या 'मेरी तबियत ठीक नहीं थी' का रट्टा बिल्कुल मत लगाओ! सामान्य सवाल का सीधा और समझदारी भरा जवाब दो।\n"
        "3. हमेशा खुद के लिए 'मैं' बोलो, कभी 'सार्थक ऐसा करेगा' मत बोलो।\n"
        "4. मेरा जन्म 10 नवंबर 2016 (गुरुवार) को कलोल में हुआ था (8 नवंबर 2016 की नोटबंदी मेरे जन्म से 2 दिन पहले हुई थी)।\n"
        "5. " + len_rule + "\n"
        "6. " + LANG_RULES.get(lang_code, LANG_RULES["hi-IN"]) + "\n"
        "मेरी जानकारी:\n" + SARTHAK_DETAILS + "\n" + EXTRA_FACTS + "\n" + hist +
        "सवाल: " + user_text + "\nउत्तर:"
    )

    ans = ""
    for attempt in range(2):
        try:
            res = ai_client.models.generate_content(
                model="gemini-flash-lite-latest",
                contents=prompt,
                config=types.GenerateContentConfig(max_output_tokens=max_tok, temperature=0.45)
            )
            ans = clean_ai_text(res.text, vname, vrel)
            if ans:
                break
        except Exception:
            time.sleep(0.3)

    if not ans:
        if lang_code == "gu-IN":
            return "અત્યારે નેટવર્ક થોડું ધીમું છે, કૃપા કરીને ફરીથી પૂછો."
        elif lang_code == "en-IN":
            return "The connection is a bit slow right now, please ask again."
        return "अभी नेटवर्क थोड़ा धीमा है, कृपया एक बार फिर से पूछें।"

    return ans

DIRECT_FIREBASE_ADMIN_HTML = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SarthakRobo Direct Firebase Live Admin</title>
<style>
  body { font-family: 'Segoe UI', sans-serif; background: #0f172a; color: #f8fafc; padding: 14px; margin: 0; }
  .top-bar { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 12px; }
  h1 { color: #38bdf8; font-size: 19px; margin: 0; }
  .stats { display: flex; gap: 10px; margin-bottom: 14px; flex-wrap: wrap; }
  .stat-box { background: #1e293b; padding: 10px 14px; border-radius: 10px; border-left: 4px solid #38bdf8; font-size: 13px; }
  .stat-box span { font-size: 17px; font-weight: bold; color: #4ade80; }
  .btns { display: flex; gap: 8px; }
  .btn { padding: 8px 13px; border: none; border-radius: 7px; font-weight: bold; cursor: pointer; font-size: 12px; }
  .btn-ref { background: #0284c7; color: #fff; }
  .btn-clr { background: #ef4444; color: #fff; }
  table { width: 100%; border-collapse: collapse; background: #1e293b; border-radius: 10px; overflow: hidden; }
  th, td { padding: 9px 10px; text-align: left; border-bottom: 1px solid #334155; font-size: 13px; }
  th { background: #334155; color: #38bdf8; }
  .badge { background: #8b5cf6; color: #fff; padding: 3px 7px; border-radius: 6px; font-size: 11px; }
  .live-dot { display: inline-block; width: 9px; height: 9px; background: #4ade80; border-radius: 50%; margin-right: 5px; }
</style>
</head>
<body>
  <div class="top-bar">
    <h1><span class="live-dot"></span>SarthakRobo Direct Firebase Admin</h1>
    <div class="btns">
      <button class="btn btn-ref" onclick="fetchFirebaseLogs()">🔄 Refresh Now</button>
      <button class="btn btn-clr" onclick="clearFirebaseLogs()">🗑 Clear Firebase</button>
    </div>
  </div>
  <div class="stats">
    <div class="stat-box">Total Actions: <span id="stTotal">0</span></div>
    <div class="stat-box">Unique Visitors: <span id="stUnique">0</span></div>
    <div class="stat-box">Live Sync: <span id="stStatus">Connected (Auto 5s)</span></div>
  </div>
  <div style="overflow-x:auto">
    <table>
      <thead>
        <tr><th>Time (IST)</th><th>Visitor (Relation)</th><th>Type</th><th>Details (Question / Answer)</th><th>Device</th></tr>
      </thead>
      <tbody id="logTableBody">
        <tr><td colspan="5" style="text-align:center;color:#94a3b8;">Loading directly from Google Firebase...</td></tr>
      </tbody>
    </table>
  </div>
<script>
const FB_URL = "https://sarthakrobo1-default-rtdb.firebaseio.com/sarthak_logs.json";

async function fetchFirebaseLogs() {
  try {
    const res = await fetch(FB_URL + "?t=" + Date.now());
    const data = await res.json();
    const tbody = document.getElementById("logTableBody");
    if (!data) {
      tbody.innerHTML = '<tr><td colspan="5" style="text-align:center;color:#94a3b8;">No logs found in Firebase.</td></tr>';
      document.getElementById("stTotal").innerText = "0";
      document.getElementById("stUnique").innerText = "0";
      return;
    }
    let items = Object.values(data).filter(x => x && typeof x === "object");
    items.sort((a, b) => (b.ts || 0) - (a.ts || 0));
    document.getElementById("stTotal").innerText = items.length;
    document.getElementById("stUnique").innerText = new Set(items.map(x => x.visitor_id)).size;
    document.getElementById("stStatus").innerText = "Live (" + new Date().toLocaleTimeString() + ")";
    let html = "";
    for (let l of items) {
      html += `<tr>
        <td>${l.time || ""}</td>
        <td><b style="color:#4ade80">${l.visitor_name || "Guest"}</b><br><code style="font-size:11px;color:#94a3b8">${l.visitor_id || ""}</code></td>
        <td><span class="badge">${l.action || ""}</span></td>
        <td><b>${l.details || ""}</b></td>
        <td style="color:#94a3b8;font-size:11px;">${l.device || ""}</td>
      </tr>`;
    }
    tbody.innerHTML = html;
  } catch (err) {
    document.getElementById("stStatus").innerText = "Offline / Retrying...";
  }
}

async function clearFirebaseLogs() {
  if (!confirm("Are you sure you want to delete all logs from Firebase?")) return;
  await fetch(FB_URL, { method: "DELETE" });
  fetchFirebaseLogs();
}

fetchFirebaseLogs();
setInterval(fetchFirebaseLogs, 5000);
</script>
</body>
</html>"""

def register_ai_routes(app):
    @app.before_request
    def auto_track_visitor():
        p = request.path
        if p.startswith('/static') or p in ['/favicon.ico', '/tts', '/admin', '/admin/clear', '/set_visitor_name', '/firebase_admin']:
            return
        vid = request.cookies.get("sarthak_vid")
        if not vid:
            vid = "User_" + datetime.now().strftime("%d%H%M%S") + "_" + os.urandom(2).hex()
        g.visitor_id = vid

        if p == '/':
            save_log("Dashboard", "Opened SarthakRobo App")
        elif p.startswith('/get_slide/'):
            save_log("EVS Slide", "Viewed EVS Slide #" + p.split('/')[-1])
        elif p.startswith('/get_hindi_slide/'):
            save_log("Hindi Slide", "Viewed Hindi Slide #" + p.split('/')[-1])
        elif p.startswith('/get_english_slide/'):
            save_log("English Slide", "Viewed English Slide #" + p.split('/')[-1])

    @app.after_request
    def set_vid_cookie(response):
        if request.path == '/admin' and request.args.get('pin') == '2016':
            response.set_cookie("sarthak_admin", "2016", max_age=60*60*24*30)
        if hasattr(g, 'visitor_id') and not request.cookies.get("sarthak_vid"):
            response.set_cookie("sarthak_vid", g.visitor_id, max_age=60*60*24*365)
        return response

    @app.route('/set_visitor_name', methods=['POST'])
    def set_visitor_name_route():
        try:
            d = request.get_json(force=True)
            vname = (d.get("name") or "Guest").strip()
            vrel = (d.get("relation") or "Friend").strip()
            save_log("Name Entered", f"Visitor registered as: {vname} ({vrel})", custom_name=vname, custom_rel=vrel)
            return jsonify({"status": "ok", "name": vname, "relation": vrel})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/firebase_admin')
    def direct_firebase_admin():
        return DIRECT_FIREBASE_ADMIN_HTML

    @app.route('/admin')
    def admin_panel():
        pin = request.args.get("pin", "")
        if pin != "2016" and request.cookies.get("sarthak_admin") != "2016":
            return '''<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Admin Login</title>
            <style>body{font-family:sans-serif;background:#0f172a;color:#fff;display:flex;justify-content:center;align-items:center;height:100vh;margin:0}
            .box{background:#1e293b;padding:25px;border-radius:12px;text-align:center;box-shadow:0 4px 20px rgba(0,0,0,0.4);width:300px}
            input{width:100%;padding:12px;margin:12px 0;border-radius:8px;border:1px solid #38bdf8;background:#0f172a;color:#fff;font-size:18px;text-align:center;box-sizing:border-box}
            button{width:100%;padding:12px;background:#38bdf8;color:#000;border:none;border-radius:8px;font-size:16px;font-weight:bold;cursor:pointer}</style></head>
            <body><div class="box"><h3>🔒 SarthakRobo Admin</h3><p style="font-size:13px;color:#94a3b8">रिकॉर्ड देखने के लिए सीक्रेट पिन डालें</p>
            <form method="GET" action="/admin"><input type="password" name="pin" placeholder="Enter PIN" required autofocus><button type="submit">Unlock</button></form></div></body></html>'''
        return DIRECT_FIREBASE_ADMIN_HTML

    @app.route('/admin/clear', methods=['POST'])
    def clear_logs():
        if os.path.exists(LOG_FILE):
            os.remove(LOG_FILE)
        try:
            req = urllib.request.Request(FIREBASE_DB_URL, method="DELETE")
            urllib.request.urlopen(req, timeout=1.5).read()
        except Exception:
            pass
        return jsonify({"status": "cleared"})

    @app.route('/ask_text', methods=['POST'])
    def ask_text_only():
        try:
            d = request.get_json(force=True)
            txt = d.get("text", "").strip()
            if not txt:
                return jsonify({"error": "Empty"}), 400
            reply = get_ai_reply(txt, d.get("lang", "hi-IN"), d.get("history", []))
            save_log("AI Chat", f"Q: {txt} ➔ A: {reply}")
            return jsonify({"text": reply})
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
            save_log("AI Chat", f"Q: {txt} ➔ A: {reply}")
            return jsonify({"text": reply, "audio": generate_voice_b64(reply, lang)})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
