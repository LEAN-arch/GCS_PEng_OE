# ======================================================================================
# GCS PROCESS ENGINEERING & OPERATIONAL EXCELLENCE COMMAND CENTER
#
# A single-file Streamlit application for the Senior Manager, Process Engineering & OpEx.
#
# VERSION: Strategic Cloud Ops & AI Transformation
#
# This dashboard provides a real-time, strategic view of the Global Cloud Services (GCS)
# process ecosystem. It is designed to manage a global OpEx team, track a portfolio
# of high-impact initiatives, visualize the opportunity pipeline, and drive the
# integration of AI into core operational workflows, in alignment with:
#   - Lean Six Sigma & DMAIC Methodologies
#   - ITIL v4 / ITSM Principles (Incident, Change, Problem Management)
#   - Cloud FinOps & ROI-Based Prioritization
#   - AI-Driven Automation & Agentic Workflow Concepts
#   - Secure Operations for US Public Sector (FedRAMP/NIST context)
#
# To Run:
# 1. Save this code as 'gcs_opex_dashboard.py'
# 2. Create 'requirements.txt' (streamlit, pandas, numpy<2.0, plotly, scikit-learn).
# 3. Install dependencies: pip install -r requirements.txt
# 4. Run from your terminal: streamlit run gcs_opex_dashboard.py
#
# ======================================================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import datetime

# ======================================================================================
# SECTION 1: APP CONFIGURATION & STYLING
# ======================================================================================
st.set_page_config(
    page_title="GCS OpEx Command Center",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<style>
    .main .block-container { padding: 1rem 3rem 3rem; }
    .stMetric { background-color: #fcfcfc; border: 1px solid #e0e0e0; border-left: 5px solid #2962ff; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: #F0F2F6; border-radius: 4px 4px 0px 0px; padding-top: 10px; padding-bottom: 10px; font-weight: 600; }
    .stTabs [aria-selected="true"] { background-color: #FFFFFF; box-shadow: 0 -2px 5px rgba(0,0,0,0.1); border-bottom-color: #FFFFFF !important; }
    .st-expander { border: 1px solid #E0E0E0 !important; border-radius: 10px !important; }
</style>
""", unsafe_allow_html=True)


# ======================================================================================
# SECTION 2: SME-DRIVEN DATA SIMULATION FOR CLOUD OPS & OPEX
# ======================================================================================
@st.cache_data(ttl=600)
def generate_master_data():
    np.random.seed(42)
    # --- 1. OpEx Initiative Portfolio ---
    initiatives_data = {
        'InitiativeID': [f'P-{i:03d}' for i in range(1, 11)],
        'Name': ['Automate L1 Incident Triage', 'Streamline Change Approval Workflow', 'Implement Proactive Problem Mgmt', 'Standardize VM Provisioning', 'Optimize CMDB Reconciliation', 'Reduce Cloud Spend Waste', 'Secure Deployment Pipeline (CI/CD)', 'Enhance DR Test Automation', 'GenAI for Knowledge Base', 'On-call Scheduling Optimization'],
        'DMAIC_Phase': np.random.choice(['Define', 'Measure', 'Analyze', 'Improve', 'Control'], 10, p=[0.1, 0.2, 0.3, 0.3, 0.1]),
        'Lead': np.random.choice(['A. Chen', 'B. Singh', 'C. Jones', 'D. Patel'], 10),
        'Impacted_Process': ['Incident Mgmt', 'Change Mgmt', 'Problem Mgmt', 'Service Request', 'Asset Mgmt', 'FinOps', 'DevOps', 'BC/DR', 'Knowledge Mgmt', 'Operations Mgmt'],
        'Expected_Annual_ROI_USD': np.random.randint(50000, 500000, 10),
        'Status': np.random.choice(['On Track', 'At Risk', 'Blocked'], 10, p=[0.7, 0.2, 0.1]),
        'Percent_Complete': np.random.randint(10, 95, 10)
    }
    initiatives_df = pd.DataFrame(initiatives_data)

    # --- 2. Opportunity Pipeline (from Stakeholder Engagement) ---
    pipeline_data = {
        'OpportunityID': [f'OPP-{i:03d}' for i in range(1, 16)],
        'Name': [f'Idea from {team}' for team in ['NOC', 'SRE', 'Security', 'Finance', 'AppDev'] * 3],
        'Sponsor_VP': ['VP, GCS Ops', 'VP, Platform Eng.', 'CISO', 'VP, Finance', 'VP, R&D'] * 3,
        'Stage': np.random.choice(['1. Identification', '2. Validation', '3. Scoping', '4. Approved Backlog'], 15, p=[0.4, 0.3, 0.2, 0.1]),
        'Est_Value_USD_yr': np.random.randint(25000, 200000, 15)
    }
    pipeline_df = pd.DataFrame(pipeline_data)

    # --- 3. Core GCS Process Metrics ---
    dates = pd.to_datetime(pd.date_range(start='2023-01-01', periods=12, freq='ME'))
    metrics_data = {
        'Month': dates,
        'Incident_MTTR_Minutes': np.random.normal(60, 10, 12) * np.linspace(1, 0.7, 12), # Improving
        'Change_Failure_Rate_Pct': np.random.normal(5, 1.5, 12) * np.linspace(1, 0.5, 12), # Improving
        'Problem_RCA_Cycle_Time_Days': np.random.normal(10, 2, 12) * np.linspace(1, 0.8, 12), # Improving
        'Manual_Effort_Hours_per_Week': np.random.normal(500, 50, 12) * np.linspace(1, 0.4, 12) # Improving via AI/Automation
    }
    metrics_df = pd.DataFrame(metrics_data)
    
    # --- 4. AI Transformation / Digital Labor Mix ---
    ai_adoption_data = {
        'Month': dates,
        'Manual': np.linspace(80, 25, 12) + np.random.uniform(-3, 3, 12),
        'AI_Assisted': np.linspace(15, 50, 12) + np.random.uniform(-3, 3, 12),
        'Fully_Agentic': np.linspace(5, 25, 12) + np.random.uniform(-3, 3, 12)
    }
    ai_adoption_df = pd.DataFrame(ai_adoption_data)
    ai_adoption_df[['Manual', 'AI_Assisted', 'Fully_Agentic']] = ai_adoption_df[['Manual', 'AI_Assisted', 'Fully_Agentic']].clip(0)
    ai_adoption_df_norm = ai_adoption_df.set_index('Month').apply(lambda x: x / x.sum(), axis=1).reset_index()

    # --- 5. Global Team Capability ---
    team_data = {
        'Team_Member': ['A. Chen', 'B. Singh', 'C. Jones', 'D. Patel', 'E. Williams', 'F. Garcia'],
        'Region': ['AMER', 'APAC', 'AMER', 'EMEA', 'AMER', 'APAC'],
        'LSS_Belt': np.random.choice(['Black Belt', 'Green Belt', 'Green Belt', 'Yellow Belt'], 6),
        'AI_Process_Integration_Skill': np.random.randint(2, 6, 6),
        'ServiceNow_Platform_Skill': np.random.randint(3, 6, 6),
        'Stakeholder_Influence_Skill': np.random.randint(3, 6, 6),
        'USFed_Cleared': np.random.choice([True, True, True, False, True, False], 6)
    }
    team_df = pd.DataFrame(team_data)
    
    return initiatives_df, pipeline_df, metrics_df, ai_adoption_df_norm, team_df

# ======================================================================================
# SECTION 3: ADVANCED VISUALIZATION FUNCTIONS
# ======================================================================================
def plot_initiative_portfolio(df):
    fig = px.timeline(df, x_start=df['Percent_Complete'] * 0, x_end='Percent_Complete', y='Name',
                      color='Status', text='DMAIC_Phase',
                      color_discrete_map={'On Track': '#2e7d32', 'At Risk': '#ffc107', 'Blocked': '#d32f2f'},
                      title='<b>OpEx Initiative Portfolio Status (by DMAIC Phase)</b>')
    fig.update_layout(xaxis_title='Percent Complete', yaxis_title='Initiative', xaxis_ticksuffix='%')
    fig.update_traces(textposition='inside')
    return fig

def plot_opportunity_pipeline(df):
    fig = px.funnel(df, x='Est_Value_USD_yr', y='Stage', color='Sponsor_VP',
                    title='<b>Opportunity Pipeline by Sponsor & Estimated Value</b>',
                    labels={'Est_Value_USD_yr': 'Estimated Annual Value (USD)'})
    fig.update_layout(yaxis_title='Funnel Stage')
    return fig

def plot_kpi_performance(df):
    fig = go.Figure()
    targets = {'Incident_MTTR_Minutes': 45, 'Change_Failure_Rate_Pct': 3, 'Problem_RCA_Cycle_Time_Days': 7}
    for i, (metric, target) in enumerate(targets.items()):
        current_value = df[metric].iloc[-1]
        fig.add_trace(go.Indicator(
            mode="number+gauge+delta",
            value=current_value,
            delta={'reference': df[metric].iloc[-2], 'decreasing': {'color': "#2e7d32"}, 'increasing': {'color': "#d32f2f"}},
            domain={'x': [i * 0.33, (i + 1) * 0.33 - 0.05], 'y': [0, 1]},
            title={'text': metric.replace('_', ' ')},
            gauge={'shape': "bullet", 'axis': {'range': [None, target * 2]},
                   'threshold': {'line': {'color': "red", 'width': 2}, 'thickness': 0.75, 'value': target},
                   'bar': {'color': "rgba(41, 98, 255, 0.7)"}}
        ))
    fig.update_layout(height=200, margin=dict(l=10, r=10, t=40, b=10))
    return fig

def plot_digital_labor_mix(df):
    fig = px.area(df, x='Month', y=['Manual', 'AI_Assisted', 'Fully_Agentic'],
                  title='<b>Evolution of Digital Labor Mix in GCS Processes</b>',
                  labels={'value': 'Percentage of Tasks', 'variable': 'Labor Type'},
                  color_discrete_map={'Manual': '#d32f2f', 'AI_Assisted': '#ffc107', 'Fully_Agentic': '#2e7d32'})
    fig.update_layout(yaxis_ticksuffix='%', yaxis_range=[0,100])
    return fig

# ======================================================================================
# SECTION 4: MAIN APPLICATION LAYOUT & SCIENTIFIC NARRATIVE
# ======================================================================================
st.title("⚙️ GCS Process Engineering & Operational Excellence Command Center")
st.markdown("##### A strategic dashboard for managing a global OpEx portfolio, driving stakeholder value, and leading AI-driven process transformation.")

# --- Load Data ---
initiatives_df, pipeline_df, metrics_df, ai_adoption_df, team_df = generate_master_data()

# --- Executive KPIs ---
st.markdown("### I. Executive Summary Dashboard")
kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
total_roi = initiatives_df['Expected_Annual_ROI_USD'].sum()
pipeline_value = pipeline_df[pipeline_df['Stage'] == '4. Approved Backlog']['Est_Value_USD_yr'].sum()
current_automation_pct = (ai_adoption_df['AI_Assisted'].iloc[-1] + ai_adoption_df['Fully_Agentic'].iloc[-1])
fed_ready_team_pct = (team_df['USFed_Cleared'].sum() / len(team_df)) * 100

kpi_col1.metric("Active Portfolio ROI", f"${total_roi/1_000_000:.2f}M", help="Total expected annual ROI from all in-flight OpEx initiatives.")
kpi_col2.metric("Approved Pipeline Value", f"${pipeline_value/1_000:.1f}K", help="Value of new opportunities in the approved backlog, generated from stakeholder engagement.")
kpi_col3.metric("AI/Automation Index", f"{current_automation_pct:.1f}%", help="Percentage of core process tasks that are either AI-assisted or fully agentic, representing progress in digital transformation.")
kpi_col4.metric("USFed Team Readiness", f"{fed_ready_team_pct:.0f}%", help="Percentage of the global team cleared to support US Public Sector customers, indicating resource flexibility.")
st.markdown("---")

# --- Tabs with Enhanced Descriptions ---
tab1, tab2, tab3, tab4 = st.tabs(["**II. OPEX INITIATIVE PORTFOLIO & PIPELINE**", "**III. GCS PROCESS PERFORMANCE**", "**IV. AI TRANSFORMATION**", "**V. GLOBAL TEAM CAPABILITY**"])

with tab1:
    st.header("II. Operational Excellence Initiative Portfolio & Opportunity Pipeline")
    st.markdown("_This section provides a comprehensive view of the entire value chain for process improvement, from initial stakeholder idea to project execution and value realization._")
    
    st.subheader("A. Active Initiative Portfolio")
    with st.expander("View Methodological Summary", expanded=False):
        st.markdown("""
        - **Purpose:** To provide a single-pane-of-glass view of all in-flight process improvement projects, their status, and their alignment with the structured DMAIC (Define, Measure, Analyze, Improve, Control) methodology.
        - **Method:** A Gantt chart is used to visualize project completeness against its lifecycle. The color indicates project health (On Track, At Risk, Blocked), while the text overlay shows the current DMAIC phase. This allows for quick identification of projects that are lagging or facing impediments.
        - **Interpretation:** This view enables the manager to assess overall portfolio health, balance resources across different phases of the Lean Six Sigma lifecycle, and hold project leads accountable for progress. 'Blocked' or 'At Risk' items require immediate management attention and intervention.
        """)
    st.plotly_chart(plot_initiative_portfolio(initiatives_df), use_container_width=True)

    st.subheader("B. New Opportunity Pipeline from Stakeholder Engagement")
    with st.expander("View Methodological Summary", expanded=False):
        st.markdown("""
        - **Purpose:** To quantify and visualize the pipeline of potential process improvement projects generated through strategic partnerships with cross-functional stakeholders. This directly measures the "value-adding work opportunities" a key responsibility of this role.
        - **Method:** A funnel chart illustrates the flow of opportunities from initial `Identification` to the `Approved Backlog`. The width of each segment represents the total estimated annual value of opportunities at that stage. Segments are color-coded by the sponsoring business leader (VP).
        - **Interpretation:** A healthy pipeline is wide at the top and demonstrates consistent conversion through the stages. This chart is critical for demonstrating proactive value creation to leadership and for forecasting future project workload for the OpEx team. A thin funnel may indicate a need for increased stakeholder outreach.
        """)
    st.plotly_chart(plot_opportunity_pipeline(pipeline_df), use_container_width=True)

with tab2:
    st.header("III. GCS Core Process Performance")
    st.markdown("_This section monitors the vital signs of key Global Cloud Services operational processes. It provides a baseline for identifying areas of friction and measuring the impact of improvement initiatives._")
    
    st.subheader("A. Key Performance Indicator (KPI) Dashboard")
    with st.expander("View Methodological Summary", expanded=False):
        st.markdown("""
        - **Purpose:** To provide a concise, at-a-glance view of the current performance of critical GCS processes against their established targets.
        - **Method:** Bullet charts are used to compare the most recent period's performance (the bar) against the target (the red line). A delta indicator shows the change from the prior period, with green indicating improvement and red indicating degradation. This is a standard visualization in executive operational dashboards.
        - **Interpretation:** This chart immediately flags which processes are operating outside of acceptable thresholds. For example, an `Incident MTTR` exceeding its target warrants an investigation and could be a candidate for a new Kaizen event or a larger DMAIC project. These metrics directly quantify the "process friction or inefficiency" this role is tasked to eliminate.
        """)
    st.plotly_chart(plot_kpi_performance(metrics_df), use_container_width=True)
    
    st.subheader("B. Historical Process Trends")
    st.dataframe(metrics_df.set_index('Month').style.format("{:.1f}"), use_container_width=True)

with tab3:
    st.header("IV. AI Transformation & Automation Intelligence")
    st.markdown("_This section tracks the strategic imperative of integrating AI and automation into GCS workflows, measuring the shift from manual human effort to intelligent, agentic systems._")

    st.subheader("A. Digital Labor Mix Analysis")
    with st.expander("View Methodological Summary", expanded=False):
        st.markdown("""
        - **Purpose:** To visualize the strategic shift in how work is accomplished within GCS, moving from manual processes to a more scalable, AI-driven operational model.
        - **Method:** A 100% stacked area chart tracks the composition of task fulfillment over time, broken into three categories:
          - **Manual:** Tasks performed entirely by a human operator.
          - **AI-Assisted:** Tasks where a human uses AI tools for guidance, analysis, or partial automation (e.g., a GenAI-powered knowledge base).
          - **Fully Agentic:** Tasks performed end-to-end by an AI agent with no human intervention (e.g., automated incident resolution for known error conditions).
        - **Interpretation:** This is the primary measure of the AI integration strategy. A successful transformation is indicated by the red area (`Manual`) shrinking over time, while the yellow (`AI-Assisted`) and green (`Fully Agentic`) areas expand. This chart provides a powerful narrative for executive leadership about the progress and impact of the AI transformation roadmap.
        """)
    st.plotly_chart(plot_digital_labor_mix(ai_adoption_df), use_container_width=True)

with tab4:
    st.header("V. Global Team Capability & Readiness")
    st.markdown("_This section provides insights into the skills, deployment readiness, and geographical distribution of the global Process Engineering & OpEx team._")

    st.subheader("A. Team Skills & Readiness Matrix")
    with st.expander("View Methodological Summary", expanded=False):
        st.markdown("""
        - **Purpose:** To assess the collective capabilities of the team against key strategic needs, identify skill gaps, and ensure readiness for critical assignments, such as supporting US Public Sector clients.
        - **Method:** A heatmap is used to visualize the skill levels of each team member across critical competencies. A separate column explicitly tracks US Federal clearance status.
        - **Interpretation:** This matrix allows for strategic project assignment (e.g., assigning a Black Belt with high AI skills to a complex automation project). It also highlights areas for professional development and training investments. The `USFed_Cleared` column is essential for resource planning on high-security contracts, ensuring compliance and operational readiness.
        """)
    st.dataframe(team_df.set_index('Team_Member'), use_container_width=True)

# ============================ SIDEBAR ============================
st.sidebar.image("https://logowik.com/content/uploads/images/servicenow5873.jpg", use_column_width=True)
st.sidebar.markdown("### Role Focus")
st.sidebar.info(
    "This dashboard is for a **Senior Manager, Process Engineering & OpEx**, focused on leading a global team to drive ROI-based improvements and AI transformation within a cloud services organization."
)
st.sidebar.markdown("### Why Join This Role?")
st.sidebar.markdown("""
- **Shape Global Evolution:** Drive how a fast-moving cloud organization adapts to an AI-enabled world.
- **Lead High-Performers:** Manage and mentor a diverse, global team of process experts.
- **Drive Measurable Impact:** See the direct impact of your work on ROI, efficiency, and automation.
- **Build Intelligent Systems:** Go beyond traditional OpEx to design and implement agentic, AI-powered workflows.
"""
)
st.sidebar.markdown("---")
st.sidebar.markdown("### Key Methodologies")
st.sidebar.markdown("""
- **Lean Six Sigma:** A disciplined, data-driven approach for eliminating defects and waste.
- **DMAIC:** The five-phase LSS framework: Define, Measure, Analyze, Improve, Control.
- **ITSM/ITIL:** A set of best practices for delivering IT services.
- **Agentic AI:** Autonomous AI systems (agents) that can perform complex tasks and make decisions without human intervention.
""")
