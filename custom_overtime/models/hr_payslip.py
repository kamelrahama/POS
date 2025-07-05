from odoo import models, fields, api

class HrPayslip(models.Model):
    _inherit = "hr.payslip"

    overtime_amount = fields.Float("Overtime Pay", compute="_compute_overtime_amount", store=True)

    @api.depends("worked_days_line_ids")
    def _compute_overtime_amount(self):
        for payslip in self:
            overtime_hours = sum(
                line.number_of_hours for line in payslip.worked_days_line_ids
                if line.work_entry_type_id.code == "OVERTIME"
            )
            payslip.overtime_amount = overtime_hours * 1  # 1 OMR per hour

    def _get_inputs(self, contract):
        """ Include overtime as an input for payroll calculation """
        inputs = super()._get_inputs(contract)
        overtime_hours = sum(
            self.worked_days_line_ids.filtered(lambda w: w.work_entry_type_id.code == "OVERTIME").mapped("number_of_hours")
        )
        inputs.append({
            "name": "Overtime Pay",
            "code": "OVERTIME",
            "amount": overtime_hours * 1,
        })
        return inputs
