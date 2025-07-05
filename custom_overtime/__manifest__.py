{
    "name": "Custom Overtime Calculation",
    "summary": "Automatically calculates overtime based on attendance hours and integrates with payroll.",
    "version": "1.0",
    "author": "Your Name",
    "depends": ["hr_attendance", "hr_payroll"],
    "data": [
        "security/ir.model.access.csv",
        "data/work_entry_type_data.xml",
        "views/overtime_views.xml",
    ],
    "installable": True,
    "application": False,
}
