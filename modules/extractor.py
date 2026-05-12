
import re


# ─────────────────────────────────────────────────────────────
# PARAM DEFINITIONS
# ─────────────────────────────────────────────────────────────


PARAM_DEFS = {

    # ── GLUCOSE / DIABETES ──────────────────────────────────

    "Glucose Fasting": {
        "patterns": [
            r"Plasma\s+Glucose\s+Fasting\s+([\d.]+)",
            r"Glucose\s+Fasting\s+([\d.]+)",
            r"Fasting\s+Glucose\s+([\d.]+)",
            r"FBS\s+([\d.]+)",
        ],
        "plausible": (20, 500),
    },

    "Glucose PP": {
        "patterns": [
            r"Plasma\s+Glucose\s+Post\s+Prandial\s+([\d.]+)",
            r"Post\s+Prandial\s+Glucose\s+([\d.]+)",
            r"PP\s+Glucose\s+([\d.]+)",
            r"PPBS\s+([\d.]+)",
        ],
        "plausible": (20, 600),
    },

    "HbA1c": {

        "patterns": [
            r"HbA1c\s*\(Glycosylated\s+Haemoglobin\)\s+([\d.]+)",
            r"HbA1c\s*\(Glycosylated\s+Hemoglobin\)\s+([\d.]+)",
            r"Glycosylated\s+Haemoglobin\)\s+([\d.]+)",
            r"HbA1c\s+([\d]+\.\d+)\s",
            r"HbA1c\s+([\d.]+)\s+(?:Normal|Prediabetes|mg)",
        ],
        "plausible": (3.0, 15.0),
    },

    # ── IRON PROFILE ────────────────────────────────────────

    "Iron": {
        "patterns": [
            r"Total\s+Iron\s+([\d.]+)",
            r"Serum\s+Iron\s+([\d.]+)",
        ],
        "plausible": (5, 400),
    },

    "Transferrin Saturation": {
        "patterns": [
            r"TRANSFERRIN\s+SATURATION\s+([\d.]+)",
            r"Transferrin\s+Saturation\s+([\d.]+)",
            r"T\.?SAT\.?\s+([\d.]+)",
        ],
        "plausible": (1, 100),
    },

    # ── THYROID ─────────────────────────────────────────────

    "T3": {
        "patterns": [
            r"Triiodothyronine\s*[-–]?\s*T3\s+([\d.]+)",
            r"T3\s+Triiodothyronine\s+([\d.]+)",
            r"\bT3\b\s+([\d.]+)",
        ],
        "plausible": (0.1, 10.0),
    },

    "T4": {
        "patterns": [
            r"Thyroxine\s*[-–]?\s*T4\s+([\d.]+)",
            r"T4\s+Thyroxine\s+([\d.]+)",
            r"\bT4\b\s+([\d.]+)",
        ],
        "plausible": (0.5, 30.0),
    },

    "TSH": {
        "patterns": [
            r"Thyroid\s+Stimulating\s+Hormone\s*[-–]?\s*TSH\s+([\d.]+)",
            r"TSH\s+Thyroid\s+Stimulating\s+([\d.]+)",
            r"\bTSH\b\s+([\d.]+)",
        ],
        "plausible": (0.001, 100.0),
    },

    # ── KIDNEY (RFT) ─────────────────────────────────────────

    "Creatinine": {

        "patterns": [
            r"Creatinine\s+([\d.]+)\s+(?:0\.|mg)",
            r"Creatinine\s+([\d.]+)",
            r"S\.\s*Creatinine\s+([\d.]+)",
            r"Serum\s+Creatinine\s+([\d.]+)",
        ],
        "plausible": (0.1, 20.0),
    },

    "Uric Acid": {
        "patterns": [
            r"Uric\s+Acid\s+([\d.]+)",
            r"Serum\s+Uric\s+Acid\s+([\d.]+)",
            r"S\.?\s*Uric\s+Acid\s+([\d.]+)",
        ],
        "plausible": (0.5, 20.0),
    },

    "Sodium": {
        "patterns": [
            r"Sodium\s+(1[0-9]{2})\b",
            r"\bNa\b\s+(1[0-9]{2})\b",
        ],
        "plausible": (100, 180),
    },

    "Potassium": {
        "patterns": [
            r"Potassium\s+([\d.]+)",
            r"\bK\b\s+([\d.]+)",
        ],
        "plausible": (1.0, 10.0),
    },

    # ── LIVER (LFT) ──────────────────────────────────────────

    "Bilirubin Total": {
        "patterns": [
            r"TOTAL\s+BILIRUBIN\s+([\d.]+)",
            r"Total\s+Bilirubin\s+([\d.]+)",
            r"T\.?\s*Bilirubin\s+([\d.]+)",
        ],
        "plausible": (0.0, 30.0),
    },

    "Bilirubin Indirect": {
        "patterns": [
            r"Indirect\s+Bilirubin\s+([\d.]+)",
            r"INDIRECT\s+BILIRUBIN\s+([\d.]+)",
            r"Unconjugated\s+Bilirubin\s+([\d.]+)",
        ],
        "plausible": (0.0, 25.0),
    },

    "SGOT": {
        "patterns": [
            r"SGOT\s*/\s*AST\s+([\d.]+)",
            r"SGOT\s+([\d.]+)",
            r"AST\s*\(SGOT\)\s+([\d.]+)",
            r"\bAST\b\s+([\d.]+)",
        ],
        "plausible": (5, 2000),
    },

    "SGPT": {
        "patterns": [
            r"SGPT\s*/\s*ALT\s+([\d.]+)",
            r"SGPT\s+([\d.]+)",
            r"ALT\s*\(SGPT\)\s+([\d.]+)",
            r"\bALT\b\s+([\d.]+)",
        ],
        "plausible": (5, 2000),
    },

    # ── LIPID PROFILE ────────────────────────────────────────

    "Triglycerides": {
        "patterns": [
            r"Triglycerides\s+([\d.]+)",
            r"Serum\s+Triglycerides\s+([\d.]+)",
            r"TG\s+([\d.]+)",
        ],
        "plausible": (20, 3000),
    },

    "Cholesterol": {
        "patterns": [
            r"Total\s+Cholesterol\s+([\d.]+)",
            r"Serum\s+Total\s+Cholesterol\s+([\d.]+)",
            r"T\.?\s*Cholesterol\s+([\d.]+)",
        ],
        "plausible": (50, 700),
    },

    "HDL": {
        "patterns": [
            r"HDL\s+Cholesterol\s+([\d.]+)",
            r"HDL[-\s]C\s+([\d.]+)",
            r"\bHDL\b\s+([\d.]+)",
        ],
        "plausible": (5, 150),
    },

    "LDL": {
        "patterns": [
            r"LDL\s+Cholesterol\s+([\d.]+)",
            r"LDL[-\s]C\s+([\d.]+)",
            r"\bLDL\b\s+([\d.]+)",
        ],
        "plausible": (20, 500),
    },

    "VLDL": {
        "patterns": [
            r"VLDL\s+Cholesterol\s+([\d.]+)",
            r"VLDL[-\s]C\s+([\d.]+)",
            r"\bVLDL\b\s+([\d.]+)",
        ],
        "plausible": (2, 200),
    },

    # ── CBC (Complete Blood Count) ────────────────────────────

    "Hemoglobin": {
        "patterns": [
            r"Hemoglobin\s+([\d.]+)",
            r"Haemoglobin\s+([\d.]+)",
            r"\bHb\b\s+([\d.]+)",
            r"\bHGB\b\s+([\d.]+)",
        ],
        "plausible": (3.0, 25.0),
    },

    "Platelets": {
        "patterns": [
            r"Platelet\s+Count\s+([\d.]+)",
            r"Platelet\s+([\d.]+)",
            r"\bPLT\b\s+([\d.]+)",
        ],
        "plausible": (0.5, 15.0),   # lakhs/cumm
    },

    "MCH": {
        "patterns": [
            r"Mean\s+Corpuscular\s+Haemoglobin\s*\(MCH\)\s+([\d.]+)",
            r"Mean\s+Corpuscular\s+Hemoglobin\s*\(MCH\)\s+([\d.]+)",
            r"\bMCH\b\s+([\d.]+)",
        ],
        "plausible": (15.0, 45.0),
    },

    "MCHC": {
        "patterns": [
            r"Mean\s+Corpuscular\s+Haemoglobin\s+Conc\b[^)]*\)\s+([\d.]+)",
            r"Mean\s+Corpuscular\s+Haemoglobin\s+Concentration\s+([\d.]+)",
            r"\bMCHC\b\s+([\d.]+)",
        ],
        "plausible": (20.0, 40.0),
    },

    "RDW": {
        "patterns": [
            r"Red\s+Cell\s+Distribution\s+Width\s+([\d.]+)",
            r"RDW[-\s]CV\s+([\d.]+)",
            r"\bRDW\b\s+([\d.]+)",
        ],
        "plausible": (8.0, 30.0),
    },

    # ── HAEMATOLOGY ──────────────────────────────────────────

    "ESR": {
        "patterns": [
            r"Erythrocyte\s+Sedimentation\s+Rate\s*[-–]?\s*ESR\s+([\d.]+)",
            r"ESR\s+Erythrocyte\s+([\d.]+)",
            r"\bESR\b\s+([\d.]+)",
        ],
        "plausible": (0, 200),
    },

    # ── VITAMINS ─────────────────────────────────────────────

    "Vitamin B12": {
        "patterns": [
            r"Vitamin\s+B[-\s]?12\s+([\d.]+)",
            r"Vit\.?\s*B[-\s]?12\s+([\d.]+)",
            r"Cyanocobalamin\s+([\d.]+)",
        ],
        "plausible": (50, 5000),
    },

    "Vitamin D": {
        "patterns": [
            r"Vitamin\s+D3?\s*/?\s*25\s*\(OH\)\s*Vitamin\s+D3?\s+([\d.]+)",
            r"25\s*\(OH\)\s*Vitamin\s+D\s+([\d.]+)",
            r"Vitamin\s+D3?\s+([\d.]+)",
            r"25\s*OH\s+Vitamin\s+D\s+([\d.]+)",
        ],
        "plausible": (3.0, 150.0),
    },
}


# ─────────────────────────────────────────────────────────────
# CORE EXTRACTION FUNCTION
# ─────────────────────────────────────────────────────────────

def extract_values(text, debug=False):
    """
    OCR text se medical values extract karo.

    Args:
        text  : str — OCR output (raw text from PDF/image)
        debug : bool — True karo to har param ka log dekho

    Returns:
        data : dict  — {param_name: float_value}
        log  : list  — debug info (har param ke liye kya hua)
    """

    data = {}
    log  = []

    for param, defn in PARAM_DEFS.items():
        patterns   = defn["patterns"]
        p_min, p_max = defn["plausible"]

        found       = False
        tried       = []

        for i, pattern in enumerate(patterns):
            match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)

            if match:
                raw_val = match.group(1)
                tried.append(f"P{i+1}✓")

                try:
                    value = float(raw_val)
                except ValueError:
                    tried[-1] += "(parse_err)"
                    continue

                if not (p_min <= value <= p_max):
                    tried[-1] += f"(out_of_plausible:{value})"
                    continue

                data[param] = value
                found = True

                if debug:
                    log.append({
                        "param"     : param,
                        "value"     : value,
                        "pattern_no": i + 1,
                        "pattern"   : pattern,
                        "status"    : "FOUND",
                        "tried"     : tried,
                    })
                break

            else:
                tried.append(f"P{i+1}✗")

        if not found and debug:
            log.append({
                "param"  : param,
                "value"  : None,
                "status" : "NOT_FOUND",
                "tried"  : tried,
            })

    return data, log


# ─────────────────────────────────────────────────────────────
# PRINT DEBUG LOG — readable format
# ─────────────────────────────────────────────────────────────

def print_debug_log(log):
    """Debug log ko readable format mein print karo."""
    found_count    = sum(1 for l in log if l["status"] == "FOUND")
    notfound_count = sum(1 for l in log if l["status"] == "NOT_FOUND")

    print(f"\n{'='*65}")
    print(f" EXTRACTOR DEBUG LOG")
    print(f" Found: {found_count}  |  Not Found: {notfound_count}  |  Total: {len(log)}")
    print(f"{'='*65}")

    for entry in log:
        status_icon = "✓" if entry["status"] == "FOUND" else "✗"
        val_str = f"  →  {entry['value']}" if entry["value"] else ""
        tried   = " ".join(entry["tried"])
        print(f" {status_icon}  {entry['param']:<30}  {val_str:<12}  [{tried}]")

    print(f"{'='*65}\n")


# ─────────────────────────────────────────────────────────────
# QUICK TEST (python extractor.py)
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sample_text = """
    BIOCHEMISTRY
    Plasma Glucose Fasting 103 70 - 110 mg/dL Hexokinase
    HbA1c (Glycosylated Haemoglobin) 5.72
    Normal : Below 5.7%
    Prediabetes : 5.7% to 6.4%
    Plasma Glucose Post Prandial 80 80 - 140 mg/dL Hexokinase
    Total Iron 67.8 33 - 193 mcg/dL
    TRANSFERRIN SATURATION 17 15 - 50 %
    Triiodothyronine - T3 1.27 0.7 -2.0 ng/mL
    Thyroxine - T4 8.71 4.5 - 12.5
    Thyroid Stimulating Hormone - TSH 3.40 0.4 - 4.2
    Creatinine 0.45 0.6-1.3 mg/dL
    Uric Acid 3.6 2.6 - 6.0 mg/dL
    Sodium 138
    Potassium 4.77
    TOTAL BILIRUBIN 1.26 0.1-0.9 mg/dL
    Indirect Bilirubin 0.91 0.1-0.6 mg/dL
    SGOT / AST 23 0 - 31 IU/L
    SGPT / ALT 22 0 - 34 IU/L
    Triglycerides 179.6 < 150 : Normal mg/dL
    Total Cholesterol 188.3 Desirable : < 200
    HDL Cholesterol 38.4 No risk: > 55
    LDL Cholesterol 113.98 Optimal: Less than 100
    VLDL Cholesterol 35.92 5.0 - 30 mg/dL
    Hemoglobin 11.4 12.0 - 15.0
    Mean Corpuscular Haemoglobin(MCH) 25.1 27 - 32 pg
    Mean Corpuscular Haemoglobin Conc (MCHC) 30.3 31 - 36 %
    Platelet Count 2.65 1.5 - 4.5 lakhs/cumm
    Red Cell Distribution Width 16.4 11.5 - 14.5 %
    Erythrocyte Sedimentation Rate - ESR 30 0 - 15 mm/hr
    Vitamin B-12 215 200 - 835 pg/mL
    Vitamin D3/25 (OH) Vitamin D3 12.5
    """

    print("Running extractor on sample text...\n")
    data, log = extract_values(sample_text, debug=True)

    print_debug_log(log)

    print("EXTRACTED DATA:")
    print("-" * 45)
    for k, v in sorted(data.items()):
        print(f"  {k:<30}  {v}")
    print(f"\nTotal extracted: {len(data)} parameters")
