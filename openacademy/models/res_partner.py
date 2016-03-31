# -*- coding: utf-8 -*-
# © <2016> <Luis Felipe Mileo>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import models, fields


class ResPartner(models.Model):

    _inherit = "res.partner"

    is_instructor = fields.Boolean()

    session_ids = fields.One2many('openacademy.session', 'id')
