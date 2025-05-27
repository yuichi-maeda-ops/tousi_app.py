import streamlit as st

st.title("資産運用シミュレーター")

tab1, tab2 = st.tabs(["1. 積立投資", "2. 元本一括投資"])

# --------- 積立投資 ---------
with tab1:
    st.header("積立投資のシミュレーション")

    monthly_amount = st.number_input("毎月の積立金額（万円）", min_value=0.0, step=1.0, key="monthly_amount")
    annual_return = st.number_input("想定利回り（年率 %）", min_value=0.0, step=0.1, key="annual_return")
    years = st.number_input("積立期間（年）", min_value=0, step=1, key="years")

    if monthly_amount > 0 and annual_return >= 0 and years > 0:
        r = annual_return / 100 / 12
        n = years * 12
        future_value = monthly_amount * ((1 + r) ** n - 1) / r
        future_value = round(future_value, 1)

        st.success(f"運用資産額： {future_value} 万円")

# --------- 元本一括投資 ---------
with tab2:
    st.header("元本一括投資のシミュレーション")

    principal = st.number_input("元本（万円）", min_value=0.0, step=1.0, key="principal")
    annual_return_lump = st.number_input("想定利回り（年率 %）", min_value=0.0, step=0.1, key="annual_return_lump")
    years_lump = st.number_input("運用期間（年）", min_value=0, step=1, key="years_lump")

    if principal > 0 and annual_return_lump >= 0 and years_lump > 0:
        r = annual_return_lump / 100
        future_value_lump = principal * (1 + r) ** years_lump
        future_value_lump = round(future_value_lump, 1)

        st.success(f"運用資産額： {future_value_lump} 万円")