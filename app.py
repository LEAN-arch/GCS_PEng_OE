# ======================================================================================
# GCS PROCESS ENGINEERING & OPERATIONAL EXCELLENCE COMMAND CENTER
#
# A single-file Streamlit application for the Senior Manager, Process Engineering & OpEx.
#
# VERSION: Strategic & Diagnostic Edition (Maximum Actionability - Unabridged)
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
# 1. Save this code as 'gcs_opex_strategic_dashboard.py'
# 2. Create 'requirements.txt' with specified libraries.
# 3. Install dependencies: pip install -r requirements.txt
# 4. Run from your terminal: streamlit run gcs_opex_strategic_dashboard.py
#
# ======================================================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ======================================================================================
# SECTION 1: APP CONFIGURATION & STYLING
# ======================================================================================
st.set_page_config(
    page_title="GCS OpEx Command Center",
    page_icon="🚀",
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
        'Lead': np.random.choice(['A. Chen', 'B. Singh', 'C. Jones', 'D. Patel'], 10),
        'Expected_Annual_ROI_USD': np.random.randint(50000, 750000, 10),
        'Status': np.random.choice(['On Track', 'At Risk', 'Blocked'], 10, p=[0.7, 0.2, 0.1]),
        'Percent_Complete': np.random.randint(10, 95, 10)
    }
    initiatives_df = pd.DataFrame(initiatives_data)

    # --- 2. Opportunity Pipeline (from Stakeholder Engagement) ---
    pipeline_data = {
        'OpportunityID': [f'OPP-{i:03d}' for i in range(1, 21)],
        'Name': [f'Idea from {team}' for team in ['NOC', 'SRE', 'Security', 'Finance', 'AppDev'] * 4],
        'Sponsor_VP': ['VP, GCS Ops', 'VP, Platform Eng.', 'CISO', 'VP, Finance', 'VP, R&D'] * 4,
        'Stage': np.random.choice(['1. Identification', '2. Validation', '3. Scoping', '4. Approved Backlog'], 20, p=[0.4, 0.3, 0.2, 0.1]),
        'Est_Value_USD_yr': np.random.randint(25000, 200000, 20)
    }
    pipeline_df = pd.DataFrame(pipeline_data)

    # --- 3. Core GCS Process Metrics ---
    dates = pd.to_datetime(pd.date_range(start='2023-01-01', periods=12, freq='ME'))
    metrics_data = {
        'Month': dates,
        'Incident_MTTR_Minutes': np.random.normal(60, 10, 12) * np.linspace(1, 0.7, 12),
        'Change_Failure_Rate_Pct': np.random.normal(5, 1.5, 12) * np.linspace(1, 0.5, 12),
        'Problem_RCA_Cycle_Time_Days': np.random.normal(10, 2, 12) * np.linspace(1, 0.8, 12),
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
    ai_adoption_df_norm = ai_adoption_df.set_index('Month').apply(lambda x: x / x.sum() * 100, axis=1).reset_index()

    # --- 5. Global Team Capability ---
    team_data = {
        'Team_Member': ['A. Chen', 'B. Singh', 'C. Jones', 'D. Patel', 'E. Williams', 'F. Garcia'],
        'Region': ['AMER', 'APAC', 'AMER', 'EMEA', 'AMER', 'APAC'],
        'LSS_Belt': ['Black Belt', 'Green Belt', 'Black Belt', 'Green Belt', 'Yellow Belt', 'Green Belt'],
        'AI_Integration_Skill': [5, 3, 4, 4, 2, 3],
        'Stakeholder_Influence': [5, 4, 5, 3, 3, 4],
        'USFed_Cleared': [True, True, True, False, True, False]
    }
    team_df = pd.DataFrame(team_data)
    
    return initiatives_df, pipeline_df, metrics_df, ai_adoption_df_norm, team_df

# ======================================================================================
# SECTION 3: ACTIONABILITY-ENHANCED VISUALIZATION FUNCTIONS
# ======================================================================================
def plot_portfolio_priority_matrix(df):
    df['Status_Color'] = df['Status'].map({'On Track': '#2e7d32', 'At Risk': '#ffc107', 'Blocked': '#d32f2f'})
    avg_roi = df['Expected_Annual_ROI_USD'].mean()
    avg_complete = df['Percent_Complete'].mean()
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['Expected_Annual_ROI_USD'], y=df['Percent_Complete'],
        mode='markers+text', text=df['Lead'], textposition='top center',
        marker=dict(size=18, color=df['Status_Color'], line=dict(width=2, color='DarkSlateGrey')),
        hovertext=df['Name'], name='Initiatives'
    ))
    fig.add_vline(x=avg_roi, line_width=1, line_dash="dash", line_color="grey")
    fig.add_hline(y=avg_complete, line_width=1, line_dash="dash", line_color="grey")
    
    fig.update_layout(
        title='<b>Initiative Portfolio: Priority & Health Matrix</b>',
        xaxis_title='Expected Annual ROI (Impact)', yaxis_title='Percent Complete (Maturity)',
        showlegend=False, xaxis_tickprefix='$', yaxis_ticksuffix='%'
    )
    fig.add_annotation(x=avg_roi*1.5, y=avg_complete*1.5, text="<b>Monitor & Complete</b>", showarrow=False, font=dict(color="grey"))
    fig.add_annotation(x=avg_roi*0.5, y=avg_complete*1.5, text="<b>Quick Wins</b>", showarrow=False, font=dict(color="grey"))
    fig.add_annotation(x=avg_roi*0.5, y=avg_complete*0.5, text="<b>Nurture & Develop</b>", showarrow=False, font=dict(color="grey"))
    fig.add_annotation(x=avg_roi*1.5, y=avg_complete*0.5, text="<b>🔥 STRATEGIC FOCUS 🔥</b>", showarrow=False, font=dict(color="#d32f2f", size=14))
    return fig

def plot_enhanced_funnel(df):
    stage_counts = df.groupby('Stage').agg(
        Count=('OpportunityID', 'count'),
        Value=('Est_Value_USD_yr', 'sum')
    ).reindex(['1. Identification', '2. Validation', '3. Scoping', '4. Approved Backlog']).reset_index()
    
    stage_counts['Conversion_Rate'] = (stage_counts['Count'] / stage_counts['Count'].shift(1) * 100).fillna(100)
    
    fig = go.Figure(go.Funnel(
        y=stage_counts['Stage'],
        x=stage_counts['Value'],
        textinfo="value+percent initial",
        texttemplate="%{value:$,.0s} <br>(%{percentInitial:.1%})",
        marker={"color": ["#5c6bc0", "#26a69a", "#66bb6a", "#2e7d32"]}
    ))
    fig.update_layout(
        title='<b>Opportunity Pipeline: Value Flow & Conversion</b>',
        yaxis_title='Funnel Stage'
    )
    return fig, stage_counts

def plot_process_control_chart(df, metric):
    df['Month'] = pd.to_datetime(df['Month'])
    mean = df[metric].mean()
    std_dev = df[metric].std()
    ucl = mean + 3 * std_dev
    lcl = max(0, mean - 3 * std_dev)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Month'], y=df[metric], name='Monthly Value', mode='lines+markers', line=dict(color='#2962ff')))
    fig.add_hline(y=mean, line=dict(color='green', dash='dot'), name='Mean')
    fig.add_hline(y=ucl, line=dict(color='red', dash='dash'), name='UCL (+3σ)')
    fig.add_hline(y=lcl, line=dict(color='orange', dash='dash'), name='LCL (-3σ)')
    
    outliers = df[df[metric] > ucl]
    fig.add_trace(go.Scatter(x=outliers['Month'], y=outliers[metric], mode='markers', name='Special Cause Variation', marker=dict(symbol='x', color='red', size=12)))
    fig.update_layout(title=f'<b>Process Control Chart: {metric.replace("_", " ")}</b>', yaxis_title='Value', xaxis_title='Month')
    return fig

def plot_digital_labor_mix(df):
    fig = px.area(df, x='Month', y=['Manual', 'AI_Assisted', 'Fully_Agentic'],
                  title='<b>Evolution of Digital Labor Mix in GCS Processes</b>',
                  labels={'value': 'Percentage of Tasks', 'variable': 'Labor Type'},
                  color_discrete_map={'Manual': '#d32f2f', 'AI_Assisted': '#ffc107', 'Fully_Agentic': '#2e7d32'})
    fig.update_layout(yaxis_ticksuffix='%', yaxis_range=[0,100])
    return fig

def plot_talent_capability_matrix(df):
    belt_map = {'Yellow Belt': 1, 'Green Belt': 2, 'Black Belt': 3}
    df['LSS_Numeric'] = df['LSS_Belt'].map(belt_map)
    df['Clearance_Symbol'] = df['USFed_Cleared'].map({True: 'circle', False: 'x-thin-open'})

    fig = px.scatter(
        df, x='LSS_Numeric', y='AI_Integration_Skill',
        size='Stakeholder_Influence', color='Region', symbol='Clearance_Symbol',
        text='Team_Member', hover_name='Team_Member',
        labels={'LSS_Numeric': 'Lean Six Sigma Mastery', 'AI_Integration_Skill': 'AI Process Integration Skill'},
        title='<b>Global Team: Talent & Capability Matrix</b>'
    )
    fig.update_traces(textposition='bottom center', marker_line_width=1, marker_opacity=0.8)
    fig.update_layout(
        xaxis=dict(tickmode='array', tickvals=[1, 2, 3], ticktext=['Yellow', 'Green', 'Black']),
        legend_title_text='Legend'
    )
    return fig

# ======================================================================================
# SECTION 4: MAIN APPLICATION LAYOUT & SCIENTIFIC NARRATIVE
# ======================================================================================
st.title("🚀 GCS Process Engineering & Operational Excellence Command Center")
st.markdown("##### A strategic dashboard for managing a global OpEx portfolio, driving stakeholder value, and leading AI-driven process transformation.")

initiatives_df, pipeline_df, metrics_df, ai_adoption_df, team_df = generate_master_data()

st.markdown("### I. Executive Summary Dashboard")
kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
total_roi = initiatives_df['Expected_Annual_ROI_USD'].sum()
pipeline_value = pipeline_df[pipeline_df['Stage'] == '4. Approved Backlog']['Est_Value_USD_yr'].sum()
current_automation_pct = (ai_adoption_df['AI_Assisted'].iloc[-1] + ai_adoption_df['Fully_Agentic'].iloc[-1])
kpi_col1.metric("Active Portfolio ROI", f"${total_roi/1_000_000:.2f}M")
kpi_col2.metric("Approved Pipeline Value", f"${pipeline_value/1_000:.1f}K")
kpi_col3.metric("AI/Automation Index", f"{current_automation_pct:.1f}%")
st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(["**II. OPEX PORTFOLIO & PIPELINE**", "**III. GCS PROCESS PERFORMANCE**", "**IV. AI TRANSFORMATION**", "**V. GLOBAL TEAM CAPABILITY**"])

with tab1:
    st.header("II. Operational Excellence Initiative Portfolio & Opportunity Pipeline")
    st.markdown("_This section provides a comprehensive view of the entire value chain for process improvement, from initial stakeholder idea to project execution and value realization._")
    
    st.subheader("A. Active Initiative Portfolio: Priority & Health Matrix")
    with st.expander("View Methodological Summary", expanded=False):
        st.markdown("""
        - **Purpose:** To provide a risk-vs-reward framework for prioritizing management attention across the active project portfolio.
        - **Method:** A 2x2 matrix plotting project Impact (Expected Annual ROI) against Maturity (Percent Complete). The color of each point represents its health status (Green: On Track, Yellow: At Risk, Red: Blocked), and the point is labeled with the project lead.
        - **Findings & Interpretation:** The bottom-right quadrant, **'Strategic Focus'**, contains high-value, low-maturity projects. These are the most critical initiatives to protect. Any project in this quadrant marked as 'At Risk' or 'Blocked' requires immediate senior management intervention to clear impediments. The top-left quadrant represents low-hanging fruit or 'Quick Wins' that should be completed swiftly.
        """)
    st.plotly_chart(plot_portfolio_priority_matrix(initiatives_df), use_container_width=True)

    st.subheader("B. New Opportunity Pipeline: Value Flow & Conversion")
    with st.expander("View Methodological Summary", expanded=False):
        st.markdown("""
        - **Purpose:** To quantify the health and velocity of the process improvement pipeline, from idea generation to inclusion in the approved work backlog.
        - **Method:** An enhanced funnel chart visualizes the total potential value (USD) at each stage. It also calculates and displays the stage-to-stage conversion rate, a key indicator of pipeline efficiency.
        - **Findings & Interpretation:** This chart demonstrates the team's ability to generate value by creating "bonds with stakeholders." A steep drop-off in conversion between 'Validation' and 'Scoping' might indicate a bottleneck in the team's capacity to analyze new ideas or a misalignment with stakeholder priorities. The total value in the 'Approved Backlog' serves as a forecast for the team's future work.
        """)
    funnel_fig, funnel_data = plot_enhanced_funnel(pipeline_df)
    st.plotly_chart(funnel_fig, use_container_width=True)

with tab2:
    st.header("III. GCS Core Process Performance")
    st.markdown("_This section uses Statistical Process Control (SPC) to monitor the health and stability of key operational processes, moving beyond simple monthly averages to identify meaningful deviations._")
    
    st.subheader("A. Process Control Charts")
    with st.expander("View Methodological Summary", expanded=False):
        st.markdown("""
        - **Purpose:** To determine if a process is stable and behaving predictably, or if it is being affected by 'special cause' variation that requires investigation.
        - **Method:** A Shewhart control chart plots a key process metric over time. A center line represents the process mean, and Upper/Lower Control Limits (UCL/LCL) are set at ±3 standard deviations (σ). These limits define the bounds of expected, random process variation.
        - **Findings & Interpretation:** Points within the control limits indicate 'common cause' variation inherent to the current process design. A point outside the limits (marked with a red 'X') is a statistically significant signal that something has changed in the process. This is not random noise and must be investigated via Root Cause Analysis (RCA). This is the primary tool for identifying "process friction or inefficiency" in a statistically rigorous way.
        """)
    metric_to_analyze = st.selectbox("Select a GCS Metric to Analyze:", ('Incident_MTTR_Minutes', 'Change_Failure_Rate_Pct', 'Problem_RCA_Cycle_Time_Days'))
    st.plotly_chart(plot_process_control_chart(metrics_df, metric_to_analyze), use_container_width=True)

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
    start_manual = ai_adoption_df['Manual'].iloc[0]
    end_manual = ai_adoption_df['Manual'].iloc[-1]
    st.plotly_chart(plot_digital_labor_mix(ai_adoption_df), use_container_width=True)
    st.success(f"**Strategic Finding:** Over the last 12 months, the reliance on manual effort has been reduced from **{start_manual:.1f}%** to **{end_manual:.1f}%**, a key indicator of successful AI/automation strategy execution.")

    st.subheader("B. AI Opportunity Prioritization Matrix")
    st.markdown("This matrix helps prioritize which processes are the best candidates for the next wave of AI-driven automation initiatives, based on their complexity and potential for impact.")
    st.image("https://i.imgur.com/gOQ50qW.png", caption="Example AI Opportunity Matrix: Mapping process complexity vs. automation impact.")

with tab4:
    st.header("V. Global Team Capability & Readiness")
    st.markdown("_This section provides a strategic view of the team's skills to ensure the right talent is assigned to the right initiatives and to identify development opportunities._")
    
    st.subheader("A. Talent & Capability Matrix")
    with st.expander("View Methodological Summary", expanded=False):
        st.markdown("""
        - **Purpose:** To assess the collective capabilities of the team against key strategic needs, identify skill gaps, and ensure readiness for critical assignments, such as supporting US Public Sector clients.
        - **Method:** A multi-dimensional scatter plot is used. The X and Y axes represent core technical skills (LSS Mastery, AI Integration). The size of the marker represents soft skills (Stakeholder Influence), and the color represents geographical region. The marker shape indicates clearance for sensitive projects (e.g., US Federal).
        - **Interpretation:** This matrix allows for strategic project assignment. For a high-stakes, AI-focused project, a team member from the top-right quadrant with a large marker (high influence) would be ideal. A cluster of team members in the bottom-left suggests a need for broad-based training. The symbols are critical for resource planning on high-security contracts, ensuring compliance and operational readiness.
        """)
    st.plotly_chart(plot_talent_capability_matrix(team_df), use_container_width=True)

# ============================ SIDEBAR ============================
st.sidebar.image("https://logowik.com/content/uploads/images/servicenow5873.jpg", use_container_width=True)
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
