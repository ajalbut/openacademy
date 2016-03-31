# -*- coding: utf-8 -*-
# © <2016> <Luis Felipe Mileo>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import models, fields
from openerp.addons.openacademy.models.session import Session


class ResPartner(models.Model):

    _inherit = "res.partner"

    is_instructor = fields.Boolean()

    teacher_category = fields.Selection(
        selection=Session.teacher_category.selection,
        string=Session.teacher_category.string
    )

    session_ids = fields.One2many('openacademy.session', 'id')
