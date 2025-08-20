import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date, timedelta
import numpy as np

# Configure page
st.set_page_config(
    page_title="IMS - Information Management System",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Language translations
TRANSLATIONS = {
    'en': {
        'login_title': 'Information Management System (IMS)',
        'login_subtitle': 'Corporate Systems Client - System Development Project',
        'username': 'Username',
        'password': 'Password',
        'login_button': 'Login',
        'remember_me': 'Remember me',
        'forgot_password': 'Forgot Password?',
        'invalid_credentials': 'Invalid username or password',
        'dashboard': 'Dashboard',
        'records_management': 'Records Management',
        'add_edit_record': 'Add/Edit Record',
        'reports_analytics': 'Reports & Analytics',
        'admin_settings': 'Admin & Settings',
        'training_documentation': 'Training & Documentation',
        'logout': 'Logout',
        'theme': 'Theme',
        'language': 'Language',
        'dark': 'Dark',
        'light': 'Light',
        'font_size': 'Font Size',
        'small': 'Small',
        'medium': 'Medium',
        'large': 'Large',
        'current_user': 'Current User',
        'system_administrator': 'System Administrator'
    },
    'es': {
        'login_title': 'Sistema de Gestión de Información (SGI)',
        'login_subtitle': 'Cliente de Sistemas Corporativos - Proyecto de Desarrollo de Sistema',
        'username': 'Usuario',
        'password': 'Contraseña',
        'login_button': 'Iniciar Sesión',
        'remember_me': 'Recordarme',
        'forgot_password': '¿Olvidaste tu contraseña?',
        'invalid_credentials': 'Usuario o contraseña inválidos',
        'dashboard': 'Panel de Control',
        'records_management': 'Gestión de Registros',
        'add_edit_record': 'Agregar/Editar Registro',
        'reports_analytics': 'Reportes y Análisis',
        'admin_settings': 'Administración y Configuración',
        'training_documentation': 'Capacitación y Documentación',
        'logout': 'Cerrar Sesión',
        'theme': 'Tema',
        'language': 'Idioma',
        'dark': 'Oscuro',
        'light': 'Claro',
        'font_size': 'Tamaño de Fuente',
        'small': 'Pequeño',
        'medium': 'Mediano',
        'large': 'Grande',
        'current_user': 'Usuario Actual',
        'system_administrator': 'Administrador del Sistema'
    },
    'fr': {
        'login_title': 'Système de Gestion d\'Information (SGI)',
        'login_subtitle': 'Client de Systèmes d\'Entreprise - Projet de Développement de Système',
        'username': 'Nom d\'utilisateur',
        'password': 'Mot de passe',
        'login_button': 'Se connecter',
        'remember_me': 'Se souvenir de moi',
        'forgot_password': 'Mot de passe oublié?',
        'invalid_credentials': 'Nom d\'utilisateur ou mot de passe invalide',
        'dashboard': 'Tableau de Bord',
        'records_management': 'Gestion des Enregistrements',
        'add_edit_record': 'Ajouter/Modifier Enregistrement',
        'reports_analytics': 'Rapports et Analyses',
        'admin_settings': 'Administration et Paramètres',
        'training_documentation': 'Formation et Documentation',
        'logout': 'Déconnexion',
        'theme': 'Thème',
        'language': 'Langue',
        'dark': 'Sombre',
        'light': 'Clair',
        'font_size': 'Taille de Police',
        'small': 'Petit',
        'medium': 'Moyen',
        'large': 'Grand',
        'current_user': 'Utilisateur Actuel',
        'system_administrator': 'Administrateur Système'
    }
}

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Dashboard'

if 'theme' not in st.session_state:
    st.session_state.theme = 'dark'

if 'language' not in st.session_state:
    st.session_state.language = 'en'

if 'font_size' not in st.session_state:
    st.session_state.font_size = 'medium'

if 'sample_records' not in st.session_state:
    st.session_state.sample_records = [
        {
            'ID': 'IMS-001',
            'Name': 'Client Contract - ABC Corp',
            'Category': 'Legal',
            'Created': '2024-01-15',
            'Modified': '2024-01-20',
            'Status': 'Active',
            'Priority': 'High',
            'Assigned': 'John Smith'
        },
        {
            'ID': 'IMS-002',
            'Name': 'Project Specifications',
            'Category': 'Technical',
            'Created': '2024-01-14',
            'Modified': '2024-01-19',
            'Status': 'Draft',
            'Priority': 'Medium',
            'Assigned': 'Jane Doe'
        },
        {
            'ID': 'IMS-003',
            'Name': 'Budget Analysis Q1',
            'Category': 'Financial',
            'Created': '2024-01-12',
            'Modified': '2024-01-18',
            'Status': 'Complete',
            'Priority': 'High',
            'Assigned': 'Bob Wilson'
        },
        {
            'ID': 'IMS-004',
            'Name': 'Security Audit Report',
            'Category': 'Security',
            'Created': '2024-01-10',
            'Modified': '2024-01-17',
            'Status': 'Pending',
            'Priority': 'Critical',
            'Assigned': 'Alice Johnson'
        }
    ]

if 'sample_users' not in st.session_state:
    st.session_state.sample_users = [
        {
            'Name': 'John Smith',
            'Email': 'john.smith@company.com',
            'Role': 'Administrator',
            'Department': 'IT',
            'Last Login': '2024-01-20 10:30',
            'Status': 'Active'
        },
        {
            'Name': 'Jane Doe',
            'Email': 'jane.doe@company.com',
            'Role': 'Manager',
            'Department': 'Operations',
            'Last Login': '2024-01-20 09:15',
            'Status': 'Active'
        },
        {
            'Name': 'Bob Wilson',
            'Email': 'bob.wilson@company.com',
            'Role': 'User',
            'Department': 'Finance',
            'Last Login': '2024-01-19 16:45',
            'Status': 'Active'
        },
        {
            'Name': 'Alice Johnson',
            'Email': 'alice.johnson@company.com',
            'Role': 'User',
            'Department': 'Security',
            'Last Login': '2024-01-18 14:20',
            'Status': 'Inactive'
        }
    ]

# Get current language translations
def get_text(key):
    return TRANSLATIONS[st.session_state.language].get(key, key)

# Custom CSS based on theme
def get_custom_css():
    # Font size mapping
    font_sizes = {
        'small': {'base': '0.85rem', 'h1': '1.8rem', 'h2': '1.4rem'},
        'medium': {'base': '1rem', 'h1': '2rem', 'h2': '1.6rem'},
        'large': {'base': '1.15rem', 'h1': '2.2rem', 'h2': '1.8rem'}
    }

    current_font = font_sizes[st.session_state.font_size]

    if st.session_state.theme == 'dark':
        css_content = """
        <style>
            .stApp {{
                background-color: #0e1117;
                color: #fafafa;
                font-size: {font_base};
            }}
            .stApp h1 {{
                font-size: {font_h1} !important;
            }}
            .stApp h2 {{
                font-size: {font_h2} !important;
            }}
            .settings-container {{
                background-color: #262730;
                padding: 0.5rem;
                border-radius: 8px;
                border: 1px solid #404040;
                margin-bottom: 1rem;
            }}
            .settings-row {{
                display: flex;
                gap: 0.5rem;
                align-items: center;
            }}
            .settings-item {{
                flex: 1;
                min-width: 0;
            }}
            .settings-item .stSelectbox > div {{
                font-size: 0.8rem;
            }}
            .settings-item .stSelectbox label {{
                font-size: 0.75rem;
                margin-bottom: 0.2rem;
            }}
            .main-header {{
                background: linear-gradient(90deg, #1f4e79 0%, #2d5aa0 100%);
                padding: 1rem;
                border-radius: 10px;
                margin-bottom: 2rem;
                border: 1px solid #262730;
            }}
            .main-header h1 {{
                color: #fafafa;
                margin: 0;
                font-size: 2rem;
            }}
            .main-header p {{
                color: #c9d1d9;
                margin: 0.5rem 0 0 0;
            }}
            .login-container {{
                background-color: #262730;
                padding: 2rem;
                border-radius: 15px;
                border: 1px solid #404040;
                box-shadow: 0 4px 12px rgba(0,0,0,0.3);
                margin-top: 2rem;
            }}
            .login-header {{
                text-align: center;
                margin-bottom: 2rem;
            }}
            .login-header h1 {{
                color: #fafafa;
                margin-bottom: 0.5rem;
            }}
            .login-header p {{
                color: #c9d1d9;
                font-size: 0.9rem;
            }}
            .metric-card {{
                background: #262730;
                padding: 1.5rem;
                border-radius: 10px;
                border-left: 4px solid #1f4e79;
                box-shadow: 0 2px 4px rgba(0,0,0,0.3);
                margin-bottom: 1rem;
                border: 1px solid #404040;
            }}
            .sidebar-section {{
                background: #262730;
                padding: 1rem;
                border-radius: 8px;
                margin-bottom: 1rem;
                border: 1px solid #404040;
            }}
            .form-section {{
                background: #262730;
                padding: 1.5rem;
                border-radius: 10px;
                border: 1px solid #404040;
                margin-bottom: 1.5rem;
            }}
            .footer {{
                background-color: #262730;
                border-top: 1px solid #404040;
                padding: 20px;
                text-align: center;
                color: #c9d1d9;
                margin-top: 2rem;
            }}
            .stButton > button {{
                width: 100%;
                border-radius: 5px;
                background-color: #1f4e79;
                color: white;
                border: none;
            }}
            .stButton > button:hover {{
                background-color: #2d5aa0;
            }}
        </style>
        """.format(font_base=current_font['base'], font_h1=current_font['h1'], font_h2=current_font['h2'])
    else:
        css_content = """
        <style>
            .stApp {{
                background-color: #ffffff;
                color: #000000;
                font-size: {font_base};
            }}
            .stApp h1 {{
                font-size: {font_h1} !important;
            }}
            .stApp h2 {{
                font-size: {font_h2} !important;
            }}
            .settings-container {{
                background-color: #f8f9fa;
                padding: 0.5rem;
                border-radius: 8px;
                border: 1px solid #e0e0e0;
                margin-bottom: 1rem;
            }}
            .settings-row {{
                display: flex;
                gap: 0.5rem;
                align-items: center;
            }}
            .settings-item {{
                flex: 1;
                min-width: 0;
            }}
            .settings-item .stSelectbox > div {{
                font-size: 0.8rem;
            }}
            .settings-item .stSelectbox label {{
                font-size: 0.75rem;
                margin-bottom: 0.2rem;
            }}
            .main-header {{
                background: linear-gradient(90deg, #007acc 0%, #005a9e 100%);
                padding: 1rem;
                border-radius: 10px;
                margin-bottom: 2rem;
            }}
            .main-header h1 {{
                color: white;
                margin: 0;
                font-size: 2rem;
            }}
            .main-header p {{
                color: #e8f4fd;
                margin: 0.5rem 0 0 0;
            }}
            .login-container {{
                background-color: #ffffff;
                padding: 2rem;
                border-radius: 15px;
                border: 1px solid #e0e0e0;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                margin-top: 2rem;
            }}
            .login-header {{
                text-align: center;
                margin-bottom: 2rem;
            }}
            .login-header h1 {{
                color: #000000;
                margin-bottom: 0.5rem;
            }}
            .login-header p {{
                color: #666666;
                font-size: 0.9rem;
            }}
            .metric-card {{
                background: white;
                padding: 1.5rem;
                border-radius: 10px;
                border-left: 4px solid #007acc;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                margin-bottom: 1rem;
            }}
            .sidebar-section {{
                background: #f8f9fa;
                padding: 1rem;
                border-radius: 8px;
                margin-bottom: 1rem;
            }}
            .form-section {{
                background: #ffffff;
                padding: 1.5rem;
                border-radius: 10px;
                border: 1px solid #e0e0e0;
                margin-bottom: 1.5rem;
            }}
            .footer {{
                background-color: #f8f9fa;
                border-top: 1px solid #e0e0e0;
                padding: 20px;
                text-align: center;
                color: #666666;
                margin-top: 2rem;
            }}
            .stButton > button {{
                width: 100%;
                border-radius: 5px;
                background-color: #007acc;
                color: white;
                border: none;
            }}
            .stButton > button:hover {{
                background-color: #005a9e;
            }}
        </style>
        """.format(font_base=current_font['base'], font_h1=current_font['h1'], font_h2=current_font['h2'])

    return css_content

# Apply custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

# Login function
def login_user(username, password):
    # Simple authentication (in real app, use proper authentication)
    valid_users = {
        'admin': 'admin123',
        'john.smith': 'password123',
        'jane.doe': 'password123',
        'demo': 'demo'
    }
    return username in valid_users and valid_users[username] == password

# Login page
if not st.session_state.logged_in:
    # Settings at the top in a compact container
    st.markdown("""
    <div class="settings-container">
        <div style="text-align: center; font-weight: bold; margin-bottom: 0.5rem;">Settings</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        language_options = {'EN': 'en', 'ES': 'es', 'FR': 'fr'}
        selected_lang = st.selectbox(
            get_text('language'),
            options=list(language_options.keys()),
            index=list(language_options.values()).index(st.session_state.language),
            key="login_lang"
        )
        if language_options[selected_lang] != st.session_state.language:
            st.session_state.language = language_options[selected_lang]
            st.rerun()

    with col2:
        theme_options = {get_text('dark'): 'dark', get_text('light'): 'light'}
        selected_theme = st.selectbox(
            get_text('theme'),
            options=list(theme_options.keys()),
            index=list(theme_options.values()).index(st.session_state.theme),
            key="login_theme"
        )
        if theme_options[selected_theme] != st.session_state.theme:
            st.session_state.theme = theme_options[selected_theme]
            st.rerun()

    with col3:
        font_options = {get_text('small'): 'small', get_text('medium'): 'medium', get_text('large'): 'large'}
        selected_font = st.selectbox(
            get_text('font_size'),
            options=list(font_options.keys()),
            index=list(font_options.values()).index(st.session_state.font_size),
            key="login_font"
        )
        if font_options[selected_font] != st.session_state.font_size:
            st.session_state.font_size = font_options[selected_font]
            st.rerun()

    # Centered login form
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("""
        <div class="login-container">
            <div class="login-header">
                <h1>{}</h1>
                <p>{}</p>
            </div>
        </div>
        """.format(get_text('login_title'), get_text('login_subtitle')), unsafe_allow_html=True)

        with st.form("login_form"):
            username = st.text_input(get_text('username'), placeholder="Enter username")
            password = st.text_input(get_text('password'), type="password", placeholder="Enter password")

            col_remember, col_forgot = st.columns(2)
            with col_remember:
                remember_me = st.checkbox(get_text('remember_me'))
            with col_forgot:
                st.markdown(f"[{get_text('forgot_password')}](#)")

            st.markdown("<br>", unsafe_allow_html=True)

            login_button = st.form_submit_button(get_text('login_button'), use_container_width=True)

            if login_button:
                if login_user(username, password):
                    st.session_state.logged_in = True
                    st.session_state.current_user = username
                    st.rerun()
                else:
                    st.error(get_text('invalid_credentials'))

        # Demo credentials info
        st.info("Demo credentials: username: 'demo', password: 'demo'")

    # Footer for login page
    st.markdown("""
    <div class="footer">
        <p><strong>Information Management System (IMS)</strong> | Version 0.0.7</p>
        <p>System Development Project | Corporate Systems Client</p>
        <p>For technical support: support@company.com | Phone: +1 (555) 123-4567</p>
    </div>
    """, unsafe_allow_html=True)

else:
    # Main application (logged in)

    # Header
    st.markdown("""
    <div class="main-header">
        <h1>{}</h1>
        <p><strong>System Development Project</strong> | Client: Corporate Systems Client | Project Manager: System Development Engineer</p>
    </div>
    """.format(get_text('login_title')), unsafe_allow_html=True)

    # Sidebar Navigation
    with st.sidebar:
        st.markdown(f"### **Navigation**")

        # Theme, language, and font size controls
        col1, col2, col3 = st.columns(3)
        with col1:
            theme_options = {get_text('dark'): 'dark', get_text('light'): 'light'}
            selected_theme = st.selectbox(
                get_text('theme'),
                options=list(theme_options.keys()),
                index=list(theme_options.values()).index(st.session_state.theme),
                key="sidebar_theme"
            )
            if theme_options[selected_theme] != st.session_state.theme:
                st.session_state.theme = theme_options[selected_theme]
                st.rerun()

        with col2:
            language_options = {'EN': 'en', 'ES': 'es', 'FR': 'fr'}
            selected_lang = st.selectbox(
                get_text('language'),
                options=list(language_options.keys()),
                index=list(language_options.values()).index(st.session_state.language),
                key="sidebar_lang"
            )
            if language_options[selected_lang] != st.session_state.language:
                st.session_state.language = language_options[selected_lang]
                st.rerun()

        with col3:
            font_options = {get_text('small'): 'small', get_text('medium'): 'medium', get_text('large'): 'large'}
            selected_font = st.selectbox(
                get_text('font_size'),
                options=list(font_options.keys()),
                index=list(font_options.values()).index(st.session_state.font_size),
                key="sidebar_font"
            )
            if font_options[selected_font] != st.session_state.font_size:
                st.session_state.font_size = font_options[selected_font]
                st.rerun()

        st.markdown("---")

        # Main navigation buttons
        if st.button(get_text('dashboard'), key="nav_dashboard", use_container_width=True):
            st.session_state.current_page = 'Dashboard'

        if st.button(get_text('records_management'), key="nav_records", use_container_width=True):
            st.session_state.current_page = 'Records'

        if st.button(get_text('add_edit_record'), key="nav_add_record", use_container_width=True):
            st.session_state.current_page = 'Add Record'

        if st.button(get_text('reports_analytics'), key="nav_reports", use_container_width=True):
            st.session_state.current_page = 'Reports'

        if st.button(get_text('admin_settings'), key="nav_admin", use_container_width=True):
            st.session_state.current_page = 'Admin'

        if st.button(get_text('training_documentation'), key="nav_training", use_container_width=True):
            st.session_state.current_page = 'Training'

        st.markdown("---")

        # User profile section
        st.markdown(f"### **{get_text('current_user')}**")
        st.info(f"**John Smith**\n{get_text('system_administrator')}\n john.smith@company.com")

        st.markdown("### **Quick Stats**")
        st.metric("Active Records", "1,247", "23")
        st.metric("Pending Tasks", "23", "-5")
        st.metric("System Health", "98.2%", "0.5%")

        st.markdown("---")

        # Logout button
        if st.button(get_text('logout'), key="logout", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.current_user = None
            st.rerun()

    # Main content area based on selected page
    if st.session_state.current_page == 'Dashboard':
        st.markdown("## Dashboard Overview")

        # Key metrics row
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                label="Total Records",
                value="1,247",
                delta="23 this week"
            )

        with col2:
            st.metric(
                label="Pending Tasks",
                value="23",
                delta="-5 from yesterday"
            )

        with col3:
            st.metric(
                label="This Month",
                value="156",
                delta="12% increase"
            )

        with col4:
            st.metric(
                label="System Health",
                value="98.2%",
                delta="0.5% improvement"
            )

        # Charts section
        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Records by Category")
            categories = ['Legal', 'Technical', 'Financial', 'Security', 'Operations']
            values = [245, 389, 156, 89, 368]

            fig = px.pie(
                values=values,
                names=categories,
                title="Distribution of Records by Category"
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("Activity Timeline")
            dates = pd.date_range(start='2024-01-01', end='2024-01-20', freq='D')
            activities = np.random.randint(10, 50, size=len(dates))

            fig = px.line(
                x=dates,
                y=activities,
                title="Daily System Activity"
            )
            fig.update_layout(xaxis_title="Date", yaxis_title="Activities")
            st.plotly_chart(fig, use_container_width=True)

        # Recent activity table
        st.subheader("Recent Activity")
        recent_activities = pd.DataFrame([
            {'Action': 'Record Updated', 'User': 'Jane Doe', 'Time': '2 min ago', 'Status': 'Complete'},
            {'Action': 'New Record Added', 'User': 'Bob Wilson', 'Time': '15 min ago', 'Status': 'Pending'},
            {'Action': 'Report Generated', 'User': 'System', 'Time': '1 hour ago', 'Status': 'Complete'},
            {'Action': 'User Login', 'User': 'Alice Johnson', 'Time': '2 hours ago', 'Status': 'Complete'},
            {'Action': 'Security Scan', 'User': 'System', 'Time': '3 hours ago', 'Status': 'Complete'}
        ])

        st.dataframe(recent_activities, use_container_width=True, hide_index=True)

    elif st.session_state.current_page == 'Records':
        st.markdown("## Records Management")

        # Search and filter section
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])

        with col1:
            search_query = st.text_input("Search records...", placeholder="Enter keywords to search")

        with col2:
            category_filter = st.selectbox("Category", ['All', 'Legal', 'Technical', 'Financial', 'Security'])

        with col3:
            status_filter = st.selectbox("Status", ['All', 'Active', 'Draft', 'Complete', 'Pending'])

        with col4:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Refresh", use_container_width=True):
                st.rerun()

        st.markdown("---")

        # Records table
        st.subheader("All Records")

        # Convert to DataFrame for better display
        records_df = pd.DataFrame(st.session_state.sample_records)

        # Apply filters
        if category_filter != 'All':
            records_df = records_df[records_df['Category'] == category_filter]

        if status_filter != 'All':
            records_df = records_df[records_df['Status'] == status_filter]

        if search_query:
            records_df = records_df[records_df['Name'].str.contains(search_query, case=False, na=False)]

        # Display table
        st.dataframe(records_df, use_container_width=True, hide_index=True)

    # Placeholder for other pages
    else:
        st.info(f"Content for {st.session_state.current_page} page would be displayed here.")

    # Footer
    st.markdown("""
    <div class="footer">
        <p><strong>Information Management System (IMS)</strong> | Version 0.0.7</p>
        <p>System Development Project | Corporate Systems Client</p>
        <p>For technical support: support@company.com | Phone: +1 (555) 123-4567</p>
    </div>
    """, unsafe_allow_html=True)
