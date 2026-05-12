
rules = {

    # ═══════════════════════════════════════════
    # BLOOD SUGAR / DIABETES
    # ═══════════════════════════════════════════

    "Glucose Fasting": {
        "low": 70, "high": 110, "unit": "mg/dL", "category": "Diabetes",

        "meaning_low_en":   "Blood sugar is very low (hypoglycemia). May cause dizziness and weakness.",
        "meaning_low_hi":   "रक्त शर्करा बहुत कम है। चक्कर और कमज़ोरी हो सकती है।",
        "meaning_low_hin":  "Blood sugar bahut kam hai (hypoglycemia). Chakkar, kamzori ho sakti hai.",

        "meaning_high_en":  "Fasting sugar is high — may indicate diabetes or pre-diabetes.",
        "meaning_high_hi":  "उपवास शर्करा अधिक है — मधुमेह या प्री-डायबिटीज़ का संकेत।",
        "meaning_high_hin": "Fasting sugar high hai — diabetes ya pre-diabetes ka sign ho sakta hai.",

        "suggestion_low_en":   "Eat something sweet immediately. See a doctor.",
        "suggestion_low_hi":   "तुरंत कुछ मीठा खाएं। डॉक्टर से मिलें।",
        "suggestion_low_hin":  "Turant kuch meetha khao. Doctor se milo.",

        "suggestion_high_en":  "Reduce sugar intake. Ask your doctor to test HbA1c.",
        "suggestion_high_hi":  "चीनी का सेवन कम करें। डॉक्टर से HbA1c परीक्षण करवाएं।",
        "suggestion_high_hin": "Sugar intake kam karo. Doctor se HbA1c test karwao.",
    },

    "Glucose PP": {
        "low": 80, "high": 140, "unit": "mg/dL", "category": "Diabetes",

        "meaning_low_en":   "Blood sugar is still very low even after eating.",
        "meaning_low_hi":   "खाने के बाद भी रक्त शर्करा बहुत कम है।",
        "meaning_low_hin":  "Khana khane ke baad bhi sugar bahut kam hai.",

        "meaning_high_en":  "Post-meal sugar is quite high — diabetes control may be poor.",
        "meaning_high_hi":  "खाने के बाद शर्करा काफ़ी अधिक है — मधुमेह नियंत्रण ठीक नहीं।",
        "meaning_high_hin": "Khane ke baad sugar kaafi zyada hai — diabetes control kharab ho sakta hai.",

        "suggestion_low_en":   "See your doctor.",
        "suggestion_low_hi":   "डॉक्टर से मिलें।",
        "suggestion_low_hin":  "Doctor se milo.",

        "suggestion_high_en":  "Control your diet, avoid refined carbs. See a doctor.",
        "suggestion_high_hi":  "आहार नियंत्रित करें, रिफाइंड कार्ब्स से बचें। डॉक्टर से मिलें।",
        "suggestion_high_hin": "Diet control karo, refined carbs avoid karo. Doctor se milo.",
    },

    "HbA1c": {
        "low": 4.0, "high": 5.7, "unit": "%", "category": "Diabetes",

        "meaning_low_en":   "HbA1c abnormally low — possible haemolytic condition.",
        "meaning_low_hi":   "HbA1c असामान्य रूप से कम है — संभावित हीमोलिटिक स्थिति।",
        "meaning_low_hin":  "HbA1c abnormally low — possible haemolytic condition.",

        "meaning_high_en":  "HbA1c above 5.7% — pre-diabetes or diabetes zone. Average blood sugar was high over 3 months.",
        "meaning_high_hi":  "HbA1c 5.7% से अधिक — प्री-डायबिटीज़ या मधुमेह क्षेत्र। 3 महीने की औसत शर्करा अधिक रही।",
        "meaning_high_hin": "HbA1c 5.7% se zyada hai — prediabetes ya diabetes zone mein. Pichle 3 mahine ka average sugar high raha.",

        "suggestion_low_en":   "See a doctor.",
        "suggestion_low_hi":   "डॉक्टर से मिलें।",
        "suggestion_low_hin":  "Doctor se milo.",

        "suggestion_high_en":  "Reduce sugar and refined flour. Walk 30 minutes daily. See a doctor.",
        "suggestion_high_hi":  "चीनी और मैदा कम करें। रोज़ 30 मिनट चलें। डॉक्टर से मिलें।",
        "suggestion_high_hin": "Sugar aur maida bilkul kam karo. Roz 30 min walk karo. Doctor se milo.",
    },

    # ═══════════════════════════════════════════
    # IRON PROFILE
    # ═══════════════════════════════════════════

    "Iron": {
        "low": 33, "high": 193, "unit": "mcg/dL", "category": "Iron Profile",

        "meaning_low_en":   "Iron deficiency — may cause anaemia, fatigue, hair loss.",
        "meaning_low_hi":   "आयरन की कमी — एनीमिया, थकान, बाल झड़ना हो सकता है।",
        "meaning_low_hin":  "Iron ki kami hai — anaemia ho sakta hai, thakaan, baal girna.",

        "meaning_high_en":  "Iron is too high — may put load on the liver.",
        "meaning_high_hi":  "आयरन बहुत अधिक है — यकृत पर भार पड़ सकता है।",
        "meaning_high_hin": "Iron zyada hai — liver pe load pad sakta hai.",

        "suggestion_low_en":   "Eat iron-rich foods: spinach, chickpeas, dates. Take iron supplements as advised by your doctor.",
        "suggestion_low_hi":   "आयरन युक्त आहार: पालक, चना, खजूर। डॉक्टर की सलाह से आयरन सप्लीमेंट लें।",
        "suggestion_low_hin":  "Iron-rich foods khao: palak, chana, khajoor. Doctor se iron supplement lo.",

        "suggestion_high_en":  "See a doctor — do not take extra iron supplements.",
        "suggestion_high_hi":  "डॉक्टर से मिलें — अतिरिक्त आयरन सप्लीमेंट न लें।",
        "suggestion_high_hin": "Doctor se milo — zyada iron supplements mat lo.",
    },

    "Transferrin Saturation": {
        "low": 15, "high": 50, "unit": "%", "category": "Iron Profile",

        "meaning_low_en":   "Transferrin saturation is low — iron stores are not being filled properly.",
        "meaning_low_hi":   "ट्रांसफरिन संतृप्ति कम है — आयरन भंडार ठीक से नहीं भर रहे।",
        "meaning_low_hin":  "Transferrin saturation kam — iron stores theek se fill nahi hain.",

        "meaning_high_en":  "Indication of iron overload — possible haemochromatosis.",
        "meaning_high_hi":  "आयरन अधिभार का संकेत — हेमोक्रोमैटोसिस संभव।",
        "meaning_high_hin": "Iron overload ka indication — haemochromatosis possible.",

        "suggestion_low_en":   "Ask your doctor about iron supplements.",
        "suggestion_low_hi":   "डॉक्टर से आयरन सप्लीमेंट के बारे में पूछें।",
        "suggestion_low_hin":  "Doctor se iron supplement ke baare mein poocho.",

        "suggestion_high_en":  "See a doctor — stop iron intake now.",
        "suggestion_high_hi":  "डॉक्टर से मिलें — आयरन का सेवन अभी बंद करें।",
        "suggestion_high_hin": "Doctor se milo — iron intake band karo abhi.",
    },

    # ═══════════════════════════════════════════
    # THYROID
    # ═══════════════════════════════════════════

    "T3": {
        "low": 0.7, "high": 2.0, "unit": "ng/mL", "category": "Thyroid",

        "meaning_low_en":   "T3 is low — sign of hypothyroidism. Fatigue, weight gain, feeling cold.",
        "meaning_low_hi":   "T3 कम है — हाइपोथायरॉइडिज़्म का संकेत। थकान, वजन बढ़ना, ठंड लगना।",
        "meaning_low_hin":  "T3 low — hypothyroidism ka sign. Thakaan, weight gain, thand lagti hai.",

        "meaning_high_en":  "T3 is high — hyperthyroidism. Rapid heartbeat, weight loss, anxiety.",
        "meaning_high_hi":  "T3 अधिक है — हाइपरथायरॉइडिज़्म। दिल तेज़ धड़कना, वजन घटना, चिंता।",
        "meaning_high_hin": "T3 high — hyperthyroidism. Dil tez dhakdhakana, weight loss, anxiety.",

        "suggestion_low_en":   "See an endocrinologist. Thyroid hormone deficiency needs treatment.",
        "suggestion_low_hi":   "एंडोक्रिनोलॉजिस्ट से मिलें। थायरॉइड हार्मोन की कमी का इलाज होगा।",
        "suggestion_low_hin":  "Endocrinologist se milo. Thyroid hormone deficiency treat karna hoga.",

        "suggestion_high_en":  "See an endocrinologist — thyroid is overactive.",
        "suggestion_high_hi":  "एंडोक्रिनोलॉजिस्ट से मिलें — थायरॉइड अति-सक्रिय है।",
        "suggestion_high_hin": "Endocrinologist se milo — thyroid overactive hai.",
    },

    "T4": {
        "low": 4.5, "high": 12.5, "unit": "µg/dL", "category": "Thyroid",

        "meaning_low_en":   "Thyroxine is low — hypothyroidism.",
        "meaning_low_hi":   "थायरोक्सिन कम है — हाइपोथायरॉइडिज़्म।",
        "meaning_low_hin":  "Thyroxine low — hypothyroidism.",

        "meaning_high_en":  "Thyroxine is high — hyperthyroidism.",
        "meaning_high_hi":  "थायरोक्सिन अधिक है — हाइपरथायरॉइडिज़्म।",
        "meaning_high_hin": "Thyroxine high — hyperthyroidism.",

        "suggestion_low_en":   "Ask your doctor about thyroid medication.",
        "suggestion_low_hi":   "डॉक्टर से थायरॉइड दवा के बारे में पूछें।",
        "suggestion_low_hin":  "Doctor se thyroid medication ke baare mein poocho.",

        "suggestion_high_en":  "See a doctor immediately.",
        "suggestion_high_hi":  "तुरंत डॉक्टर से मिलें।",
        "suggestion_high_hin": "Doctor se immediately milo.",
    },

    "TSH": {
        "low": 0.4, "high": 4.2, "unit": "µIU/mL", "category": "Thyroid",

        "meaning_low_en":   "TSH is very low — hyperthyroidism, thyroid is overactive.",
        "meaning_low_hi":   "TSH बहुत कम है — हाइपरथायरॉइडिज़्म, थायरॉइड अति-सक्रिय है।",
        "meaning_low_hin":  "TSH bahut kam — hyperthyroidism, thyroid overactive hai.",

        "meaning_high_en":  "TSH is high — hypothyroidism, thyroid is underactive.",
        "meaning_high_hi":  "TSH अधिक है — हाइपोथायरॉइडिज़्म, थायरॉइड कम-सक्रिय है।",
        "meaning_high_hin": "TSH zyada — hypothyroidism, thyroid underactive hai.",

        "suggestion_low_en":   "See an endocrinologist urgently.",
        "suggestion_low_hi":   "तुरंत एंडोक्रिनोलॉजिस्ट से मिलें।",
        "suggestion_low_hin":  "Endocrinologist se milo urgently.",

        "suggestion_high_en":  "See a doctor — medication like Levothyroxine may be needed.",
        "suggestion_high_hi":  "डॉक्टर से मिलें — लेवोथायरोक्सिन जैसी दवा की ज़रूरत हो सकती है।",
        "suggestion_high_hin": "Doctor se milo — Levothyroxine jaise medication ki zaroorat ho sakti hai.",
    },

    # ═══════════════════════════════════════════
    # KIDNEY (RFT)
    # ═══════════════════════════════════════════

    "Creatinine": {
        "low": 0.6, "high": 1.3, "unit": "mg/dL", "category": "Kidney",

        "meaning_low_en":   "Creatinine is low — muscular weakness or low muscle mass. Common in females.",
        "meaning_low_hi":   "क्रिएटिनिन कम है — मांसपेशियों की कमज़ोरी। महिलाओं में सामान्य।",
        "meaning_low_hin":  "Creatinine kam — muscular weakness ya low muscle mass. Females mein common.",

        "meaning_high_en":  "Creatinine is high — kidneys may not be filtering properly. Serious sign.",
        "meaning_high_hi":  "क्रिएटिनिन अधिक है — गुर्दे ठीक से फ़िल्टर नहीं कर रहे। गंभीर संकेत।",
        "meaning_high_hin": "Creatinine high — kidney properly filter nahi kar rahi. Serious sign.",

        "suggestion_low_en":   "No action alone — discuss with your doctor.",
        "suggestion_low_hi":   "अकेले कोई कार्रवाई नहीं — डॉक्टर से चर्चा करें।",
        "suggestion_low_hin":  "Akele koi action nahi — doctor se discuss karo.",

        "suggestion_high_en":  "Drink more water. Get kidney function tests done urgently.",
        "suggestion_high_hi":  "अधिक पानी पिएं। तुरंत किडनी फ़ंक्शन परीक्षण करवाएं।",
        "suggestion_high_hin": "Paani zyada piyo. Doctor se kidney function test karwao urgently.",
    },

    "Uric Acid": {
        "low": 2.6, "high": 6.0, "unit": "mg/dL", "category": "Kidney",

        "meaning_low_en":   "Uric acid is very low — rare condition.",
        "meaning_low_hi":   "यूरिक एसिड बहुत कम है — दुर्लभ स्थिति।",
        "meaning_low_hin":  "Uric acid bahut kam — rare condition.",

        "meaning_high_en":  "High uric acid — risk of gout, joint pain, kidney stones.",
        "meaning_high_hi":  "यूरिक एसिड अधिक है — गाउट, जोड़ों में दर्द, गुर्दे की पथरी का जोखिम।",
        "meaning_high_hin": "Uric acid high (hyperuricemia) — gout ka risk, joints mein dard, kidney stones.",

        "suggestion_low_en":   "See a doctor.",
        "suggestion_low_hi":   "डॉक्टर से मिलें।",
        "suggestion_low_hin":  "Doctor se milo.",

        "suggestion_high_en":  "Avoid red meat, seafood, alcohol. Drink more water. See a doctor.",
        "suggestion_high_hi":  "लाल मांस, समुद्री भोजन, शराब से बचें। अधिक पानी पिएं। डॉक्टर से मिलें।",
        "suggestion_high_hin": "Red meat, seafood, alcohol avoid karo. Zyada paani piyo. Doctor se milo.",
    },

    "Sodium": {
        "low": 136, "high": 145, "unit": "mmol/L", "category": "Kidney",

        "meaning_low_en":   "Hyponatremia — too much water or kidney issue. Weakness, confusion.",
        "meaning_low_hi":   "हाइपोनेट्रेमिया — अधिक पानी या गुर्दे की समस्या। कमज़ोरी, भ्रम।",
        "meaning_low_hin":  "Hyponatremia — zyada paani peena ya kidney issue. Weakness, confusion.",

        "meaning_high_en":  "Hypernatremia — dehydration or kidney issue.",
        "meaning_high_hi":  "हाइपरनेट्रेमिया — निर्जलीकरण या गुर्दे की समस्या।",
        "meaning_high_hin": "Hypernatremia — dehydration ya kidney issue.",

        "suggestion_low_en":   "See a doctor — electrolyte balance needs correction.",
        "suggestion_low_hi":   "डॉक्टर से मिलें — इलेक्ट्रोलाइट संतुलन ठीक करना होगा।",
        "suggestion_low_hin":  "Doctor se milo — electrolyte balance theek karna padega.",

        "suggestion_high_en":  "Drink more water. See a doctor.",
        "suggestion_high_hi":  "अधिक पानी पिएं। डॉक्टर से मिलें।",
        "suggestion_high_hin": "Zyada paani piyo. Doctor se milo.",
    },

    "Potassium": {
        "low": 3.5, "high": 5.1, "unit": "mmol/L", "category": "Kidney",

        "meaning_low_en":   "Hypokalemia — muscle cramps, heart rhythm problems.",
        "meaning_low_hi":   "हाइपोकेलेमिया — मांसपेशियों में ऐंठन, दिल की धड़कन में समस्या।",
        "meaning_low_hin":  "Hypokalemia — muscle cramps, dil ki dharkan mein problem. Bananas, potatoes khao.",

        "meaning_high_en":  "Hyperkalemia — dangerous for the heart.",
        "meaning_high_hi":  "हाइपरकेलेमिया — हृदय के लिए खतरनाक।",
        "meaning_high_hin": "Hyperkalemia — dil ke liye dangerous. Kidney zyada potassium retain kar rahi.",

        "suggestion_low_en":   "Eat banana, potato, yoghurt. See a doctor.",
        "suggestion_low_hi":   "केला, आलू, दही खाएं। डॉक्टर से मिलें।",
        "suggestion_low_hin":  "Banana, aalu, dahi khao. Doctor se milo.",

        "suggestion_high_en":  "See a doctor urgently — this is risky for the heart.",
        "suggestion_high_hi":  "तुरंत डॉक्टर से मिलें — यह हृदय के लिए जोखिम भरा है।",
        "suggestion_high_hin": "Doctor se urgently milo — ye dil ke liye risky hai.",
    },

    # ═══════════════════════════════════════════
    # LIVER (LFT)
    # ═══════════════════════════════════════════

    "Bilirubin Total": {
        "low": 0.1, "high": 0.9, "unit": "mg/dL", "category": "Liver",

        "meaning_low_en":   "Practically impossible — ignore.",
        "meaning_low_hi":   "व्यावहारिक रूप से असंभव — नज़रअंदाज़ करें।",
        "meaning_low_hin":  "Practically impossible — ignore if below 0.1.",

        "meaning_high_en":  "Bilirubin is high — sign of jaundice. Liver or RBC breakdown problem.",
        "meaning_high_hi":  "बिलीरुबिन अधिक है — पीलिया का संकेत। यकृत या RBC टूटने में समस्या।",
        "meaning_high_hin": "Bilirubin high — jaundice ka sign. Liver ya RBC breakdown mein problem.",

        "suggestion_low_en":   "No action needed.",
        "suggestion_low_hi":   "कोई कार्रवाई आवश्यक नहीं।",
        "suggestion_low_hin":  "No action needed.",

        "suggestion_high_en":  "Stop alcohol completely. Get a liver ultrasound.",
        "suggestion_high_hi":  "शराब बिल्कुल बंद करें। लिवर अल्ट्रासाउंड करवाएं।",
        "suggestion_high_hin": "Alcohol bilkul band karo. Doctor se liver ultrasound karwao.",
    },

    "Bilirubin Indirect": {
        "low": 0.1, "high": 0.6, "unit": "mg/dL", "category": "Liver",

        "meaning_low_en":   "No concern.",
        "meaning_low_hi":   "कोई चिंता नहीं।",
        "meaning_low_hin":  "No concern.",

        "meaning_high_en":  "Indirect bilirubin is high — RBCs breaking down or Gilbert's syndrome.",
        "meaning_high_hi":  "अप्रत्यक्ष बिलीरुबिन अधिक है — RBC टूट रही हैं या गिल्बर्ट सिंड्रोम।",
        "meaning_high_hin": "Indirect bilirubin high — RBC toot rahi hain (haemolysis) ya Gilbert's syndrome.",

        "suggestion_low_en":   "No action needed.",
        "suggestion_low_hi":   "कोई कार्रवाई आवश्यक नहीं।",
        "suggestion_low_hin":  "No action needed.",

        "suggestion_high_en":  "Get a blood test — rule out RBC problem.",
        "suggestion_high_hi":  "रक्त परीक्षण करवाएं — RBC समस्या से इंकार करें।",
        "suggestion_high_hin": "Doctor se blood test karwao — RBC problem rule out karo.",
    },

    "SGOT": {
        "low": 0, "high": 31, "unit": "IU/L", "category": "Liver",

        "meaning_low_en":   "No concern.",
        "meaning_low_hi":   "कोई चिंता नहीं।",
        "meaning_low_hin":  "No concern.",

        "meaning_high_en":  "Liver enzyme is high — liver damage, fatty liver or heart problem.",
        "meaning_high_hi":  "यकृत एंज़ाइम अधिक है — यकृत क्षति, फैटी लिवर या हृदय समस्या।",
        "meaning_high_hin": "Liver enzyme high — liver damage, fatty liver, ya heart problem.",

        "suggestion_low_en":   "Normal.",
        "suggestion_low_hi":   "सामान्य।",
        "suggestion_low_hin":  "Normal.",

        "suggestion_high_en":  "Avoid alcohol and paracetamol overuse. Get liver tests done.",
        "suggestion_high_hi":  "शराब और पेरासिटामोल से बचें। यकृत परीक्षण करवाएं।",
        "suggestion_high_hin": "Alcohol/paracetamol avoid karo. Doctor se liver test karwao.",
    },

    "SGPT": {
        "low": 0, "high": 34, "unit": "IU/L", "category": "Liver",

        "meaning_low_en":   "No concern.",
        "meaning_low_hi":   "कोई चिंता नहीं।",
        "meaning_low_hin":  "No concern.",

        "meaning_high_en":  "SGPT is high — clear sign of liver inflammation. Fatty liver is likely.",
        "meaning_high_hi":  "SGPT अधिक है — यकृत सूजन का स्पष्ट संकेत। फैटी लिवर संभव।",
        "meaning_high_hin": "SGPT high — liver inflammation ka clear sign. Fatty liver likely.",

        "suggestion_low_en":   "Normal.",
        "suggestion_low_hi":   "सामान्य।",
        "suggestion_low_hin":  "Normal.",

        "suggestion_high_en":  "Avoid fatty foods. Lose weight. See a doctor.",
        "suggestion_high_hi":  "वसायुक्त भोजन से बचें। वजन कम करें। डॉक्टर से मिलें।",
        "suggestion_high_hin": "Fatty foods avoid karo. Weight kam karo. Doctor se milo.",
    },

    # ═══════════════════════════════════════════
    # LIPID PROFILE
    # ═══════════════════════════════════════════

    "Triglycerides": {
        "high": 150, "unit": "mg/dL", "category": "Lipid",

        "meaning_high_en":  "Triglycerides are high — increased risk of heart disease and pancreatitis.",
        "meaning_high_hi":  "ट्राइग्लिसराइड्स अधिक हैं — हृदय रोग और अग्नाशयशोथ का जोखिम बढ़ गया।",
        "meaning_high_hin": "Triglycerides high — heart disease aur pancreatitis ka risk badh gaya.",

        "suggestion_high_en":  "Avoid sweets, refined flour and alcohol. Walk daily. Consider fish oil (ask your doctor).",
        "suggestion_high_hi":  "मिठाई, मैदा, शराब से बचें। रोज़ चलें। फ़िश ऑयल पर विचार करें (डॉक्टर से पूछें)।",
        "suggestion_high_hin": "Meetha, maida, alcohol avoid karo. Roz walk karo. Fish oil lo (doctor se poocho).",
    },

    "Cholesterol": {
        "high": 200, "unit": "mg/dL", "category": "Lipid",

        "meaning_high_en":  "Total cholesterol is high — risk of heart disease.",
        "meaning_high_hi":  "कुल कोलेस्ट्रॉल अधिक है — हृदय रोग का जोखिम।",
        "meaning_high_hin": "Total cholesterol high — dil ki bimari ka risk.",

        "suggestion_high_en":  "Reduce saturated fat. Exercise. Ask your doctor about statins.",
        "suggestion_high_hi":  "संतृप्त वसा कम करें। व्यायाम करें। डॉक्टर से स्टैटिन पूछें।",
        "suggestion_high_hin": "Saturated fat kam karo. Exercise karo. Doctor se statin ke baare mein poocho.",
    },

    "HDL": {
        "low": 55, "unit": "mg/dL", "category": "Lipid",

        "meaning_low_en":   "HDL (good cholesterol) is low — higher risk of heart disease. Women should have >55.",
        "meaning_low_hi":   "HDL (अच्छा कोलेस्ट्रॉल) कम है — हृदय रोग का जोखिम। महिलाओं में >55 होना चाहिए।",
        "meaning_low_hin":  "HDL (good cholesterol) kam hai — dil ki bimari ka risk zyada hai. Women mein >55 hona chahiye.",

        "suggestion_low_en":   "Exercise more. Eat olive oil, nuts, avocado. Stop smoking.",
        "suggestion_low_hi":   "अधिक व्यायाम करें। जैतून का तेल, मेवे, एवोकाडो खाएं। धूम्रपान बंद करें।",
        "suggestion_low_hin":  "Exercise badao, olive oil, nuts, avocado khao. Smoking band karo.",
    },

    "LDL": {
        "high": 100, "unit": "mg/dL", "category": "Lipid",

        "meaning_high_en":  "LDL (bad cholesterol) above optimal — risk of artery blockage.",
        "meaning_high_hi":  "LDL (खराब कोलेस्ट्रॉल) इष्टतम से अधिक — धमनी अवरोध का जोखिम।",
        "meaning_high_hin": "LDL (bad cholesterol) optimal se zyada hai — arteries block hone ka risk.",

        "suggestion_high_en":  "Reduce saturated fats. Eat more oats and fibre.",
        "suggestion_high_hi":  "संतृप्त वसा कम करें। जई और फाइबर अधिक खाएं।",
        "suggestion_high_hin": "Saturated fat (ghee, butter, red meat) kam karo. Oats, fiber zyada khao.",
    },

    "VLDL": {
        "high": 30, "unit": "mg/dL", "category": "Lipid",

        "meaning_high_en":  "VLDL is high — carries triglycerides. Heart risk indicator.",
        "meaning_high_hi":  "VLDL अधिक है — ट्राइग्लिसराइड्स ले जाता है। हृदय जोखिम संकेतक।",
        "meaning_high_hin": "VLDL high — ye type triglycerides carry karta hai. Heart risk indicator.",

        "suggestion_high_en":  "Reduce triglycerides — stop sweets and refined carbs completely.",
        "suggestion_high_hi":  "ट्राइग्लिसराइड्स कम करें — मिठाई और रिफाइंड कार्ब्स पूरी तरह बंद करें।",
        "suggestion_high_hin": "Triglycerides kam karo — meetha aur refined carbs bilkul band.",
    },

    # ═══════════════════════════════════════════
    # CBC
    # ═══════════════════════════════════════════

    "Hemoglobin": {
        "low": 12.0, "high": 15.0, "unit": "g/dL", "category": "CBC",

        "meaning_low_en":   "Anaemia — low RBCs or haemoglobin. Fatigue, dizziness, shortness of breath.",
        "meaning_low_hi":   "एनीमिया — RBC या हीमोग्लोबिन कम है। थकान, चक्कर, सांस फूलना।",
        "meaning_low_hin":  "Anaemia hai — RBC ya haemoglobin kam hai. Thakaan, chakkar, saans phoolna.",

        "meaning_high_en":  "Haemoglobin is high — dehydration or bone marrow issue.",
        "meaning_high_hi":  "हीमोग्लोबिन अधिक है — निर्जलीकरण या अस्थि मज्जा की समस्या।",
        "meaning_high_hin": "Haemoglobin zyada — dehydration ya bone marrow issue.",

        "suggestion_low_en":   "Iron-rich diet: spinach, chickpeas, meat. Take Vitamin C too. Get iron supplements from your doctor.",
        "suggestion_low_hi":   "आयरन युक्त आहार: पालक, चना, मांस। विटामिन C भी लें। डॉक्टर से आयरन सप्लीमेंट लें।",
        "suggestion_low_hin":  "Iron-rich diet: palak, chana, meat. Vitamin C bhi lo. Doctor se iron supplement lo.",

        "suggestion_high_en":  "Drink more water. See a doctor.",
        "suggestion_high_hi":  "अधिक पानी पिएं। डॉक्टर से मिलें।",
        "suggestion_high_hin": "Zyada paani piyo. Doctor se milo.",
    },

    "MCH": {
        "low": 27, "high": 32, "unit": "pg", "category": "CBC",

        "meaning_low_en":   "MCH is low — less haemoglobin in RBCs. Sign of iron deficiency anaemia.",
        "meaning_low_hi":   "MCH कम है — RBC में हीमोग्लोबिन कम। आयरन की कमी से एनीमिया।",
        "meaning_low_hin":  "MCH low — RBC mein haemoglobin kam hai. Iron deficiency anaemia ka sign.",

        "meaning_high_en":  "MCH is high — Vitamin B12 or folate deficiency.",
        "meaning_high_hi":  "MCH अधिक है — विटामिन B12 या फोलेट की कमी।",
        "meaning_high_hin": "MCH high — vitamin B12 ya folate ki kami.",

        "suggestion_low_en":   "Take more iron and Vitamin C. See a doctor.",
        "suggestion_low_hi":   "आयरन और विटामिन C अधिक लें। डॉक्टर से मिलें।",
        "suggestion_low_hin":  "Iron aur vitamin C zyada lo. Doctor se milo.",

        "suggestion_high_en":  "Take B12 and folate supplements. See a doctor.",
        "suggestion_high_hi":  "B12 और फोलेट सप्लीमेंट लें। डॉक्टर से मिलें।",
        "suggestion_high_hin": "B12 aur folate supplement lo. Doctor se milo.",
    },

    "MCHC": {
        "low": 31, "high": 36, "unit": "%", "category": "CBC",

        "meaning_low_en":   "MCHC is low — confirms iron deficiency anaemia.",
        "meaning_low_hi":   "MCHC कम है — आयरन की कमी से एनीमिया की पुष्टि।",
        "meaning_low_hin":  "MCHC low — iron deficiency anaemia confirm karta hai.",

        "meaning_high_en":  "MCHC is high — sign of haemolysis.",
        "meaning_high_hi":  "MCHC अधिक है — हीमोलिसिस का संकेत।",
        "meaning_high_hin": "MCHC high — haemolysis ka sign.",

        "suggestion_low_en":   "Start iron supplements (with doctor). Eat spinach and meat.",
        "suggestion_low_hi":   "आयरन सप्लीमेंट शुरू करें (डॉक्टर के साथ)। पालक, मांस खाएं।",
        "suggestion_low_hin":  "Iron supplement shuru karo (doctor ke saath). Palak, meat khao.",

        "suggestion_high_en":  "Get a blood film test from your doctor.",
        "suggestion_high_hi":  "डॉक्टर से ब्लड फ़िल्म टेस्ट करवाएं।",
        "suggestion_high_hin": "Doctor se blood film test karwao.",
    },

    "RDW": {
        "low": 11.5, "high": 14.5, "unit": "%", "category": "CBC",

        "meaning_low_en":   "RDW is low — unusual, usually no concern.",
        "meaning_low_hi":   "RDW कम है — असामान्य, आमतौर पर कोई चिंता नहीं।",
        "meaning_low_hin":  "RDW kam — unusual, usually no concern.",

        "meaning_high_en":  "RDW is high — RBC sizes are unequal. Sign of mixed anaemia — both iron and B12 deficiency may be present.",
        "meaning_high_hi":  "RDW अधिक है — RBC का आकार असमान है। मिश्रित एनीमिया — आयरन और B12 दोनों की कमी हो सकती है।",
        "meaning_high_hin": "RDW high — RBC ka size unequal hai (anisocytosis). Mixed anaemia ka sign — iron + B12 ki kami dono ho sakti hain.",

        "suggestion_low_en":   "No action.",
        "suggestion_low_hi":   "कोई कार्रवाई नहीं।",
        "suggestion_low_hin":  "No action.",

        "suggestion_high_en":  "Get iron, B12 and folate tests done. Complete evaluation is essential.",
        "suggestion_high_hi":  "आयरन, B12 और फोलेट परीक्षण करवाएं। पूर्ण मूल्यांकन ज़रूरी।",
        "suggestion_high_hin": "Doctor se iron, B12, folate test karwao. Complete evaluation zaroor karo.",
    },

    "Platelets": {
        "low": 1.5, "high": 4.5, "unit": "lakhs/cumm", "category": "CBC",

        "meaning_low_en":   "Platelet count is low (thrombocytopenia) — increased risk of bleeding.",
        "meaning_low_hi":   "प्लेटलेट काउंट कम है — रक्तस्राव का जोखिम बढ़ गया।",
        "meaning_low_hin":  "Platelets kam (thrombocytopenia) — bleeding ka risk badh gaya.",

        "meaning_high_en":  "Platelet count is high — risk of clotting.",
        "meaning_high_hi":  "प्लेटलेट काउंट अधिक है — थक्के बनने का जोखिम।",
        "meaning_high_hin": "Platelets zyada — clotting ka risk.",

        "suggestion_low_en":   "See a doctor urgently. Avoid injury.",
        "suggestion_low_hi":   "तुरंत डॉक्टर से मिलें। चोट से बचें।",
        "suggestion_low_hin":  "Doctor se urgently milo. Injury se bachao.",

        "suggestion_high_en":  "See a doctor.",
        "suggestion_high_hi":  "डॉक्टर से मिलें।",
        "suggestion_high_hin": "Doctor se milo.",
    },

    # ═══════════════════════════════════════════
    # HAEMATOLOGY
    # ═══════════════════════════════════════════

    "ESR": {
        "low": 0, "high": 20, "unit": "mm/hr", "category": "Inflammation",

        "meaning_low_en":   "No concern.",
        "meaning_low_hi":   "कोई चिंता नहीं।",
        "meaning_low_hin":  "No concern.",

        "meaning_high_en":  "ESR is high — inflammation somewhere in the body. Possible infection, arthritis or autoimmune disease.",
        "meaning_high_hi":  "ESR अधिक है — शरीर में कहीं सूजन है। संक्रमण, गठिया, स्व-प्रतिरक्षा रोग संभव।",
        "meaning_high_hin": "ESR high — inflammation hai body mein kahin. Infection, arthritis, autoimmune disease possible.",

        "suggestion_low_en":   "Normal.",
        "suggestion_low_hi":   "सामान्य।",
        "suggestion_low_hin":  "Normal.",

        "suggestion_high_en":  "Get a detailed check from your doctor — find the cause. Also get a CRP test.",
        "suggestion_high_hi":  "डॉक्टर से विस्तृत जाँच करवाएं। CRP परीक्षण भी करवाएं।",
        "suggestion_high_hin": "Doctor se detailed check karo — cause dhundna zaroor hai. CRP test bhi karwao.",
    },

    # ═══════════════════════════════════════════
    # VITAMINS
    # ═══════════════════════════════════════════

    "Vitamin B12": {
        "low": 200, "high": 835, "unit": "pg/mL", "category": "Vitamins",

        "meaning_low_en":   "B12 deficient — nerve damage, anaemia, memory problems, tingling in hands and feet.",
        "meaning_low_hi":   "B12 की कमी — तंत्रिका क्षति, एनीमिया, स्मृति समस्याएं, हाथ-पैर में झनझनाहट।",
        "meaning_low_hin":  "B12 deficient — nerve damage, anaemia, memory problems, hands-feet mein jhanjhanahat.",

        "meaning_high_en":  "B12 is very high — usually harmless but rule out liver or blood disorder.",
        "meaning_high_hi":  "B12 बहुत अधिक है — आमतौर पर हानिरहित लेकिन यकृत/रक्त विकार से इंकार करें।",
        "meaning_high_hin": "B12 bahut zyada — usually harmless but liver ya blood disorder rule out karo.",

        "suggestion_low_en":   "Take B12 supplement (methylcobalamin is best). Eat more dairy, eggs and meat. Ask your doctor about injections.",
        "suggestion_low_hi":   "B12 सप्लीमेंट लें (मिथाइलकोबालामिन)। डेयरी, अंडे, मांस खाएं। इंजेक्शन के लिए डॉक्टर से पूछें।",
        "suggestion_low_hin":  "B12 supplement lo (methylcobalamin best hai). Dairy, eggs, meat zyada khao. Doctor se injection bhi bol sakte ho.",

        "suggestion_high_en":  "Check with your doctor.",
        "suggestion_high_hi":  "डॉक्टर से जाँच करवाएं।",
        "suggestion_high_hin": "Doctor se check karo.",
    },

    "Vitamin D": {
        "low": 30, "high": 70, "unit": "ng/mL", "category": "Vitamins",

        "meaning_low_en":   "Vitamin D is deficient — weak bones, low immunity, depression, fatigue. Very common in India.",
        "meaning_low_hi":   "विटामिन D की कमी — हड्डियां कमज़ोर, रोग प्रतिरोधक क्षमता कम, अवसाद, थकान। भारत में बहुत सामान्य।",
        "meaning_low_hin":  "Vitamin D deficient/insufficient — bones kamzor, immunity low, depression, thakaan. India mein bahut common.",

        "meaning_high_en":  "Vitamin D toxicity — may cause nausea and kidney stones.",
        "meaning_high_hi":  "विटामिन D विषाक्तता — मतली और गुर्दे की पथरी हो सकती है।",
        "meaning_high_hin": "Vitamin D toxicity — nausea, kidney stones ho sakte hain.",

        "suggestion_low_en":   "Sit in morning sunlight 15-20 minutes daily. Take Vitamin D3 (1000-2000 IU). Ask your doctor about the dose.",
        "suggestion_low_hi":   "रोज़ सुबह 15-20 मिनट धूप में बैठें। विटामिन D3 (1000-2000 IU) लें। डॉक्टर से खुराक तय करवाएं।",
        "suggestion_low_hin":  "Roz 15-20 min dhoop mein baitho (subah). Vitamin D3 supplement lo (1000-2000 IU). Doctor se dose decide karo.",

        "suggestion_high_en":  "Stop Vitamin D supplement. See a doctor.",
        "suggestion_high_hi":  "विटामिन D सप्लीमेंट बंद करें। डॉक्टर से मिलें।",
        "suggestion_high_hin": "Vitamin D supplement band karo. Doctor se milo.",
    },
}


# ─────────────────────────────────────────────
# CATEGORY ORDER
# ─────────────────────────────────────────────
CATEGORY_ORDER = [
    "Diabetes", "Thyroid", "CBC", "Iron Profile",
    "Lipid", "Liver", "Kidney", "Inflammation", "Vitamins",
]


# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────

def get_category(param_name: str) -> str:
    return rules.get(param_name, {}).get("category", "Other")


def get_rule_text(param_name: str, key: str, lang: str = "hin") -> str:
    lang = lang if lang in ("en", "hi", "hin") else "hin"
    rule = rules.get(param_name, {})

    val = rule.get(f"{key}_{lang}")
    if val:
        return val
    val = rule.get(f"{key}_hin")
    if val:
        return val
    return rule.get(key, "")
