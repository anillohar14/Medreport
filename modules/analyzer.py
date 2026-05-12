from .rules import rules, CATEGORY_ORDER, get_rule_text
from .lang_utils import t, normalise_lang


def _get_severity(value, rule):
    low, high = rule.get("low"), rule.get("high")
    deviation, status, color = 0.0, "Normal", "#22c55e"

    if high is not None and value > high:
        deviation = ((value - high) / high) * 100
        if deviation > 50:   status, color = "Critical",      "#dc2626"
        elif deviation > 20: status, color = "High",          "#ef4444"
        else:                status, color = "Borderline-High","#f97316"
    elif low is not None and value < low:
        deviation = ((low - value) / low) * 100
        if deviation > 50:   status, color = "Critical",      "#7c3aed"
        elif deviation > 20: status, color = "Low",           "#ef4444"
        else:                status, color = "Borderline-Low","#f97316"

    return status, color, round(deviation, 1)


def _calculate_health_score(all_results):
    score = 100
    for r in all_results:
        s = r["status"]
        if "Critical" in s:        score -= 15
        elif s in ("High","Low"):  score -= 7
        elif "Borderline" in s:    score -= 3
    return max(score, 0)


# ─── Pattern text in all 3 languages ─────────────────────────
_PT = {
    "anaemia_name": {
        "en":  "Iron Deficiency Anaemia",
        "hi":  "आयरन की कमी से एनीमिया",
        "hin": "Iron Deficiency Anaemia",
    },
    "anaemia_expl": {
        "en":  "Haemoglobin, MCH and MCHC — all three are low. Classic pattern of Iron Deficiency Anaemia. RBCs become small due to lack of iron and carry less haemoglobin.",
        "hi":  "हीमोग्लोबिन, MCH और MCHC — तीनों कम हैं। आयरन की कमी से एनीमिया का क्लासिक पैटर्न। आयरन की कमी से RBC छोटी हो जाती हैं।",
        "hin": "Hemoglobin, MCH aur MCHC — teeno low hain. Ye Iron Deficiency Anaemia ka classic pattern hai. Body mein iron ki kami se RBC chhota ho jata hai aur unme haemoglobin bhi kam hoti hai.",
    },
    "anaemia_action": {
        "en":  "1. Start iron supplement (ask doctor).\n2. Take with Vitamin C for better absorption.\n3. Eat spinach, chickpeas, dates, meat.\n4. Avoid tea/coffee with food.\n5. Repeat CBC after 3 months.",
        "hi":  "1. आयरन सप्लीमेंट शुरू करें (डॉक्टर से)।\n2. विटामिन C के साथ लें — अवशोषण बढ़ता है।\n3. पालक, चना, खजूर, मांस खाएं।\n4. खाने के साथ चाय/कॉफी न पिएं।\n5. 3 महीने बाद CBC दोबारा करवाएं।",
        "hin": "1. Iron supplement shuru karo — doctor se lo.\n2. Vitamin C ke saath lo — absorption badhti hai.\n3. Palak, chana, khajoor, meat zyada khao.\n4. Chai/coffee khaane ke saath mat piyo.\n5. 3 mahine baad CBC repeat karo.",
    },
    "cardio_name": {
        "en":  "Cardiovascular Risk Pattern",
        "hi":  "हृदय जोखिम पैटर्न",
        "hin": "Cardiovascular Risk Pattern",
    },
    "cardio_expl": {
        "en":  "Triglycerides high, HDL (good cholesterol) low, VLDL high — this combination is a heart disease risk indicator.",
        "hi":  "ट्राइग्लिसराइड्स अधिक, HDL कम, VLDL अधिक — यह हृदय रोग जोखिम का संकेतक है।",
        "hin": "Triglycerides high, HDL (good cholesterol) low, aur VLDL high — ye combination dil ki bimari ka risk indicator hai.",
    },
    "cardio_action": {
        "en":  "1. Reduce sweets, refined flour and rice.\n2. Walk 30-45 minutes daily.\n3. Eat olive oil, nuts and avocado.\n4. Consider Omega-3 — ask your doctor.\n5. See a cardiologist.",
        "hi":  "1. मिठाई, मैदा, चावल कम करें।\n2. रोज़ 30-45 मिनट चलें।\n3. जैतून का तेल, मेवे, एवोकाडो खाएं।\n4. ओमेगा-3 पर विचार करें — डॉक्टर से पूछें।\n5. हृदय रोग विशेषज्ञ से मिलें।",
        "hin": "1. Meetha, maida, rice kam karo.\n2. Roz 30-45 min brisk walk karo.\n3. Olive oil, nuts, avocado lo.\n4. Omega-3 consider karo — doctor se poocho.\n5. Cardiologist se ek baar milo.",
    },
    "vit_name": {
        "en":  "Vitamin Deficiency",
        "hi":  "विटामिन की कमी",
        "hin": "Vitamin Deficiency",
    },
    "vit_expl": {
        "en":  "Vitamin D is deficient (deficiency zone <20). Very common in India, especially women above 40. Causes fatigue, bone pain, and low immunity.",
        "hi":  "विटामिन D की कमी है (कमी क्षेत्र <20)। भारत में बहुत सामान्य है, विशेषकर 40+ महिलाओं में।",
        "hin": "Vitamin D deficient hai (deficiency zone <20). India mein ye bahut common hai, khaaskar women mein 40+ ke baad. Thakaan, bone pain, aur immunity problems cause karta hai.",
    },
    "vit_action": {
        "en":  "1. Vitamin D3: 60,000 IU weekly for 8 weeks (confirm with doctor).\n2. Then maintenance: 1000-2000 IU daily.\n3. Morning sunlight 15-20 min without sunscreen.\n4. For B12: eat yoghurt, milk, eggs, paneer.\n5. Retest Vitamin D after 3 months.",
        "hi":  "1. विटामिन D3: 60,000 IU साप्ताहिक × 8 सप्ताह (डॉक्टर से पुष्टि)।\n2. रखरखाव: 1000-2000 IU दैनिक।\n3. सुबह 15-20 मिनट धूप में — सनस्क्रीन के बिना।\n4. B12: दही, दूध, अंडे, पनीर खाएं।\n5. 3 महीने बाद पुनः जांच।",
        "hin": "1. Vitamin D3: 60,000 IU weekly x 8 hafte — doctor se confirm karo.\n2. Maintenance: 1000-2000 IU daily.\n3. Subah 15-20 min dhoop — bina sunscreen.\n4. B12 ke liye: dahi, doodh, eggs, paneer khao.\n5. 3 mahine baad Vitamin D re-test karo.",
    },
    "bili_name": {
        "en":  "Elevated Bilirubin — Liver Watch",
        "hi":  "बढ़ा हुआ बिलीरुबिन — यकृत निगरानी",
        "hin": "Elevated Bilirubin — Liver Watch",
    },
    "bili_expl": {
        "en":  "Total and Indirect Bilirubin are slightly elevated. SGOT/SGPT are normal — so this is not liver cell damage. Could be Gilbert's Syndrome or mild haemolysis — usually benign but must be confirmed.",
        "hi":  "कुल और अप्रत्यक्ष बिलीरुबिन थोड़े अधिक हैं। SGOT/SGPT सामान्य हैं — यकृत कोशिका क्षति नहीं। गिल्बर्ट सिंड्रोम या हल्का हीमोलिसिस हो सकता है।",
        "hin": "Total aur Indirect Bilirubin dono slightly elevated hain. SGOT/SGPT normal hain — liver cell damage nahi lagta. Ye Gilbert's Syndrome ya mild haemolysis ho sakta hai — usually benign. Lekin confirm zaroor karo.",
    },
    "bili_action": {
        "en":  "1. Stop alcohol completely.\n2. Avoid paracetamol overuse.\n3. Get a liver ultrasound.\n4. Repeat LFT in 4-6 weeks.\n5. Get Reticulocyte Count to rule out haemolysis.",
        "hi":  "1. शराब बिल्कुल बंद करें।\n2. पेरासिटामोल का अत्यधिक उपयोग न करें।\n3. लिवर अल्ट्रासाउंड करवाएं।\n4. 4-6 सप्ताह में LFT दोबारा करवाएं।\n5. रेटिकुलोसाइट काउंट भी करवाएं।",
        "hin": "1. Alcohol bilkul band karo.\n2. Paracetamol overuse avoid karo.\n3. Liver ultrasound karwao.\n4. 4-6 hafte mein LFT repeat karo.\n5. Reticulocyte Count bhi karwao.",
    },
    "esr_name": {
        "en":  "Elevated Inflammation Marker (ESR)",
        "hi":  "बढ़ा हुआ सूजन संकेतक (ESR)",
        "hin": "Elevated Inflammation Marker (ESR)",
    },
    "esr_expl": {
        "en":  "ESR is high — normal for women is 0-20. ESR is non-specific — it shows inflammation somewhere in the body. Could be due to anaemia, infection, arthritis or autoimmune condition.",
        "hi":  "ESR अधिक है — महिलाओं के लिए सामान्य 0-20 है। ESR गैर-विशिष्ट है — शरीर में कहीं सूजन है।",
        "hin": "ESR high hai — normal for women is 0-20. ESR ek non-specific test hai — body mein kahin inflammation hai. Anaemia, infection, arthritis ya autoimmune condition ho sakta hai.",
    },
    "esr_action": {
        "en":  "1. Treat anaemia first — iron deficiency can raise ESR.\n2. Get a CRP test — more specific.\n3. If joint pain, see a rheumatologist.\n4. ESR must be seen in context.",
        "hi":  "1. पहले एनीमिया का इलाज करें।\n2. CRP परीक्षण करवाएं — अधिक विशिष्ट।\n3. जोड़ों में दर्द है तो रुमेटोलॉजिस्ट से मिलें।\n4. ESR को संदर्भ में देखें।",
        "hin": "1. Pehle anaemia treat karo — iron deficiency ESR badha sakti hai.\n2. CRP test karwao — zyada specific hai.\n3. Joints mein dard hai toh rheumatologist se milo.\n4. ESR ko context mein dekho.",
    },
}

def _pt(key, lang):
    return _PT.get(key, {}).get(lang) or _PT.get(key, {}).get("hin", "")


def _detect_patterns(data, lang):
    patterns = []

    # ── Anaemia ──
    sc = 0
    if data.get("Hemoglobin",99)<12: sc+=2
    if data.get("MCH",99)<27:        sc+=2
    if data.get("MCHC",99)<31:       sc+=2
    if data.get("RDW",0)>14.5:       sc+=1
    if data.get("Iron",99)<60:       sc+=1
    if sc >= 4:
        patterns.append({
            "name":pt("anaemia_name",lang),"confidence":"High" if sc>=6 else "Moderate",
            "color":"#ef4444","involved":["Hemoglobin","MCH","MCHC","RDW","Iron"],
            "explanation":pt("anaemia_expl",lang),"action":pt("anaemia_action",lang),
        })

    # ── Cardiovascular ──
    sc = 0
    if data.get("Triglycerides",0)>150: sc+=2
    if data.get("HDL",99)<55:           sc+=2
    if data.get("LDL",0)>100:           sc+=1
    if data.get("VLDL",0)>30:           sc+=2
    if data.get("Cholesterol",0)>200:   sc+=1
    if sc >= 4:
        patterns.append({
            "name":pt("cardio_name",lang),"confidence":"High" if sc>=6 else "Moderate",
            "color":"#f97316","involved":["Triglycerides","HDL","LDL","VLDL","Cholesterol"],
            "explanation":pt("cardio_expl",lang),"action":pt("cardio_action",lang),
        })

    # ── Vitamin ──
    sc = 0
    if data.get("Vitamin D",99)<30:  sc+=3
    if data.get("Vitamin B12",0)<300: sc+=1
    if sc >= 3:
        patterns.append({
            "name":pt("vit_name",lang),"confidence":"High",
            "color":"#a855f7","involved":["Vitamin D","Vitamin B12"],
            "explanation":pt("vit_expl",lang),"action":pt("vit_action",lang),
        })

    # ── Bilirubin ──
    sc = 0
    if data.get("Bilirubin Total",0)>0.9:    sc+=2
    if data.get("Bilirubin Indirect",0)>0.6: sc+=2
    if data.get("SGOT",0)>31: sc+=1
    if data.get("SGPT",0)>34: sc+=1
    if sc >= 3:
        patterns.append({
            "name":pt("bili_name",lang),"confidence":"Moderate",
            "color":"#eab308","involved":["Bilirubin Total","Bilirubin Indirect"],
            "explanation":pt("bili_expl",lang),"action":pt("bili_action",lang),
        })

    # ── ESR ──
    if data.get("ESR",0) > 20:
        patterns.append({
            "name":pt("esr_name",lang),"confidence":"Moderate",
            "color":"#f97316","involved":["ESR"],
            "explanation":pt("esr_expl",lang),"action":pt("esr_action",lang),
        })

    return patterns

def pt(key, lang):
    return _PT.get(key,{}).get(lang) or _PT.get(key,{}).get("hin","")


def analyze(data: dict, lang: str = "hin") -> dict:
    lang = normalise_lang(lang)
    all_results = []

    for param, value in data.items():
        if param not in rules:
            continue
        rule = rules[param]
        status, color, deviation = _get_severity(value, rule)

        if "High" in status:
            meaning    = get_rule_text(param, "meaning_high",    lang)
            suggestion = get_rule_text(param, "suggestion_high", lang)
        elif "Low" in status:
            meaning    = get_rule_text(param, "meaning_low",     lang)
            suggestion = get_rule_text(param, "suggestion_low",  lang)
        else:
            meaning = suggestion = ""

        all_results.append({
            "name":param,"value":value,"unit":rule.get("unit",""),
            "status":status,"color":color,"deviation":deviation,
            "category":rule.get("category","Other"),
            "meaning":meaning,"suggestion":suggestion,
        })

    issues     = [r for r in all_results if r["status"] not in ("Normal",) and "Borderline" not in r["status"]]
    borderline = [r for r in all_results if "Borderline" in r["status"]]
    normal     = [r for r in all_results if r["status"] == "Normal"]
    issues.sort(key=lambda x: x["deviation"], reverse=True)

    by_category = {}
    for cat in CATEGORY_ORDER:
        ci = [r for r in (issues+borderline) if r["category"]==cat]
        cn = [r for r in normal if r["category"]==cat]
        if ci or cn:
            by_category[cat] = {"issues":ci,"normal":cn,"has_problems":len(ci)>0}

    health_score = _calculate_health_score(all_results)
    if health_score >= 85:   score_label, score_color = t("score_good",lang),     "#22c55e"
    elif health_score >= 65: score_label, score_color = t("score_moderate",lang),  "#f97316"
    elif health_score >= 40: score_label, score_color = t("score_poor",lang),      "#ef4444"
    else:                    score_label, score_color = t("score_critical",lang),   "#7c3aed"

    patterns = _detect_patterns(data, lang)

    crit_n = sum(1 for r in issues if r["status"]=="Critical")
    high_n = sum(1 for r in issues if r["status"] in ("High","Low"))
    bord_n = len(borderline)

    if issues or borderline:
        summary = t("summary_issues",lang,c=crit_n,h=high_n,b=bord_n,s=health_score,l=score_label)
    else:
        summary = t("summary_all_ok",lang,s=health_score,l=score_label)

    if issues:
        final_advice = t("advice_has_issues",lang,p=issues[0]["name"],st=issues[0]["status"])
    elif borderline:
        final_advice = t("advice_borderline",lang)
    else:
        final_advice = t("advice_all_ok",lang)

    return {
        "summary":summary,"health_score":health_score,"score_label":score_label,
        "score_color":score_color,"issues":issues,"borderline":borderline,"normal":normal,
        "by_category":by_category,"patterns":patterns,"final_advice":final_advice,
        "total_checked":len(all_results),"lang":lang,
    }
