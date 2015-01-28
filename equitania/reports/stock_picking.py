## -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time
from openerp.osv import osv
from openerp.report import report_sxw


class stock_picking(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(stock_picking, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'get_pickings':self.get_pickings,
        })
    def get_pickings(self, object):
        result = []
        for l in object:
            if l.eq_move_id:
                if l.eq_move_id.picking_id not in result:
                    result.append(l.eq_move_id.picking_id)
        return result
    
class report_invoice(osv.AbstractModel):
    _name = 'report.account.report_invoice'
    _inherit = 'report.abstract_report'
    _template = 'account.report_invoice'
    _wrapped_report_class = stock_picking

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
