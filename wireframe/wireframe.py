import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date, timedelta
import numpy as np

# Configure page
st.set_page_config(
    page_title="IMS - Information Management System",
    page_icon="X",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #007acc 0%, #005a9e 100%);
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .main-header h1 {
        color: white;
        margin: 0;
        font-size: 2rem;
    }
    .main-header p {
        color: #e8f4fd;
        margin: 0.5rem 0 0 0;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #007acc;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .status-active { color: #28a745; font-weight: bold; }
    .status-pending { color: #ffc107; font-weight: bold; }
    .status-inactive { color: #dc3545; font-weight: bold; }
    .status-draft { color: #6c757d; font-weight: bold; }
    .status-complete { color: #28a745; font-weight: bold; }
    .sidebar-section {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    .form-section {
        background: #ffffff;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        margin-bottom: 1.5rem;
    }
    .data-table {
        font-size: 0.9rem;
    }
    .stButton > button {
        width: 100%;
        border-radius: 5px;
    }
    .success-button {
        background-color: #28a745;
        color: white;
    }
    .danger-button {
        background-color: #dc3545;
        color: white;
    }
    .warning-button {
        background-color: #ffc107;
        color: black;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Dashboard'

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

# Header
st.markdown("""
<div class="main-header">
    <h1>Corporate Information Management System (IMS)</h1>
    <p><strong>System Development Project</strong> | Client: Corporate Systems Client | Project Manager: System Development Engineer</p>
</div>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("### **Navigation**")
    
    # Main navigation buttons
    if st.button("Dashboard", key="nav_dashboard", use_container_width=True):
        st.session_state.current_page = 'Dashboard'
    
    if st.button("Records Management", key="nav_records", use_container_width=True):
        st.session_state.current_page = 'Records'
    
    if st.button("Add/Edit Record", key="nav_add_record", use_container_width=True):
        st.session_state.current_page = 'Add Record'
    
    if st.button("Reports & Analytics", key="nav_reports", use_container_width=True):
        st.session_state.current_page = 'Reports'
    
    if st.button("Admin & Settings", key="nav_admin", use_container_width=True):
        st.session_state.current_page = 'Admin'
    
    if st.button("Training & Documentation", key="nav_training", use_container_width=True):
        st.session_state.current_page = 'Training'
    
    st.markdown("---")
    
    # User profile section
    st.markdown("### **Current User**")
    st.info("**John Smith**\nSystem Administrator\n john.smith@company.com")
    
    st.markdown("### **Quick Stats**")
    st.metric("Active Records", "1,247", "23")
    st.metric("Pending Tasks", "23", "-5")
    st.metric("System Health", "98.2%", "0.5%")

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
        {'Action': 'Report Generated', 'User': 'System', 'Time': '1 hour ago', 'Status':  'Complete'},
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
    
    # Action buttons
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("➕ Add New Record", key="add_new", use_container_width=True):
            st.session_state.current_page = 'Add Record'
            st.rerun()
    
    with col2:
        st.button("Export Data", use_container_width=True)
    
    with col3:
        st.button("Bulk Actions", use_container_width=True)
    
    with col4:
        st.button("Advanced Filter", use_container_width=True)
    
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
    
    # Display table with custom styling
    st.dataframe(
        records_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "ID": st.column_config.TextColumn("Record ID", width="small"),
            "Name": st.column_config.TextColumn("Record Name", width="large"),
            "Category": st.column_config.TextColumn("Category", width="small"),
            "Status": st.column_config.TextColumn("Status", width="small"),
            "Priority": st.column_config.TextColumn("Priority", width="small"),
            "Created": st.column_config.DateColumn("Created", width="small"),
            "Modified": st.column_config.DateColumn("Modified", width="small"),
            "Assigned": st.column_config.TextColumn("Assigned To", width="medium")
        }
    )
    
    # Record actions
    if not records_df.empty:
        st.subheader("Quick Actions")
        selected_record = st.selectbox("Select record for actions:", records_df['ID'].tolist())
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.button("View Details", use_container_width=True)
        with col2:
            st.button("Edit Record", use_container_width=True)
        with col3:
            st.button("Duplicate", use_container_width=True)
        with col4:
            st.button("Delete", use_container_width=True)

elif st.session_state.current_page == 'Add Record':
    st.markdown("## Add/Edit Record")
    
    # Form header
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("### Creating New Record")
    with col2:
        form_mode = st.selectbox("Mode:", ["Add New", "Edit Existing"])
    
    st.markdown("---")
    
    # Main form
    with st.form("record_form"):
        st.markdown("####Basic Information")
        
        col1, col2 = st.columns([2, 1])
        with col1:
            record_title = st.text_input("Record Title *", placeholder="Enter record title...")
        with col2:
            record_id = st.text_input("Record ID", value="IMS-005", disabled=True)
        
        col1, col2 = st.columns(2)
        with col1:
            category = st.selectbox("Category *", [
                "Select Category",
                "Legal Documents",
                "Technical Specifications", 
                "Financial Records",
                "Project Files",
                "Client Communications",
                "Security Documents"
            ])
        with col2:
            priority = st.selectbox("Priority Level", ["Low", "Medium", "High", "Critical"])
        
        description = st.text_area("Description", 
                                 placeholder="Enter detailed description of the record...",
                                 height=100)
        
        col1, col2 = st.columns(2)
        with col1:
            start_date = st.date_input("Start Date", value=date.today())
        with col2:
            end_date = st.date_input("End Date", value=date.today() + timedelta(days=30))
        
        tags = st.text_input("Tags", placeholder="contract, client, important, Q1-2024")
        
        st.markdown("####File Attachments")
        uploaded_files = st.file_uploader(
            "Choose files to attach",
            accept_multiple_files=True,
            type=['pdf', 'doc', 'docx', 'xls', 'xlsx', 'png', 'jpg', 'jpeg']
        )
        
        if uploaded_files:
            st.write(f"{len(uploaded_files)} file(s) selected:")
            for file in uploaded_files:
                st.write(f"  • {file.name} ({file.size} bytes)")
        
        st.markdown("####Access & Permissions")
        
        visibility = st.radio(
            "Visibility:",
            ["Public (All users can view)", "Restricted (Selected users only)", "Private (Only me)"]
        )
        
        if visibility == "Restricted (Selected users only)":
            assigned_users = st.multiselect(
                "Assign to users:",
                ["John Smith", "Jane Doe", "Bob Wilson", "Alice Johnson", "Mike Davis"]
            )
        
        col1, col2 = st.columns(2)
        with col1:
            status = st.selectbox("Initial Status", ["Draft", "Active", "Pending Review"])
        with col2:
            department = st.selectbox("Department", ["IT", "Finance", "Operations", "Legal", "HR"])
        
        st.markdown("---")
        
        # Form buttons
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            submitted = st.form_submit_button("Save Record", use_container_width=True)
        with col2:
            save_continue = st.form_submit_button("Save & Continue", use_container_width=True)
        with col3:
            draft = st.form_submit_button("Save as Draft", use_container_width=True)
        with col4:
            cancel = st.form_submit_button("Cancel", use_container_width=True)
        
        # Form submission handling
        if submitted or save_continue or draft:
            if record_title and category != "Select Category":
                new_record = {
                    'ID': record_id,
                    'Name': record_title,
                    'Category': category.split(' ')[0],  # Take first word
                    'Created': start_date.strftime('%Y-%m-%d'),
                    'Modified': start_date.strftime('%Y-%m-%d'),
                    'Status': 'Draft' if draft else status,
                    'Priority': priority,
                    'Assigned': 'John Smith'  # Current user
                }
                
                st.session_state.sample_records.append(new_record)
                st.success("Record saved successfully!")
                
                if save_continue:
                    st.info("Ready to add another record")
                elif not draft:
                    st.session_state.current_page = 'Records'
                    st.rerun()
            else:
                st.error("Please fill in all required fields (marked with *)")
        
        if cancel:
            st.session_state.current_page = 'Records'
            st.rerun()

elif st.session_state.current_page == 'Reports':
    st.markdown("## Reports & Analytics")
    
    # Report type selector
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        report_type = st.selectbox("Select Report Type:", [
            "Usage Analytics",
            "Performance Metrics", 
            "Security Audit",
            "Data Quality Report",
            "User Activity Report",
            "Custom Report"
        ])
    
    with col2:
        date_range = st.selectbox("Time Period:", [
            "Last 7 days",
            "Last 30 days",
            "Last 90 days",
            "This Year",
            "Custom Range"
        ])
    
    with col3:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Generate Report", use_container_width=True):
            st.balloons()
    
    st.markdown("---")
    
    # Quick stats dashboard
    st.subheader("Quick Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Records", "1,247", "12%")
    with col2:
        st.metric("Active Users", "45", "8%")
    with col3:
        st.metric("Storage Used", "2.3 TB", "5%")
    with col4:
        st.metric("System Uptime", "99.8%", "0.2%")
    
    # Charts and visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Monthly Activity Trend")
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        activities = [234, 289, 345, 423, 567, 612]
        
        fig = px.bar(x=months, y=activities, title="Monthly System Activity")
        fig.update_layout(xaxis_title="Month", yaxis_title="Activities")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("User Activity Distribution")
        users = ['John S.', 'Jane D.', 'Bob W.', 'Alice J.', 'Mike D.']
        activity_counts = [156, 134, 98, 87, 65]
        
        fig = px.pie(values=activity_counts, names=users, title="User Activity Share")
        st.plotly_chart(fig, use_container_width=True)
    
    # Report history table
    st.subheader("Recent Reports")
    
    report_history = pd.DataFrame([
        {
            'Report Name': 'Monthly Usage Summary',
            'Type': 'Analytics',
            'Generated': '2024-01-20 09:30',
            'Status': 'Ready',
            'Size': '2.3 MB'
        },
        {
            'Report Name': 'Security Audit Q1',
            'Type': 'Security', 
            'Generated': '2024-01-19 14:15',
            'Status': 'Processing',
            'Size': 'Pending'
        },
        {
            'Report Name': 'Data Quality Check',
            'Type': 'System',
            'Generated': '2024-01-18 11:45',
            'Status': 'Ready',
            'Size': '1.8 MB'
        }
    ])
    
    st.dataframe(report_history, use_container_width=True, hide_index=True)
    
    # Action buttons for reports
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.button("Download Report", use_container_width=True)
    with col2:
        st.button("Email Report", use_container_width=True)
    with col3:
        st.button("Schedule Report", use_container_width=True)
    with col4:
        st.button("Refresh Data", use_container_width=True)

elif st.session_state.current_page == 'Admin':
    st.markdown("## Administration & Settings")
    
    # Admin tabs
    admin_tab = st.tabs(["User Management", "System Settings", "Security", "Backup & Restore"])
    
    with admin_tab[0]:  # User Management
        st.subheader("User Management")
        
        # User actions
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button("Add New User", use_container_width=True):
                st.info("Add User form would open here")
        with col2:
            st.button("Export Users", use_container_width=True)
        with col3:
            st.button("Send Invites", use_container_width=True)
        with col4:
            st.button("Sync with AD", use_container_width=True)
        
        # User filters
        col1, col2, col3 = st.columns(3)
        with col1:
            role_filter = st.selectbox("Filter by Role:", ["All Roles", "Administrator", "Manager", "User", "Viewer"])
        with col2:
            dept_filter = st.selectbox("Filter by Department:", ["All Departments", "IT", "Finance", "Operations", "Legal", "HR"])
        with col3:
            status_filter_admin = st.selectbox("Filter by Status:", ["All Status", "Active", "Inactive", "Pending"])
        
        # Users table
        users_df = pd.DataFrame(st.session_state.sample_users)
        
        # Apply filters
        if role_filter != "All Roles":
            users_df = users_df[users_df['Role'] == role_filter]
        if dept_filter != "All Departments":
            users_df = users_df[users_df['Department'] == dept_filter]
        if status_filter_admin != "All Status":
            users_df = users_df[users_df['Status'] == status_filter_admin]
        
        st.dataframe(
            users_df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Name": st.column_config.TextColumn("Full Name", width="medium"),
                "Email": st.column_config.TextColumn("Email Address", width="large"),
                "Role": st.column_config.TextColumn("Role", width="small"),
                "Department": st.column_config.TextColumn("Department", width="small"),
                "Last Login": st.column_config.TextColumn("Last Login", width="medium"),
                "Status": st.column_config.TextColumn("Status", width="small")
            }
        )
        
        # User actions
        if not users_df.empty:
            selected_user = st.selectbox("Select user for actions:", users_df['Name'].tolist())
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.button("Edit User", use_container_width=True)
            with col2:
                st.button("Reset Password", use_container_width=True)
            with col3:
                st.button("Change Permissions", use_container_width=True)
            with col4:
                st.button("Deactivate", use_container_width=True)
    
    with admin_tab[1]:  # System Settings
        st.subheader("System Configuration")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("####General Settings")
            company_name = st.text_input("Company Name", value="Corporate Systems Client")
            system_name = st.text_input("System Name", value="Information Management System")
            time_zone = st.selectbox("Time Zone", ["UTC-5 (EST)", "UTC-8 (PST)", "UTC+0 (GMT)", "UTC+1 (CET)"])
            language = st.selectbox("Default Language", ["English", "Spanish", "French", "German"])
            
            st.markdown("####mail Settings")
            smtp_server = st.text_input("SMTP Server", value="mail.company.com")
            smtp_port = st.number_input("SMTP Port", value=587, min_value=1, max_value=65535)
            email_from = st.text_input("From Email", value="noreply@company.com")
        
        with col2:
            st.markdown("####Security Settings")
            session_timeout = st.number_input("Session Timeout (minutes)", value=30, min_value=5, max_value=480)
            password_policy = st.selectbox("Password Policy", ["Standard", "Strong", "Custom"])
            two_factor = st.checkbox("Enable Two-Factor Authentication", value=True)
            login_attempts = st.number_input("Max Login Attempts", value=3, min_value=1, max_value=10)
            
            st.markdown("####Data Settings")
            backup_frequency = st.selectbox("Backup Frequency", ["Daily", "Weekly", "Monthly"])
            retention_period = st.number_input("Data Retention (days)", value=365, min_value=30, max_value=2555)
            auto_archive = st.checkbox("Auto-archive old records", value=True)
        
        if st.button("Save Settings", use_container_width=True):
            st.success("Settings saved successfully!")
    
    with admin_tab[2]:  # Security
        st.subheader("Security Management")
        
        # Security metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Security Score", "92%", "2%")
        with col2:
            st.metric("Failed Logins", "12", "5")
        with col3:
            st.metric("Active Sessions", "23", "3")
        with col4:
            st.metric("Last Scan", "2 hrs ago", "")
        
        st.markdown("####Security Audit Log")
        security_log = pd.DataFrame([
            {'Timestamp': '2024-01-20 10:30', 'Event': 'Login Success', 'User': 'john.smith', 'IP': '192.168.1.100', 'Risk': 'Low'},
            {'Timestamp': '2024-01-20 10:25', 'Event': 'Failed Login', 'User': 'unknown', 'IP': '203.45.67.89', 'Risk': 'Medium'},
            {'Timestamp': '2024-01-20 10:20', 'Event': 'Password Change', 'User': 'jane.doe', 'IP': '192.168.1.105', 'Risk': 'Low'},
            {'Timestamp': '2024-01-20 09:45', 'Event': 'File Access', 'User': 'bob.wilson', 'IP': '192.168.1.110', 'Risk': 'Low'},
            {'Timestamp': '2024-01-20 09:30', 'Event': 'Admin Access', 'User': 'john.smith', 'IP': '192.168.1.100', 'Risk': 'Medium'}
        ])
        
        st.dataframe(security_log, use_container_width=True, hide_index=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.button("Run Security Scan", use_container_width=True)
        with col2:
            st.button("Generate Security Report", use_container_width=True)
        with col3:
            st.button("View Alerts", use_container_width=True)
    
    with admin_tab[3]:  # Backup & Restore
        st.subheader("Backup & Restore")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("####Backup Management")
            st.info("Last backup: 2024-01-20 02:00 AM (Success)")
            
            backup_schedule = st.selectbox("Backup Schedule:", ["Daily at 2:00 AM", "Weekly on Sunday", "Monthly on 1st", "Manual Only"])
            include_files = st.checkbox("Include uploaded files", value=True)
            compress_backup = st.checkbox("Compress backup files", value=True)
            
            if st.button("Run Backup Now", use_container_width=True):
                with st.spinner("Creating backup..."):
                    import time
                    time.sleep(2)
                st.success("Backup completed successfully!")
        
        with col2:
            st.markdown("####Restore Options")
            
            backup_files = ["2024-01-20_02-00.bak", "2024-01-19_02-00.bak", "2024-01-18_02-00.bak"]
            selected_backup = st.selectbox("Select backup to restore:", backup_files)
            
            restore_options = st.multiselect("Restore components:", 
                ["Database", "User Files", "System Settings", "User Accounts"], 
                default=["Database"])
            
            if st.button("Restore from Backup", use_container_width=True):
                st.warning("This action cannot be undone. Please confirm you want to proceed.")

elif st.session_state.current_page == 'Training':
    st.markdown("## Training & Documentation")
    
    # Training navigation tabs
    training_tabs = st.tabs(["User Guide", "Training Modules", "Quick Reference", "FAQ", "Video Tutorials", "Support"])
    
    with training_tabs[0]:  # User Guide
        st.subheader("System User Guide")
        
        # User guide sections
        guide_sections = st.selectbox("Select Guide Section:", [
            "Getting Started",
            "Navigation & Interface",
            "Managing Records",
            "Creating Reports", 
            "User Management",
            "System Administration",
            "Security & Permissions",
            "Troubleshooting"
        ])
        
        if guide_sections == "Getting Started":
            st.markdown("""
            ###Welcome to the Information Management System
            
            This comprehensive guide will help you get started with the IMS platform.
            
            #### First Steps:
            1. **Login**: Use your corporate credentials to access the system
            2. **Dashboard**: Familiarize yourself with the main dashboard layout
            3. **Navigation**: Learn to use the sidebar navigation menu
            4. **Profile**: Complete your user profile setup
            
            #### System Overview:
            The IMS is designed to help organizations manage their information assets efficiently:
            - **Records Management**: Create, edit, and organize documents
            - **Collaboration**: Share and collaborate on records with team members
            - **Reporting**: Generate insights from your data
            - **Security**: Maintain data security and access controls
            """)
            
            st.info("**Tip**: Start by exploring the Dashboard to get familiar with the system layout.")
            
        elif guide_sections == "Managing Records":
            st.markdown("""
            ###Records Management Guide
            
            #### Creating New Records:
            1. Navigate to **Records Management** from the sidebar
            2. Click the **"+ Add New Record"** button
            3. Fill in the required information:
               - Record Title (required)
               - Category (required)
               - Description
               - Priority Level
               - Tags
            4. Set access permissions
            5. Upload any relevant files
            6. Save the record
            
            #### Organizing Records:
            - **Categories**: Use categories to group related records
            - **Tags**: Add descriptive tags for easy searching
            - **Folders**: Organize records in logical folder structures
            - **Search**: Use the search functionality to find records quickly
            
            #### Best Practices:
            - Use descriptive titles and clear descriptions
            - Apply consistent tagging conventions
            - Regularly review and update record statuses
            - Set appropriate access permissions
            """)
            
        # Add downloadable user manual
        st.markdown("###Downloadable Resources")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.download_button(
                label="Download User Manual (PDF)",
                data="Sample user manual content...",
                file_name="IMS_User_Manual.pdf",
                mime="application/pdf",
                use_container_width=True
            )
        
        with col2:
            st.download_button(
                label="Download Quick Reference",
                data="Quick reference guide content...",
                file_name="IMS_Quick_Reference.pdf", 
                mime="application/pdf",
                use_container_width=True
            )
        
        with col3:
            st.download_button(
                label="Admin Guide",
                data="Administrator guide content...",
                file_name="IMS_Admin_Guide.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    
    with training_tabs[1]:  # Training Modules
        st.subheader("Interactive Training Modules")
        
        # Training progress
        st.markdown("###Your Training Progress")
        progress_col1, progress_col2, progress_col3 = st.columns(3)
        
        with progress_col1:
            st.metric("Completed Modules", "3/8", "37.5%")
        with progress_col2:
            st.metric("Time Spent", "2.5 hours", "+30 min")
        with progress_col3:
            st.metric("Certification Progress", "60%", "+15%")
        
        st.progress(0.375)  # 37.5% progress
        
        # Training modules list
        st.markdown("###Available Training Modules")
        
        training_modules = [
            {"Module": "System Basics", "Duration": "30 min", "Status": "Completed", "Score": "95%"},
            {"Module": "Record Management", "Duration": "45 min", "Status": "Completed", "Score": "88%"},
            {"Module": "Collaboration Features", "Duration": "25 min", "Status": "Completed", "Score": "92%"},
            {"Module": "Report Generation", "Duration": "35 min", "Status": "In Progress", "Score": "65%"},
            {"Module": "Advanced Search", "Duration": "20 min", "Status": "Not Started", "Score": "-"},
            {"Module": "Security & Permissions", "Duration": "40 min", "Status": "Not Started", "Score": "-"},
            {"Module": "System Administration", "Duration": "60 min", "Status": "Not Started", "Score": "-"},
            {"Module": "Troubleshooting", "Duration": "30 min", "Status": "Not Started", "Score": "-"}
        ]
        
        modules_df = pd.DataFrame(training_modules)
        st.dataframe(modules_df, use_container_width=True, hide_index=True)
        
        # Module actions
        selected_module = st.selectbox("Select module to start:", 
            [m["Module"] for m in training_modules if "Not Started" in m["Status"] or "In Progress" in m["Status"]])
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Start Module", use_container_width=True):
                st.success(f"Starting module: {selected_module}")
        with col2:
            st.button("Take Assessment", use_container_width=True)
        with col3:
            st.button("View Certificate", use_container_width=True)
    
    with training_tabs[2]:  # Quick Reference
        st.subheader("Quick Reference Guide")
        
        # Quick reference sections
        ref_col1, ref_col2 = st.columns(2)
        
        with ref_col1:
            st.markdown("""
            ###Keyboard Shortcuts
            
            | Action | Shortcut |
            |--------|----------|
            | New Record | `Ctrl + N` |
            | Search | `Ctrl + F` |
            | Save | `Ctrl + S` |
            | Print | `Ctrl + P` |
            | Help | `F1` |
            | Refresh | `F5` |
            | Logout | `Ctrl + L` |
            
            ###Search Operators
            
            | Operator | Example | Description |
            |----------|---------|-------------|
            | `AND` | `contract AND legal` | Both terms |
            | `OR` | `budget OR finance` | Either term |
            | `NOT` | `project NOT archived` | Exclude term |
            | `"quotes"` | `"project plan"` | Exact phrase |
            | `*` | `proj*` | Wildcard |
            """)
        
        with ref_col2:
            st.markdown("""
            ###Status Indicators
            
            | Symbol | Status | Description |
            |--------|--------|-------------|
            |   | Active | Record is active and current |
            |   | Pending | Awaiting review or approval |
            |   | Inactive | Record is disabled |
            |   | Draft | Work in progress |
            |   | Complete | Task or process finished |
            |   | Processing | System is working |
            
            ###Priority Levels
            
            | Level | Color | When to Use |
            |-------|-------|-------------|
            |   Critical | Red | Immediate attention required |
            |   High | Orange | Important, handle soon |
            |   Medium | Yellow | Normal priority |
            |   Low | Green | Handle when convenient |
            """)
        
        # Common tasks checklist
        st.markdown("###Common Tasks Checklist")
        
        task_col1, task_col2 = st.columns(2)
        
        with task_col1:
            st.markdown("**Daily Tasks:**")
            st.checkbox("Check dashboard for new notifications")
            st.checkbox("Review assigned records")
            st.checkbox("Update record statuses")
            st.checkbox("Respond to collaboration requests")
        
        with task_col2:
            st.markdown("**Weekly Tasks:**")
            st.checkbox("Generate weekly activity report")
            st.checkbox("Archive completed records")
            st.checkbox("Review security alerts")
            st.checkbox("Update team on progress")
    
    with training_tabs[3]:  # FAQ
        st.subheader("Frequently Asked Questions")
        
        # FAQ categories
        faq_category = st.selectbox("Select Category:", [
            "General Usage",
            "Account & Access", 
            "Records Management",
            "Technical Issues",
            "Security & Privacy"
        ])
        
        if faq_category == "General Usage":
            with st.expander("How do I navigate the system?"):
                st.markdown("""
                Use the sidebar navigation menu to move between different sections:
                - **Dashboard**: Overview and quick stats
                - **Records**: Manage your documents and files
                - **Reports**: Generate and view analytics
                - **Admin**: System administration (if authorized)
                """)
            
            with st.expander("How do I search for records?"):
                st.markdown("""
                1. Use the search bar at the top of the Records page
                2. Enter keywords related to your record
                3. Use filters to narrow results by category, status, or date
                4. Use search operators (AND, OR, NOT) for advanced searches
                """)
            
            with st.expander("Can I customize the dashboard?"):
                st.markdown("""
                Yes! You can customize your dashboard by:
                - Rearranging widget order
                - Choosing which metrics to display
                - Setting default time ranges for charts
                - Creating custom quick-access buttons
                """)
        
        elif faq_category == "Records Management":
            with st.expander("What file types can I upload?"):
                st.markdown("""
                The system supports the following file types:
                - **Documents**: PDF, DOC, DOCX, TXT, RTF
                - **Spreadsheets**: XLS, XLSX, CSV
                - **Images**: PNG, JPG, JPEG, GIF
                - **Archives**: ZIP, RAR
                - **Maximum file size**: 10MB per file
                """)
            
            with st.expander("How do I set record permissions?"):
                st.markdown("""
                When creating or editing a record:
                1. Go to the "Access & Permissions" section
                2. Choose visibility level:
                   - **Public**: All users can view
                   - **Restricted**: Only selected users
                   - **Private**: Only you can access
                3. For restricted records, select specific users or groups
                """)
        
        # Search FAQ
        st.markdown("###Search FAQ")
        faq_search = st.text_input("Search FAQ:", placeholder="Type your question...")
        
        if faq_search:
            st.info(f"Searching for: '{faq_search}'")
            st.markdown("**Suggested topics:**")
            st.write("• How to reset password")
            st.write("• Record sharing permissions") 
            st.write("• System backup procedures")
    
    with training_tabs[4]:  # Video Tutorials
        st.subheader("Video Tutorials")
        
        # Video tutorial categories
        video_col1, video_col2 = st.columns(2)
        
        with video_col1:
            st.markdown("### Getting Started Videos")
            
            tutorials = [
                {"title": "System Overview & Navigation", "duration": "5:32", "views": "1,234"},
                {"title": "Creating Your First Record", "duration": "7:45", "views": "987"},
                {"title": "Understanding Dashboard Widgets", "duration": "4:18", "views": "756"},
                {"title": "Basic Search Techniques", "duration": "6:23", "views": "654"}
            ]
            
            for tutorial in tutorials:
                with st.container():
                    col_thumb, col_info = st.columns([1, 3])
                    
                    with col_thumb:
                        st.markdown("")  # Video thumbnail placeholder
                    
                    with col_info:
                        st.markdown(f"**{tutorial['title']}**")
                        st.caption(f"Duration: {tutorial['duration']} | Views: {tutorial['views']}")
                        if st.button(f"Watch", key=f"watch_{tutorial['title']}", use_container_width=True):
                            st.info(f"Playing: {tutorial['title']}")
        
        with video_col2:
            st.markdown("###Advanced Features")
            
            advanced_tutorials = [
                {"title": "Advanced Search & Filtering", "duration": "8:12", "views": "543"},
                {"title": "Creating Custom Reports", "duration": "12:34", "views": "432"},
                {"title": "User Management & Permissions", "duration": "9:56", "views": "321"},
                {"title": "System Administration", "duration": "15:22", "views": "210"}
            ]
            
            for tutorial in advanced_tutorials:
                with st.container():
                    col_thumb, col_info = st.columns([1, 3])
                    
                    with col_thumb:
                        st.markdown("")  # Video thumbnail placeholder
                    
                    with col_info:
                        st.markdown(f"**{tutorial['title']}**")
                        st.caption(f"Duration: {tutorial['duration']} | Views: {tutorial['views']}")
                        if st.button(f"Watch", key=f"watch_adv_{tutorial['title']}", use_container_width=True):
                            st.info(f"Playing: {tutorial['title']}")
        
        # Video playlist
        st.markdown("### 📺 Recommended Learning Path")
        learning_path = [
            "1. System Overview & Navigation",
            "2. Creating Your First Record", 
            "3. Understanding Dashboard Widgets",
            "4. Basic Search Techniques",
            "5. Advanced Search & Filtering",
            "6. Creating Custom Reports"
        ]
        
        for i, step in enumerate(learning_path):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(step)
            with col2:
                if i < 3:  # First 3 completed
                    st.markdown("")
                elif i == 3:  # Current step
                    st.markdown("")
                else:  # Future steps
                    st.markdown("")
    
    with training_tabs[5]:  # Support
        st.subheader("Support & Help")
        
        support_col1, support_col2 = st.columns(2)
        
        with support_col1:
            st.markdown("###Get Help")
            
            # Support ticket form
            with st.form("support_ticket"):
                st.markdown("**Submit Support Ticket**")
                
                ticket_type = st.selectbox("Issue Type:", [
                    "Technical Problem",
                    "Account Access",
                    "Feature Request", 
                    "Training Question",
                    "Bug Report",
                    "Other"
                ])
                
                priority = st.selectbox("Priority:", ["Low", "Medium", "High", "Urgent"])
                
                subject = st.text_input("Subject:", placeholder="Brief description of your issue")
                
                description = st.text_area("Description:", 
                    placeholder="Please provide detailed information about your issue...",
                    height=100)
                
                attachment = st.file_uploader("Attach screenshot or file (optional):")
                
                if st.form_submit_button("Submit Ticket", use_container_width=True):
                    st.success("Support ticket submitted successfully! Ticket #IMS-2024-001")
        
        with support_col2:
            st.markdown("###Contact Information")
            
            st.info("""
            **Email Support**  
            support@company.com  
            Response time: 2-4 hours
            
            **Phone Support**  
            +1 (555) 123-4567  
            Hours: Mon-Fri 8AM-6PM EST
            
            **Live Chat**  
            Available on this page  
            Hours: Mon-Fri 9AM-5PM EST
            
            **Knowledge Base**  
            help.company.com/ims
            """)
            
            st.markdown("###Support Statistics")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Avg Response Time", "2.3 hours")
                st.metric("Resolution Rate", "94%")
            with col2:
                st.metric("Satisfaction Score", "4.6/5")
                st.metric("Open Tickets", "12")
        
        # Recent tickets
        st.markdown("###Your Recent Tickets")
        
        user_tickets = pd.DataFrame([
            {
                'Ticket ID': 'IMS-2024-001',
                'Subject': 'Cannot upload large files',
                'Status': 'In Progress',
                'Created': '2024-01-20',
                'Priority': 'Medium'
            },
            {
                'Ticket ID': 'IMS-2024-002', 
                'Subject': 'Password reset not working',
                'Status': 'Resolved',
                'Created': '2024-01-18',
                'Priority': 'High'
            }
        ])
        
        st.dataframe(user_tickets, use_container_width=True, hide_index=True)
        
        # Live chat simulation
        st.markdown("###Live Chat")
        if st.button("Start Live Chat", use_container_width=True):
            st.success("Connecting you with a support agent...")
            st.info("**Agent Sarah**: Hello! How can I help you today?")

# Footer with additional information
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p><strong>Information Management System (IMS)</strong> | Version 2.1.0</p>
    <p>System Development Project | Corporate Systems Client</p>
    <p>For technical support: support@company.com | Phone: +1 (555) 123-4567</p>
</div>
""", unsafe_allow_html=True)
