# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2016 Luis Felipe Miléo - KMEE INFORMATICA LTDA
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################

from openerp import models, fields


class AccountInvoiceReport(models.Model):

    _inherit = "account.invoice.report"

    department_id = fields.Many2one(
        'hr.department',
        'Department', readonly=True)

    def _select(self):
        return super(AccountInvoiceReport, self)._select() + \
            ", sub.department_id as department_id"

    def _sub_select(self):
        return super(AccountInvoiceReport, self)._sub_select() + \
            ", ai.department_id as department_id"

    def _group_by(self):
        return super(AccountInvoiceReport, self)._group_by() + \
            ", ai.department_id"
