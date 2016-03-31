# -*- coding: utf-8 -*-
# © <2016> <Luis Felipe Mileo>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import fields, models


class Attendee(models.Model):

    _name = "openacademy.attendee"
    _description = "Attendee"

    name = fields.Char(
        string="Name",
        help="Insira o nome do Attendee"
    )

    partner_id = fields.Many2one('res.partner', ondelete='cascade')
    session_id = fields.Many2one('openacademy.session', ondelete='cascade')
