def get_tab_name(status_id):
    if status_id == 1:
        status_bucket = 1
    if status_id == 2 or status_id == 3 or status_id == 4:
        status_bucket = 2
    if status_id == 5:
        status_bucket = 5
    if status_id == 6 or status_id == 7 or status_id == 8:
        status_bucket = 3
    if status_id == 9 or status_id == 10:
        status_bucket = 4

    status_bucket_name = {
        1: "unassignedTab",
        2: "preparationTab",
        3: "finalizationTab",
        4: "closureTab",
        5: "reviewTab",
        6: "extensionTab",
        7: "overviewTab"
    }
    return status_bucket_name[status_bucket]


def get_filter_status(status):
    status_name = {
        1: "Initial",
        2: "Assigned",
        3: "In Progress",
        4: "Mgr Review",
        5: "Admin Review",
        6: "Info Pending",
        7: "Client Review",
        8: "Efile Auth",
        9: "Efiled",
        10: "Closed"
    }
    return status_name[status]


def get_bns_type(bns_type):
    bns_type_name = {
        1: "Sole-Prop",
        2: "LP",
        3: "LLP",
        4: "LLC",
        5: "C-Corp",
        6: "S-Corp",
        7: "Non-Profit"
    }
    return bns_type_name[bns_type]


def get_bns_frequency(bns_frequency):
    bns_frequency_name = {
        0: "None",
        1: "Monthly",
        2: "Quarterly",
        3: "Yearly",
        4: "Bi-Monthly",
    }
    return bns_frequency_name[int(bns_frequency)]


def get_upload_doc_source(doc_source):
    doc_source_name = {
        1: "Sent to Client",
        2: "Received from Client",
        3: "Internal CPA Only",
        4: "Internal Team",
        5: "Esign"
    }
    return doc_source_name[doc_source]


def get_upload_file_type(file_type):
    file_type_name = {
        1: "Tax Return",
        2: "W-2",
        3: "1095",
        4: "1098",
        5: "1098-T",
        6: "1099-B",
        7: "1099-DIV",
        8: "1099-INT",
        9: "1099-MISC",
        10: "1099-NEC",
        11: "1099-G",
        12: "1099-R",
        13: "1099-SSA",
        14: "1099-SA (HSA)",
        15: "Business Income and Expense",
        16: "Bank Statement",
        17: "Cash Donation",
        18: "Credit Card Statement",
        19: "Closing Statement",
        20: "DMV Fees",
        21: "Dependent Care Expense",
        22: "Efile Acceptance Letter",
        23: "Efile Authorization Letter",
        24: "Estimated Tax Payment",
        25: "Energy Credit",
        26: "FBAR",
        27: "IRA Contribution",
        28: "K1-1120S, 1065",
        29: "Non-Cash Donation",
        30: "Organizer",
        31: "Payroll Expense",
        32: "Property Tax",
        33: "Quarterly Payroll Form",
        34: "ROTH Conversion",
        35: "Sch C - Income and Expense",
        36: "Sch E - Rental Income and Expense",
        37: "SEP Simple IRA",
        38: "Solo 401K",
        39: "Other",
    }
    return file_type_name[file_type]


def get_emp_type(num):
    emp_type = {1: "Team Member", 2: "Team Manager", 3: "Front Office"}
    return emp_type[num]


def get_filter_project_month(month):
    month_name = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"

    }
    return month_name[month]
