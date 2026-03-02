import streamlit as st
from model import predict_yield

st.set_page_config(page_title="Crop Yield Prediction", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
/* ===== Global ===== */
.block-container { padding-top: 1.2rem !important; max-width: 1200px; }
h1,h2,h3 { margin-bottom: 0.25rem; }
.main { background: #fbfcfa; }

/* ===== Soft wrapper ===== */
.soft-card{
  background:#fff;
  border:none !important;          /* remove border */
  border-radius:0 !important;      /* remove rounded top */
  padding:0 !important;            /* remove empty top spacing */
  box-shadow:none !important;      /* remove subtle line */
}

/* ===== Section header ===== */
.sec-title{
  font-size:26px;
  font-weight:900;
  color:#162116;
  display:flex;
  align-items:center;
  gap:12px;
  margin:4px 0 14px 0;
}
.sec-ico{
  width:44px; height:44px;
  border-radius:14px;
  background:#eaf3ea;
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:20px;
}

/* ===== Param grid ===== */
.param-grid{ display:grid; grid-template-columns:1fr 1fr; gap:18px 22px; }
.param{ display:flex; flex-direction:column; gap:8px; }
.param-label{
  display:flex; align-items:center; gap:10px;
  font-weight:800; color:#1b2a1b; font-size:16px;
}
.param-label span.ico{ color:#2f6f44; font-size:16px; }
.unit-pill{
  margin-left:auto;
  color:#6b7a6b; font-weight:700; font-size:13px;
}

/* ===== Slider ===== */
div[data-testid="stSlider"]{ padding-top:0px; }
div[data-testid="stSlider"] > label{ display:none; }
div[data-testid="stSlider"] [data-baseweb="slider"]{ margin-top:-6px; }
div[data-testid="stSlider"] [role="slider"]{ box-shadow:none !important; }

/* Green slider theme */
div[data-testid="stSlider"] [data-baseweb="slider"] div[role="slider"]{
  background:#2f6f44 !important;
}
div[data-testid="stSlider"] [data-baseweb="slider"] div[data-testid="stTickBar"]{
  display:none !important;
}
div[data-testid="stSlider"] [data-baseweb="slider"] div[aria-hidden="true"]{
  background:#e9eee6 !important;
}
div[data-testid="stSlider"] [data-baseweb="slider"] div[aria-hidden="true"] > div{
  background:#2f6f44 !important;
}

/* ===== Number input ===== */
div[data-testid="stNumberInput"] > label{ display:none !important; }
div[data-testid="stNumberInput"] input{
  background:#fff !important;
  border:1px solid #dfe6dc !important;
  border-radius:14px !important;
  height:46px !important;
  font-weight:800 !important;
  font-size:16px !important;
  color:#162116 !important;
  padding:0 12px !important;
}
div[data-testid="stNumberInput"] button{ display:none !important; }

/* ===== Predict button ===== */
.predict-btn div.stButton > button{
  height:56px !important;
  border-radius:18px !important;
  width:100% !important;
  font-weight:900 !important;
  font-size:18px !important;
  background:#2f6f44 !important;
  border:1px solid #2b643e !important;
  color:#fff !important;
}
.predict-btn div.stButton > button:hover{ filter:brightness(0.97); }

/* ===== Results ===== */
.results-title{
  font-size:26px;
  font-weight:900;
  color:#162116;
  display:flex;
  align-items:center;
  gap:12px;
  margin-bottom:14px;
}
.result-cards{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:16px;
  margin-bottom:16px;
}
.small-card{
  background:#fff;
  border:1px solid #e6ebe3;
  border-radius:18px;
  padding:16px;
}
.center{
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
  gap:6px;
  min-height:120px;
}
.muted{ color:#708070; font-weight:700; }
.big-num{ font-size:56px; font-weight:900; color:#162116; line-height:1; }
.units{ color:#708070; font-weight:800; }

/* ===== Improved Yield Badge ===== */
.badge{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  gap:8px;
  padding:8px 18px;
  border-radius:12px;          /* less rounded */
  font-weight:800;
  font-size:15px;
  letter-spacing:0.3px;
  min-height:40px;
  white-space:nowrap;
}

/* Category colors */
.badge.low{
  background:#fee2e2;
  color:#b91c1c;
}

.badge.medium{
  background:#fef3c7;
  color:#92400e;
}

.badge.high{
  background:#dcfce7;
  color:#166534;
}

/* Yield level bar */
.bar-card{
  background:#fff;
  border:1px solid #e6ebe3;
  border-radius:18px;
  padding:16px;
}
.bar-top{
  display:flex; align-items:center; gap:10px;
  font-weight:900; color:#1b2a1b;
  margin-bottom:12px;
}
.track{
  height:14px;
  border-radius:999px;
  background:#e9eee6;
  overflow:hidden;
}
.fill{ height:100%; border-radius:999px; }
.scale{
  display:flex; justify-content:space-between;
  margin-top:10px;
  color:#708070;
  font-weight:800;
}

# /* =========================================================
#    ✅ Crop Selection: Radio as Cards (NO dot/line, WITH icons)
#    ========================================================= */
# div[data-testid="stRadio"] > label{ display:none !important; }

# div[data-testid="stRadio"] div[role="radiogroup"]{
#   display:flex !important;
#   gap:18px !important;
#   flex-wrap:nowrap !important;
# }

# /* Card label */
# div[data-testid="stRadio"] div[role="radiogroup"] > label{
#   flex:1 1 0 !important;
#   min-width: 180px !important;
#   border:2px solid #e6ebe3 !important;
#   background:#fff !important;
#   border-radius:22px !important;
#   padding:18px 14px !important;
#   text-align:center !important;
#   cursor:pointer !important;
#   position:relative !important;
# }

# /* Selected card */
# div[data-testid="stRadio"] div[role="radiogroup"] > label:has(input:checked){
#   border-color:#2f6f44 !important;
#   box-shadow:0 0 0 3px rgba(47,111,68,0.10) !important;
# }

# /* HARD hide BaseWeb radio control (this removes grey line + dot) */
# div[data-testid="stRadio"] div[role="radiogroup"] > label [data-baseweb="radio"]{
#   display:none !important;
# }
# div[data-testid="stRadio"] div[role="radiogroup"] > label input{
#   position:absolute !important;
#   opacity:0 !important;
#   width:0 !important;
#   height:0 !important;
# }

# /* The visible text container */
# div[data-testid="stRadio"] div[role="radiogroup"] > label > div{
#   display:flex !important;
#   flex-direction:column !important;
#   align-items:center !important;
#   justify-content:center !important;
#   gap:12px !important;
#   font-weight:900 !important;
#   font-size:22px !important;
#   color:#162116 !important;
#   white-space:nowrap !important;
# }

# /* Icon box */
# div[data-testid="stRadio"] div[role="radiogroup"] > label > div::before{
#   content:"";
#   width:72px;
#   height:64px;
#   border-radius:18px;
#   background:#eef3ee;
#   display:flex;
#   align-items:center;
#   justify-content:center;
#   font-size:32px;
# }

# /* Icon mapping */
# div[data-testid="stRadio"] div[role="radiogroup"] > label:has(input[value="Wheat"]) > div::before{ content:"🌾"; }
# div[data-testid="stRadio"] div[role="radiogroup"] > label:has(input[value="Rice"])  > div::before{ content:"💧"; }
# div[data-testid="stRadio"] div[role="radiogroup"] > label:has(input[value="Maize"]) > div::before{ content:"🌽"; }

/* =========================
   Crop radio -> cards FIX
   ========================= */

/* hide radio label title */
div[data-testid="stRadio"] > label { display:none !important; }

/* layout in a row */
div[data-testid="stRadio"] div[role="radiogroup"]{
  display:flex !important;
  gap:18px !important;
  flex-wrap:nowrap !important;
}

/* each option = card */
div[data-testid="stRadio"] div[role="radiogroup"] > label{
  flex:1 1 0 !important;
  min-width:180px !important;
  border:2px solid #e6ebe3 !important;
  background:#fff !important;
  border-radius:22px !important;
  padding:18px 14px !important;
  text-align:center !important;
  cursor:pointer !important;
  position:relative !important;
}

/* selected card */
div[data-testid="stRadio"] div[role="radiogroup"] > label:has(input:checked){
  border-color:#2f6f44 !important;
  box-shadow:0 0 0 3px rgba(47,111,68,0.10) !important;
}

/* ✅ kill the built-in radio UI (this removes grey line + dot + circle)
   Streamlit usually renders the control in the FIRST child div of label */
div[data-testid="stRadio"] div[role="radiogroup"] > label > div:first-child{
  display:none !important;
}

/* hide the actual input too */
div[data-testid="stRadio"] div[role="radiogroup"] > label input{
  position:absolute !important;
  opacity:0 !important;
  width:0 !important;
  height:0 !important;
}

/* ✅ the visible text container is usually the LAST child div */
div[data-testid="stRadio"] div[role="radiogroup"] > label{
  display:flex !important;
  align-items:center !important;
  justify-content:center !important;
}

div[data-testid="stRadio"] div[role="radiogroup"] > label > div:last-child{
  display:flex !important;
  flex-direction:column !important;
  align-items:center !important;
  justify-content:center !important;
  gap:14px !important;
  text-align:center !important;
}

/* icon box (on LAST child only) */
div[data-testid="stRadio"] div[role="radiogroup"] > label > div:last-child::before{
  content:"";
  width:72px;
  height:64px;
  border-radius:18px;
  background:#eef3ee;
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:32px;
}

/* icon mapping by position (stable now) */
div[data-testid="stRadio"] div[role="radiogroup"] > label:nth-child(1) > div:last-child::before{ content:"🌾"; }
div[data-testid="stRadio"] div[role="radiogroup"] > label:nth-child(2) > div:last-child::before{ content:"💧"; }
div[data-testid="stRadio"] div[role="radiogroup"] > label:nth-child(3) > div:last-child::before{ content:"🌽"; }


</style>
""", unsafe_allow_html=True)


# ---------------- State ----------------
if "crop" not in st.session_state:
    st.session_state.crop = "Wheat"
if "last_yield" not in st.session_state:
    st.session_state.last_yield = None
if "last_category" not in st.session_state:
    st.session_state.last_category = None

# Defaults (tweak as per your dataset)
defaults = {
    "temp": 25.0,
    "rain": 120.0,
    "humidity": 65.0,
    "sunlight": 8.0,
    "altitude": 300.0,
    "wind": 2.1,
    "ph": 6.5,
    "nitrogen": 0.35,
    "phosphorus": 18.0,
    "potassium": 140.0
}
for k, v in defaults.items():
    st.session_state.setdefault(k, v)

# ---------------- Helpers ----------------

def param_slider(key, label, icon, unit, min_v, max_v, step, decimals=1):
    num_k = f"{key}_num"
    sl_k  = f"{key}_sl"

    # initialize shared value
    if key not in st.session_state:
        st.session_state[key] = float(min_v)

    # keep widget states aligned with shared value (on first render)
    if num_k not in st.session_state:
        st.session_state[num_k] = st.session_state[key]
    if sl_k not in st.session_state:
        st.session_state[sl_k] = st.session_state[key]

    def from_num():
        v = float(st.session_state[num_k])
        v = max(float(min_v), min(float(max_v), v))
        st.session_state[key] = round(v, decimals)
        st.session_state[sl_k] = st.session_state[key]

    def from_slider():
        v = float(st.session_state[sl_k])
        v = max(float(min_v), min(float(max_v), v))
        st.session_state[key] = round(v, decimals)
        st.session_state[num_k] = st.session_state[key]

    st.markdown(
        f"<div class='param-label'><span class='ico'>{icon}</span>{label}"
        f"<span class='unit-pill'>{unit}</span></div>",
        unsafe_allow_html=True
    )

    c1, c2 = st.columns([1, 2], gap="medium")

    with c1:
        st.number_input(
            label="",
            key=num_k,
            min_value=float(min_v),
            max_value=float(max_v),
            step=float(step),
            format=f"%.{decimals}f",
            label_visibility="collapsed",
            on_change=from_num,
        )

    with c2:
        st.slider(
            label="",
            min_value=float(min_v),
            max_value=float(max_v),
            step=float(step),
            key=sl_k,
            label_visibility="collapsed",
            on_change=from_slider,
        )

def payload():
    return {
        "Crop": st.session_state.crop,
        "Temperature (C)": st.session_state.temp,
        "Rainfall (mm)": st.session_state.rain,
        "Humidity (%)": st.session_state.humidity,
        "Sunlight (hours)": st.session_state.sunlight,
        "Soil pH": st.session_state.ph,
        "Soil Nitrogen (%)": st.session_state.nitrogen,
        "Soil Phosphorus (ppm)": st.session_state.phosphorus,
        "Soil Potassium (ppm)": st.session_state.potassium,
        "Altitude (m)": st.session_state.altitude,
        "Wind Speed (m/s)": st.session_state.wind,
    }

def badge_class(cat: str):
    c = (cat or "").lower()
    if "high" in c: return "high"
    if "medium" in c: return "medium"
    return "low"

def yield_fill_and_color(y):
    # Map yield to 0..1 for bar fill (adjust to your realistic range)
    # Example: 0 to 10 tons/ha
    lo, hi = 0.0, 10.0
    p = 0.0 if y is None else (y - lo) / (hi - lo)
    p = max(0.0, min(1.0, p))
    # Color by category-ish
    if p < 0.33:
        return p, "#e53935"
    if p < 0.66:
        return p, "#f59e0b"
    return p, "#16a34a"

# ---------------- Layout ----------------
st.markdown("<h1 style='text-align:center; font-weight:900; color:#162116;'>Crop Yield Prediction</h1>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; color:#708070; font-weight:700; margin-bottom:18px;'>Adjust inputs and predict expected yield.</div>", unsafe_allow_html=True)

left, right = st.columns([3, 2], gap="large")

# -------- LEFT --------
with left:
    st.markdown("<div class='soft-card'>", unsafe_allow_html=True)

    st.markdown("<div class='sec-title'><div class='sec-ico'>🌱</div>Crop Selection</div>", unsafe_allow_html=True)

    if "crop" not in st.session_state:
        st.session_state["crop"] = "Wheat"

    crop = st.radio(
        label="",
        options=["Wheat", "Rice", "Maize"],
        horizontal=True,
        label_visibility="collapsed",
        index=["Wheat", "Rice", "Maize"].index(st.session_state["crop"]),
        key="crop_radio"
    )

    st.session_state["crop"] = crop

    st.markdown("<div class='sec-title' style='margin-top:6px;'><div class='sec-ico'>☀️</div>Environmental Parameters</div>", unsafe_allow_html=True)
    st.markdown("<div class='param-grid'>", unsafe_allow_html=True)

    with st.container():
        # Use columns to keep the grid spacing consistent
        g1, g2 = st.columns(2, gap="large")
        with g1:
            param_slider("temp", "Temperature", "🌡️", "°C", 0, 50, 0.5, 1)
            param_slider("humidity", "Humidity", "💧", "%", 0, 100, 1, 0)
            param_slider("altitude", "Altitude", "⛰️", "m", -50, 6000, 10, 0)
        with g2:
            param_slider("rain", "Rainfall", "🌧️", "mm", 0, 1000, 5, 0)
            param_slider("sunlight", "Sunlight", "☀️", "hrs", 0, 24, 0.5, 1)
            param_slider("wind", "Wind Speed", "🍃", "m/s", 0, 40, 0.1, 1)

    st.markdown("<div class='sec-title' style='margin-top:18px;'><div class='sec-ico'>🧪</div>Soil Parameters</div>", unsafe_allow_html=True)

    s1, s2 = st.columns(2, gap="large")
    with s1:
        param_slider("ph", "Soil pH", "⚗️", "pH", 0, 14, 0.1, 1)
        param_slider("phosphorus", "Phosphorus", "⚡", "ppm", 0, 200, 1, 0)
    with s2:
        param_slider("nitrogen", "Nitrogen", "🧬", "%", 0, 5, 0.01, 2)
        param_slider("potassium", "Potassium", "🧱", "ppm", 0, 500, 1, 0)

    st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)
    st.markdown("<div class='predict-btn'>", unsafe_allow_html=True)
    predict_clicked = st.button("⚡  Predict Yield", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# -------- RIGHT --------
with right:
    st.markdown("<div class='soft-card'>", unsafe_allow_html=True)
    st.markdown("<div class='results-title'><div class='sec-ico'>📈</div>Prediction Results</div>", unsafe_allow_html=True)

    if predict_clicked:
        y, cat = predict_yield(payload())
        st.session_state.last_yield = float(y)
        st.session_state.last_category = str(cat)

    y = st.session_state.last_yield
    cat = st.session_state.last_category

    if y is None:
        st.markdown("<div class='muted'>Click <b>Predict Yield</b> to see results.</div>", unsafe_allow_html=True)
    else:
        col1, col2 = st.columns(2, gap="small")

        # -------- Predicted Yield --------
        with col1:
            st.markdown("""
            <div class='small-card'>
            <div class='center'>
                <div class='muted'>Predicted Yield</div>
                <div class='big-num'>{:.1f}</div>
                <div class='units'>tons / ha</div>
            </div>
            </div>
            """.format(y), unsafe_allow_html=True)

        # -------- Yield Category --------
        with col2:
            bc = badge_class(cat)

            st.markdown(f"""
            <div class='small-card'>
            <div class='center'>
                <div class='muted'>Yield Category</div>
                <div style='display:flex; align-items:center; justify-content:center; gap:12px;'>
                <div style='font-size:18px;'>🏅</div>
                <div class='badge {bc}'>{cat}</div>
                </div>
                </div>
            </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)