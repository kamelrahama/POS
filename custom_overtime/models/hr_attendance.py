from odoo import models, fields, api
from datetime import timedelta

class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    overtime_hours = fields.Float("Overtime Hours", compute="_compute_overtime_hours", store=True)

class HrWorkEntryType(models.Model):
    _inherit = "hr.work.entry.type"

    is_paid = fields.Boolean(string="Is Paid", default=False)

    @api.depends("worked_hours")
    def _compute_overtime_hours(self):
        for record in self:
            record.overtime_hours = max(0, record.worked_hours - 9)  # Only extra hours count

    def _create_overtime_work_entry(self):
        """ Automatically create a work entry for overtime if applicable """
        WorkEntry = self.env["hr.work.entry"]
        work_entry_type = self.env.ref("custom_overtime.work_entry_type_overtime")

        for attendance in self:
            if attendance.overtime_hours > 0:
                WorkEntry.create({
                    "name": f"Overtime {attendance.employee_id.name}",
                    "employee_id": attendance.employee_id.id,
                    "work_entry_type_id": work_entry_type.id,
                    "date_start": attendance.check_in,
                    "date_stop": attendance.check_out,
                    "duration": attendance.overtime_hours,
                    "state": "draft",
                })

    @api.model
    def cron_generate_overtime_entries(self):
        """ Scheduled job to create overtime work entries daily """
        self.search([])._create_overtime_work_entry()
