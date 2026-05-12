UI_STRINGS = {

    # ── Error messages ──────────────────────────────────────

    "err_no_file": {
        "en":  "No file received in request.",
        "hi":  "अनुरोध में कोई फ़ाइल नहीं मिली।",
        "hin": "Request mein koi file nahi mili.",
    },
    "err_no_select": {
        "en":  "No file selected.",
        "hi":  "कोई फ़ाइल चुनी नहीं गई।",
        "hin": "File select nahi ki.",
    },
    "err_no_values": {
        "en":  "No medical values found in PDF.\nIs the PDF correct? Is Tesseract installed?",
        "hi":  "PDF में कोई मेडिकल मान नहीं मिले।\nक्या PDF सही है? क्या Tesseract इंस्टॉल है?",
        "hin": "PDF se koi medical values nahi mile.\nCheck karo: PDF sahi hai? Tesseract install hai?",
    },

    # ── Health score labels ───────────────────────────────────

    "score_good": {
        "en":  "Good",
        "hi":  "अच्छा",
        "hin": "Accha",
    },
    "score_moderate": {
        "en":  "Moderate",
        "hi":  "सामान्य",
        "hin": "Theek-Thaak",
    },
    "score_poor": {
        "en":  "Poor",
        "hi":  "खराब",
        "hin": "Kharab",
    },
    "score_critical": {
        "en":  "Critical",
        "hi":  "गंभीर",
        "hin": "Critical",
    },

    # ── Summary text ─────────────────────────────────────────

    "summary_issues": {
        "en":  "{c} critical, {h} out-of-range, {b} borderline parameters found. Health score: {s}/100 ({l}).",
        "hi":  "{c} गंभीर, {h} सीमा से बाहर, {b} सीमारेखा पैरामीटर मिले। स्वास्थ्य स्कोर: {s}/100 ({l})।",
        "hin": "{c} critical, {h} out-of-range, {b} borderline parameters mile. Health score: {s}/100 ({l}).",
    },
    "summary_all_ok": {
        "en":  "All parameters look normal. Health score: {s}/100 ({l}).",
        "hi":  "सभी पैरामीटर सामान्य हैं। स्वास्थ्य स्कोर: {s}/100 ({l})।",
        "hin": "Sab parameters normal hain. Health score: {s}/100 ({l}).",
    },

    # ── Final advice ─────────────────────────────────────────

    "advice_has_issues": {
        "en":  "Pay attention to '{p}' ({st}) first. Read the patterns and suggestions below carefully. Final diagnosis must be done by a doctor — this report is only a guide.",
        "hi":  "सबसे पहले '{p}' ({st}) पर ध्यान दें। नीचे दिए गए पैटर्न और सुझाव ध्यान से पढ़ें। अंतिम निदान केवल डॉक्टर ही कर सकते हैं — यह रिपोर्ट सिर्फ मार्गदर्शन के लिए है।",
        "hin": "Sabse pehle '{p}' pe dhyan do ({st}). Neeche diye gaye patterns aur suggestions zaroor padho. Kisi bhi bimari ka final diagnosis doctor hi karta hai — ye report sirf guide karne ke liye hai.",
    },
    "advice_borderline": {
        "en":  "No critical issue found, but some values are in the borderline zone. Improve your lifestyle and retest in 3 months.",
        "hi":  "कोई गंभीर समस्या नहीं है, लेकिन कुछ मान सीमारेखा क्षेत्र में हैं। जीवनशैली सुधारें और 3 महीने में पुनः परीक्षण करें।",
        "hin": "Koi critical issue nahi hai, lekin kuch values borderline zone mein hain. Lifestyle improve karo aur 3 mahine mein retest karo.",
    },
    "advice_all_ok": {
        "en":  "Everything is in normal range. Keep up the good lifestyle!",
        "hi":  "सब कुछ सामान्य सीमा में है। अच्छी जीवनशैली बनाए रखें!",
        "hin": "Sab kuch normal range mein hai. Acchi lifestyle banaye rakho!",
    },

    # ── Consult doctor default ────────────────────────────────

    "consult": {
        "en":  "Consult your doctor.",
        "hi":  "डॉक्टर से मिलें।",
        "hin": "Doctor se milo.",
    },
}


# ─────────────────────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────────────────────

VALID_LANGS = ("en", "hi", "hin")
DEFAULT_LANG = "en"


def normalise_lang(lang: str) -> str:
    """
    User se jo bhi lang aaye — validate karo.
    Invalid ho toh default (en) use karo.
    """
    if lang and lang.lower() in VALID_LANGS:
        return lang.lower()
    return DEFAULT_LANG


def t(key: str, lang: str = DEFAULT_LANG, **kwargs) -> str:
    """
    UI string translation function.

    Usage:
        t("err_no_file", lang)
        t("summary_issues", lang, c=1, h=7, b=4, s=41, l="Kharab")
    """
    lang = normalise_lang(lang)
    entry = UI_STRINGS.get(key, {})
    text  = entry.get(lang) or entry.get(DEFAULT_LANG) or key

    if kwargs:
        try:
            text = text.format(**kwargs)
        except KeyError:
            pass

    return text


def get_lang_key(base_key: str, lang: str) -> str:
    """
    rules.py mein language-specific key banana.

    Example:
        get_lang_key("meaning_low", "hi")  →  "meaning_low_hi"
        get_lang_key("meaning_low", "en")  →  "meaning_low_en"
        get_lang_key("meaning_low", "hin") →  "meaning_low_hin"

    Fallback order:
        requested lang → hin (Hinglish) → en (English) → base key (no suffix)
    """
    lang = normalise_lang(lang)
    return f"{base_key}_{lang}"
